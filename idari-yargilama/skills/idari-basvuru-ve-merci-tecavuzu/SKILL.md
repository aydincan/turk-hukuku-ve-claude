---
name: idari-basvuru-ve-merci-tecavuzu
description: "Dava öncesi üst makama başvuru, zorunlu idari başvuru yolları, zımni ret kavramı ve idari merci tecavüzü değerlendirilirken kullanılır; bir işleme doğrudan dava açılabilir mi yoksa önce idareye başvurulmalı mı sorusunda başvurulur."
---

# İdari Başvuru, Zımni Ret ve Merci Tecavüzü

## Görev
Dava açılmadan önce idareye başvurunun zorunlu mu ihtiyari mi olduğunu, zımni ret sürelerini ve merci tecavüzünün sonuçlarını belirleyerek davanın usulden reddini önlemek.

## Soğuk başlangıç (intake)
- İlgili mevzuat, dava öncesi zorunlu bir idari başvuru (itiraz) öngörüyor mu?
- İlgili idareye yapılmış bir başvuru var mı; başvuru tarihi ve cevap durumu?
- İdare hiç cevap vermedi mi (zımni ret) yoksa açık ret mi verdi?
- Başvuru dava açma süresi içinde mi yapıldı?

## Denetim şeması
1. **İhtiyari başvuru ve sürenin durması** (İYUK m.11): İlgililer dava açma süresi içinde, işlemi yapan veya üst makama başvurarak işlemin kaldırılması/geri alınması/değiştirilmesini isteyebilir. Bu başvuru işlemeye başlamış dava süresini **durdurur**.
2. **Zımni ret** (İYUK m.10): İlgililerin idareye yaptıkları başvurulara **60 gün** içinde cevap verilmezse istek reddedilmiş (zımni ret) sayılır; bu sürenin bitiminden itibaren dava açma süresi işler. İdare 60 gün geçtikten sonra cevap verirse, cevap tarihinden itibaren dava süresi yeniden işlemeye başlar.
3. **m.11 zımni reddi**: m.11 başvurusuna 30 gün (özel kanunda farklı süre yoksa) içinde cevap verilmezse istek reddedilmiş sayılır ve durmuş olan dava süresi kaldığı yerden işlemeye devam eder.
4. **Zorunlu idari başvuru / merci tecavüzü** (İYUK m.15/1-e): Mevzuat dava açmadan önce tüketilmesi zorunlu bir başvuru yolu öngörmüşse (ör. bazı vergi/gümrük itirazları, kamu ihalesinde KİK'e itirazen şikâyet), bu yol tüketilmeden açılan dava **merci tecavüzü** nedeniyle reddedilir ve dilekçe ilgili mercie tevdi olunur.
5. **İspat yükü**: Başvuru ve tebliğ tarihlerini ispat ilgilidedir; başvurunun kayıtlı/iadeli yapılması önerilir.
6. **Ara sonuç**: Başvurunun ihtiyari mi zorunlu mu olduğu ayrımı, hem süre hesabını hem de merci tecavüzü riskini doğrudan etkiler; tereddütte zorunlu yol varsayımıyla hareket güvenlidir.

## Çıktı modülleri
- Başvuru türü (ihtiyari/zorunlu) tespiti
- Zımni ret ve süre etkisi hesabı
- Merci tecavüzü riski ve gerekli başvuru taslağı

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
