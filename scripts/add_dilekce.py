#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İki eklentinin part dosyasına somut 'dilekçe şablonları' becerisi ekler
(ceza-muhakemesi ve vergi-davalari). Kaynak = part dosyaları olduğundan,
merge_parts.py + generate.py ile kalıcıdır. Idempotent: beceri zaten varsa atlar.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, "scripts", "parts")

CEZA_GOVDE = r"""# Dilekçe Şablonları — Ceza Muhakemesi

## Görev
Tutuklamaya itiraz, tahliye/adli kontrol talebi ve istinaf başvurusu için usule uygun,
doldurulabilir dilekçe iskeletleri sunmak. Şablonlar olaya göre `[doldurulacak: …]`
yer tutucularıyla uyarlanır; künye/karar numarası uydurulmaz.

## Soğuk başlangıç (intake)
- Hangi dilekçe gerekiyor (itiraz / tahliye / adli kontrol / istinaf)?
- Kararı veren merci, tarih ve dosya/sorgu numarası nedir?
- Suç, tutuklama nedeni ve müvekkilin kişisel durumu nedir?
- Süre işliyor mu (itiraz 7 gün — CMK m.268; istinaf 7 gün — CMK m.273)?

## Şablon 1 — Tutuklamaya İtiraz (CMK m.267-271)
```
[KARARI VEREN] SULH CEZA HÂKİMLİĞİNE / ASLİYE/AĞIR CEZA MAHKEMESİNE
(İtirazı incelemeye yetkili mercie sunulmak üzere)

SORUŞTURMA/DOSYA NO : [doldurulacak]
İTİRAZ EDEN ŞÜPHELİ/SANIK : [Ad Soyad] (Kurgusal/gerçek olaya göre)
MÜDAFİ : Av. [Ad Soyad]
KONU : [tarih] tarihli tutuklama kararına itirazımızdan ibarettir.

AÇIKLAMALAR
1. [Yakalama/gözaltı/sorgu sürecinin özeti — doldurulacak].
2. Kuvvetli suç şüphesini gösteren SOMUT delil yoktur (CMK m.100/1): [gerekçe].
3. Tutuklama nedeni gerçekleşmemiştir (CMK m.100/2 — kaçma/delil karartma): [gerekçe].
4. Tedbir ÖLÇÜSÜZDÜR; adli kontrol yeterlidir (CMK m.101/1, m.109; Anayasa m.13).
5. Müvekkilin sabit ikameti/işi/sağlık durumu: [doldurulacak].

HUKUKİ NEDENLER : CMK m.100, 101, 104, 105, 109, 267-271; Anayasa m.13, 19; AİHS m.5.
SONUÇ VE İSTEM : Tutuklama kararının KALDIRILMASINA ve müvekkilin TAHLİYESİNE,
kabul görmezse ADLİ KONTROL uygulanmasına karar verilmesini saygıyla talep ederiz. [tarih]
                                                              Müdafi [imza]
```

## Şablon 2 — Tahliye / Adli Kontrol Talebi (CMK m.104, m.109)
```
[DOSYANIN BULUNDUĞU] MAHKEMESİNE / CUMHURİYET BAŞSAVCILIĞINA

DOSYA NO : [doldurulacak]
TALEP EDEN : [Ad Soyad] — Müdafi Av. [Ad Soyad]
KONU : Tahliye, olmazsa adli kontrol uygulanması talebidir.

AÇIKLAMALAR
1. Tutuklulukta geçen süre ve soruşturmanın geldiği aşama: [doldurulacak].
2. Tutuklama nedenleri ortadan kalkmıştır / hiç oluşmamıştır (CMK m.104).
3. Adli kontrol tedbirleri yeterlidir (CMK m.109/3 — yurt dışı çıkış yasağı, imza, güvence vb.).

SONUÇ : Müvekkilin TAHLİYESİNE, aksi halde uygun ADLİ KONTROL tedbirine karar verilmesini
talep ederiz. [tarih] — Müdafi [imza]
```

## Şablon 3 — İstinaf Başvuru Dilekçesi (CMK m.272 vd.)
```
[KARARI VEREN] MAHKEMESİNE
(… BÖLGE ADLİYE MAHKEMESİ İLGİLİ CEZA DAİRESİNE gönderilmek üzere)

DOSYA / KARAR NO : [doldurulacak]
İSTİNAF EDEN : [Ad Soyad] — Müdafi Av. [Ad Soyad]
KONU : [tarih-sayı] hükmün istinaf incelemesiyle KALDIRILMASI / DÜZELTİLMESİ istemidir.

İSTİNAF SEBEPLERİ
1. Maddi olayın değerlendirilmesinde hata (delil): [doldurulacak].
2. Hukuka aykırılık (CMK m.289 mutlak bozma nedenleri dahil): [doldurulacak].
3. Sübut/vasıf/ceza tayini yönünden hata: [doldurulacak].

HUKUKİ NEDENLER : CMK m.272-281, 289.
SONUÇ : Hükmün KALDIRILARAK [beraat/iade/yeniden hüküm] yönünde karar verilmesini talep
ederiz. Süre: hükmün tefhim/tebliğinden itibaren 7 gün (CMK m.273). [tarih] — Müdafi [imza]
```

## Çıktı modülleri
- Olaya uyarlanmış, yer tutucuları doldurulmuş dilekçe metni.
- Süre kontrolü notu (itiraz/istinaf süreleri ve son gün).
- Dayanak madde listesi ve eklenecek belge dizini.
- `[doğrulanacak]` işaretli içtihat yeri (varsa)."""

