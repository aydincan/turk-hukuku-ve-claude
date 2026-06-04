---
name: ihtarname-tebligat-sadelestirme
description: "Alınan bir ihtarnameyi, tebligatı veya icra/ödeme emrini müvekkile açıklamak; ne istendiğini, hangi süre içinde ne yapılması gerektiğini ve yapılmazsa ne olacağını yalın anlatmak gerektiğinde kullanılır."
---

# İhtarname ve Tebligat Sadeleştirme

## Görev
Müvekkile ulaşan ihtarname, tebligat, ödeme emri veya icra emrini; "kim, ne istiyor, kaç gün
içinde ne yapmalıyım, yapmazsam ne olur" sorularına net cevap verecek şekilde sadeleştirmek.
Bu belgelerde süreler hayati olduğu için doğruluk önceliklidir.

## Soğuk başlangıç (intake)
1. Belge türü nedir (noter ihtarı, ödeme emri, icra emri, tebliğ edilen dava/karar)?
2. Tebliğ tarihi nedir (süre bu tarihten işler)?
3. Talep edilen edim (ödeme, tahliye, ifa) ve miktarı?
4. Müvekkilin elinde itiraz/savunma için belge var mı?

## Denetim şeması
1. SÜRE BAŞLANGICI: Tebliğ tarihi sabitlenir; süreler bu tarihten işler. Ödeme emrine itiraz
   süresi (İİK m.62 — yedi gün), kambiyo takibinde itiraz (İİK m.168 — beş gün), kira temerrüt
   ihtarında ödeme süresi (TBK m.315) gibi süreler takvim tarihiyle yazılır.
2. TALEBİN NETLİĞİ: Ne istendiği (asıl alacak, faiz, masraf ayrımıyla) ve dayanağı yalın aktarılır.
3. SEÇENEKLER VE SONUÇLAR (risk): "Öderim / itiraz ederim / hiçbir şey yapmam" seçeneklerinin
   sonuçları açıkça yazılır. İtiraz edilmezse takibin kesinleşeceği (İİK m.62/son, m.78 haciz)
   net belirtilir; kambiyo takibinde itirazın icrayı durdurmadığı uyarılır.
4. YETKİ/İCRA DAİRESİ: Hangi icra dairesi/mahkeme, hangi merciye itiraz yapılacağı belirtilir.
5. İSPAT NOTU: İtiraz veya ödeme tarihinin ve şeklinin kanıtlanabilir olması gerektiği hatırlatılır.
6. ARA SONUÇ (istisna): Sade açıklama bilgilendirmedir; asıl bağlayıcı belge tebliğ edilen
   evraktır. Süre kaçırma riski varsa derhal vekille temas uyarısı eklenir.

## Çıktı modülleri
- "Size ne tebliğ edildi, kim, ne istiyor" özeti.
- Son tarih ve kalan gün (takvimli).
- Seçenekler / sonuçları tablosu.
- Acil yapılması gerekenler ve uyarı notu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
