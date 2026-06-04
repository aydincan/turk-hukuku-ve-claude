---
name: dava-dilekcesi-mimarisi
description: "HMK m.119'a uygun, zorunlu unsurları eksiksiz bir dava dilekçesi taslamak; vakıa-hukuki sebep-talep sonucu yapısını kurmak, delilleri vakıalarla bağlamak ve eksik unsurlardan doğan reddi önlemek için."
---

# Dava Dilekçesi Mimarisi (HMK m.119)

## Görev
HMK m.119'un zorunlu unsurlarını taşıyan, vakıaları delillerle bağlanmış, talep sonucu açık ve infaza elverişli bir dava dilekçesi iskeleti üretmek.

## Soğuk başlangıç (intake)
- Talep türü ne? (eda / tespit / inşai; terditli/seçimlik/kısmi mi?)
- Dava değeri belirli mi, belirsiz alacak davası (m.107) mı?
- Hangi vakıalar hangi delillerle ispatlanacak?
- Faiz türü ve başlangıç tarihi ne olacak?

## Denetim şeması
1. **Zorunlu unsurlar** (HMK m.119/1): mahkeme adı; tarafların ad-soyad/unvan, adres ve TC/vergi no; varsa vekil bilgisi; davanın konusu ve dava değeri; **vakıaların açık özeti** (a-h bentleri); ileri sürülen her vakıanın **hangi delille ispat edileceği** (m.119/1-f, delil bağlama); **dayanılan hukuki sebepler**; **açık talep sonucu**; imza.
2. **Eksiklik sonucu** (m.119/2): Bazı unsurlardaki eksiklik için bir haftalık kesin süre verilir; tamamlanmazsa dava açılmamış sayılır. Vakıa ve talep sonucu gibi çekirdek unsurlar bu kapsamdadır.
3. **Talep sonucu tasarımı**: Eda davasında miktar/ifa açık; **belirsiz alacak** (m.107) veya **kısmi dava** (m.109) tercihi bilinçli yapılır — belirsiz alacakta sonradan artırım faiz ve zamanaşımı bakımından avantajlıdır.
4. **Delil bağlama disiplini**: Her vakıanın altına dayandığı delil (senet, tanık, bilirkişi, keşif, yemin) yazılır; "her türlü delil" ibaresi tek başına yetersiz sayılabilir; senetle ispat zorunlu vakıada (m.200) tanık delili sınırlıdır.
5. **Harç ve gider avansı**: Dava değerine göre nispi/maktu harç ve gider avansı (m.120) yatırılır; eksikse dava şartı eksikliği (m.114/1-g) doğar.

Ara sonuç: Unsur kontrol listesi tamamlanmadan dilekçe sonuçlandırılmaz.

## Çıktı modülleri
- m.119 unsur kontrol listesi (var/eksik).
- Vakıa–delil eşleştirme tablosu.
- Talep sonucu (faiz/masraf/vekâlet ücreti dâhil) ve [doldurulacak] yer tutucular.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
