---
name: ispat-delil-medya
description: "Basın-medya davalarında yayın içeriğinin tespiti, dijital delilin toplanması ve korunması, gerçeklik ve kamu yararının ispatı söz konusu olduğunda kullanılır."
---

# İspat ve Delil (Medya Uyuşmazlıkları)

## Görev
Yayın içeriğini güvenilir biçimde tespit ve sabitlemek, dijital delili kaybolmadan toplamak, ispat yükünü doğru dağıtmak ve gerçeklik/kamu yararı savunmasını delillendirmek.

## Soğuk başlangıç (intake)
1. İhlal eden içerik hâlâ erişilebilir mi; kaybolma riski var mı?
2. İçeriğin yayın tarihi ve değişiklik geçmişi belgelenebilir mi?
3. İddianın gerçekliğini destekleyen kaynak/belge var mı?
4. Tanık, ekran görüntüsü, noter tespiti mevcut mu?

## Denetim şeması
1. **İçeriğin sabitlenmesi**: Online içerik için ekran görüntüsü yeterli olmayabilir; noter tespiti, web arşivi (arşiv hizmeti) ve HMK m.400 vd. delil tespiti yoluna başvurulur. İçeriğin silinme riski varsa acil delil tespiti istenir.
2. **Dijital delil**: Bütünlük ve değişmezlik için meta veriler, URL, tarih damgası korunur; mümkünse adli bilişim raporu alınır.
3. **İspat yükü dağılımı (TMK m.6)**: Davacı saldırıyı ve zararı; davalı hukuka uygunluk sebebini (gerçeklik, kamu yararı, rıza) ispatlar. Değer yargısında yeterli olgusal temelin varlığı yayıncıdan beklenir.
4. **Gerçekliğin ispatı**: Maddi vakıa iddiasında, yayıncı görünür gerçeklik ve özen ölçütünü karşıladığını belgeyle ortaya koyar.
5. **Bilirkişi**: Teknik içerik, dijital delil veya zarar hesabı için bilirkişi incelemesi (HMK m.266) gerekebilir.
6. **Ara sonuç**: Deliller güvenli biçimde sabitlenmiş ve ispat yükü doğru dağıtılmışsa davada konum sağlamlaşır.

## Çıktı modülleri
- Delil sabitleme kontrol listesi (noter/arşiv/adli bilişim)
- İspat yükü dağılım tablosu
- Delil tespiti talebi dilekçesi iskeleti

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
