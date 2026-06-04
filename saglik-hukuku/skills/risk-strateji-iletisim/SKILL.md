---
name: risk-strateji-iletisim
description: "Tıbbi uyuşmazlıkta hekim, hastane veya hasta tarafının dava başarı şansını, risklerini ve müzakere/sulh seçeneklerini değerlendirmek ve müvekkile sade bir yol haritası sunmak için kullanılır."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Mevcut delil ve hukuki duruma göre tarafın kazanma/kaybetme riskini değerlendirmek, dava-sulh-arabuluculuk seçeneklerini tartmak ve müvekkile anlaşılır bir strateji sunmak.

## Soğuk başlangıç (intake)
1. Temsil edilen taraf kim: hasta/yakını, hekim, hastane, sigorta?
2. Eldeki en güçlü ve en zayıf delil hangisi?
3. Tarafın önceliği: tazminat miktarı, hız, mesleki itibar, ceza riskini bertaraf?
4. Mesleki sorumluluk (zorunlu/ihtiyari) sigortası var mı?

## Denetim şeması
1. **Olgu-hukuk uyumu**: Sorumluluk unsurları (kusur, illiyet, zarar, onam) mevcut delille ne ölçüde karşılanıyor? Her unsur için güç skoru (zayıf/orta/güçlü).
2. **Karşı taraf senaryosu**: Komplikasyon savunması, müterafik kusur (TBK m.52), aydınlatmanın ispatı, zamanaşımı def'i gibi olası savunmalar öngörülür.
3. **Bilirkişi/ATK riski**: Sonuç büyük ölçüde rapora bağlı; rapor lehe/aleyhe çıkma olasılığı strateji belirler.
4. **Sigorta ve rücu**: Hekim mesleki sorumluluk sigortası, kamu hekiminde idarenin rücu riski (3359 Ek m.18) değerlendirilir.
5. **Çözüm yolu seçimi**: Dava, sulh, arabuluculuk; ceza riski varsa savunma stratejisiyle eşgüdüm. Maliyet-fayda ve süre karşılaştırması.
6. **Müvekkil iletişimi**: Sonuç olasılıkları abartısız ve sade dille; garanti verilmez, en iyi/orta/en kötü senaryo sunulur. Ara sonuç: önerilen yol ve gerekçesi.

## Çıktı modülleri
- Unsur bazlı güç skoru tablosu
- Senaryo analizi (en iyi/orta/en kötü)
- Strateji önerisi (dava/sulh/arabuluculuk)
- Müvekkile sade dilde özet ve yapılacaklar listesi

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
