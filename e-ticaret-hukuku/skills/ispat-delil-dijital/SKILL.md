---
name: ispat-delil-dijital
description: "E-ticaret uyuşmazlığında onay kayıtları, ekran görüntüleri, e-posta/SMS logları, İYS kayıtları gibi dijital delillerin toplanması, ispat yükünün dağıtılması ve delillerin mahkemede kullanılması gerektiğinde kullanılır."
---

# İspat ve Dijital Delil

## Görev
E-ticaret uyuşmazlığında ispat yükünün taraflar arasında dağılımını belirlemek; dijital delilleri (log, onay kaydı, ekran görüntüsü, İYS, ödeme kaydı) hukuka uygun ve ispat değeri yüksek biçimde derlemek.

## Soğuk başlangıç (intake)
- İspatlanması gereken vakıa ne (bilgilendirme yapıldı mı, onay var mı, teslim/iade oldu mu)?
- Eldeki dijital kayıtlar neler ve nerede tutuluyor?
- Karşı tarafın elindeki kayıtlar için delil tespiti/ibraz gerekecek mi?
- Veri tüketici işlemi mi, ticari iş mi (senetle/tanıkla ispat sınırı)?

## Denetim şeması
1. İspat yükü dağılımı (TMK m.6): kural olarak iddia eden ispatlar; ancak e-ticarette bilgilendirme, ticari ileti onayı, sipariş teyidi ve teslim gibi yükümlülüklerin yerine getirildiğini sağlayıcı ispatlar. Onay/aydınlatmanın varlığını veri sorumlusu/sağlayıcı gösterir.
2. Delil türleri: e-posta/SMS logları, İYS onay-ret kayıtları, sunucu logları, ekran görüntüleri, ödeme/banka kayıtları, kargo teslim verisi; bunlar HMK m.199 anlamında belge sayılabilen elektronik veriler olarak değerlendirilir.
3. Hukuka uygun elde etme: delilin hukuka aykırı yolla elde edilmemiş olması (HMK m.189/2); karşı tarafın özel iletişimine izinsiz erişim sakıncalıdır.
4. Senetle ispat ve istisna: tüketici işlemlerinde ve ticari işlerde ispat kuralları ile senetle ispat zorunluluğunun sınırları (HMK m.200-201) gözetilir; e-ticaret kayıtları çoğu kez yazılı delil başlangıcı/belge işlevi görür.
5. Delil güçlendirme: gerektiğinde delil tespiti (HMK m.400 vd.), bilirkişi (log analizi), e-imza/zaman damgası ile bütünlük teyidi; karşı tarafa ait kayıtlar için ibraz talebi (HMK m.219 vd.).
Ara sonuç: vakıa-delil eşleştirme matrisi ve eksik delil listesi.

## Çıktı modülleri
- İspat yükü ve vakıa-delil matrisi.
- Dijital delil derleme/saklama protokolü.
- Delil tespiti/ibraz talebi taslağı.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
