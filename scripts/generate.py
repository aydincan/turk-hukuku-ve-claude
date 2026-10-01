#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude ve Türk Hukuku — depo üreteci.

Girdi:
  scripts/catalog.json   : pazar yapılandırması + ~80 eklenti tanımı (yetkili kaynak)
  scripts/content.json   : (opsiyonel) workflow ajanlarının ürettiği hukuki gövde
                           { "<slug>": { "referans_md": str,
                                          "beceriler": [ {slug, ad, aciklama, govde_md}, ... ] } }

Çıktı: kökte .claude-plugin/marketplace.json + her eklenti için tam dizin yapısı,
       kök README.md ve SKILLS.md dizini.

Ajan içeriği eksikse şablon yedeği kullanılır; depo her hâlükârda eksiksiz ve geçerli kalır.
"""
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "scripts", "catalog.json")
CONTENT = os.path.join(ROOT, "scripts", "content.json")


def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# --------------------------------------------------------------------------
# Standart bloklar (her beceriye eklenir — kaynak hijyeni ajan'dan bağımsız tutarlı)
# --------------------------------------------------------------------------

def kaynak_footer(slug):
    return f"""
## Plugin bağlamı

Bu beceri `{slug}` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
çalışır; bir konu eklentinin dışına taştığında ilgili başka eklentiyi işaret eder,
aksi hâlde bu eklentinin uygun bir sonraki becerisini önerir.

## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar; mahkeme (Yargıtay / Danıştay /
  Anayasa Mahkemesi / Bölge Adliye Mahkemesi / Bölge İdare Mahkemesi), daire, **esas ve
  karar numarası**, tarih ve doğrulanabilir kaynak ile verilir
  (ör. `karararama.yargitay.gov.tr`, `karararama.danistay.gov.tr`,
  `kararlarbilgibankasi.anayasa.gov.tr`, `mevzuat.gov.tr`, UYAP Emsal).
  **Model hafızasından karar numarası ÜRETME.** Emin olunmayan her künye `[doğrulanacak]`
  olarak işaretlenir.
- **Mevzuat** madde / fıkra / bent ile gösterilir (ör. "TBK m.49/1", "HMK m.114/1-ç").
- **Doktrin** yalnızca kullanıcı kaynağı sağladığında veya lisanslı canlı erişim
  belgelendiğinde kullanılır; yazar, eser, baskı ve sayfa ile.
- Varsayımlar açıkça **"varsayım"** diye işaretlenir; sahte kesinlik üretilmez.
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
"""


def kaltstart_bloku():
    return """## Soğuk başlangıç (intake)

Başta yalnızca bir sonraki adım için zorunlu olanı sor. Materyal varsa onunla çalış ve
yalnızca belirleyici olan tek soruyu sor.

1. **Rol ve hedef:** Kim soruyor (avukat, hukuk müşaviri, taraf, şirket, kurum) ve
   istenen çıktı ne (mütalaa, dilekçe, tablo, kontrol listesi, sözleşme, e-posta)?
2. **Olay:** Çekişmesiz olgular, çekişmeli noktalar ve eksikler neler?
3. **Süreler:** Hak düşürücü süre, zamanaşımı, tebligat, duruşma, itiraz süresi var mı?
4. **Belgeler:** Hangi sözleşme, tebligat, bilirkişi raporu, tapu, ekstre, e-posta var?
5. **Biçim:** Ne kadar ayrıntı, kim için, hangi üslup ve atıf düzeniyle?
"""


# --------------------------------------------------------------------------
# Sessiz yükleme + üslup başlığı (yalnızca genel-bakış router becerisinde)
# --------------------------------------------------------------------------

def router_konversasyon():
    return """## Konuşma üslubu: kısa başla, hızla belgeye in

