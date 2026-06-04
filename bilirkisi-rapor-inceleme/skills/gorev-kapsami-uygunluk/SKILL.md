---
name: gorev-kapsami-uygunluk
description: "Raporun, mahkemenin verdiği görevlendirme kararının ve sorulan soruların sınırları içinde kalıp kalmadığını; kapsam aşımı veya eksik yanıt bulunup bulunmadığını denetlemek istendiğinde kullanılır."
---

# Görevlendirme Kapsamı ve Uygunluk Denetimi

## Görev
Raporu görevlendirme kararının çıpasına oturtmak: bilirkişiye yazılı olarak bildirilen görev kapsamı ve süre (HMK m.273) ile raporun fiilen yanıtladığı hususları karşılaştırıp **kapsam aşımı** ve **eksik yanıt** kusurlarını tespit etmek.

## Soğuk başlangıç (intake)
- Görevlendirme kararının tam metni ve bilirkişiye sorulan sorular elinizde mi?
- Bilirkişiye verilen kesin süre içinde mi rapor sunulmuş?
- Rapor, sorulmayan bir hususta görüş bildiriyor mu?
- Sorulduğu hâlde yanıtsız kalan soru var mı?

## Denetim şeması
1. **Yazılı kapsamla karşılaştırma (HMK m.273):** Görev, kapsamı ve süresi yazılı bildirilir. Sorular tek tek listelenir; her sorunun raporda karşılığı işaretlenir. Karşılıksız kalan → **eksik**; sorulmadığı hâlde yanıtlanan → **aşım**.
2. **Hukuki nitelendirme aşımı (HMK m.266, m.279/son):** Bilirkişinin "kusur oranı %X, davalı sorumludur, şu tazminata hükmedilmeli" gibi hukuki sonuç çıkarması görev sınırının aşılmasıdır; nitelendirme hâkime aittir.
3. **Uzmanlık alanı sınırı (6754 s.K. m.3):** Bilirkişi yalnızca uzmanlık ve teknik alanında görüş verebilir; alan dışı görüş ret/itiraz sebebidir. Heyet raporlarında her üyenin alanı kontrol edilir.
4. **Bizzat ifa (HMK m.277):** Görev devredilemez; rapor fiilen başka kişiye hazırlatılmışsa aşımdır.
5. **Ara sonuç:** Eksik yanıtlar → **ek rapor** talebi; aşım ve alan dışı görüş → **esasa itiraz / rapora itibar edilmemesi** talebi (HMK m.281, m.282).

## Çıktı modülleri
- Soru-yanıt eşleştirme tablosu (sorulan / yanıtlanan / eksik / aşım).
- Hukuki nitelendirme aşımı içeren paragrafların listesi.
- Uzmanlık alanı uyumsuzluğu notu.
- Kapsam temelli itiraz paragrafı taslağı.

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
