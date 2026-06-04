---
name: tarhiyat-ve-tebligat
description: "İkmalen, re'sen veya idarece yapılan tarhiyatın hukuka uygunluğunu ve tebligatın geçerliliğini denetlemek; ihbarnamenin biçim ve süre yönünden incelenmesi gerektiğinde kullanılır."
---

# Tarhiyat Türleri ve Tebligat Denetimi

## Görev
Mükellefe tebliğ edilen vergi/ceza ihbarnamesindeki tarhiyatın türünü, şartlarının oluşup oluşmadığını ve tebligatın geçerliliğini denetleyerek savunma veya dava stratejisinin temelini kurmak.

## Soğuk başlangıç (intake)
1. İhbarnamede tarhiyat türü belirtilmiş mi (ikmalen / re'sen / idarece)?
2. Re'sen tarh ise dayanak (defter ibraz etmeme, takdir komisyonu, VTR) nedir?
3. İhbarname kime, nasıl ve hangi tarihte tebliğ edildi?
4. Matrah farkının dayanağı (vergi tekniği raporu, tutanak) elde var mı?
5. Tarh edilen verginin ait olduğu dönem ve zamanaşımı durumu nedir?

## Denetim şeması
1. **Tarh türü tespiti:** Beyana dayanan tarh asıl usuldür; ek tarhiyatta ikmalen tarh (VUK m.29 — defter/belgeye veya kanuni ölçülere dayanan matrah farkı) ile re'sen tarh (VUK m.30 — matrahın defter-belge-kanuni ölçülerle tespiti mümkün olmadığında) ayrımını yap. Türün yanlış seçimi tek başına iptal sebebi olabilir.
2. **Re'sen takdir sebebi:** VUK m.30/2 bentlerinden hangisinin gerçekleştiğini doğrula (beyanname verilmemesi, defter tutulmaması/ibraz edilmemesi, kayıtların gerçeği yansıtmaması). Sebep yoksa re'sen tarh sakattır.
3. **Takdir/rapor dayanağı:** Matrah farkı vergi inceleme raporu (VUK m.140) veya takdir komisyonu kararına (VUK m.72 vd.) dayanmalı; gerekçesiz, somut tespite dayanmayan takdir denetlenir.
4. **İhbarnamenin unsurları:** VUK m.35 — ihbarnamede bulunması gereken zorunlu bilgiler (verginin nev'i, dönem, matrah, oran, dayanak, vergi/ceza miktarı, itiraz yolları). Eksiklik savunulabilirliği etkiler.
5. **Tebligat geçerliliği:** VUK m.93-109. Tebligat usulsüzse süre başlamaz; muhatap dışı kişiye tebliğ, adres yokluğu, ilanen tebliğ şartlarının (VUK m.103) oluşmaması incelenir. Ara sonuç: süre işlemeye başladı mı?
6. **İspat yükü:** Tarhiyatın maddi dayanağını idare ispatlar; mükellef tebligat/şekil sakatlığını ileri sürerse onu ispatlar.

## Çıktı modülleri
- Tarhiyat tür-şart uygunluk tablosu (sebep / dayanak / sonuç).
- Tebligat geçerlilik kontrol listesi ve süre başlangıç tarihi.
- İhbarname şekil denetimi notu (VUK m.35 eksiklik listesi).
- Savunma/dava argüman taslağı ve istenecek rapor listesi.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
