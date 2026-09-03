---
name: zamanasimi-sikayet-dava-engelleri
description: "Dava ve ceza zamanaşımı sürelerini, şikâyete bağlı suçlarda süre ve usulü, önödeme ve uzlaştırmayı hesaplamak ve dava engellerini denetlemek gerektiğinde kullanılır."
---

# Zamanaşımı, Şikâyet ve Dava Engelleri

## Görev
Bir ceza dosyasında dava açma/yürütme engellerini denetlemek: dava ve ceza zamanaşımı, şikâyet süresi, önödeme ve uzlaştırma kurumlarını hesaplamak.

## Soğuk başlangıç (intake)
- Suçun yasal cezasının üst sınırı nedir (zamanaşımı buna göre belirlenir)?
- Suç tarihi ve varsa son kesen işlem tarihi nedir?
- Suç şikâyete bağlı mı; mağdur faili ve fiili ne zaman öğrendi?
- Suç önödeme veya uzlaştırma kapsamında mı?

## Denetim şeması
1. **Dava zamanaşımı süreleri (m.66):** Cezanın üst sınırına göre kademeli süreler (örn. 5 yıldan az hapiste 8 yıl, 5-20 yıl arası fiillerde artan süreler); süre suçun işlendiği günden işler (m.66/6). Çocuklarda süreler indirilir.
2. **Kesen ve durduran nedenler (m.67):** İfade alma, tutuklama, iddianame, mahkûmiyet kararı gibi işlemler süreyi keser; kesilmeyle yeniden başlar fakat uzatılmış süreyi (yarısından fazla) geçemez. Ara sonuç: en son hangi işlem kesti?
3. **Ceza zamanaşımı (m.68-69):** Kesinleşmiş cezanın infaz edilememesi süreleri; ceza türü ve miktarına göre.
4. **Şikâyet (m.73):** Şikâyete bağlı suçlarda mağdur fiili ve faili öğrenmesinden itibaren altı ay içinde şikâyet etmelidir; süre geçerse kovuşturma yapılamaz. Şikâyetten vazgeçme davayı/cezayı düşürür.
5. **Önödeme (m.75):** Yalnızca adli para cezası veya üst sınırı belirli hapsi gerektiren suçlarda; belirlenen miktarın ödenmesiyle kamu davası açılmaz/düşer.
6. **Uzlaştırma (CMK m.253):** Kapsamdaki suçlarda uzlaştırma zorunlu ön koşuldur; uzlaşma kovuşturmaya yer olmadığına ya da düşmeye yol açar. Ara sonuç: dosya uzlaştırma kapsamında mı?

## Çıktı modülleri
- Zamanaşımı hesap tablosu (başlangıç, kesen işlemler, son tarih).
- Şikâyet süresi ve usul kontrolü.
- Önödeme/uzlaştırma uygunluk notu.
- Dava engeli sonucu ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
