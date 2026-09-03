---
name: musade-hak-yoksunluklari
description: "Müsadere, belli hakları kullanmaktan yoksun bırakma ve diğer güvenlik tedbirlerinin infazı ile bu yoksunlukların sona ermesini değerlendirmek gerektiğinde kullanılır."
---

# Güvenlik Tedbirleri, Müsadere ve Hak Yoksunluklarının İnfazı

## Görev
Hapis/para cezası yanında hükmedilen güvenlik tedbirlerinin (müsadere, hak yoksunlukları) infazını ve bunların ne zaman sona ereceğini TCK ve 5275 çerçevesinde belirlemek.

## Soğuk başlangıç (intake)
- Hükümde hangi güvenlik tedbiri var (müsadere, hak yoksunluğu, sınır dışı, tedavi)?
- Müsadere eşya mı kazanç mı; üçüncü kişi hakkı söz konusu mu?
- Hak yoksunlukları mahkûmiyetin kanuni sonucu mu, ayrıca hükmedilmiş mi?
- Koşullu salıverilme/erteleme yoksunlukların süresini etkiliyor mu?

## Denetim şeması
1. Hak yoksunlukları: TCK m.53 kasten işlenen suçtan mahkûmiyetin kanuni sonucu olarak belirli hakları kullanmaktan yoksunluğu öngörür; kural olarak cezanın infazı tamamlanıncaya kadar sürer, belirli istisnalarda farklı süre uygulanır. Ara sonuç: yoksunluğun kapsamı ve süresi.
2. Müsadere: eşya müsaderesi (TCK m.54) ve kazanç müsaderesi (TCK m.55) ayrı denetlenir; iyiniyetli üçüncü kişiye ait eşya korunur, müsadere konusu mülkiyet ilişkisi araştırılır. İspat: malın suçla bağlantısı ve mülkiyet durumu.
3. Diğer tedbirler: akıl hastalarına özgü tedavi/koruma tedbirleri (TCK m.57), tüzel kişiler hakkında güvenlik tedbirleri (TCK m.60), yabancılarda sınır dışı (TCK m.59).
4. İnfaz usulü: güvenlik tedbirleri 5275 genel hükümlerine ve ilgili yönetmeliklere göre Cumhuriyet savcılığınca infaz edilir.
5. Sona erme/iade: hak yoksunlukları infazın tamamlanmasıyla; yasaklanmış hakların geri verilmesi için ayrı bir karar gerekebilir (5352 sayılı Adli Sicil Kanunu m.13/A çerçevesinde). Müsadere edilen ancak iadesi gereken eşya için iade usulü işletilir.
6. İtiraz: müsadere/iade ve yoksunluk uygulamasına karşı hükmü veren mahkeme veya infaz hâkimliği yolu; ilkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
7. Ara sonuç: tedbir kapsamı + süre/sona erme + başvuru mercii.

## Çıktı modülleri
- Güvenlik tedbiri envanteri ve süre tablosu.
- Üçüncü kişi hakkı/iade kontrol listesi.
- Yasaklanmış hakların geri verilmesi veya iade talebi dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
