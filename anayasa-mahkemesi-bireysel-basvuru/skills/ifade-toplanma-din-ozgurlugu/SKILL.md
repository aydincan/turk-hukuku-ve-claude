---
name: ifade-toplanma-din-ozgurlugu
description: "İfade ve basın özgürlüğü, örgütlenme/toplantı ve gösteri, din ve vicdan özgürlüğüne yönelik yaptırım, ceza, yasak veya müdahaleler iddia edildiğinde kullanılır."
---

# İfade, Toplanma ve Din Özgürlüğü İhlali

## Görev
m.26 (ifade), m.28 (basın), m.33-34 (örgütlenme, toplantı-gösteri) ve m.24 (din-vicdan) kapsamındaki müdahalelerin m.13 süzgecinden geçirilerek ölçülü olup olmadığını değerlendirmek.

## Soğuk başlangıç (intake)
- Müdahale neye yöneldi (söz, yazı, paylaşım, gösteri, dernek/sendika eylemi, inanç pratiği)?
- Müdahale türü: ceza, idari yaptırım, yasak, görevden uzaklaştırma, erişim engeli?
- Müdahalenin kanuni dayanağı ve güttüğü meşru amaç nedir?
- İfade/eylem kamusal tartışmaya, siyasete veya gazetecilik faaliyetine mi ilişkin?

## Denetim şeması
1. Müdahalenin varlığı — yaptırım, ceza, yasak veya caydırıcı (chilling) etki doğuran her tedbir müdahaledir.
2. Kanunilik — m.13: erişilebilir, öngörülebilir ve belirli kanun şartı; muğlak/aşırı geniş norm uygulaması ihlale yol açabilir.
3. Meşru amaç — m.26/2 ve ilgili maddelerdeki sınırlama sebepleri (millî güvenlik, kamu düzeni, başkalarının hak ve şöhreti vb.).
4. Demokratik toplumda gereklilik ve ölçülülük — "zorlayıcı toplumsal ihtiyaç" var mı; tedbir ile amaç orantılı mı; daha hafif araç mümkün mü. Siyasi söylem, kamu yararına haber ve eleştiriye geniş koruma; ifadenin değer yargısı mı olgu açıklaması mı olduğu; yaptırımın ağırlığı ve caydırıcı etkisi tartılır.
5. Toplanma/örgütlenme — barışçıl gösteriye ve dernek/sendika faaliyetine müdahalede aynı üçlü test; barışçıllık karinesi.
6. Din-vicdan — inancı açıklama özgürlüğüne müdahalede tarafsızlık ve çoğulculuk ölçütü.

Denge: İfade ile başkalarının kişilik hakkı (m.17/m.20) çatışıyorsa AYM çatışan haklar arasında adil denge kurar.

İspat yükü: müdahaleyi başvurucu; gerekliliği ve orantılılığı kamu makamı temellendirir.

Ara sonuç: hangi ölçütte ihlal bulunduğu.

## Çıktı modülleri
- Müdahale türü ve ilgili madde tespiti.
- Üçlü test altlaması (kanunilik–amaç–gereklilik/ölçülülük).
- Caydırıcı etki ve yaptırım ağırlığı notu.
- İlke kararlarına atıf [doğrulanacak].

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
