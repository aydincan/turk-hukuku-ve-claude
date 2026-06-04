---
name: kabahat-suc-ayrimi-ve-ictima
description: "Aynı fiilin hem kabahat hem suç oluşturduğu, ya da birden çok kabahatin birleştiği durumlarda fikri içtima, zincirleme kabahat ve mükerrer cezalandırma yasağını çözümlemek gerektiğinde kullanılır."
---

# Kabahat-Suç Ayrımı ve İçtima

## Görev
Bir fiilin hem kabahat hem suç sayıldığı veya birden çok kabahatin çakıştığı hallerde, hangi yaptırımın uygulanacağını ve mükerrer cezalandırma riskini 5326 m.15 çerçevesinde çözmek.

## Soğuk başlangıç (intake)
- Aynı fiil hem idari yaptırıma hem ceza soruşturmasına mı konu?
- Tek fiil mi, aynı türden birden çok fiil mi (zincirleme) söz konusu?
- Hangi kanunlar devrede (özel kanun kabahati + TCK suçu)?
- Daha önce verilmiş bir ceza/yaptırım var mı (kesinleşme durumu)?

## Denetim şeması
1. **Fikri içtima — kabahat/suç çakışması (5326 m.15/3):** Bir fiil hem kabahat hem suç oluşturuyorsa kural olarak yalnızca **suçtan** dolayı yaptırım uygulanır; suçtan ceza verilemeyen hallerde kabahat yaptırımı devreye girer. Bu, ne bis in idem (aynı fiilden iki kez cezalandırılmama) ile uyumludur.
2. **Bir fiille birden çok kabahat (5326 m.15/1):** En ağır idari para cezası uygulanır; idari tedbirler ayrıca tatbik edilebilir.
3. **Aynı kabahatin birden çok işlenmesi (5326 m.15/2):** Her bir kabahat için ayrı ceza; istisnaları madde metniyle kontrol et.
4. **Suçtan beraat/düşme etkisi:** Suçtan mahkûmiyet dışı bir sonuç çıkarsa kabahat yaptırımı yolunun açık kalıp kalmadığını, zamanaşımıyla birlikte değerlendir (5326 m.15/3, m.20).
5. **Kesinleşme ve ne bis in idem:** Aynı maddi fiil için idari ve adli yaptırımın birlikte uygulanması, AYM/AİHM içtihadında ne bis in idem yönünden tartışmalıdır; ilkesel atıf yapılır, künye `[doğrulanacak]` işaretlenir (kararlarbilgibankasi.anayasa.gov.tr).

İspatta her iki sürecin dosyası karşılaştırılır; fiil kimliği (aynı maddi olay) belirleyicidir.

## Çıktı modülleri
- İçtima nitelendirme notu (m.15 hangi fıkra).
- Mükerrer cezalandırma riski değerlendirmesi.
- Strateji önerisi (hangi yaptırımın akıbeti beklenmeli).

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
