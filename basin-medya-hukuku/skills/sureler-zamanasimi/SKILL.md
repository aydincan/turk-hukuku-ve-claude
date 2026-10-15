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
