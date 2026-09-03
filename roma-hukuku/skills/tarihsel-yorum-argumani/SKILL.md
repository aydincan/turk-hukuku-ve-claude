---
name: tarihsel-yorum-argumani
description: "Yürürlükteki bir maddenin yorumunda TMK m.1 çerçevesinde tarihî ve sistematik argüman üretilecekse; bir hükmün kökeninin (İsviçre/Roma) bugünkü anlamı aydınlatmak için kullanılacağı durumlarda devreye girer."
---

# Tarihsel-Sistematik Yorum Argümanı Üretimi

## Görev
Yürürlükteki bir Türk hükmünün yorumunda, kökenini (Roma/İsviçre/Pandekt) kullanarak TMK m.1 çerçevesinde tarihî ve sistematik yorum argümanı üretmek; bu argümanı yürürlükteki normun yerine değil, onun anlamını desteklemek için konumlamak.

## Soğuk başlangıç (intake)
- Hangi madde ve hangi yorum sorunu (lafzî belirsizlik, boşluk, çatışma)?
- Tarihî argüman lehte mi aleyhte mi kullanılacak?
- Karşı argüman (amaçsal/güncel yorum) da gerekiyor mu?

## Denetim şeması
1. Yorum sorununu çerçevele: TMK m.1 — kanun lafzıyla ve ruhuyla uygulanır; boşlukta hâkim örf-âdet, yoksa kendisi kural koyarmış gibi karar verir; yerleşik doktrin ve içtihattan yararlanır. Yorum yöntemini belirle: lafzî, sistematik, tarihî, amaçsal.
2. Tarihî kaynağı tespit et: maddenin İsviçre kaynağını (ZGB/OR) ve gerekiyorsa Roma kökünü resepsiyon zinciri yoluyla sapta. Kaynak normun lafzı/amacı ile Türk metni arasındaki farkı işaretle.
3. Tarihî argümanı kur: kanun koyucunun iktibasta korumak istediği amacı, kaynak hukuktaki yerleşik anlamı yürürlükteki maddenin yorumuna taşı. Roma kökeni varsa, kavramın klasik işlevini bugünkü anlamı aydınlatmak için kullan.
4. Sistematik argümanı ekle: maddenin TMK/TBK içindeki konumu, komşu hükümlerle (ör. genel-özel norm, TMK m.2-3 dürüstlük süzgeci) ilişkisini kur. lex specialis ve sistematik bütünlük argümanını uygula.
5. Sınır ve denge: tarihî argüman amaçsal/güncel yoruma feda edilebilir; kanun koyucunun iradesi ile bugünkü ihtiyaç çatışırsa, yürürlükteki amaçsal yorumun üstünlüğünü kabul et. Tarihî argüman destekleyicidir, belirleyici değil; bunu açıkça yaz.
6. Karşı argümanı tartı: tarihî yoruma karşı amaçsal/teleolojik itirazı kur ve hangisinin somut olayda baskın olduğunu gerekçelendir. Ara sonuç: yorum sonucunu ve tarihî argümanın ağırlığını netleştir.

İspat/dayanak: TMK m.1 ve ilgili madde ile; kaynak norm (ZGB/OR) ve Roma kökü fragman/künye ile [doğrulanacak]; mahkeme tarihî-sistematik yorum kullanmışsa karararama.yargitay.gov.tr üzerinden doğrula, karar numarası uydurma.

## Çıktı modülleri
- Yorum argümanı bloğu: madde + sorun + tarihî kök + sistematik konum + sonuç.
- Karşı argüman ve tartı notu.
- Sınır uyarısı: tarihî argüman destekleyici, yürürlükteki norm belirleyici.

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
