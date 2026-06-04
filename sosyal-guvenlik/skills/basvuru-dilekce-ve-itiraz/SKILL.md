---
name: basvuru-dilekce-ve-itiraz
description: "SGK'ya idari başvuru/itiraz, iş mahkemesinde dava ve cevap dilekçeleri ile gelir testi/idari para cezası itiraz metinlerinin taslağı hazırlanması gerektiğinde kullanılır."
---

# Başvuru, Dilekçe ve İtiraz Taslağı

## Görev
Sosyal güvenlik uyuşmazlığına uygun idari başvuru, itiraz ve yargı dilekçelerini doğru yapı ve dayanaklarla taslaklamak; yer tutucu disiplinini korumak.

## Soğuk başlangıç (intake)
- Hangi belge gerekiyor: SGK'ya itiraz, dava dilekçesi, cevap, gelir testi/idari para cezası itirazı mı?
- Taraflar ve statüleri kim (sigortalı, işveren, SGK, hak sahipleri)?
- Talep sonucu net mi (tespit, iptal, aylık bağlanması, alacak)?
- İdari aşama tamamlandı mı; tebliğ ve süre durumu nedir?

## Denetim şeması
1. Tür seçimi: İdari aşamada SGK'ya itiraz/başvuru (5510 m.101); yargıda iş mahkemesinde dava (7036 m.5). Yanlış mercie verilen dilekçe usul riski yaratır.
2. İskelet — HMK m.119: Dava dilekçesinde mahkeme, taraflar, konu, vakıalar, hukuki sebepler, deliller ve talep sonucu eksiksiz yer alır; cevapta HMK m.129 unsurları.
3. Dayanak yerleştirme: İlgili 5510 maddeleri (statüye/uyuşmazlığa göre m.4, m.13, m.21, m.28, m.41, m.60, m.80, m.86, m.93) ve usul (7036, HMK) doğru atıfla bağlanır.
4. Delil bağlama: Her vakıaya delil iliştirilir; SGK'dan getirtilecek belgeler ve tanıklar dilekçede gösterilir.
5. Yer tutucu disiplini: Bilinmeyen tarih/tutar/ad alanları `[doldurulacak]` ile işaretlenir; uydurma rakam/künye girilmez. Ara sonuç: gönderime hazır taslak iskeleti.

## Çıktı modülleri
- Seçilen tür için dilekçe/itiraz iskeleti.
- Dayanak madde ve delil bloğu.
- `[doldurulacak]` alan listesi ve ek belge kontrol listesi.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
