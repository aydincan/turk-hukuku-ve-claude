---
name: sartlar-ve-denetim-semasi
description: "Sebepsiz zenginleşmenin dört unsurunu (zenginleşme, fakirleşme, illiyet, haklı sebebin yokluğu) somut olaya adım adım uygulamak ve talebin doğup doğmadığını test etmek gerektiğinde kullanılır."
---

# Unsurlar ve Ana Denetim Şeması

## Görev
TBK m.77/1 unsurlarını somut olaya altlayarak iade alacağının doğup doğmadığını denetlemek; "haklı sebep" kavramını ve illiyet bağını uygulamalı olarak çözmek. Bu, alanın çekirdek denetimidir.

## Soğuk başlangıç (intake)
- Zenginleşen tarafın malvarlığında ne arttı veya hangi gider/borçtan kurtuldu?
- Fakirleşen tarafta karşılık gelen azalma nedir; emek mi, mal mı, para mı?
- Kayma neye dayanıyordu; o sebep baştan yok mu, geçersiz mi, sonradan mı düştü?
- Tarafların iyiniyet/kötüniyet durumu ve kazanımın hâlâ mevcut olup olmadığı?

## Denetim şeması
1. **Zenginleşme (m.77/1).** Malvarlığında olumlu (yeni değer girişi) veya olumsuz (borçtan/giderden kurtulma) artış. Hizmet/kullanım gibi maddi olmayan yararlar da zenginleşmedir; ölçüsü tasarruf edilen masraf veya rayiç karşılıktır.
2. **Fakirleşme.** Karşı tarafın malvarlığından veya emeğinden bir değer çıkmış olmalı. Bazı müdahale hallerinde fakirleşme aranmaz veya kazanç ölçü alınır; bu nokta tartışmalıdır ve somut talebe göre belirlenir.
3. **İlliyet bağı.** Zenginleşme ile fakirleşme aynı olgudan kaynaklanmalı (doğrudan kayma). Dolaylı kazanımlarda (üçlü ilişkiler) talep yönü dikkatle belirlenir; kural olarak kendi sözleşme ilişkisi içinde iade istenir.
4. **Haklı sebebin yokluğu.** Kayma; geçerli bir sözleşme, kanun hükmü, mahkeme kararı veya bağışlama iradesi gibi hukuken onaylanan bir temele dayanmıyorsa "sebepsiz"dir. Haklı sebep başlangıçta yok (geçersiz), hiç gerçekleşmeyecek (gerçekleşmeyen) veya sonradan ortadan kalkmış (sona eren) olabilir.
5. **İspat yükü (TMK m.6, m.78).** İade isteyen; zenginleşmeyi, kendi kazandırmasını ve sebebin bulunmadığını/geçersizliğini ispatlar. Borçlanmadığı halde ödeyen, m.78 uyarınca yanılarak (hata ile) ödediğini de ortaya koymalıdır.
6. **Ara sonuç.** Dört unsur sağlanıyorsa iade borcu doğar; sağlanmıyorsa (ör. geçerli bağışlama, ifa edilmiş geçerli sözleşme) talep reddedilir. İade kapsamı için m.79 (iyiniyet ayrımı) bir sonraki adımdır.

## Çıktı modülleri
- Unsur-unsur altlama tablosu (var/yok + dayanak).
- Haklı sebep analizi notu.
- İlliyet/üçlü ilişki şeması (gerekiyorsa).

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