Bu beceri bir giriş kapısıdır: kullanıcı çoğunlukla dosyasıyla gelen bir hukukçudur ve
çalışma planı ister, ders değil. İlk yanıtta olayı yerine oturt; yalnızca cevabı sonraki
adımı gerçekten değiştirecek soruyu sor, gerisini `[netleştirilecek: …]` yer tutucusuyla
bırakıp ilk taslağa geç. Ayrıntı, iş ürünü gerektiriyorsa verilir: gerçek altlama,
tablo, kronoloji, risk ve ispat yükü analizi, dilekçe veya mütalaa metni. Gerekçe bu
ürünün parçasıdır; madde tekrarı ve kendini tanıtma değildir.
"""


def sessiz_yukleme_bloku():
    return """### 0. Sessiz yükleme — bağlam yazısı olmadan materyal

Kullanıcı yalnızca bir belge, ekran görüntüsü, tablo, ZIP veya dosya yığını yükleyip görev
yazmazsa, yüklemeyi iş emri say. Prompt bekleme. Dikkatli bir hukuki yardımcı gibi çalış:
önce aceleyi sabitle, sonra materyali yerine oturt, sonra en iyi sonraki adımı öner.

Önce süre ve aciliyet taraması, çünkü kaçırılan bir süre geri alınamaz: görünür tebligat,
duruşma, ödeme/itiraz süresi, zamanaşımı veya hak düşürücü süre varsa yanıt
`Süre uyarısı: ...` ile başlar; son gün, kalan gün sayısı ve süre dolmuşsa bu açıkça
yazılır. Ardından yanıtta şunlar bulunur:

- **Materyal sınıflaması:** tek cümleyle ne olduğu (dava dilekçesi, karar, sözleşme,
  tebligat, ihbarname, bilirkişi raporu, ekstre, UYAP belgesi, tapu, e-posta).
- **Bağlam çıpaları:** gönderen, muhatap, esas/karar no, mahkeme/kurum/karşı taraf, tarih,
  görülebilir yaşam olayı; okunamayan kısım açıkça belirtilir.
- **Hukuki konu:** materyalin bağlandığı hukuk dalı, norm grubu veya çalışma modu.
- **Yönlendirme:** bu eklentiden uygun uzman beceri; isabet netse o yönde çalış, birden çok
  yol varsa bir birincil yol ve en çok iki alternatif.
"""


# --------------------------------------------------------------------------
# Genel-bakış (router) becerisi
# --------------------------------------------------------------------------

def build_router(plugin, beceriler):
    slug = plugin["slug"]
    baslik = plugin["baslik"]
    aciklama = plugin["aciklama"]
    kanunlar = ", ".join(plugin.get("kanunlar", [])) or "ilgili mevzuat"

    rows = "\n".join(
        f"| `{b['slug']}` | {b['aciklama']} |"
        for b in beceriler
    )

    desc = (
        f"{baslik} eklentisine giriş, hızlı triyaj ve iş akışı yönlendirmesi. "
        f"Rol, hedef, süre, belge, risk ve istenen çıktıyı sorar; bu eklentideki uygun "
        f"uzman becerileri önerir ve net bir çalışma planına bağlar. Bağlam yazısı olmadan "
        f"belge yüklendiğinde bağımsız tepki verir: materyali sınıflar, süre/aciliyet "
        f"taraması yapar, uygun uzman beceriye yönlendirir ya da tek bir belirleyici soru sorar."
    )

    return f"""---
name: genel-bakis
description: "{desc}"
---

{router_konversasyon()}

# {baslik} — Genel Bakış

Bu genel-bakış becerisi **{baslik}** eklentisinin hızlı giriş kapısıdır. Resepsiyon,
triyaj, proje yönetimi ve kalite kontrolü tek yerde: önce kısaca netleştir, sonra doğru
çalışma yolunu seç, sonra bu eklentinin uygun uzman becerilerini öner.

**Eklenti odağı:** {aciklama}
**Başat mevzuat:** {kanunlar}

{sessiz_yukleme_bloku()}

