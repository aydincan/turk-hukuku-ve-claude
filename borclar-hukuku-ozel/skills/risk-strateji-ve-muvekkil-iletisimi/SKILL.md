---
name: risk-strateji-ve-muvekkil-iletisimi
description: "Sözleşme uyuşmazlığında dava/sulh seçeneklerini tartmak, kazanma olasılığı ve maliyet-fayda analizini yapmak ve müvekkile anlaşılır bir yol haritası sunmak gerektiğinde kullanılır."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
İsimli sözleşme uyuşmazlığında hukuki pozisyonu gerçekçi tartmak, dava/sulh/ihtar seçeneklerini maliyet-fayda ve süre ekseninde değerlendirmek, müvekkile sade ve dürüst bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (tahsil, tahliye, sözleşmeden kurtulma, ilişkiyi sürdürme)?
- Eldeki delillerin gücü ve karşı tarafın muhtemel savunması?
- Zaman baskısı (yakın süreler, ticari ihtiyaç)?
- Risk iştahı ve bütçe (harç, vekâlet ücreti, bilirkişi)?

## Denetim şeması
1. **Pozisyon analizi.** Maddi vakıaları hukuki unsurlarla altla; her unsur için delil gücünü (güçlü/zayıf/eksik) işaretle. Zayıf halka (ör. süresinde ihbar ispatı, kefalette şekil) belirginleştirilir.
2. **Senaryo matrisi.** En iyi/orta/en kötü sonuç; kazanma olasılığı kaba bant olarak (yüksek/orta/düşük) verilir, kesin oran vaadinden kaçınılır. Karşı dava/takas riski değerlendirilir.
3. **Maliyet-fayda.** Tahmini harç ve giderler, yargılama süresi (istinaf/temyiz dâhil), tahsil kabiliyeti (karşı tarafın ödeme gücü, İİK takip riski). Düşük tutarlı işte arabuluculuk/sulh önceliklenir.
4. **Süre ve usul riski.** Yakın zamanaşımı/hak düşürücü süre, dava şartı arabuluculuk eksikliği, görev-yetki hatası gibi usulden ret riskleri öne alınır.
5. **Strateji seçimi.** İhtar → arabuluculuk → dava sıralaması; ihtiyati tedbir/haciz (İİK m.257) gereği; delil tespiti ihtiyacı. Sulh için makul aralık ve müzakere kozları belirlenir.
6. **Müvekkil iletişimi.** Hukuki sonuç sade Türkçe ile, seçeneklerin artı/eksisi ve önerilen adım net olarak yazılır; varsayımlar ve `[doğrulanacak]` veriler açıkça belirtilir, kesin kazanç taahhüdü verilmez. Ara sonuç: önerilen yol + gerekçe + sonraki adım listesi.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti.
- Müvekkile sade bilgilendirme notu ve aksiyon planı.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
