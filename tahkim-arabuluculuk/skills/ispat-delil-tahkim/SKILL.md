---
name: ispat-delil-tahkim
description: "Tahkim yargılamasında delil sunumu, tanık ve bilirkişi, belge ibrazı ile ispat yükünün dağılımını planlamak; arabuluculuk beyanlarının delil yasağını gözetmek gerektiğinde kullanılır."
---

# Tahkimde İspat ve Delil Yönetimi

## Görev
Tahkimde delil stratejisini kurmak: hangi vakıayı kimin ispatlayacağı, hangi delillerin
nasıl sunulacağı ve usul güvencelerinin (hukuki dinlenilme, eşit muamele) korunması.
Ayrıca arabuluculuk beyanlarının sonraki davada kullanılamayacağını gözetmek.

## Soğuk başlangıç (intake)
1. Tahkim iç (HMK) mi MTK mı, kurumsal kurallar (ör. ISTAC, ICC) uygulanıyor mu?
2. Çekişmeli vakıalar neler, ispat yükü kimde?
3. Tanık, bilirkişi, belge ibrazı ihtiyacı var mı?
4. Daha önce arabuluculuk yapıldıysa orada açıklanan beyan/belge var mı?

## Denetim şeması
1. **İspat yükü**: Genel kural **TMK m.6** — iddia eden ispatla yükümlüdür; tahkimde de
   esastır. Çekişmeli vakıalar ve karşı tarafın ikrarı ayrıştırılır.
2. **Delil sunumu ve usul**: Hakem heyeti delillerin toplanmasını yönetir; taraflara
   **eşit muamele** ve **hukuki dinlenilme hakkı** tanınmalıdır (**HMK m.423**,
   **MTK m.8/A**). Bu ilkelerin ihlali iptal sebebidir (**HMK m.439/2-ç**, **MTK m.15/A**).
3. **Mahkeme yardımı**: Hakem heyeti tanığı zorla getiremez veya üçüncü kişiden belge
   ibrazını cebren sağlayamaz; bunun için **delil toplanmasında mahkeme yardımı** istenir
   (**HMK m.432**). Kurumsal kurallarda belge ibrazı (örn. IBA Delil Kuralları) tarafların
   anlaşmasıyla uygulanabilir.
4. **Arabuluculuk delil yasağı**: Arabuluculukta ileri sürülen görüş, öneri, kabul ve
   belgeler sonraki yargılamada/tahkimde **delil olarak kullanılamaz** (**HUAK m.5**); bu
   sınır delil listesinde işaretlenir.
5. **Ara sonuç**: İspat yükü tablosu, delil planı ve usul riski uyarıları.

## Çıktı modülleri
- Vakıa-delil-ispat yükü matrisi.
- Tanık/bilirkişi/belge ibraz talep taslakları.
- Mahkeme yardımı (HMK m.432) başvuru notu; HUAK m.5 delil yasağı uyarısı.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
