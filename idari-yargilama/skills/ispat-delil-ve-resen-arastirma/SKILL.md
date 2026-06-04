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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
