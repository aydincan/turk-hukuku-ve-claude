---
name: cinsel-suclar
description: "Cinsel saldırı, çocukların cinsel istismarı, reşit olmayanla cinsel ilişki ve cinsel taciz suçlarının unsurlarını, yaş ve rıza meselesini hassasiyetle değerlendirmek gerektiğinde kullanılır."
---

# Cinsel Dokunulmazlığa Karşı Suçlar

## Görev
Cinsel dokunulmazlığa karşı suçlarda doğru tipi belirlemek, yaş ve rıza eşiklerini, nitelikli halleri ve delil hassasiyetlerini madde metniyle değerlendirmek. Bu alan azami özen ve mağdur hassasiyeti gerektirir.

## Soğuk başlangıç (intake)
- Mağdurun yaşı kaç (15 yaş ve altı / 15-18 arası / yetişkin ayrımı belirleyici)?
- Fiil sözle/davranışla taciz mi, bedensel temas mı, vücuda organ/cisim sokma mı?
- Cebir, tehdit, hile veya iradeyi etkileyen başka bir hâl var mı?
- Fail ile mağdur arasında akrabalık, vesayet, eğitim/sağlık/kamu görevi ilişkisi var mı?

## Denetim şeması
1. Yetişkine karşı cinsel saldırı (TCK m.102): Cinsel davranışla vücut dokunulmazlığı ihlali (m.102/1); fiilin vücuda organ/cisim sokma suretiyle işlenmesi nitelikli (m.102/2). Eşe karşı işlenmesinde şikâyet aranır. Nitelikli haller m.102/3 (kamu görevi/vesayet ilişkisi, silah, birden fazla kişi).
2. Çocukların cinsel istismarı (TCK m.103): 15 yaşını tamamlamamış veya tamamlamış olsa da fiilin anlamını algılayamayan çocuklara karşı her türlü cinsel davranış rıza aranmaksızın istismardır. Sarkıntılık düzeyinde kalma ile organ/cisim sokma ayrı cezalandırılır; nitelikli haller cezayı ağırlaştırır.
3. Reşit olmayanla cinsel ilişki (TCK m.104): 15 yaşını bitirmiş çocukla cebir/tehdit/hile olmaksızın rızaen cinsel ilişki; kural olarak şikâyete bağlı, fail-mağdur arasındaki belirli ilişkilerde resen kovuşturma.
4. Cinsel taciz (TCK m.105): Bedensel temas içermeyen, cinsel amaçlı rahatsız edici davranış; iş/aile/hizmet ilişkisinden yararlanma veya teşhir nitelikli hal. Şikâyete bağlı (kamu görevi nüfuzu hali hariç).
5. Rıza ve ehliyet: Yaş eşiğinin altındaki çocukta rıza geçersizdir. İradeyi etkileyen hâller (akıl hastalığı, bilinç kaybı, hile) saldırıyı ağırlaştırır. Hukuka uygunluk sebebi olarak rızanın geçerli olabileceği sınırı dikkatle çiz.
6. İspat ve ara sonuç: Adli/psikiyatrik rapor, beyan tutarlılığı, fizik delil ve yaş tespiti kritiktir. Mağdur beyanının değerlendirilmesinde ilkesel Yargıtay içtihadına atıf yap (karararama.yargitay.gov.tr; künye `[doğrulanacak]`). Uygulanacak madde, şikâyet durumu ve görevli ağır ceza mahkemesini sonuçlandır.

## Çıktı modülleri
- Tip ve nitelikli hal belirleme notu (yaş/rıza/temas düzeyi madde atıflı).
- Delil ve rapor değerlendirme listesi (mağdur hassasiyetiyle).
- Şikâyet/resen kovuşturma ve görev özeti.

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
