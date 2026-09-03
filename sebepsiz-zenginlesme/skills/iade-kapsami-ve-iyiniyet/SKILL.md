---
name: iade-kapsami-ve-iyiniyet
description: "Zenginleşenin neyi, ne ölçüde geri vereceğini, semere ve faizin nasıl hesaplanacağını ve kazanımın elden çıkması halinde sorumluluğun değişip değişmediğini belirlemek gerektiğinde kullanılır."
---

# İadenin Kapsamı ve İyiniyet/Kötüniyet Ayrımı

## Görev
İade borcunun kapsamını TBK m.79 ekseninde belirlemek: iyiniyetli zenginleşenin "elde kalan zenginleşme" ile, kötüniyetli olanın tam iade ile sorumluluğunu ayırmak; semere, kullanım yararı ve faizi doğru hesaplamak. Bu beceri davanın miktarını belirler.

## Soğuk başlangıç (intake)
- İade konusu ne; aynen iade mümkün mü yoksa değer iadesi mi gerekiyor?
- Zenginleşen, kazanımı aldığında sebepsizliği biliyor muydu, bilmeli miydi?
- Kazanım kısmen/tamamen elden çıktı mı; nasıl (tüketim, devir, kayıp)?
- Kazanımdan semere/gelir elde edildi mi; kullanım yararı söz konusu mu?

## Denetim şeması
1. **Kural: elde kalan zenginleşme (m.79/1).** İyiniyetli zenginleşen, geri verme isteminden önce elinden çıkardığı ölçüde iadeyle yükümlü değildir; yalnızca hâlâ malvarlığında bulunan zenginleşmeyi iade eder.
2. **İstisna: kötüniyet/öngörü (m.79/2).** Zenginleşen, elden çıkarmada iyiniyetli değilse veya iadeyi (geri vermek zorunda kalacağını) hesaba katması gerekiyorduysa, elden çıkmış olsa bile tam değerden sorumludur.
3. **Aynen mi değer mi iade.** Mümkünse aynen iade; mümkün değilse (tüketilmiş, devredilmiş, türü gereği) rayiç değer üzerinden değer iadesi. Kullanım ve hizmet yararı rayiç karşılık (tasarruf edilen masraf) ile ölçülür.
4. **Semere ve faiz.** İyiniyetli zenginleşen toplanan semereleri ve kullanma karşılığını sınırlı verir; kötüniyetli olan elde ettiği ve elde edebileceği tüm semere/faizden sorumlu. Para borcunda temerrüt faizi başlangıcı (TBK m.117 ihtar / dava tarihi) ayrıca belirlenir.
5. **İspat yükü.** Zenginleşmenin elden çıktığını ve kendi iyiniyetini zenginleşen ispatlar (m.79/1); kötüniyet/öngörü iddiasını iade isteyen ileri sürer.
6. **Ara sonuç.** İade miktarı = aynen iade veya değer + semere/faiz; iyiniyet ayrımına göre net rakam ve faiz başlangıç tarihi çıkarılır. Giderler m.80 ile mahsup edilir.

## Çıktı modülleri
- İade miktarı hesap tablosu (anapara + semere + faiz).
- İyiniyet/kötüniyet değerlendirme notu (m.79/2 ölçütleri).
- Aynen/değer iade kararı gerekçesi.

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
