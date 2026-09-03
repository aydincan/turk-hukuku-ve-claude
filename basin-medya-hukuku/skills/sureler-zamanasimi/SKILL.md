---
name: sureler-zamanasimi
description: "Basın-medya uyuşmazlıklarında cevap-düzeltme, şikâyet, dava açma ve tazminat zamanaşımı sürelerini doğru hesaplamak ve hak kaybını önlemek gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
İlgili tüm süreleri (cevap-düzeltme, şikâyet, idari dava, tazminat zamanaşımı) tespit etmek, başlangıç anlarını belirlemek ve bir süre takvimi kurmak.

## Soğuk başlangıç (intake)
1. Yayın/ihlal tarihi tam olarak nedir?
2. Mağdur ihlali ve faili ne zaman öğrendi?
3. Hedeflenen yol nedir (düzeltme, şikâyet, tazminat, iptal)?
4. İhlal süregelen (online erişilebilir) nitelikte mi?

## Denetim şeması
1. **Cevap-düzeltme**: Basın Kanunu m.14 uyarınca yayından itibaren iki ay içinde sorumlu müdüre başvuru; reddi/ihmali hâlinde hâkimliğe başvuru süresi de kısadır ve hak düşürücüdür.
2. **Ceza şikâyeti**: Şikâyete bağlı suçlarda (örn. hakaret) şikâyet süresi, fiil ve failin öğrenilmesinden itibaren altı aydır (TCK m.73). Basın Kanunu m.26 basın suçlarında dava açma sürelerini özel düzenler.
3. **Haksız fiil/tazminat zamanaşımı**: TBK m.72 — zarar görenin zararı ve faili öğrendiği tarihten itibaren iki yıl, her hâlde fiilin işlenmesinden itibaren on yıl. Fiil aynı zamanda suç oluşturuyor ve ceza zamanaşımı daha uzunsa, o uzun süre tazminata da uygulanır.
4. **İdari dava**: RTÜK/BTK işlemlerine karşı iptal davası tebliğden itibaren altmış gün (İYUK m.7).
5. **Süregelen ihlal**: Online içerikte erişilebilirlik sürdükçe ihlalin sürdüğü ve zamanaşımının buna göre değerlendirileceği yaklaşımı dikkate alınır [ilkesel; Yargıtay içtihadı doğrulanacak].
6. **Ara sonuç**: Her yol için ayrı süre takvimi çıkarılır; en yakın süre öncelikli işaretlenir.

## Çıktı modülleri
- Süre takvimi tablosu (yol-süre-başlangıç-bitiş)
- Hak düşürücü/zamanaşımı ayrımı notu
- Acil aksiyon uyarı listesi

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
