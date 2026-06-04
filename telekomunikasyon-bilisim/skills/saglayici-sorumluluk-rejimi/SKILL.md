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
