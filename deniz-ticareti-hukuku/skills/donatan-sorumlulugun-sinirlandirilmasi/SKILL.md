---
name: donatan-sorumlulugun-sinirlandirilmasi
description: "Donatan/gemi işletme müteahhidinin deniz alacaklarına karşı sorumluluğunu küresel olarak sınırlandırması (LLMC sınırlı sorumluluk fonu) ya da alacaklının bu sınırı aşmaya çalışması söz konusu olduğunda kullan."
---

# Donatanın Sorumluluğu ve Sınırlandırılması

## Görev
Donatanın deniz alacaklarına karşı topluca (global) sorumluluğunu sınırlandırma hakkını değerlendirmek; sınırlı sorumluluk fonunun kurulması ve dağıtımını planlamak veya alacaklı adına sınırın aşılabileceği halleri araştırmak.

## Soğuk başlangıç (intake)
- Talepler hangi nitelikte (yük, can/beden, liman tesisi zararı, kirlilik)?
- Donatan/gemi işletme müteahhidi sıfatı kimde; geminin tonajı (gros ton) nedir?
- Sınırlandırmaya tabi olmayan veya sınırı kaldıran bir kusur (kasıt/pervasızlık) iddiası var mı?
- Fon kurulacak mı; başka ülkede paralel takip/fon var mı?

## Denetim şeması
1. **Sorumluluğun temeli**: Donatanın gemi adamlarının kusurundan sorumluluğunu (TTK m.1062) ve gemi işletme müteahhidinin konumunu (TTK m.1065) belirle.
2. **Sınırlandırmaya tabi alacaklar**: Hangi alacakların topluca sınırlandırmaya tabi olduğunu (TTK m.1328 vd., 1976 LLMC esaslı) tespit et; mürettebat alacakları, kurtarma ücreti ve bazı kirlilik alacakları gibi sınır dışı kalanları ayır.
3. **Sınır miktarı (fon)**: Geminin tonajına göre, can zararı ve diğer zararlar için ayrı limit dilimlerini hesapla; sınırlı sorumluluk fonunun kurulması, fona başvuru ve dağıtım sırasını belirt.
4. **Sınırın kalkması**: Zararın, donatanın bizzat **kasten veya pervasızca ve muhtemelen böyle bir zararın doğacağı bilinciyle** yaptığı fiilden doğduğu ispatlanırsa sınırlandırma hakkı düşer; bu yüksek eşiği değerlendir.
5. **İspat ve ara sonuç**: Sınırlandırma hakkını donatan ileri sürer; sınırın kalkmasını iddia eden alacaklı ağır kusuru ispatlar. Çıktıda fon tutarını, sınır dışı alacakları ve sınırın aşılma ihtimalini gerekçeli sonuca bağla.

## Çıktı modülleri
- Sınırlandırmaya tabi/sınır dışı alacaklar tablosu
- Tonaja göre fon limiti hesap taslağı
- Fon kurma veya sınırı aşma strateji notu

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
