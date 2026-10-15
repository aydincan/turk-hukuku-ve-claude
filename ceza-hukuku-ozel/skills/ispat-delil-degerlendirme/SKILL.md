---
name: ispat-delil-degerlendirme
description: "Bir ceza dosyasındaki delilleri suç unsurları bakımından tartmak, delil yasaklarını kontrol etmek ve hukuki nitelendirmenin delil durumuyla uyumunu denetlemek gerektiğinde kullanılır."
---

# İspat, Delil ve Suç Vasfı Değerlendirmesi

## Görev
Dosyadaki delilleri her bir suç unsuru (tipiklik, kast, nitelikli hal) bakımından eşleştirmek, hukuka aykırı delilleri ayıklamak ve isnadın delil durumuyla örtüşüp örtüşmediğini değerlendirmek.

## Soğuk başlangıç (intake)
- İsnat edilen suç ve hangi unsurların ispatı tartışmalı?
- Dosyada hangi deliller var (beyan, görüntü/ses kaydı, dijital veri, bilirkişi raporu, fizik delil)?
- Deliller hukuka uygun yöntemle (arama-el koyma, iletişimin denetlenmesi) mı elde edildi?
- Tek delil mağdur/müşteki beyanı mı, yoksa beyanı destekleyen yan deliller var mı?

## Denetim şeması
1. Unsur-delil eşlemesi: Her suç unsuru için (fiil, netice, nedensellik, kast, nitelikli hal) dosyadaki hangi delilin onu ispatladığını yaz. İspatsız kalan unsur, beraat veya vasıf değişikliği gerektirir.
2. Delil yasakları: Hukuka aykırı yöntemle elde edilen deliller hükme esas alınamaz (Anayasa m.38/6; CMK m.206/2-a, m.217/2, m.230/1). Aramada usulsüzlük, hukuka aykırı iletişim tespiti veya işkence/baskıyla alınan ifade bu kapsamdadır.
3. Beyan delillerinin değerlendirilmesi: Mağdur/tanık beyanlarının istikrarı, çelişkileri, menfaat ilişkisi ve yan delillerle desteklenip desteklenmediği. Tek beyana dayalı mahkûmiyetin sınırları için ilkesel Yargıtay içtihadına atıf (karararama.yargitay.gov.tr; künye `[doğrulanacak]`).
4. Bilirkişi ve teknik deliller: İğfal kabiliyeti, yaralanma derecesi, dijital iz analizi gibi teknik konularda raporun dayanağı ve metodolojisi denetlenir; çelişki halinde ek rapor/yeni bilirkişi talep edilir.
5. Şüpheden sanık yararlanır (in dubio pro reo): Unsurlardan biri makul şüphe düzeyinde dahi ispatlanamıyorsa, lehe yorum ve beraat değerlendirmesi yapılır. Vasıf değişikliği (örn. yağmadan hırsızlığa, nitelikli halden basit hale) gündeme gelebilir.
6. Ara sonuç: İspatlanan/ispatlanamayan unsurlar listesi + ayıklanması gereken deliller + olası suç vasfı ve beklenen sonuç (mahkûmiyet/beraat/vasıf değişikliği).

## Çıktı modülleri
- Unsur-delil eşleme tablosu (unsur, dayanak delil, güç derecesi).
- Delil yasağı/itiraz noktaları listesi (madde atıflı).
- Suç vasfı ve sonuç senaryosu değerlendirmesi.

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
