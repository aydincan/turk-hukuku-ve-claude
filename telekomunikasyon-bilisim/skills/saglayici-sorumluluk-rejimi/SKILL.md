---
name: saglayici-sorumluluk-rejimi
description: "Bir internet aktörünün içerik, yer, erişim veya toplu kullanım sağlayıcı sıfatının ve buna bağlı yükümlülük ile sorumluluk sınırlarının (uyar-kaldır, log tutma, bilgi verme) belirlenmesi gerektiğinde kullanılır."
---

# İçerik, Yer ve Erişim Sağlayıcı Sorumluluk Rejimi

## Görev
İnternet aktörünün 5651 kapsamındaki sıfatını kesin biçimde belirlemek ve bu sıfata bağlı yükümlülükler ile hukuki/cezai sorumluluk sınırlarını tespit ederek uyum veya savunma çerçevesini kurmak.

## Soğuk başlangıç (intake)
1. Aktör ne yapıyor: içeriği kendisi mi üretiyor, başkasının içeriğini mi barındırıyor, salt erişim mi sağlıyor, ortak alan/wifi mı sunuyor?
2. Şikâyet konusu içerik üçüncü kişiye mi ait; aktör bundan haberdar edildi mi?
3. Log/trafik kaydı tutuluyor mu, ne kadar süreyle; bilgi talebi geldi mi?
4. Aktör yurt içinde mi yurt dışında mı; temsilci var mı?

## Denetim şeması
1. **Sıfat tespiti**: 5651 m.2 — içerik sağlayıcı (kendi ürettiği içerik), yer sağlayıcı (barındıran), erişim sağlayıcı (internet erişimi sunan), toplu kullanım sağlayıcı (ortak erişim). Ara sonuç: hangi sıfat, dolayısıyla hangi rejim.
2. **İçerik sağlayıcı**: m.4 — kendi içeriğinden tam sorumlu; bağlantı verdiği başkasının içeriğinden kural olarak sorumlu değildir (benimseme/sunuş hali istisna). Sorumluluk doğrudan ve tam.
3. **Yer sağlayıcı**: m.5 — hukuka aykırı içeriği denetleme yükümlülüğü yok; ancak m.8/m.9 kapsamında haberdar edilip teknik imkân varsa kaldırma (uyar-kaldır) ve trafik bilgisi saklama/sunma yükümlülüğü var. Haberdar edilmeden sorumluluk doğmaz.
4. **Erişim sağlayıcı**: m.6 — kendisine bildirilen erişim engelleme kararını uygulama, trafik bilgisini saklama (yönetmelikteki süreyle) ve faaliyete son verirken bildirim yükümlülüğü; içeriği kontrol/araştırma yükümlülüğü yok.
5. **Yaptırım**: Bilgi/belge verme, log tutma ve karar uygulama yükümlülüklerinin ihlali idari para cezası (m.5, m.6 ve ilgili hükümler) doğurur; ayrıca içerikle bağlantılı TCK suçları (ör. m.243-245) ayrı değerlendirilir.

İspat açısından log/trafik kayıtları, uyar-kaldır bildirimi ve haberdar edilme tarihi belirleyicidir; haberdar edilme anı sorumluluğun başlangıcını işaretler.

## Çıktı modülleri
- Sağlayıcı sıfatı ve yükümlülük matrisi.
- Uyar-kaldır/bilgi talebi yanıt taslağı.
- Sorumluluk sınırı ve risk değerlendirmesi.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
