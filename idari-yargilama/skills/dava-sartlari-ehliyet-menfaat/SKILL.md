---
name: dava-sartlari-ehliyet-menfaat
description: "Davacının dava açma ehliyetinin, iptal davasında menfaatinin veya tam yargıda kişisel hak ihlalinin, husumetin ve kesin işlem şartının incelenmesi gerektiğinde kullanılır; davanın ilk inceleme aşamasında reddedilme riskini değerlendirmek için başvurulur."
---

# Dava Şartları, Ehliyet ve Menfaat

## Görev
Davanın esasa girilmeden reddine yol açacak dava şartı eksikliklerini önceden tespit etmek: ehliyet, menfaat/kişisel hak, husumet, kesin-yürütülebilir işlem ve idari merci tecavüzü.

## Soğuk başlangıç (intake)
- Davacı gerçek/tüzel kişi mi; dava ehliyeti ve temsil yetkisi var mı?
- Davacının işlemle güncel, kişisel ve meşru bir menfaat ilişkisi nedir?
- Davalı olarak doğru idare gösterildi mi?
- İşlem kesin ve yürütülebilir mi, yoksa hazırlık işlemi mi?

## Denetim şeması
1. **Ehliyet** (İYUK m.31 yollamasıyla HMK m.50 vd.): Taraf ve dava ehliyeti aranır. Tüzel kişilerde organın temsil yetkisi ve dava açma kararı; kamu kurumu niteliğindeki meslek kuruluşlarında üyelerinin ortak menfaatini ilgilendiren işlemlere karşı dava ehliyeti gözetilir.
2. **Menfaat / kişisel hak** (İYUK m.2): İptal davasında **menfaat ihlali** yeterlidir; menfaat güncel, kişisel ve meşru olmalı (subjektif kamu hukuku ilişkisi). Düzenleyici işlemlere karşı menfaat daha geniş yorumlanır. Tam yargıda ise **kişisel hak ihlali** aranır.
3. **Husumet** (davalı idarenin doğru gösterilmesi): Yanlış idareye husumet yöneltilmesi tek başına ret sebebi değildir; mahkeme gerçek hasmı resen belirleyip dilekçeyi tebliğ ettirebilir (İYUK m.15/1-c uygulaması).
4. **Kesin ve yürütülebilir işlem** (İYUK m.14/3-d): İcrai olmayan görüş, mütalaa, hazırlık işlemleri dava edilemez. Zincir işlemde nihai/kesin işlem dava konusu yapılır.
5. **İdari merci tecavüzü** (İYUK m.15/1-e): Mevzuat zorunlu bir idari başvuru öngörmüşse, bu yol tüketilmeden açılan dava görev/merci yönünden reddedilip dilekçe ilgili mercie tevdi edilir.
6. **Ara sonuç**: İlk inceleme (İYUK m.14) sırrasında saptanan eksiklikler m.15 sonuçlarına bağlanır; bazıları (ehliyet, kesin işlem, süre) doğrudan ret, bazıları düzeltme/merci tayini ile sonuçlanır.

## Çıktı modülleri
- Dava şartı kontrol listesi (karşılandı/risk/eksik)
- Husumet ve kesin işlem tespiti
- Ret riskini azaltıcı düzeltme önerileri

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
