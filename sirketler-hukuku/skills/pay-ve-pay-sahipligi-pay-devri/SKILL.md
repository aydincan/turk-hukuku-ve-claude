---
name: pay-ve-pay-sahipligi-pay-devri
description: "Anonim şirkette pay ve pay senedi, nama/hamiline yazılı pay devri ve bağlam (TTK m.490-493), limited şirkette esas sermaye payı devri (m.595), imtiyaz ve pay sahipliği hakları konuları gündeme geldiğinde; devrin geçerliliği ve pay defteri kaydı için kullanılır."
---

# Pay, Pay Sahipliği ve Pay Devri

## Görev
Payın hukuki niteliğini, devir usulünü ve geçerlilik şartlarını saptamak; pay sahipliği hak ve borçlarını, imtiyaz ve bağlam (devir sınırlaması) hükümlerini doğru uygulamak.

## Soğuk başlangıç (intake)
1. Şirket AŞ mi Ltd. mi; pay nama mı hamiline yazılı mı, senet bastırıldı mı?
2. Devir konusu pay üzerinde bağlam, imtiyaz veya rehin var mı?
3. Devir bedeli/ayni mi; devir sözleşmesi yazılı mı?
4. AŞ'de senetsiz pay devri mi (alacağın temliki) söz konusu?
5. Ltd.'de genel kurul onayı alındı mı, pay defterine işlendi mi?

## Denetim şeması
1. Pay senedi: AŞ nama/hamiline yazılı pay senetleri m.484-486; hamiline yazılı pay senedi devri MKK'ya bildirim + zilyetlik geçişi (m.489).
2. AŞ nama yazılı pay devri: ciro + zilyetlik geçişi (m.490/2); senetsiz payda alacağın devri hükümleri. Bağlam: esas sözleşmeyle devrin sınırlanması m.491-493; şirketin onaydan kaçınması ancak kanunda öngörülen önemli sebeplerle (m.493) ya da gerçek değerden devralma teklifiyle.
3. Ltd. pay devri: yazılı şekil + imzaların noter onayı + genel kurul onayı (m.595); aksi sözleşmede yoksa onay şarttır; ret için haklı sebep aranmaz ancak esas sözleşme düzenleyebilir. Devir pay defterine işlenir.
4. Pay sahipliği hakları: oy hakkı (m.434), bilgi alma-inceleme (m.437), kâr payı (m.507), rüçhan (m.461), tasfiye payı; oyda imtiyaz m.479; imtiyazlı pay sahipleri özel kurulu m.454.
5. Borçlar: sermaye koyma borcu (m.480 sınırı: tek borç ilkesi), temerrüt ve ıskat (m.482-483).
6. Geçiş/kayıt: Pay defteri (m.499); şirkete karşı pay sahipliği için kayıt önemlidir.
7. İspat: Devrin geçerli şekli ve onayı devralan tarafından; bağlam/önalım iddiası ileri sürence ispatlanır.

## Çıktı modülleri
- Pay devir sözleşmesi/temlik taslağı (şekil ve onay şartlı).
- Pay defteri kayıt ve bildirim adımları.
- Bağlam/imtiyaz analiz notu.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
