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
