---
name: surelerin-zamanasimi
description: "Deniz ticareti alacak ve taleplerinde hangi sürenin geçtiğini, kesilme-durma hallerini ve ihbar/protesto sürelerini hesaplamak; dava ya da savunmada zamanaşımı definin gündeme geleceği her durumda kullan."
---

# Süreler ve Zamanaşımı

## Görev
Deniz ticareti taleplerinde uygulanacak zamanaşımı süresini doğru tespit etmek; başlangıç anını, kesilme ve durma hallerini, ihbar/protesto sürelerini hesaplamak; zamanaşımı definin geçerli olup olmadığını değerlendirmek.

## Soğuk başlangıç (intake)
- Talep hangi olaydan doğuyor (taşıma, çatma, kurtarma, avarya, sigorta)?
- Olayın/zararın gerçekleştiği ve öğrenildiği tarih nedir?
- Araya giren dava, ihtiyati haciz, ikrar veya yazılı talep var mı (kesilme)?
- İhbar/protesto süreleri korunmuş mu?

## Denetim şeması
1. **Talebin türü ve süresi**: Eşyaya ilişkin deniz taşımasından doğan taşıyana karşı taleplerde **bir yıllık** zamanaşımını (TTK m.1188) uygula; çatmadan doğan tazminat taleplerinde **iki yıllık** süreyi (TTK m.1297) hesapla. Kurtarma, avarya ve sigorta için ilgili özel süreleri ayrıca teyit et.
2. **Başlangıç anı**: Sürenin başlangıcını olaya göre belirle — taşımada eşyanın teslim edildiği veya edilmesi gereken gün; çatmada kaza günü; rücu taleplerinde ise asıl borcun ödendiği an gibi.
3. **Kesilme ve durma**: TBK m.154 vd. (dava açılması, icra takibi, ikrar, hakeme başvuru) kesilme sebeplerini ve TBK m.153 durma sebeplerini deniz alacağına uyarlayarak değerlendir; ihtiyati haczin süreye etkisini gözet.
4. **İhbar/protesto süreleri**: Yük ziya/hasarında açık hasarda teslim anında, gizli hasarda kanuni süre içinde ihbar; sürastarya ve avarya bildirimleri gibi sözleşmesel/yasal sürelerin korunup korunmadığını ayrı tablo ile kontrol et.
5. **İspat ve ara sonuç**: Zamanaşımını def olarak ileri süren taraf ispatlar; kesilme/durmayı iddia eden bunu ispatlar. Çıktıda son günü, kalan süreyi ve definin geçerliliğini gerekçeli sonuca bağla; süreler yaklaşıyorsa derhal koruyucu işlem öner.

## Çıktı modülleri
- Talep türüne göre zamanaşımı süresi tablosu
- Başlangıç-kesilme-durma kronolojisi
- İhbar/protesto kontrol listesi ve son gün uyarısı

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