### 1. 60 saniyede intake

Kullanıcının verdiğini görünür biçimde özetle; yeniden sorma.

| Nokta | Soru | Neden önemli? |
|---|---|---|
| Rol | Kim soruyor: avukat, müşavir, taraf, şirket, kurum? | Bakış açısı ve üslubu belirler. |
| Hedef | Sonunda ne olmalı: inceleme, dilekçe, mütalaa, kontrol listesi, sözleşme? | Çıktıyı baştan doğru kurar. |
| Olay | Ne oldu, taraflar kim, hangi tarih ve tutarlar kesin? | Havada iş kurmamak için. |
| Süreler | Süre, tebligat, itiraz, dava açma, zamanaşımı, kapanış tarihi var mı? | Acele işleri önce sabitler. |
| Belgeler | Hangi dosya, tapu, tebligat, sözleşme, tablo, e-posta var? | Tahmin değil dosya çalışması. |
| Risk | Sorumluluk, zamanaşımı, idari para cezası, ceza, masraf riski nerede? | Öncelik ve ihtiyatı ayarlar. |
| Biçim | Ne kadar ayrıntı, kime, hangi üslup ve atıf düzeniyle? | Sonucu doğrudan kullanılır kılar. |

### 2. Hızlı triyaj

1. **Süre kontrolü:** Süreler, görev/yetki, şekil şartları ve dönülemez adımları işaretle.
2. **Olay çekirdeği:** 3–7 cümlede kesin / çekişmeli / eksik ayrımını sabitle.
3. **Çalışma modu seç:** kısa inceleme, derin analiz, belge taslağı, müzakere stratejisi,
   dosya çıkarımı, red-team veya müvekkil iletişimi.
4. **Uzman beceri öner:** Bu eklentiden 2–5 uygun beceriyi gerekçesiyle ver.
5. **Sonraki adım:** Bir beceri net uyuyorsa onunla devam et; birkaçı uyuyorsa kısa seçim sun.
6. **Kalite kapısı:** Sonda kaynak, süre, varsayım, açık olgu ve sonraki eylemi denetle.

### 3. Bu eklentideki uzman beceriler

| Beceri | Ne zaman? |
|---|---|
{rows}

### 4. Yönlendirme kuralları

- **Önce bu eklentinin becerilerini** öner. Konu görünür biçimde başka dala taşıyorsa
  ilgili diğer eklentiyi (ör. `hukuk-metodolojisi`, `atif-turk-hukuku`,
  `hukuk-muhakemesi`, `icra-iflas-hukuku`) köprü olarak an,
- Hiçbir zaman yalnızca beceri adı verme; **ne için, ne zaman, hangi girdi eksik, çıktı ne**
  olduğunu da söyle.
- Dosya büyük/dağınıksa önce bir dosya/tablo/triyaj becerisi öner, sonra maddi inceleme.
- Güncel mevzuat/içtihat/idari uygulama gerekiyorsa açıkça kaynak ve güncellik kontrolü planla.

## Kalite sözü

- Varsayımları görünür ve kısa tut.
- Bitirmeden önce bu eklentinin uygun uzman becerilerini öner.
- Sonda her zaman net bir sonraki adım ver.
{kaynak_footer(slug)}"""


# --------------------------------------------------------------------------
# Uzman beceri (ajan gövdesi varsa onu, yoksa şablon)
# --------------------------------------------------------------------------

def build_skill(plugin, beceri):
    slug = plugin["slug"]
    b_slug = beceri["slug"]
    ad = beceri.get("ad", b_slug)
    aciklama = beceri.get("aciklama", "").replace('"', "'")
    govde = (beceri.get("govde_md") or "").strip()
    kanunlar = ", ".join(plugin.get("kanunlar", [])) or "ilgili mevzuat"

    if not govde:
        govde = f"""# {ad}

## Görev

