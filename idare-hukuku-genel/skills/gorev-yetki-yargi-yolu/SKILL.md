---
name: gorev-yetki-yargi-yolu
description: "Bir uyuşmazlıkta idari yargı mı adli yargı mı görevli, hangi mahkeme (idare/vergi/Danıştay) ve yer yönünden hangi yer mahkemesi yetkili sorularını çözmek için kullanılır; dava açılmadan önce yol haritası kurarken başvurulur."
---

# Görev, Yetki ve Yargı Yolu Belirleme

## Görev
Uyuşmazlığın idari mi adli yargıda görüleceğini, idari yargı içinde görevli mahkemeyi (idare/vergi mahkemesi/Danıştay) ve yer yönünden yetkili mahkemeyi belirlemek; yanlış yola gitme riskini sıfırlamak.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı idari işlem/eylem/idari sözleşme mi, yoksa özel hukuk ilişkisi mi?
2. Konu vergi/gümrük mü, genel idari mi, kamulaştırma bedeli mi?
3. İşlemi yapan idare nerede; taşınmaz/uygulama yeri neresi?
4. İşlem ilk derecede Danıştay'da mı görülecek nitelikte (belirli düzenleyici işlemler)?

## Denetim şeması
1. **İdari/adli ayrımı.** İdari işlem/eylem/idari sözleşme → idari yargı. İdarenin özel hukuk ilişkileri, kamulaştırma **bedeli**, fiili el atma tazminatı → adli yargı. Tereddütte uyuşmazlık mahkemesi içtihadına başvur (`[doğrulanacak]`).
2. **İdari yargı içi görev.** Vergi/gümrük/benzeri mali yükümlülük uyuşmazlıkları → **vergi mahkemesi**; genel idari uyuşmazlıklar → **idare mahkemesi**; 2575 sayılı Kanun'da sayılan belirli düzenleyici işlemler → ilk derecede **Danıştay**.
3. **Tek hâkim/kurul.** 2576 sayılı Kanun uyarınca belirli parasal sınır altındaki davalar tek hâkimle; üstü kurul halinde. Güncel parasal sınırı teyit et (`[doğrulanacak]`).
4. **Yer yetkisi.** Kural: işlemi/eylemi yapan idarenin bulunduğu yer mahkemesi (İYUK m.32). Taşınmaza, kamu görevlilerine, tam yargıya ilişkin özel yetki kuralları (m.33-36) ayrıdır.
5. **İdari merci tecavüzü.** Önce idari başvuru gerekiyorsa (m.11/m.13) doğrudan dava açılırsa dilekçe ilgili mercie tevdi edilir (m.15/1-e); bunu baştan öngör.
6. **Ara sonuç.** Yargı yolu + görevli mahkeme + yetkili yer + tek hâkim/kurul tespiti; varsa zorunlu ön başvuru uyarısı.

## Çıktı modülleri
- Yargı yolu karar ağacı (idari/adli).
- Görevli mahkeme (idare/vergi/Danıştay) ve yer yetkisi tespiti.
- Zorunlu ön başvuru/idari merci uyarısı.
- Yanlış yola gitme riskine karşı kontrol listesi.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
