---
name: dilekce-sablonlari
description: "Tutuklamaya itiraz, tahliye/adli kontrol talebi ve istinaf başvurusu için usule uygun, doldurulabilir dilekçe iskeletleri gerektiğinde kullanılır; süre ve dayanak maddeleriyle birlikte olaya uyarlanır."
---

# Dilekçe Şablonları — Ceza Muhakemesi

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
- `[doğrulanacak]` işaretli içtihat yeri (varsa).

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