{beceri.get("aciklama", ad)} Bu beceri **{plugin['baslik']}** kapsamında ({kanunlar})
yapılandırılmış, aktarılabilir bir iş ürünü üretir.

{kaltstart_bloku()}

## Denetim şeması

Çıktı şu içeriksel kurguyu izlemeli:

1. **Olayı sabitle** — çekişmeli/çekişmesiz olguları ayır, eksik tablosu çıkar.
2. **Hukuki nitelendirme** — başat mevzuat ({kanunlar}); ilgili doğrulanmış içtihat;
   varsa kullanıcı kaynaklı doktrin.
3. **Altlama (subsumtion)** — üst cümle, tanım/şart, somut olaya uygulama, ara sonuç.
4. **Sonuç ve eylem önerisi** — somut, sorumlu kişi ve süre ile.

## Çıktı modülleri

- Başlıklı, gerekçeli inceleme notu.
- Okunabilirliği artırıyorsa tablo ve kontrol listeleri.
- Gerekiyorsa dilekçe / sözleşme / başvuru iskeleti (`[doldurulacak: …]` yer tutucularıyla).
- Mahkeme, tarih, esas/karar no ve doğrulanabilir bağlantı içeren kaynak listesi.
"""

    return f"""---
name: {b_slug}
description: "{aciklama}"
---

{govde}
{kaynak_footer(slug)}"""


# --------------------------------------------------------------------------
# Referans metodoloji belgesi
# --------------------------------------------------------------------------

def build_reference(plugin, referans_md):
    if referans_md and referans_md.strip():
        return referans_md.strip() + "\n"
    kanunlar = ", ".join(plugin.get("kanunlar", [])) or "ilgili mevzuat"
    return f"""# {plugin['baslik']} — Metodoloji ve Kaynak Notu

## Kapsam

{plugin['aciklama']}

**Başat mevzuat:** {kanunlar}

## Çalışma yöntemi

1. Olayı ve belgeyi merkeze al: olgular, deliller, süreler, görev/yetki ve istenen iş
   ürünü önce netleşir.
2. Hukuki nitelendirmeyi başat mevzuat üzerinden kur; norm-olay altlamasını açık yap.
3. İçtihadı yalnızca doğrulanmış künyeyle kullan (bkz. Kaynak kuralı). Model hafızasından
   karar numarası üretme.
4. Sonucu kullanılabilir biçimde ver: kısa görünüm, denetim yolu, risk ışıkları, eksik
   listesi ve somut sonraki adımlar.

## Kaynak hijyeni

- İçtihat: mahkeme + daire + esas/karar no + tarih + doğrulanabilir kaynak.
- Mevzuat: madde/fıkra/bent.
- Doktrin: yalnızca kullanıcı kaynağı veya lisanslı erişimle; yazar-eser-sayfa.
- Belirsizler `[doğrulanacak]` olarak işaretlenir.
"""


# --------------------------------------------------------------------------
# plugin.json + eklenti README
# --------------------------------------------------------------------------

def build_plugin_json(plugin, pazar):
    obj = {
        "name": plugin["slug"],
        "version": pazar["surum"],
        "description": plugin["aciklama"],
        "license": pazar["lisans"],
        "author": {"name": pazar["sahip"]},
        "homepage": pazar["anasayfa"],
        "keywords": plugin.get("anahtar", []),
    }
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def build_plugin_readme(plugin, beceriler, pazar):
    kanunlar = ", ".join(plugin.get("kanunlar", [])) or "—"
    bsatir = "\n".join(f"- `{b['slug']}` — {b['aciklama']}" for b in beceriler)
    return f"""# {plugin['baslik']}

{plugin['aciklama']}

**Başat mevzuat:** {kanunlar}

