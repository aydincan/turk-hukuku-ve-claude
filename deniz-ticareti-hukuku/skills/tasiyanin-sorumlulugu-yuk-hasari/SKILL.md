---
name: tasiyanin-sorumlulugu-yuk-hasari
description: "Taşınan yükün ziyaa uğraması, hasar görmesi veya gecikmesi nedeniyle taşıyana karşı talep ya da savunma hazırlanırken; sorumluluğun şartlarını, kurtuluş hallerini, sorumluluk sınırını ve ihbar yükümlülüğünü değerlendirmek için kullan."
---

# Taşıyanın Sorumluluğu ve Yük Ziya/Hasarı

## Görev
Yükün ziya, hasar veya gecikmesinden doğan zararda taşıyanın sorumlu tutulup tutulamayacağını belirlemek; kurtuluş hallerini ve sorumluluk sınırını uygulamak; ihbar ve protesto sürelerinin korunup korunmadığını denetlemek.

## Soğuk başlangıç (intake)
- Yük tamamen mi kayıp, kısmen mi hasarlı, yoksa gecikmeli mi teslim edildi?
- Hasar yükleme öncesi, taşıma sırasında mı yoksa boşaltma sonrası mı gerçekleşti?
- Teslimde sörvey/ekspertiz yapıldı mı; ziya-hasar ihbarı süresinde yapıldı mı?
- Yükün cinsi, koli/birim sayısı ve brüt ağırlığı (sorumluluk sınırı hesabı için)?

## Denetim şeması
1. **Sorumluluğun temeli**: Taşıyan, yükü teslim aldığı andan teslim edinceye kadar ziya ve hasardan kural olarak sorumludur (TTK m.1178 vd.); kusur karinesine dayanan bir sorumluluktur.
2. **Denize elverişlilik**: Zararın gemi denize/yola/yüke elverişsizliğinden doğduğu iddiasında taşıyanın gereken özeni gösterdiğini ispatı (TTK m.1141, m.1180); özen gösterilmemişse kurtuluş yoktur.
3. **Kurtuluş halleri (istisnalar)**: Teknik kusur/yangın gibi kanunda sayılan sorumluluktan kurtuluş sebeplerini (TTK m.1180-1182 çerçevesinde) ve bunların ispat yükünü değerlendir; navlun sözleşmesindeki sorumsuzluk kayıtlarının emredici sınırlar karşısında geçerliliğini denetle.
4. **Sorumluluk sınırı**: Tazminat, koli/birim başına veya kilogram başına hesaplanan tutarla sınırlıdır (TTK m.1186 — Lahey-Visby esaslı SDR sınırı); konteyner içeriğinin konişmentoda dökümüne göre birim sayısının nasıl belirleneceğini hesapla. Taşıyanın kasdı/pervasızlığı sınırı kaldırır.
5. **İhbar ve ara sonuç**: Açık hasarda teslim anında, gizli hasarda kanunda öngörülen süre içinde ihbar yapılmazsa karine taşıyan lehine işler. Eşyaya ilişkin taleplerde **bir yıllık** zamanaşımını (TTK m.1188) hesapla. Çıktıda sorumluluk-kurtuluş-sınır zincirini sıralı sonuçla.

## Çıktı modülleri
- Sorumluluk/kurtuluş değerlendirme tablosu
- Sorumluluk sınırı hesap taslağı (birim ve kilogram)
- İhbar/zamanaşımı kontrol listesi ve talep/savunma stratejisi

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
