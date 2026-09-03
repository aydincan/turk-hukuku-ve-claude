---
name: temel-kavramlar-ve-sistem
description: "İmar hukukunun kavram haritası ve planlama kademeleri sorulduğunda; emsal-TAKS-KAKS-çekme mesafesi, çevre düzeni-nazım-uygulama planı zinciri, idari-adli yargı ayrımı ve hangi işlemin hangi rejime tabi olduğu netleştirilmek istendiğinde kullanılır."
---

# Temel Kavramlar ve Planlama Hiyerarşisi

## Görev
İmar dosyasının doğru çerçevelenmesi için kavramsal altyapıyı kurmak: planlama kademelerini, yapılaşma parametrelerini ve uyuşmazlığın hangi yargı koluna ait olduğunu belirlemek.

## Soğuk başlangıç (intake)
- İhtilaf hangi işlemden çıkıyor: imar planı/değişikliği mi, ruhsat mı, yıkım/ceza mı, kamulaştırma mı?
- Taşınmazın imar durumu nedir (ada/parsel, mevcut plan ölçeği, fonksiyon)?
- İşlemi tesis eden idare hangisi (belediye, büyükşehir, bakanlık)?
- Elinizde plan paftası, imar durum belgesi, ruhsat veya tebligat var mı?

## Denetim şeması
1. **Planlama hiyerarşisi (3194 m.6-8)**: Çevre düzeni planı (1/100.000-1/25.000) → nazım imar planı (1/5000) → uygulama imar planı (1/1000). Alt ölçekli plan üst ölçeğe ve şehircilik ilkelerine, kamu yararına, planlama esaslarına aykırı olamaz. Aykırılık iptal sebebidir.
2. **Yapılaşma parametreleri**: TAKS (taban alanı kat sayısı), KAKS/emsal (kat alanı kat sayısı), çekme mesafeleri, Hmax, ada/parsel bazında yapılaşma; Planlı Alanlar İmar Yönetmeliği'ndeki tanımlarla okunur. Plan notları parametre kadar bağlayıcıdır.
3. **Yargı kolu ayrımı**: Plan, ruhsat, yıkım, encümen para cezası → **idari yargı (iptal/tam yargı)**. Kamulaştırma bedel tespiti ve kamulaştırmasız el atma bedeli, kat karşılığı inşaat ve taşınmaz satış uyuşmazlıkları → **adli yargı**. Yanlış yargı kolu = görev yönünden ret riski.
4. **İşlem tipi-rejim eşleştirmesi**: Her işlemin dayanağı kademe ve mevzuat maddesi ile bağlanır (ör. yıkım → m.32; para cezası → m.42; DOP → m.18).
5. **Ara sonuç**: Uyuşmazlığın türü, yargı kolu, görevli mahkeme ve dayanak normlar bir cümlede sabitlenir; sonraki beceri buradan beslenir.

## Çıktı modülleri
- Kavram-parametre sözlüğü (emsal/TAKS/KAKS/çekme/Hmax tanımlı).
- Planlama hiyerarşisi şeması ve somut dosyadaki kademe konumu.
- Yargı kolu ve görevli mahkeme tespit notu.
- Bir sonraki adıma yönlendirme (plan denetimi / ruhsat / yıkım-ceza / kamulaştırma).

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