VERGI_GOVDE = r"""# Dilekçe Şablonları — Vergi Davaları

## Görev
İhbarnamenin iptali (yürütmeyi durdurma talepli), ödeme emrine itiraz ve istinaf için
usule uygun, doldurulabilir dilekçe iskeletleri sunmak. Süre ve tutar mutlaka kontrol
edilir; künye uydurulmaz.

## Soğuk başlangıç (intake)
- Dava konusu işlem ne (vergi/ceza ihbarnamesi mi, ödeme emri mi)?
- Tebliğ tarihi ve dava açma süresi (genel 30 gün — İYUK m.7; ödeme emri 15 gün — 6183 m.58)?
- Vergi türü, dönem, matrah farkı ve ceza tutarı?
- Yürütmeyi durdurma isteniyor mu (İYUK m.27)?

## Şablon 1 — İhbarname İptali Davası (YD talepli) (İYUK m.2, m.27)
```
… VERGİ MAHKEMESİ BAŞKANLIĞINA
(YÜRÜTMENİN DURDURULMASI TALEPLİDİR)

DAVACI : [Ad/Unvan], VKN/TCKN [doldurulacak], adres
VEKİLİ : Av. [Ad Soyad]
DAVALI : [doldurulacak] Vergi Dairesi Müdürlüğü
TEBLİĞ TARİHİ : [doldurulacak]
D. KONUSU : [tarih-sayı] vergi/ceza ihbarnamesi ile tarh edilen [vergi türü] vergisi
([dönem]) ve [vergi ziyaı/usulsüzlük] cezasının İPTALİ ile İYUK m.27 uyarınca
YÜRÜTMENİN DURDURULMASI istemidir.
TUTAR : [vergi] TL + [ceza] TL.

AÇIKLAMALAR
1. İnceleme/olay özeti: [doldurulacak].
2. Re'sen takdir sebebi oluşmamıştır (VUK m.30): [gerekçe].
3. Matrah farkı somut, hukuken geçerli tespite dayanmamaktadır: [gerekçe].
4. Vergi ziyaı cezası şartları yoktur (VUK m.341, 344); [varsa] tek fiil-tek ceza.
5. İhbarnamenin/tebligatın şekil/usul sakatlığı: [VUK m.35, 93-109 — doldurulacak].
6. YD ŞARTLARI mevcuttur: açık hukuka aykırılık + telafisi güç/imkânsız zarar (İYUK m.27/2).

HUKUKİ NEDENLER : 213 s. VUK; 2577 s. İYUK m.2, 7, 27; [ilgili maddi vergi kanunu].
DELİLLER : İhbarname, vergi inceleme/takdir raporu, defter-belge, [doldurulacak].
SONUÇ VE İSTEM : Öncelikle YÜRÜTMENİN DURDURULMASINA; esastan dava konusu tarhiyat ve
cezanın İPTALİNE; yargılama gideri ve vekâlet ücretinin davalı idareye yükletilmesine
karar verilmesini saygıyla talep ederiz. [tarih] — Davacı Vekili [imza]
```

## Şablon 2 — Ödeme Emrine İtiraz (6183 m.58 / İYUK)
```
… VERGİ MAHKEMESİ BAŞKANLIĞINA

DAVACI / VEKİLİ : [doldurulacak]
DAVALI : [doldurulacak] Vergi Dairesi Müdürlüğü
TEBLİĞ TARİHİ : [doldurulacak]  (Dava süresi: 15 gün — 6183 s.K. m.58)
D. KONUSU : [tarih-sayı] ödeme emrinin İPTALİ istemidir.

AÇIKLAMALAR (6183 m.58 sınırlı itiraz sebepleri)
1. "Böyle bir borç yoktur": [gerekçe — örn. tarhiyat dava konusu/iptal edilmiş].
2. "Borç kısmen ödenmiştir": [gerekçe/dekont].
3. "Borç zamanaşımına uğramıştır": (tahsil zamanaşımı 5 yıl — 6183 m.102) [gerekçe].

HUKUKİ NEDENLER : 6183 s.K. m.58, 102; 2577 s. İYUK.
SONUÇ : Ödeme emrinin İPTALİNE karar verilmesini talep ederiz. [tarih] — Vekil [imza]
```

## Şablon 3 — İstinaf Dilekçesi (İYUK m.45)
```
… BÖLGE İDARE MAHKEMESİ İLGİLİ VERGİ DAVA DAİRESİNE
(… Vergi Mahkemesi aracılığıyla)

KARAR NO : [doldurulacak]   (İstinaf süresi: kararın tebliğinden 30 gün — İYUK m.45)
İSTİNAF EDEN / VEKİLİ : [doldurulacak]
KONU : [tarih-sayı] kararın KALDIRILMASI istemidir.

İSTİNAF SEBEPLERİ
1. Hukuka aykırı değerlendirme: [doldurulacak].
2. Eksik inceleme / delil değerlendirme hatası: [doldurulacak].
3. [varsa] usul hatası.

HUKUKİ NEDENLER : 2577 s. İYUK m.45, 46.
SONUÇ : Kararın KALDIRILARAK davanın kabulüne / [talep] karar verilmesini talep ederiz.
[tarih] — Vekil [imza]
```

## Çıktı modülleri
- Olaya uyarlanmış dilekçe metni (yer tutucular doldurulmuş).
- Süre tablosu (tebliğ → son gün; 30/15 gün ayrımı).
- Tutar ve hesaplama özeti; eklenecek belge dizini.
- `[doğrulanacak]` işaretli içtihat yeri (varsa)."""

