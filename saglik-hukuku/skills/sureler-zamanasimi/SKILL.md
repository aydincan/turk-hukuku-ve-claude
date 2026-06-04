---
name: sureler-zamanasimi
description: "Tıbbi sorumluluk talebinde hangi zamanaşımı süresinin (sözleşme, haksız fiil, idari, cezai) işlediğini ve başlangıç anını hesaplamak için kullanılır; rejim seçiminin tazminat hakkına etkisini ortaya koyar."
---

# Süreler ve Zamanaşımı

## Görev
Talebin hangi zamanaşımına tabi olduğunu, sürelerin başlangıç anını ve kesilme/durma hâllerini hesaplamak; en lehe rejimi tespit etmek.

## Soğuk başlangıç (intake)
1. Hukuki sebep sözleşme mi, haksız fiil mi, idari mi, cezai mi?
2. Zararın ve failin öğrenildiği tarih nedir?
3. Olay üzerinden kaç yıl geçti?
4. Daha ağır cezayı gerektiren bir suç söz konusu mu (ceza zamanaşımı)?

## Denetim şeması
1. **Sözleşmesel sorumluluk (vekâlet)**: Kural olarak TBK m.146 — 10 yıllık genel zamanaşımı. Sözleşme rejimi davacı için süre avantajı sağlar.
2. **Haksız fiil**: TBK m.72 — fiil ve failin öğrenilmesinden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanır (uzamış zamanaşımı).
3. **İdari (tam yargı)**: İYUK m.13 — zararın öğrenilmesinden itibaren 1 yıl ve her hâlde olaydan itibaren 5 yıl içinde idareye başvuru; dava süreleri İYUK m.7.
4. **Cezai**: Dava zamanaşımı TCK m.66; taksirle öldürme/yaralamada suçun cezasına göre değişir. Şikâyete bağlı yaralamada TCK m.73 — 6 ay şikâyet süresi.
5. **Başlangıç anı sorunu**: Geç ortaya çıkan zararlarda (gizli sakatlık) öğrenme anı kritiktir; objektif öğrenme aranır.
6. **Ara sonuç**: Birden çok rejim varsa davacı için en uzun olan seçilir; zamanaşımı def'i karşı tarafça ileri sürülmedikçe re'sen dikkate alınmaz.

## Çıktı modülleri
- Rejim bazlı zamanaşımı tablosu (süre + başlangıç)
- En lehe süre seçimi gerekçesi
- Kesilme/durma ve başvuru takvimi
- Süre riski uyarısı (kritik tarih)

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
