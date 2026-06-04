---
name: itiraz-dilekce-taslagi
description: "Tespit edilen bulguları iki haftalık süre içinde mahkemeye sunulacak somut, gerekçeli bir itiraz dilekçesine dönüştürmek; ek rapor, yeni bilirkişi veya rapora itibar edilmemesi taleplerini formüle etmek istendiğinde kullanılır."
---

# Bilirkişi Raporuna İtiraz Dilekçesi Taslağı

## Görev
Denetim bulgularını HMK m.281'e uygun, süresinde ve somutlaştırılmış bir itiraz dilekçesine dökmek; talep sonucunu (ek rapor / yeni heyet / itibar edilmemesi) bulgu ağırlığına göre netleştirmek.

## Soğuk başlangıç (intake)
- Rapor size hangi tarihte tebliğ edildi (iki haftalık sürenin başlangıcı)?
- Hangi bulgular dilekçeye girecek ve her biri hangi dayanağa çıpalı?
- Asıl talebiniz ek rapor mu, yeni bilirkişi mi, rapora itibar edilmemesi mi?
- Karşı uzman mütalaası ekleyecek misiniz?

## Denetim şeması
1. **Süre kontrolü (HMK m.281):** İtiraz, raporun tebliğinden itibaren iki hafta içinde yapılır. Son gün hesaplanır; süre geçecekse ek süre/mazeret değerlendirilir. Süre dilekçenin en üstünde teyit edilir.
2. **Somutlaştırma zorunluluğu:** "Rapor hatalıdır" gibi soyut itiraz sonuç doğurmaz; her itiraz, rapordaki sayfa/paragraf + görevlendirme sorusu + dosya deliliyle gerekçelendirilir.
3. **Talep sınıflandırması (HMK m.281):** Eksik/belirsiz husus → eksikliğin tamamlanması (ek rapor); yöntem/tarafsızlık kusuru → yeni bilirkişi/heyet; hukuki nitelendirme aşımı/caizsizlik → rapora itibar edilmemesi (HMK m.282 ile rapor hâkimi bağlamaz vurgusu).
4. **Dilekçe mimarisi:** Başlık ve süre teyidi; özet; bulgu bulgu itirazlar (her biri dayanaklı); varsa karşı uzman mütalaasına atıf; talep sonucu. Yer tutucular **[doldurulacak]** olarak işaretlenir.
5. **Ara sonuç:** Dilekçe, tek tek bulguların talep sonucuyla bağlandığı, denetlenebilir bir metne dönüşür.

## Çıktı modülleri
- Süre teyitli dilekçe başlığı ve özet bloğu.
- Numaralı, dayanaklı itiraz maddeleri (sayfa + soru + delil çıpalı).
- Talep sonucu paragrafı (ek rapor / yeni heyet / itibar edilmemesi).
- Eklenecek belge/mütalaa dizini ve [doldurulacak] kontrol listesi.

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
