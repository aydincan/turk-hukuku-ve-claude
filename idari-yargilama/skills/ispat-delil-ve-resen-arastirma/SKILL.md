---
name: ispat-delil-ve-resen-arastirma
description: "İdari yargıda ispat yükünün dağılımı, resen araştırma ilkesi, ara karar ile belge getirtme, bilirkişi ve keşif kullanımı değerlendirilirken kullanılır; idarenin işlem dayanaklarını sunmaması veya delil eksikliği sorununda başvurulur."
---

# İspat, Delil ve Resen Araştırma

## Görev
İdari yargılamanın resen araştırma ilkesi çerçevesinde ispat yükünü dağıtmak, eksik delilleri ara kararla tamamlatmak ve bilirkişi/keşif gibi araçları doğru kullanmak.

## Soğuk başlangıç (intake)
- İşlemin sebebine/dayanağına ilişkin belgeler kimde (idarede mi, davacıda mı)?
- Çekişmeli maddi olgular neler; teknik/hesap bilirkişisi gerekli mi?
- İdare savunmasında dayanak belgeleri sundu mu?
- Hangi olgu ispatlanamazsa dava aleyhe sonuçlanır?

## Denetim şeması
1. **Resen araştırma ilkesi** (İYUK m.20): İdari yargıda hâkim, davanın çözümü için gerekli her türlü bilgi ve belgeyi taraflardan ve ilgili yerlerden **resen** isteyebilir; tahkikatı kendisi yürütür. Bu, dispozitif ilkenin yumuşatılmış hâlidir.
2. **İspat yükünün dağılımı**: İptal davasında işlemin sebep ve maddi dayanağını ortaya koymak kural olarak idareye düşer; idare işleminin hukuka uygunluğunu belgelendirmelidir. Tam yargıda zararın varlığı ve miktarını ispat kural olarak davacıdadır.
3. **Belge getirtme / ara karar**: Mahkeme idareden işlem dosyasının tamamını ister; idare belgeleri sunmaktan kaçınırsa bu durum işlem aleyhine değerlendirilebilir (idarenin savunma hakkıyla dengeli).
4. **Bilirkişi ve keşif** (İYUK m.31 yollamasıyla HMK ilgili hükümleri): Çözümü özel/teknik bilgi gerektiren hâllerde bilirkişi; mahallinde inceleme gerektiren hâllerde keşif yapılır. Bilirkişi raporu hâkimi bağlamaz, denetlenir.
5. **Delil yasakları ve gizlilik**: Devlet sırrı/ticari sır içeren belgelerde özel rejim gözetilir; hukuka aykırı elde edilen delil değerlendirilmez.
6. **Ara sonuç**: Resen araştırma, davacının ispat külfetini tümüyle kaldırmaz; davacı somut iddiasını ve başlangıç delilini sunmalı, mahkeme bunu tamamlatmalıdır.

## Çıktı modülleri
- İspat yükü dağılım tablosu (olgu / yük / delil)
- Ara karar talep listesi (getirtilecek belgeler)
- Bilirkişi/keşif gerekçesi taslağı

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