**Alan sayfası:** [turk-hukuku.com/beceriler/{plugin['slug']}](https://turk-hukuku.com/beceriler/{plugin['slug']}/) ·
Terminal kullanmıyorsanız aynı beceriler [masaüstü uygulamasında](https://turk-hukuku.com/uygulama/) da var.

## Beceriler

- `genel-bakis` — Giriş, triyaj ve yönlendirme (önce bunu çalıştırın).
{bsatir}

## Kullanım

```
/plugin install {plugin['slug']}@{pazar['ad']}
```

Eklenti kurulduktan sonra Claude'a olayınızı anlatın ya da belgeyi yükleyin; `genel-bakis`
becerisi sizi uygun uzman beceriye yönlendirir.

---

> ⚠️ **Sorumluluk reddi:** Bu eklenti deneyseldir ve **hukuki danışmanlık değildir**.
> Çıktılar yürürlükteki mevzuat ve doğrulanmış içtihatla teyit edilmelidir. Nihai
> sorumluluk yetkili hukukçudadır. Ayrıntı için kökteki `SORUMLULUK-REDDI.md`.
"""


# --------------------------------------------------------------------------
# Yedek (fallback) beceri seti — ajan içeriği yoksa
# --------------------------------------------------------------------------

def default_beceriler(plugin):
    return [
        {"slug": "temel-kavramlar-ve-sistem",
         "ad": "Temel Kavramlar ve Sistematik",
         "aciklama": f"{plugin['baslik']} alanının temel kavramları, sistematiği ve "
                     f"başat normlarının haritası; hızlı oryantasyon ve doğru norm seçimi."},
        {"slug": "denetim-semasi",
         "ad": "Denetim Şeması",
         "aciklama": f"{plugin['baslik']} için adım adım inceleme/denetim şeması: şartlar, "
                     f"istisnalar, ispat yükü ve ara sonuçlar."},
        {"slug": "dava-ve-yol-haritasi",
         "ad": "Dava ve Yol Haritası",
         "aciklama": f"{plugin['baslik']} uyuşmazlıklarında görev/yetki, dava türü, deliller "
                     f"ve aşamalar; strateji ve risk haritası."},
        {"slug": "dilekce-ve-belge-taslagi",
         "ad": "Dilekçe ve Belge Taslağı",
         "aciklama": f"{plugin['baslik']} kapsamında dilekçe, sözleşme veya başvuru "
                     f"iskeleti; vakıa-hukuki sebep-talep mimarisi ve yer tutucular."},
        {"slug": "sureler-ve-zamanasimi",
         "ad": "Süreler ve Zamanaşımı",
         "aciklama": f"{plugin['baslik']} alanında zamanaşımı, hak düşürücü süre, dava ve "
                     f"itiraz süreleri; süre takvimi ve risk uyarıları."},
        {"slug": "ictihat-ve-mevzuat-arama",
         "ad": "İçtihat ve Mevzuat Arama",
         "aciklama": f"{plugin['baslik']} için doğrulanabilir içtihat ve güncel mevzuat "
                     f"arama yol haritası; künye doğrulama ve kaynak hijyeni."},
    ]


# --------------------------------------------------------------------------
# Kök README + SKILLS dizini + marketplace.json
# --------------------------------------------------------------------------

def build_marketplace(pazar, eklentiler):
    obj = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": pazar["ad"],
        "description": pazar["aciklama"],
        "owner": {"name": pazar["sahip"]},
        "plugins": [
            {
                "name": e["slug"],
                "source": f"./{e['slug']}",
                "description": e["aciklama"],
                "version": pazar["surum"],
                "author": {"name": pazar["sahip"]},
            }
            for e in eklentiler
        ],
    }
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def build_root_readme(pazar, gruplar, eklentiler, skill_counts):
    toplam_eklenti = len(eklentiler)
    toplam_beceri = sum(skill_counts.values())
    kurulum = pazar.get("kurulum_yolu", "aydincan/turk-hukuku-ve-claude")

    # grup grup tablo
    bloklar = []
    for gkey, gad in gruplar.items():
        gege = [e for e in eklentiler if e["grup"] == gkey]
        if not gege:
            continue
        satirlar = "\n".join(
            f"| `{e['slug']}` | [{e['baslik']}](https://turk-hukuku.com/beceriler/{e['slug']}/) | {e['aciklama']} |"
            for e in gege
        )
        bloklar.append(f"### {gad}\n\n| Eklenti | Başlık | Açıklama |\n|---|---|---|\n{satirlar}\n")
    katalog = "\n".join(bloklar)

    return f"""# {pazar['baslik']}

> **{pazar['baslik']}** — Türk hukuku için deneysel bir Claude Code beceri (skill)
> koleksiyonu. Avukat, hukuk müşaviri, hâkim/savcı adayı, akademisyen ve hukuk öğrencisi
> için metodoloji, atıf hijyeni, sözleşme, dava ve mütalaa iş akışları.

{pazar['aciklama']}

**{toplam_eklenti} eklenti · {toplam_beceri} beceri · {pazar['lisans']}**

**Yazar:** {pazar['sahip']}

> *{pazar.get('ithaf', '')}*

> **Terminal kullanmıyor musunuz?** Aynı beceriler ve resmî kaynak bağlantısı, Mac ve Windows
> için bir [masaüstü uygulamasında](https://turk-hukuku.com/uygulama/) da var: indirin, yapay
> zekâ anahtarınızı ekleyin, sorun. Tüm hukuk alanları ve rehberler: [turk-hukuku.com](https://turk-hukuku.com/).

---

## ⚠️ Önce bunu okuyun

Bu proje **hukuki danışmanlık değildir** ve **denenmiş bir ürün değildir** — denemek için
teknik bir oyun alanıdır. Çıktılar **yürürlükteki mevzuat ve doğrulanmış güncel içtihatla**
teyit edilmelidir. Avukat-müvekkil sırrı (TCK m.285-286, 1136 s.K.), KVKK (6698),
yurt dışı veri aktarımı ve mesleki yükümlülükler bakımından dağıtımın kendi durumunuza
uygunluğunu **bağımsız olarak** denetleyin. Ayrıntı: [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md).

## Kurulum

### Claude Code (terminal)

```bash
/plugin marketplace add https://github.com/{kurulum}
/plugin install <eklenti-adı>@{pazar['ad']}
```

Örnek:

```bash
/plugin install hukuk-metodolojisi@{pazar['ad']}
/plugin install borclar-hukuku-genel@{pazar['ad']}
```

Ayrıntılı kurulum (Claude Desktop dâhil) için [`KURULUM.md`](./KURULUM.md).

## Nasıl çalışır?

1. **Önce temel eklentileri yükleyin:** [`hukuk-metodolojisi`](./hukuk-metodolojisi) ve
   [`atif-turk-hukuku`](./atif-turk-hukuku) — yöntem ve kaynak hijyeni tüm alanların
   zeminidir.
2. **Çalışma alanınıza uyan uzmanlık eklentilerini** etkinleştirin.
3. **Olayı anlatın veya dosyayı yükleyin** (sessiz yükleme desteklenir).
4. Her eklentinin `genel-bakis` becerisi sizi triyajdan geçirir ve uygun uzman beceriye
   yönlendirir.
5. **Çıktı**: gerekçeli mütalaa, dilekçe/sözleşme taslağı, kontrol listesi veya yapılandırılmış analiz.

## Kaynak hijyeni (projenin omurgası)

Her beceri katı bir kaynak kuralına uyar:

- **İçtihat asla model hafızasından zikredilmez.** Her karar mahkeme + daire +
  **esas/karar no** + tarih + doğrulanabilir kaynakla verilir; emin olunmayan künye
  `[doğrulanacak]` işaretlenir.
- **Mevzuat** madde/fıkra/bent ile; **doktrin** yalnızca kullanıcı kaynağıyla.

## Örnek dosyalar

[`ornek-dosyalar/`](./ornek-dosyalar) altında, eklentileri gerçekçi bir olayla denemek için
hazırlanmış **kurgusal ve anonim** örnek dava dosyaları bulunur — iş alacağı, kira/tahliye,
ayıplı mal, **vergi davaları** (re'sen tarhiyat), ceza soruşturması, boşanma, karşılıksız çek
ve KVKK veri ihlali. Hepsi yalnızca eğitim/deneme amaçlıdır.

## Eklenti kataloğu

{katalog}

## Yazar ve lisans

**Yazar / telif sahibi:** {pazar['sahip']}

Bu proje **{pazar['lisans']}** koşullarıyla sunulur. Telif © 2026 {pazar['sahip']}.
Bkz. [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT), [`NOTICE`](./NOTICE).

> "Claude" Anthropic'in markasıdır; bu proje Anthropic ile resmî olarak ilişkili değildir.
"""


def build_skills_index(gruplar, eklentiler, content):
    lines = ["# Beceri Dizini (SKILLS.md)\n",
             "Her eklentinin `genel-bakis` (giriş/triyaj/yönlendirme) becerisi vardır; "
             "aşağıda uzman beceriler listelenir.\n"]
    for gkey, gad in gruplar.items():
        gege = [e for e in eklentiler if e["grup"] == gkey]
        if not gege:
            continue
        lines.append(f"\n## {gad}\n")
        for e in gege:
            slug = e["slug"]
            beceriler = (content.get(slug, {}) or {}).get("beceriler") or default_beceriler(e)
            lines.append(f"\n### `{slug}` — {e['baslik']}\n")
            lines.append(f"- `genel-bakis` — Giriş, triyaj ve yönlendirme")
            for b in beceriler:
                lines.append(f"- `{b['slug']}` — {b['aciklama']}")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Ana akış
# --------------------------------------------------------------------------

def main():
    cat = load_json(CATALOG)
    content = load_json(CONTENT, default={}) or {}
    pazar = cat["pazar"]
    gruplar = cat["gruplar"]
    eklentiler = cat["eklentiler"]

    skill_counts = {}

    for e in eklentiler:
        slug = e["slug"]
        c = content.get(slug, {}) or {}
        beceriler = c.get("beceriler") or default_beceriler(e)
        skill_counts[slug] = len(beceriler) + 1  # + genel-bakis

        base = os.path.join(ROOT, slug)
        # eski/yetim beceri dizinlerini temizle (idempotent üretim)
        shutil.rmtree(os.path.join(base, "skills"), ignore_errors=True)
        # plugin.json
        write(os.path.join(base, ".claude-plugin", "plugin.json"),
              build_plugin_json(e, pazar))
        # README
        write(os.path.join(base, "README.md"),
              build_plugin_readme(e, beceriler, pazar))
        # reference
        write(os.path.join(base, "references", f"{slug}-metodoloji.md"),
              build_reference(e, c.get("referans_md")))
        # router skill
        write(os.path.join(base, "skills", "genel-bakis", "SKILL.md"),
              build_router(e, beceriler))
        # specialist skills
        for b in beceriler:
            write(os.path.join(base, "skills", b["slug"], "SKILL.md"),
                  build_skill(e, b))

    # marketplace.json
    write(os.path.join(ROOT, ".claude-plugin", "marketplace.json"),
          build_marketplace(pazar, eklentiler))
    # kök README + SKILLS
    write(os.path.join(ROOT, "README.md"),
          build_root_readme(pazar, gruplar, eklentiler, skill_counts))
    write(os.path.join(ROOT, "SKILLS.md"),
          build_skills_index(gruplar, eklentiler, content))

    print(f"Üretildi: {len(eklentiler)} eklenti, {sum(skill_counts.values())} beceri "
          f"(genel-bakis dâhil).")
    print(f"İçerik kaynağı: {'content.json' if content else 'YALNIZCA ŞABLON (yedek)'}")


if __name__ == "__main__":
    main()
