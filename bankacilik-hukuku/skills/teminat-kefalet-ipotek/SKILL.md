---
name: teminat-kefalet-ipotek
description: "Krediye bağlanan kefalet, ipotek, taşınır rehni veya banka teminat mektubunun geçerlilik şartlarını, kapsamını ve paraya çevrilmesini denetlemek; özellikle kefalette şekil ve eş rızası eksikliğini tespit etmek gerektiğinde kullanılır."
---

# Banka Teminatları (Kefalet, İpotek, Rehin, Teminat Mektubu)

## Görev
Bir banka alacağının teminatını (kefalet, ipotek, taşınır rehni, teminat mektubu) geçerlilik, kapsam ve sorumluluk üst sınırı bakımından denetlemek; teminatın paraya çevrilmesinde izlenecek yolu belirlemek.

## Soğuk başlangıç (intake)
- Teminat türü: adi/müteselsil kefalet, ipotek, ticari işletme rehni/taşınır rehni, banka teminat mektubu?
- Kefil/rehin veren gerçek kişi mi; evli ise eş rızası alınmış mı?
- Teminat belirli bir borç için mi yoksa "doğmuş/doğacak tüm borçlar" için mi (üst sınır ipoteği/azami kefalet)?
- Asıl borç muaccel mi; temerrüt ve ihtar süreci tamam mı?

## Denetim şeması
1. **Kefalette geçerlilik (TBK m.583)**: Kefalet sözleşmesi yazılı şekilde olmalı; kefilin sorumlu olacağı azami miktar, kefalet tarihi ve müteselsil kefil olunuyorsa bu husus kefilin **el yazısıyla** belirtilmelidir. Bu unsurların eksikliği kefaleti geçersiz kılar.
2. **Eşin rızası (TBK m.584)**: Eşlerden biri diğerinin yazılı rızası olmadan kefil olamaz; rıza en geç sözleşme kurulurken alınmalıdır. Ticari işletmeyle ilgili kefaletlerde m.584/3 istisnası (ticaret siciline kayıtlı tacirin verdiği kefalet vb.) ayrıca değerlendirilir.
3. **Kefaletin kapsamı ve süre**: Müteselsil kefilden doğrudan talep şartları (TBK m.586), kefile rücu, alacaklının özen ve teminatları koruma yükümlülüğü (TBK m.594) incelenir. Belirsiz süreli kefalette m.598 fesih imkânı kontrol edilir.
4. **İpotek/rehin**: İpoteğin tapuda tesisi, üst sınır (limit) ipoteğinde kapsam, fekki; taşınır/ticari işletme rehninde tescil. Paraya çevirme İİK m.145 vd. (rehnin paraya çevrilmesi yolu) ile yürür; krediye dayalı rehinde takip yolu doğru seçilmelidir.
5. **Teminat mektubu**: Banka teminat mektubu kural olarak bağımsız (garanti) niteliktedir; ilk talepte ödeme kaydı, def'ilerden bağımsızlık, süre ve istisnaen kötüniyet/açık hukuka aykırılık (def'i hakkı) değerlendirilir. Ara sonuç olarak teminatın geçerli/geçersiz olduğunu, kapsamını ve uygulanabilir takip yolunu yaz.

## Çıktı modülleri
- Teminat geçerlilik kontrol listesi (şekil, üst sınır, eş rızası, tescil).
- Sorumluluk kapsamı ve üst sınır analizi.
- Paraya çevirme/talep yolu adımları.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
