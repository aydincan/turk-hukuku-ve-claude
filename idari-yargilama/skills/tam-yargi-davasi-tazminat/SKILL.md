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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
