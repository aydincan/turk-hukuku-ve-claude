---
name: ceza-idari-bilirkisi
description: "Bilirkişi raporu ceza muhakemesinden (CMK) veya idari yargıdan (İYUK) geliyorsa, bu kollara özgü usul kuralları, ATK ve rapora karşı savunma/itiraz olanaklarını değerlendirmek istendiğinde kullanılır."
---

# Ceza ve İdari Yargıda Bilirkişi Raporu

## Görev
Hukuk yargılamasından farklı işleyen ceza ve idari yargı kollarındaki bilirkişi rejimini denetlemek: CMK m.62-73 ve İYUK m.31 yollamasıyla HMK kurallarını doğru uygulayıp rapora karşı savunma/itirazı kurmak.

## Soğuk başlangıç (intake)
- Rapor ceza dosyasından mı (soruşturma/kovuşturma) yoksa idari yargıdan mı geliyor?
- Ceza dosyasında rapor resmî bilirkişiden mi, ATK'dan mı, yoksa özel uzmandan mı?
- İdari davada bilirkişi keşfi/incelemesi yapıldı mı?
- Rapor aleyhe ve hangi noktada hatalı?

## Denetim şeması
1. **Ceza muhakemesi (CMK m.63-67):** Bilirkişi atanması, görev kapsamı ve rapor içeriği CMK m.67'ye göre denetlenir; çözümü uzmanlığı gerektiren hâllerde başvurulur. Bilirkişi hukuki sorunda görüş veremez. Taraflar uzman mütalaası (CMK m.67/son ve m.178 kapsamında) sunarak rapora karşı koyabilir.
2. **ATK raporları:** Adli Tıp Kurumu raporlarına da itiraz edilebilir; rapora karşı bilimsel/yöntemsel itiraz, üst kurul/yeni inceleme talebiyle desteklenir. ATK raporu da hâkimi mutlak bağlamaz.
3. **İdari yargı (İYUK m.31):** İYUK; bilirkişi, keşif ve delil tespitinde HMK'ya yollar. Bu nedenle HMK m.266-282 denetim mantığı idari davada da geçerlidir; rapora itiraz HMK m.281 çerçevesinde sunulur.
4. **Uzmanlık alanı sınırı (6754 s.K. m.3):** Her üç kolda da alan dışı ve hukuki nitelendirme içeren görüş itiraz sebebidir.
5. **Ara sonuç:** Yargı koluna göre doğru usul kuralı seçilir; rapora karşı uygun araç (itiraz, uzman mütalaası, yeni/ek inceleme) belirlenir.

## Çıktı modülleri
- Yargı koluna göre uygulanacak usul kuralları haritası (CMK / İYUK→HMK).
- Rapora karşı kullanılabilecek araçların listesi (itiraz / uzman mütalaası / yeni inceleme).
- ATK/resmî rapor için özel itiraz notları.
- Kola uygun itiraz/savunma paragrafı taslağı.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
