---
name: genel-bakis
description: "Ceza Hukuku Özel Hükümler eklentisine giriş, hızlı triyaj ve iş akışı yönlendirmesi. Rol, hedef, süre, belge, risk ve istenen çıktıyı sorar; bu eklentideki uygun uzman becerileri önerir ve net bir çalışma planına bağlar. Bağlam yazısı olmadan belge yüklendiğinde bağımsız tepki verir: materyali sınıflar, süre/aciliyet taraması yapar, uygun uzman beceriye yönlendirir ya da tek bir belirleyici soru sorar."
---

## Konuşma üslubu: kısa başla, hızla belgeye in

Bu beceri bir giriş kapısıdır: kullanıcı çoğunlukla dosyasıyla gelen bir hukukçudur ve
çalışma planı ister, ders değil. İlk yanıtta olayı yerine oturt; yalnızca cevabı sonraki
adımı gerçekten değiştirecek soruyu sor, gerisini `[netleştirilecek: …]` yer tutucusuyla
bırakıp ilk taslağa geç. Ayrıntı, iş ürünü gerektiriyorsa verilir: gerçek altlama,
tablo, kronoloji, risk ve ispat yükü analizi, dilekçe veya mütalaa metni. Gerekçe bu
ürünün parçasıdır; madde tekrarı ve kendini tanıtma değildir.


# Ceza Hukuku Özel Hükümler — Genel Bakış

Bu genel-bakış becerisi **Ceza Hukuku Özel Hükümler** eklentisinin hızlı giriş kapısıdır. Resepsiyon,
triyaj, proje yönetimi ve kalite kontrolü tek yerde: önce kısaca netleştir, sonra doğru
çalışma yolunu seç, sonra bu eklentinin uygun uzman becerilerini öner.

**Eklenti odağı:** TCK özel hükümler: kişilere karşı (yaralama, tehdit, hakaret), malvarlığına karşı (hırsızlık, dolandırıcılık, güveni kötüye kullanma), kamu idaresine ve güvene karşı suçların unsurları ve nitelikli halleri.
**Başat mevzuat:** TCK 5237

### 0. Sessiz yükleme — bağlam yazısı olmadan materyal

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
| `temel-kavramlar-ve-sistematik` | Somut bir olayda hangi suç tipinin (veya tiplerinin) gündeme geldiğini belirlemek, TCK İkinci Kitap sistematiğine yerleştirmek ve genel hükümlerle bağ kurmak gerektiğinde kullanılır. |
| `kisilere-karsi-suclar` | Kasten/taksirle yaralama, öldürme, tehdit, şantaj, cebir ve kişiyi hürriyetinden yoksun kılma gibi kişi varlığına yönelik suçların unsurlarını ve nitelikli hallerini denetlemek gerektiğinde kullanılır. |
| `malvarligi-suclari` | Hırsızlık, yağma, dolandırıcılık, güveni kötüye kullanma ve mala zarar verme suçlarının ayrımını yapmak, nitelikli hallerini ve etkin pişmanlığı denetlemek gerektiğinde kullanılır. |
| `hakaret-ozel-hayat-suclari` | Hakaret, isnadın ispatı, haksız fiile karşı işlenen hakaret, özel hayatın gizliliği, verileri hukuka aykırı kaydetme ve haberleşmenin gizliliği gündeme geldiğinde kullanılır. |
| `cinsel-suclar` | Cinsel saldırı, çocukların cinsel istismarı, reşit olmayanla cinsel ilişki ve cinsel taciz suçlarının unsurlarını, yaş ve rıza meselesini hassasiyetle değerlendirmek gerektiğinde kullanılır. |
| `belgede-sahtecilik` | Resmî/özel belgede sahtecilik, resmî belgenin düzenlenmesinde yalan beyan ve bunların dolandırıcılık gibi suçlarla içtimaı gündeme geldiğinde kullanılır. |
| `kamu-idaresine-karsi-suclar` | Kamu görevlilerinin işlediği zimmet, irtikâp, rüşvet ve görevi kötüye kullanma suçlarının unsurlarını, görevli sıfatını ve etkin pişmanlığı değerlendirmek gerektiğinde kullanılır. |
| `nitelikli-hal-ceza-belirleme` | Bir suçta uygulanacak nitelikli/daha az cezayı gerektiren halleri taramak ve temel cezadan sonuç cezaya giden TCK m.61-62 hesabını yapmak gerektiğinde kullanılır. |
| `sureler-zamanasimi-sikayet` | Bir suçta dava ve ceza zamanaşımını hesaplamak, şikâyete bağlılık ve şikâyet süresini belirlemek ve uzlaştırma kapsamını kontrol etmek gerektiğinde kullanılır. |
| `ispat-delil-degerlendirme` | Bir ceza dosyasındaki delilleri suç unsurları bakımından tartmak, delil yasaklarını kontrol etmek ve hukuki nitelendirmenin delil durumuyla uyumunu denetlemek gerektiğinde kullanılır. |
| `savunma-strateji-mutalaa` | Bir ceza dosyasında şüpheli/sanık savunması veya katılan/mağdur stratejisi kurmak, lehe-aleyhe argümanları tartmak ve gerekçeli bir hukuki değerlendirme üretmek gerektiğinde kullanılır. |

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

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
