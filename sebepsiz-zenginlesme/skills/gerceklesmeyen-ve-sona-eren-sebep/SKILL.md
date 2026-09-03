---
name: gerceklesmeyen-ve-sona-eren-sebep
description: "Bir edim ileride doğacak bir sebep için verildiği halde o sebep gerçekleşmediğinde veya başlangıçta var olan sebep sonradan ortadan kalktığında iadeyi belirlemek gerektiğinde kullanılır."
---

# Gerçekleşmeyen ve Sona Eren Sebep

## Görev
TBK m.77/2'nin diğer iki tipini denetlemek: gerçekleşmeyen sebep (condictio ob causam futuram) ve sona eren sebep (condictio ob causam finitam). Tipik örnekler: gerçekleşmeyen evlenme/sözleşme beklentisiyle yapılan kazandırmalar, geçersiz hale gelen veya bozulan ilişkide kalan edimler, dönmeyle (TBK m.125) tasfiye edilen edimler.

## Soğuk başlangıç (intake)
- Edim hangi ileriki sebep/amaç için verildi; o sebep gerçekleşti mi?
- Başlangıçta geçerli bir sebep var mıydı; sonradan hangi olayla ortadan kalktı?
- Sözleşmeden dönme, bozucu şart, fesih gibi bir tasfiye sebebi var mı?
- Karşı taraf edimi aldıktan sonra elden çıkardı mı; iyiniyetli mi?

## Denetim şeması
1. **Gerçekleşmeyen sebep.** Edim, ileride doğması beklenen bir sebep/amaç için verilmiş ama o amaç kesin olarak gerçekleşmemişse iade gerekir (m.77/2). Karşı tarafın amacın gerçekleşmesini bilerek engellemesi de iadeyi haklı kılar.
2. **Sona eren sebep.** Kazandırma anında geçerli olan sebep sonradan ortadan kalkarsa (bozucu şartın gerçekleşmesi, sözleşmenin geçmişe etkili sona ermesi), o ana kadarki edim sebepsiz hale gelir.
3. **Dönme ile yarışma/ayrım.** Sözleşmeden dönmede (TBK m.125/2) verilen edimlerin iadesi kural olarak dönmenin kendi tasfiye rejimine tâbidir; sebepsiz zenginleşme tamamlayıcı rol oynar. Hangi rejimin uygulanacağı önce belirlenir.
4. **İade kapsamı (m.79).** İyiniyetli zenginleşen yalnızca elinde kalan zenginleşme ölçüsünde; kötüniyetli olan veya iadeyi göze almalıydıysa tam iade ile sorumlu. Semere ve kullanım yararı iyiniyete göre eklenir.
5. **İspat.** Sebebin gerçekleşmediğini/sona erdiğini iade isteyen ispatlar; karşı taraf sebebin gerçekleştiğini veya kazandırmanın bağışlama amaçlı olduğunu ileri sürerse onu ispatlar.
6. **Ara sonuç.** Tip + iade kapsamı + faiz/semere başlangıcı + zamanaşımı (m.82, öğrenmeden 2 yıl) haritası çıkar.

## Çıktı modülleri
- Tip teşhisi ve tasfiye rejimi seçim notu (dönme mi, m.77 mi).
- İade kapsamı tablosu (iyiniyet ayrımıyla).
- İade talebi dava iskeleti.

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
