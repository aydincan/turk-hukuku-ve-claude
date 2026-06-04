---
name: e-ticaret-kvkk-veri
description: "E-ticaret sitesi veya platformunun müşteri verisi işleme, açık rıza, aydınlatma, çerez ve veri aktarımı yükümlülüklerinin KVKK uyumunun denetlenmesi gerektiğinde kullanılır."
---

# E-Ticarette Kişisel Veri ve KVKK Uyumu

## Görev
E-ticaret faaliyetinde toplanan kişisel verilerin (üyelik, sipariş, ödeme, davranışsal/çerez verisi) 6698 sayılı KVKK'ya uygun işlenmesini denetlemek; ticari ileti onayı ile KVKK rızasının ayrıştırılmasını sağlamak.

## Soğuk başlangıç (intake)
- Hangi veri kategorileri işleniyor (kimlik, iletişim, ödeme, konum, çerez/davranış)?
- İşlemenin hukuki sebebi ne (sözleşmenin ifası, meşru menfaat, açık rıza)?
- Yurt dışına aktarım var mı (yurt dışı ödeme/bulut/pazarlama araçları)?
- Aydınlatma metni, çerez politikası ve VERBİS kaydı mevcut mu?

## Denetim şeması
1. Hukuki sebep (6698 m.5): sipariş/teslim için işleme çoğu kez sözleşmenin ifası (m.5/2-c) ya da meşru menfaate (m.5/2-f) dayanır; pazarlama/profilleme için kural olarak açık rıza gerekir. Rıza, hizmet şartına bağlanamaz.
2. Aydınlatma (6698 m.10): veri sorumlusu kimliği, işleme amaçları, aktarım, toplama yöntemi ve hakları içeren aydınlatma yapılır; ticari ileti onayından ayrı belgelenir.
3. Ticari ileti–KVKK ayrımı: 6563 ileti onayı ile KVKK açık rızası farklı hukuki kurumlardır; tek kutucukla birlikte alınması sakıncalıdır, ayrı ayrı ve özgür iradeyle alınmalıdır.
4. Aktarım (6698 m.9): yurt dışı aktarımda 2024 değişikliği sonrası yeterlilik kararı, uygun güvenceler (standart sözleşme/bağlayıcı kurallar) ya da istisna zemini aranır; standart sözleşme Kurula bildirilir.
5. Güvenlik ve ihlal (6698 m.12): teknik-idari tedbirler; veri ihlalinde Kurula ve ilgili kişiye makul sürede bildirim.
İspat yükü: rıza, aydınlatma ve tedbirlerin varlığını veri sorumlusu ispatlar.

## Çıktı modülleri
- Veri işleme envanteri ve hukuki sebep tablosu.
- Aydınlatma/açık rıza/çerez metni boşluk raporu.
- Aktarım ve ihlal müdahale notu.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
