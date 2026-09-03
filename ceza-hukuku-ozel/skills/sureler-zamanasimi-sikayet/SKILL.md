---
name: sureler-zamanasimi-sikayet
description: "Bir suçta dava ve ceza zamanaşımını hesaplamak, şikâyete bağlılık ve şikâyet süresini belirlemek ve uzlaştırma kapsamını kontrol etmek gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Şikâyet

## Görev
Suç bazında dava/ceza zamanaşımını, şikâyete bağlılığı ve süresini, uzlaştırma ve önödeme kapsamını belirleyerek usuli zamanaşımı risklerini önceden tespit etmek.

## Soğuk başlangıç (intake)
- Suç tipi ve uygulanacak fıkra (cezanın üst sınırı) nedir?
- Suç ne zaman işlendi (kesintisiz/zincirleme suçta sona erme tarihi)?
- Suç şikâyete bağlı mı; mağdur fiili ve faili ne zaman öğrendi?
- Daha önce kesen/durduran bir işlem (iddianame, savunma alınması) yapıldı mı?

## Denetim şeması
1. Dava zamanaşımı (TCK m.66): Suçun gerektirdiği cezanın üst sınırına göre kademeli süreler (örn. beş yıldan fazla olmayan hapis için 8 yıl, vb.). Çocuklarda süreler indirilir (m.66/2). Başlangıç m.66/6 (tamamlanma/sona erme/netice anı).
2. Zamanaşımını kesen/durduran haller (TCK m.67): Şüphelinin sorgusu, iddianame düzenlenmesi, mahkûmiyet kararı gibi işlemler keser; kesilmeden sonra süre yeniden işler ancak yarısından fazla uzayamaz (m.67/4). Durma sebepleri (izin/karar bekleme) ayrıca değerlendirilir.
3. Şikâyet (TCK m.73): Şikâyete bağlı suçlarda fiili ve faili öğrenmeden itibaren 6 ay içinde şikâyet; süre geçerse soruşturma yapılamaz. Şikâyetten vazgeçme davayı/cezayı düşürür (kabul şartıyla). Birden çok mağdur/fail halinde bölünebilirlik kuralları.
4. Hangi suçlar şikâyete bağlı: Basit yaralama (TCK m.86/2), hakaret (m.131, kamu görevlisine görevden dolayı hariç), tehdit değil ama bazı malvarlığı suçlarında akrabalık hali (m.167) gibi. Her tip için madde metnini teyit et.
5. Uzlaştırma ve önödeme: Uzlaştırma kapsamındaki suçlar CMK m.253-254 listesine göre belirlenir (şikâyete bağlı suçlar ve sayılan bazı suçlar); önödeme TCK m.75 kapsamındaki hafif suçlarda. Bunlar zamanaşımından ayrı süreçlerdir.
6. Ceza zamanaşımı (TCK m.68) ve ara sonuç: Kesinleşmiş cezanın infaz edilebilirliği için süreler. Olayda dava açma/şikâyet/zamanaşımı son tarihlerini takvimle ve riskli tarihleri işaretle.

## Çıktı modülleri
- Zamanaşımı ve şikâyet takvimi (suç, başlangıç tarihi, son tarih, kesen işlemler).
- Şikâyete bağlılık ve uzlaştırma/önödeme uygunluk tablosu.
- Riskli tarih uyarıları ve gerekli işlem listesi.

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
