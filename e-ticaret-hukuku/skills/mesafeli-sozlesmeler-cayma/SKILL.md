---
name: mesafeli-sozlesmeler-cayma
description: "İnternetten yapılan tüketici satışlarında ön bilgilendirme, 14 günlük cayma hakkı, iade ve teslim yükümlülüklerinin denetlenmesi veya tüketici/satıcı tarafında bir uyuşmazlığın çözülmesi gerektiğinde kullanılır."
---

# Mesafeli Sözleşmeler ve Cayma Hakkı

## Görev
6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği kapsamında tüketiciyle elektronik ortamda kurulan satış/hizmet sözleşmelerinde ön bilgilendirme, cayma hakkı, iade ve teslim yükümlülüklerini denetlemek; uyuşmazlığı çözmek.

## Soğuk başlangıç (intake)
- Alıcı tüketici mi (gerçek kişi, ticari amaç dışı)?
- Sözleşme konusu mal mı hizmet mi; cayma istisnası kapsamına giriyor mu (ısmarlama, hızla bozulan, dijital içerik, hijyenik ürün)?
- Ön bilgilendirme formu sunuldu ve onaylandı mı; cayma süresi başladı mı?
- Cayma bildirimi ne zaman, hangi kanaldan yapıldı?

## Denetim şeması
1. Kapsam (6502 m.48): mesafeli sözleşme, satıcı/sağlayıcı ile tüketicinin eş zamanlı fiziksel varlığı olmaksızın, uzaktan iletişim aracıyla kurulan sözleşmedir.
2. Ön bilgilendirme: tüketiciye sözleşme kurulmadan önce malın temel nitelikleri, toplam fiyat, cayma hakkı, teslim ve şikâyet bilgileri yazılı/kalıcı veri saklayıcısıyla verilir; verilmediği takdirde cayma süresi etkilenir.
3. Cayma hakkı: tüketici 14 gün içinde gerekçesiz ve cezasız cayabilir. Süre malda teslim, hizmette sözleşme tarihinden işler. Ön bilgilendirme yapılmamışsa süre uzar (Yönetmelik uyarınca ek süre). Cayma sonrası satıcı bedeli 14 gün içinde iade eder; tüketici malı süresinde geri gönderir.
4. İstisnalar (Yönetmelik): cayma hakkının kullanılamayacağı haller (kişiye özel üretim, çabuk bozulan, ambalajı açılmış hijyenik/dijital ürünler vb.) somut olayla eşleştirilir.
5. Teslim ve ayıp: teslim süresi (kural olarak 30 gün) ve ayıplı maldan sorumluluk (6502 m.8 vd.) ayrıca değerlendirilir.
İspat yükü: ön bilgilendirmenin yapıldığını satıcı, caymanın süresinde olduğunu tüketici ispatlar.
Yol: Tüketici Hakem Heyeti (parasal sınır altında) veya Tüketici Mahkemesi.

## Çıktı modülleri
- Cayma hakkı denetim tablosu (süre-istisna-iade).
- Tüketici Hakem Heyeti/mahkeme başvuru iskeleti.
- Ön bilgilendirme/iade prosedürü düzeltme notu.

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
