---
name: ispat-delil-dijital
description: "İçerik ihlali, erişim engelleme dayanağı, trafik-log kaydı, abonelik/fatura uyuşmazlığı ve yetkilendirme ihlali gibi konularda hangi dijital delilin nasıl elde edileceği ve değerlendirileceği belirlenirken kullanılır."
---

# Telekom-Bilişimde İspat ve Dijital Delil

## Görev
Telekom/internet dosyasında ispat yükünü doğru dağıtmak; dijital delili (log, IP/zaman damgası, ekran görüntüsü, BTK/USOM yazışması) hukuken kullanılabilir ve bütünlüğü korunmuş biçimde toplamak ve bilirkişi incelemesine hazırlamak.

## Soğuk başlangıç (intake)
1. İspatı gereken vakıa nedir (içeriğin varlığı/içeriği, ihlal, fatura, taşıma reddi, yükümlülük ihlali)?
2. Mevcut deliller hangileri (sözleşme, log, ekran görüntüsü, BTK yazışması, fatura)?
3. Veri kimde: işletmeci, yer/erişim sağlayıcı, BTK/USOM mu; erişim yetkisi/karar var mı?
4. Teknik konu (IP eşleştirme, içerik bütünlüğü, ölçüm) bilirkişi gerektiriyor mu?

## Denetim şeması
1. **İspat yükü**: HMK m.190 ve TMK m.6 — iddia eden ispatla yükümlü. İdari yaptırımda ihlali BTK ispatlar; sağlayıcı sorumluluğunda haberdar edilme tarihi mağdurca, uyum yer/erişim sağlayıcıca belgelenir.
2. **İçerik delili**: İnternet içeriği için zamanlı ve doğrulanabilir tespit (noter tespiti, e-tespit, ekran görüntüsü + URL + tarih); içerik değişebilir olduğundan delil tespiti (HMK m.400 vd.) ve gerekirse adli kopya alınır.
3. **Trafik/log ve IP**: 5651 kapsamında yer/erişim sağlayıcının tuttuğu trafik bilgisi ve log; IP-abone eşleştirmesi işletmeciden müzekkereyle istenir. Zaman damgası ve saat dilimi tutarlılığı denetlenir; eksik/çelişkili kayıt sonucu çürütür.
4. **Resmî yazışma**: BTK/USOM kararları ve yazışmaları, yetkilendirme ve abonelik kayıtları öncelikli yazılı delildir (HMK m.199 vd.); ticari defterler TTK m.64 kapsamında değerlendirilir.
5. **Bilirkişi**: IP eşleştirme, içerik bütünlüğü/manipülasyon, hizmet kalitesi/kesinti ölçümü gibi teknik konularda HMK m.266 vd. bilirkişi; rapor metodolojisi ve dayanak verisi denetlenir, çelişki için ek rapor istenir. Hukuka aykırı elde edilen delil (yetkisiz dinleme/kayıt) değerlendirme dışı tutulur.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu (vakıa/delil/kaynak).
- Delil tespiti ve müzekkere talep listesi (IP-abone eşleştirme dâhil).
- Bilirkişiye sorulacak teknik sorular taslağı.

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
