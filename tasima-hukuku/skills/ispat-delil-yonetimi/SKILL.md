---
name: ispat-delil-yonetimi
description: "Taşıma uyuşmazlığında zararın taşıma süresinde doğduğunun, eşyanın durumunun ve kurtuluş sebeplerinin ispatı, ispat yükünün dağılımı ve delillerin (belge, ekspertiz, kayıt) toplanması gerektiğinde kullanılır."
---

# İspat ve Delil Yönetimi

## Görev
Taşıma davasında kimin neyi ispatlayacağını belirlemek, taşıma belgelerinden doğan karineleri işletmek ve delil setini eksiksiz oluşturmak.

## Soğuk başlangıç (intake)
1. İddia ne: eşya teslimde sağlam değildi / zarar taşıma süresinde doğdu / taşıyıcı kusurlu?
2. Hangi belgeler mevcut: taşıma senedi/CMR, teslim makbuzu, rezerv şerhleri, ekspertiz?
3. Eşyanın teslim alındığı andaki durumu nasıl kayıtlandı?
4. Karşı taraf hangi kurtuluş sebebini ileri sürüyor?

## Denetim şeması
1. **Temel ispat yükü:** Hak sahibi, zararın eşya taşıyıcının zilyetliğinde (teslim alma-teslim arası) doğduğunu ispatlar; taşıyıcı kurtuluş sebebini ispatlar (TTK m.875, m.876; CMR m.18/1).
2. **Belgeden doğan karineler:** TTK m.858 / CMR m.9 — rezervsiz/şerhsiz teslim alma, eşyanın senette yazılı iyi durumda teslim alındığı karinesini doğurur; taşıyıcının teslimde rezerv koymaması, iyi teslim karinesini güçlendirir.
3. **Özel risk karineleri:** TTK m.878 / CMR m.18/2 — sayılan risklerden biri varsa zararın o sebepten doğduğu karine sayılır; hak sahibi aksini ispatla yükümlü olur.
4. **Delil türleri:** Taşıma senedi/CMR belgesi, teslim-tesellüm tutanakları, tartım/sayım kayıtları, dijital takip (GPS/telematik) verileri, sıcaklık kayıtları (soğuk zincir), ekspertiz/sürvey raporu, faturalar.
5. **Delil tespiti ve bilirkişi:** Eşyanın hasar durumu için HMK m.400 delil tespiti; teknik değerlendirme için bilirkişi/sürveyör raporu; hesap için ticari defterler (TTK m.83, HMK m.222).
6. **İspat ölçüsü:** Tam ispat aranır; karinelerin kaydırdığı yük dikkate alınır.
7. **Ara sonuç:** Lehte-aleyhte ispat dağılımı ve eksik delillerin tamamlanma planı.

## Çıktı modülleri
- İspat yükü dağılım tablosu (iddia / yük sahibi / dayanak madde).
- Delil dizini ve eksik delil tamamlama listesi.
- Karine analizi ve aksini ispat stratejisi.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
