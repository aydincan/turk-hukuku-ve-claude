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
