---
name: temel-kavramlar-ve-sistem
description: "Kıymetli evrakın türlerini, kambiyo senedi kavramını ve genel ilkeleri ayırt etmek; bir belgenin kıymetli evrak/kambiyo senedi olup olmadığını ve hangi rejime tabi olduğunu belirlemek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Önüne gelen belgenin kıymetli evrak olup olmadığını, eğer öyleyse hangi tür (nama, emre, hamiline) ve hangi alt rejim (kambiyo senedi / diğer) içinde bulunduğunu belirlemek; çek-bono-poliçe ayrımını ve uygulanacak temel normları sabitlemek.

## Soğuk başlangıç (intake)
- Belge fiziken hangi senet tipi olarak adlandırılmış (çek, bono/senet, poliçe) ve metinde bu kelime geçiyor mu?
- Senet emre mi, nama mı, hamiline mi düzenlenmiş; üzerinde "emre" veya "emre yazılı değildir" kaydı var mı?
- Bedel, vade, taraflar, imza ve tanzim yeri-tarihi okunabiliyor mu; eksik unsur var mı?
- Belge alacaklı için takip mi, müvekkil için savunma mı amaçlanıyor?

## Denetim şeması
1. Kıymetli evrak tanımı: hak senetten ayrı ileri sürülemiyor/devredilemiyorsa kıymetli evraktır (TTK m.645). Salt ispat belgesi (örn. adi senet, makbuz) bu kapsamda değildir.
2. Tür tayini: senedin devir biçimi nama (m.654), emre (m.824 vd. genel; kambiyoda m.681) ya da hamiline (m.658) midir? Çek ve bono emre senet olarak doğar, aksi kayıtla nama dönüşebilir.
3. Kambiyo senedi süzgeci: senet çek (m.780), bono (m.776) veya poliçe (m.671) tanımına ve şekil şartlarına uyuyor mu? Uyuyorsa kambiyo hukukunun sertleştirilmiş rejimi (mücerretlik, müteselsil sorumluluk, kambiyo takibi) devreye girer.
4. Ara sonuç — eksiklik: zorunlu unsur eksikse kambiyo vasfı yoktur (m.672/m.777/m.781); senet yalnızca adi yazılı delil olur, kambiyo takibi yapılamaz. Beyaz/açık senet ise anlaşmaya aykırı doldurma def'i (m.680) gündeme gelir; ispat yükü bunu ileri sürene aittir.
5. İlke seti: mücerretlik (sebepten soyutluk), şekle bağlılık, kambiyo taahhütlerinin bağımsızlığı (m.677) ve müteselsil sorumluluk (m.724) sonuçlarını not et.

## Çıktı modülleri
- Senet niteliği değerlendirme notu (tip + rejim + dayanak madde).
- Eksik/kusurlu unsur listesi ve kambiyo vasfına etkisi.
- Uygulanacak temel norm haritası (TTK ilgili maddeleri + gerekiyorsa 5941).

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
