---
name: giderler-ve-iade-engelleri
description: "Zenginleşenin yaptığı zorunlu/faydalı/lüks giderlerin mahsubu ile hukuka veya ahlaka aykırı amaçla yapılan kazandırmalarda iadenin reddi söz konusu olduğunda kullanılır."
---

# Giderler, Mahsup ve İade İsteyememe Halleri

## Görev
İade alacaklısının talebine karşı zenginleşenin gider iadesi haklarını (TBK m.80) ve iadeyi tümden engelleyen halleri (TBK m.78/2 ve m.81) denetlemek; bu savunmaların çoğu davanın miktarını veya kaderini belirlediği için ihtarname ve dilekçe aşamasında öne alınmalıdır.

## Soğuk başlangıç (intake)
- Zenginleşen, iade edeceği şey için masraf/gider yaptı mı; türü ne (zorunlu, faydalı, lüks)?
- Kazandırma hukuka veya ahlaka aykırı bir amaç taşıyor muydu (rüşvet, yasak iş, vb.)?
- Ödeme zamanaşımına uğramış bir borç ya da ahlaki ödev için mi yapıldı?
- Lüks gider için söküp alma mümkün mü?

## Denetim şeması
1. **Gider türlerini ayır (m.80).** Zorunlu giderler (şeyin korunması için kaçınılmaz) ve faydalı giderler (değer artıran) iade alacaklısından istenebilir; lüks (zevki için) giderler istenemez ama zenginleşen, asıl şeye zarar vermeden söküp alabilir.
2. **İyiniyet etkisi.** İyiniyetli zenginleşenin faydalı giderleri geri verme anındaki değer artışı ölçüsünde; kötüniyetli zenginleşenin gider hakları sınırlıdır. Gider alacağı, iade borcundan mahsup edilir.
3. **Hukuka/ahlaka aykırı amaç (m.81).** Hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez ("temiz el" ilkesi). Hâkim, bu şeyin Devlet Hazinesine gelir kaydedilmesine karar verebilir.
4. **m.81 sınırı.** İade yasağı, verenin de aykırılığa katıldığı hallerde işler; salt karşı tarafın amacının ahlaka aykırı olması her zaman iadeyi kapatmaz. Olayın somut ahlaki/hukuki değerlendirmesi yapılır.
5. **Geçerli sayılan ifalar (m.78/2).** Zamanaşımına uğramış borcun ödenmesi ve ahlaki ödevin ifası geri istenemez; bunlar iade engeli olarak ayrıca işaretlenir.
6. **İspat ve ara sonuç.** Giderleri ve türünü zenginleşen; aykırı amacı (m.81) iadeye karşı çıkan taraf ispatlar. Ara sonuç: net iade miktarı (gider mahsubu sonrası) ve iadenin tümden reddedilip reddedilmeyeceği.

## Çıktı modülleri
- Gider türü-mahsup tablosu.
- m.81 (ahlaka aykırılık) savunma/karşı savunma notu.
- İade engeli değerlendirmesi ve sonuç senaryosu.

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
