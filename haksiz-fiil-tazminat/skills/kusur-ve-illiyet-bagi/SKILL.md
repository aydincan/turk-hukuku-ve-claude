---
name: kusur-ve-illiyet-bagi
description: "Failin kusurlu olup olmadığı, kusurun derecesi veya fiil ile zarar arasındaki nedensellik tartışmalıysa; özellikle birden çok sebep, üçüncü kişi müdahalesi ya da mücbir sebep iddiası varsa kullanılır."
---

# Kusur ve Uygun İlliyet Bağı

## Görev
Failin kusurunu (kast/ihmal) objektif özen ölçütüyle tespit etmek ve fiil ile zarar arasındaki uygun illiyet bağını kurmak; illiyeti kesen sebepleri (mücbir sebep, zarar görenin/üçüncü kişinin ağır kusuru) denetlemek. Kusur derecesi hem sorumluluğu hem indirim/tazminat miktarını (m.51-52) etkiler.

## Soğuk başlangıç (intake)
- Fail nasıl davrandı; benzer durumdaki basiretli kişi ne yapardı?
- Zarara katkıda bulunan başka sebep/kişi var mı?
- Mücbir sebep, beklenmeyen hâl veya zarar görenin davranışı zincire girdi mi?
- Kusur sorumluluğu mu yoksa objektif sorumluluk normu mu uygulanacak?

## Denetim şeması
1. **Kusur türü ve derecesi.** Kast (zararı isteyerek/öngörerek) ya da ihmal (gerekli özeni göstermeme). Ölçü, somut kişinin yeteneği değil, aynı durumdaki makul/basiretli kişinin davranışıdır. Ağır/hafif ihmal ayrımı m.51-52 için önemlidir.
2. **İhmali davranışta yükümlülük.** Sorumluluk için hukuken bir hareket etme/önlem alma yükümü (kanun, sözleşme, önceki tehlikeli davranış, dürüstlük kuralı TMK m.2) bulunmalıdır.
3. **Uygun illiyet testi.** Fiil, hayatın olağan akışına ve genel tecrübeye göre bu tür zararı doğurmaya elverişli mi? Sadece koşul oluşturan uzak sebepler dışlanır.
4. **İlliyeti kesen sebepler.** Mücbir sebep, zarar görenin ya da üçüncü kişinin öngörülemez ve ağır kusuru, illiyet bağını tümüyle kesebilir; kısmen etkiliyse m.52 indirimi devreye girer.
5. **Çok sebepli zarar.** Birden çok failin ortak kusuru müteselsil sorumluluk doğurur (m.61); yarışan sebeplerde her birinin katkı oranı belirlenir.
6. **Ara sonuç ve ispat.** Kusuru ve illiyeti kural olarak zarar gören ispatlar (TMK m.6); kusursuz sorumlulukta kusur aranmaz, ama illiyet ve kurtuluş kanıtı (örn. m.66 özen) ayrıca değerlendirilir.

## Çıktı modülleri
- Kusur derecesi değerlendirme notu (ölçü + dayanak).
- İlliyet zinciri şeması (sebepler + kesen etkenler).
- Müterafik kusur/indirim ön değerlendirmesi.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
