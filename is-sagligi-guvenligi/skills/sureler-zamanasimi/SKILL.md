---
name: sureler-zamanasimi
description: "İş kazası tazminatı, SGK rücuu, idari ceza itirazı, bildirim ve ceza yargılamasındaki süre ve zamanaşımlarını hesaplamak ve hak kaybını önlemek için kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
İSG dosyasındaki tüm süre ve zamanaşımlarını eksiksiz tespit etmek, başlangıç anlarını doğru belirlemek ve hak düşürücü riskleri uyarmak.

## Soğuk başlangıç (intake)
- Olay/kaza tarihi, zararın/maluliyetin öğrenildiği tarih (zamanaşımı başlangıcı için kritik)?
- İdari ceza/karar tebliğ tarihi?
- Bildirimler (SGK, kolluk) ne zaman yapıldı?
- Ceza yargılaması varsa fiilin tarihi ve suç tipi?

## Denetim şeması
1. **İş kazası tazminatı zamanaşımı:** İşçinin/hak sahiplerinin işverene karşı tazminat talebi sözleşmeye dayalı olduğundan kural olarak on yıllık zamanaşımına tabidir (TBK m.146); bedensel zararda zararın gelişimi ve maluliyetin kesinleşmesi başlangıcı etkiler. Ceza zamanaşımının daha uzun olduğu hallerde uzamış (ceza) zamanaşımı uygulanabilir (TBK m.72/1 son cümle). Güncel içtihatla doğrula.
2. **SGK rücu zamanaşımı:** Halefiyet/rücuun niteliğine göre belirlenir; başlangıç ve süre için karararama.yargitay.gov.tr içtihadını `[doğrulanacak]` olarak teyit et, bellekten süre verme.
3. **İdari para cezasına itiraz (5326 m.27):** Tebliğden itibaren on beş gün; sulh ceza kararına itiraz da kısa süreli. Kabahat için soruşturma ve yerine getirme zamanaşımları (5326 m.20) ayrıca işler.
4. **Bildirim süreleri:** İş kazasının SGK'ya bildirimi kazadan sonraki üç iş günü içinde (5510 m.13/2); gecikme idari ceza ve rücu sonucu doğurur.
5. **Ceza zamanaşımı:** TCK m.66 dava zamanaşımı suç tipine göre. **Ara sonuç:** Her süreyi başlangıç anı + süre + bitiş tarihiyle tablola; en yakın tarihi öne çıkar.

## Çıktı modülleri
- Süre/zamanaşımı takvimi (başlangıç-süre-bitiş).
- Hak düşürücü/itiraz süreleri uyarı listesi.
- Doğrulanacak içtihat süreleri için kaynak notu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
