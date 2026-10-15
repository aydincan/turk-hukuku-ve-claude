---
name: sureler-zamanasimi
description: "Gümrük yükümlülüğünün tahakkuk ve tebliğ zamanaşımı, itiraz ve dava süreleri ile tahsilat sürelerinin hesaplanması gerektiğinde; hak düşürücü süre ve zamanaşımı haritası çıkarmak için kullanılır."
---

# Süreler, Zamanaşımı ve Takvim Yönetimi

## Görev
Gümrük uyuşmazlığındaki tüm kritik süreleri tek bir takvimde toplamak: yükümlülüğün tahakkuk/tebliğ zamanaşımı, idari itiraz ve uzlaşma süreleri, idari dava süreleri ve tahsilat zamanaşımı.

## Soğuk başlangıç (intake)
- Beyannamenin tescil tarihi ve yükümlülüğün doğum anı nedir?
- Ek tahakkuk/ceza kararı hangi tarihte tebliğ edildi?
- Sürece kaçakçılık ya da hapis cezasını gerektiren bir fiil karıştı mı (zamanaşımı uzayabilir)?
- Tahsilat aşaması (ödeme emri) başladı mı?

## Denetim şeması
1. Tahakkuk/tebliğ zamanaşımı: 4458 m.197 uyarınca gümrük vergileri, yükümlülüğün doğduğu tarihten itibaren kural olarak 3 yıl içinde tebliğ edilmelidir; bu süre dolduktan sonra yapılan tebligat zamanaşımına uğrar. İlgili fiilin ceza mahkemesinin görevine giren bir suç oluşturması halinde sürenin uzayabileceği (dava zamanaşımına bağlanması) gözetilir.
2. Doğum anı tespiti: Süre, yükümlülüğün doğduğu an (kural olarak beyanname tescili — m.181) esas alınarak hesaplanır; rejim ihlalinde m.182-184'teki an dikkate alınır.
3. İtiraz süresi: m.242 uyarınca kararın tebliğinden itibaren 15 gün içinde idari itiraz; itiraz merciinin 30 günlük cevap süresi ve zımni ret anı.
4. Dava süresi: İtirazın (açık/zımni) reddinin tebliğinden itibaren İYUK m.7 süresi (vergi mahkemesi 30 gün). Sürenin tatil günleri ve adli ara verme etkisi kontrol edilir.
5. Tahsilat zamanaşımı: Kesinleşen amme alacağında 6183 sayılı Kanun çerçevesinde tahsil zamanaşımı (kural 5 yıl) ve kesen/durduran sebepler ayrıca izlenir.
6. İspat ve dayanak: Tebliğ alındıları, tescil tarihleri ve süreyi kesen/durduran işlemler dosyalanır; süre savunması bu belgelere dayandırılır.
7. Ara sonuç: Tüm süreler tek takvimde toplanır; geçmiş/kaçırılmış ve yaklaşan süreler işaretlenir; zamanaşımı def'i imkânı belirlenir.

## Çıktı modülleri
- Birleşik süre/zamanaşımı takvimi (tescil → tebliğ → itiraz → dava → tahsilat)
- Zamanaşımı def'i argüman notu (uygunsa)
- Yaklaşan süre uyarı listesi

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
