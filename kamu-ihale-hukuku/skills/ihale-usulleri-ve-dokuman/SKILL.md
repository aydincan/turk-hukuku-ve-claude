---
name: ihale-usulleri-ve-dokuman
description: "Açık/belli istekliler/pazarlık/doğrudan temin usulünün doğru seçilip seçilmediğini ve idari şartname, teknik şartname, sözleşme tasarısı ile zeyilnamelerin hukuka aykırılığını incelemek gerektiğinde kullanılır."
---

# İhale Usulleri ve İhale Dokümanı Denetimi

## Görev
Seçilen ihale usulünün kanuna uygunluğunu ve ihale dokümanının (idari/teknik şartname, sözleşme tasarısı, zeyilname) rekabeti ve eşit muameleyi zedeleyip zedelemediğini denetlemek.

## Soğuk başlangıç (intake)
1. Hangi usul uygulanmış; gerekçesi ihale onay belgesinde nasıl açıklanmış?
2. Teknik şartnamede belirli marka/model/menşe işaret ediliyor mu (m.12)?
3. Yeterlik kriterleri işin niteliğiyle orantılı mı yoksa rekabeti daraltıyor mu?
4. Zeyilname ile esaslı değişiklik yapılıp süre uzatımı verilmiş mi (m.29)?

## Denetim şeması
1. **Usul seçimi:** Açık ihale ve belli istekliler arasında ihale asıldır (m.18-20). Pazarlık (m.21) ve doğrudan temin (m.22) ancak kanunda sayılan hallerle sınırlıdır; gerekçe denetlenir. Doğrudan temin bir ihale usulü değildir, m.5 ilanı/teminat şartı aranmaz ama keyfî kullanım hukuka aykırıdır.
2. **Teknik şartname (m.12):** Rekabeti engelleyecek şekilde belirli marka, patent, menşe, kaynak gösterilemez; zorunluysa "veya dengi" ibaresi aranır. Ölçülebilir, objektif kriter şartı.
3. **İdari şartname/yeterlik:** Yeterlik kriterleri (m.10) işin niteliği ve büyüklüğüyle orantılı olmalı; aşırı/gereksiz kriter rekabet ihlali sayılır.
4. **Zeyilname (m.29):** Dokümanda esaslı değişiklik zeyilname ile ve son teklif gününden makul süre önce yapılır; gerekirse teklif süresi uzatılır. Süre verilmemesi iptal sebebidir.
5. **Ara sonuç:** Dokümana yönelik aykırılık varsa süresi içinde (ihale tarihinden 3 iş günü öncesine kadar doküman içeriğine itiraz) şikâyet yoluna gidilir; süre kaçırılmışsa esas iddia konsorbe olur.

İspat yükü: Doküman aykırılığını iddia eden istekli, somut maddeyi ve rekabete etkisini gösterir; idare orantılılık gerekçesini ortaya koyar.

## Çıktı modülleri
- Usul seçim gerekçesi değerlendirme notu.
- Şartname madde-bazlı aykırılık tablosu (madde / aykırılık / dayanak / öneri).
- Zeyilname/süre uzatımı kontrol listesi.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
