---
name: tasiyici-sorumlulugu-semasi
description: "Eşyada ziya, hasar veya teslimde gecikme nedeniyle taşıyıcının sorumluluğunun kurulup kurulmadığını, kurtuluş sebeplerini ve sorumluluk sınırını adım adım denetlemek gerektiğinde kullanılır; taşıma uyuşmazlıklarının çekirdek analiz aracıdır."
---

# Taşıyıcının Sorumluluğu Denetim Şeması

## Görev
Taşıyıcının ziya, hasar veya gecikmeden doğan sorumluluğunu objektif sorumluluk esasına göre kurmak, kurtuluş kademelerini denetlemek ve tazminatın hangi sınıra tabi olduğunu belirlemek.

## Soğuk başlangıç (intake)
1. Zarar türü nedir: tam/kısmi ziya (kayıp), hasar (hâsâr), yoksa teslimde gecikme mi?
2. Eşya teslim alma ile teslim arasındaki hangi aşamada zarar gördü; teslim gerçekleşti mi?
3. Eşyanın brüt ağırlığı, cinsi ve beyan edilen değeri nedir; özel değer/menfaat beyanı yapıldı mı (TTK m.880)?
4. Taşıyıcı tarafında kasıt veya pervasızca davranış iddiası var mı?

## Denetim şeması
1. **Sorumluluğun kurulması:** TTK m.875 — taşıyıcı, eşyayı teslim aldığı andan teslim edinceye kadar ziya, hasar ve gecikmeden kusuru aranmaksızın sorumludur. CMR'de karşılığı m.17/1.
2. **Genel kurtuluş:** TTK m.876 — kaçınılmaz olay, gönderen/gönderilen kusuru, eşyanın kendine özgü ayıbı ispatlanırsa taşıyıcı kurtulur. CMR m.17/2.
3. **Özel risk sebepleri (kanıt kolaylığı):** TTK m.878 — örtüsüz araç, ambalaj yokluğu, yükleme/boşaltmanın gönderence yapılması, eşyanın özel doğası, yetersiz işaretleme, canlı hayvan gibi hallerde sebep-zarar bağlantısı karine sayılır. CMR m.17/4 ve m.18/2.
4. **İspat yükü:** Zararın taşıma süresinde doğduğunu hak sahibi; kurtuluş sebebini taşıyıcı ispatlar (TTK m.875, m.876; CMR m.18/1).
5. **Sorumluluk sınırı:** TTK m.882/1 — kg başına 8,33 ÖÇH (SDR); gecikmede taşıma ücretinin üç katı (m.882/3). CMR m.23 ve m.25.
6. **Sınırın kalkması:** TTK m.886 / CMR m.29 — taşıyıcının kastı veya pervasızca ve zararın muhtemel olduğu bilinciyle hareketi varsa sınırlardan yararlanamaz; tam zarar tazmin edilir.
7. **Ara sonuç:** Sorumlu/sorumsuz; tazminatın sınırlı mı sınırsız mı hesaplanacağı.

## Çıktı modülleri
- Sorumluluk kuruluşu ve kurtuluş kademe tablosu.
- Tazminat sınırı hesabı (kg x 8,33 SDR x güncel kur) ve gecikme tavanı.
- Sınırın kalkması (m.886/CMR 29) yönünden risk değerlendirmesi.

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