YENI = {
    "ceza-muhakemesi": {
        "slug": "dilekce-sablonlari",
        "ad": "Dilekçe Şablonları (Tutuklamaya İtiraz, Tahliye, İstinaf)",
        "aciklama": "Tutuklamaya itiraz, tahliye/adli kontrol talebi ve istinaf başvurusu için "
                    "usule uygun, doldurulabilir dilekçe iskeletleri gerektiğinde kullanılır; "
                    "süre ve dayanak maddeleriyle birlikte olaya uyarlanır.",
        "govde": CEZA_GOVDE,
    },
    "vergi-davalari": {
        "slug": "dilekce-sablonlari",
        "ad": "Dilekçe Şablonları (İhbarname İptali, Ödeme Emrine İtiraz, İstinaf)",
        "aciklama": "Vergi/ceza ihbarnamesinin iptali (yürütmeyi durdurma talepli), ödeme emrine "
                    "itiraz ve istinaf için usule uygun dilekçe iskeletleri gerektiğinde kullanılır; "
                    "dava açma süresi ve tutar kontrolüyle birlikte.",
        "govde": VERGI_GOVDE,
    },
}


def blok(b):
    return (f"<<<BECERI>>>\n"
            f"slug: {b['slug']}\n"
            f"ad: {b['ad']}\n"
            f"aciklama: {b['aciklama']}\n"
            f"<<<GOVDE>>>\n"
            f"{b['govde']}\n")


def main():
    for slug, b in YENI.items():
        path = os.path.join(PARTS, f"{slug}.part.md")
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
        if f"slug: {b['slug']}" in txt:
            print(f"  {slug}: '{b['slug']}' zaten var, atlandı.")
            continue
        idx = txt.rfind("<<<SON>>>")
        if idx == -1:
            txt = txt.rstrip() + "\n" + blok(b) + "<<<SON>>>\n"
        else:
            txt = txt[:idx] + blok(b) + txt[idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"  {slug}: '{b['slug']}' eklendi.")


if __name__ == "__main__":
    main()
