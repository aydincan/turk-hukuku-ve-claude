---
name: tam-yargi-davasi-tazminat
description: "İdari işlem veya eylemden doğan zararın tazmini, eski hâle iade veya idarenin kusurlu/kusursuz sorumluluğunun tartışıldığı durumlarda kullanılır; kamulaştırmasız el atma, hizmet kusuru, sosyal risk gibi tazmin taleplerinde başvurulur."
---

# Tam Yargı Davası ve İdarenin Sorumluluğu

## Görev
İdari işlem veya eylemden doğan kişisel zararın tazminini, idarenin sorumluluk türünü (kusurlu/kusursuz), illiyet bağını ve zarar kalemlerini doğru kurgulayarak talep etmek.

## Soğuk başlangıç (intake)
- Zarar bir idari işlemden mi yoksa fiili bir eylemden mi doğdu?
- Eylem tarihinden bu yana ne kadar süre geçti (m.13 süreleri)?
- Zarar kalemleri neler: maddi (fiili zarar, yoksun kalınan kâr), manevi?
- İdarenin hizmeti kötü/geç/hiç işletilmesi söz konusu mu?

## Denetim şeması
1. **Ön başvuru şartı** (İYUK m.13): İdari eylemlerden doğan zararlarda dava açmadan önce eylemi öğrenme tarihinden itibaren **1 yıl** ve her hâlde eylem tarihinden itibaren **5 yıl** içinde ilgili idareye başvuru zorunludur. İdari işlemden doğan tam yargı davasında ise m.7/m.12 süreleri uygulanır.
2. **Sorumluluk türü**:
   - **Hizmet kusuru** (kusurlu sorumluluk): Hizmetin kötü, geç veya hiç işlememesi. Kusur idareye izafe edilir; kişiselleştirme aranmaz.
   - **Kusursuz sorumluluk**: Tehlike (riskli faaliyet) ilkesi ve fedakârlığın denkleştirilmesi (kamu külfetleri karşısında eşitlik) ilkeleri. Terör/sosyal risk zararlarında sosyal risk ilkesi.
3. **İlliyet bağı**: İdari faaliyet ile zarar arasında uygun nedensellik aranır. Mücbir sebep, beklenmeyen hâl, zarar görenin/üçüncü kişinin ağır kusuru illiyeti kesebilir veya tazminatta indirim sebebi olabilir.
4. **Zararın ispatı ve hesabı**: Zarar gerçek, kesin ve idari faaliyetle illiyetli olmalı. Maddi tazminatta fiili zarar ve yoksun kalınan kazanç; bedensel zararda işgücü kaybı, destekten yoksun kalma; manevi tazminatta takdiri ölçütler. İspat yükü kural olarak zarar görende; resen araştırma ilkesi geçerlidir (İYUK m.20).
5. **Ara sonuç**: Faiz başlangıcı (başvuru/dava tarihi) ve faiz türü ayrıca belirlenir; ıslah ile talep artırımı mümkündür (İYUK m.16/4).

## Çıktı modülleri
- Sorumluluk türü ve illiyet analizi notu
- Zarar kalemleri tablosu (maddi/manevi, dayanak)
- Ön başvuru ve dava süresi takvimi

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
