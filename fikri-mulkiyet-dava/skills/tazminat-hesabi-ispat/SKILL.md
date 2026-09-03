---
name: tazminat-hesabi-ispat
description: "Fikri-sınai tecavüzde maddi tazminat (yoksun kalınan kazanç, lisans bedeli), itibar ve manevi tazminat hesabı ile zararın ve tecavüz edenin kazancının ispatı, defter ibrazı ve bilirkişi gerektiğinde kullanılır."
---

# Tazminat Hesabı ve İspat-Delil

## Görev
Tecavüzden doğan zararı ve tazminatı SMK m.150-151 ile FSEK m.68/m.70 çerçevesinde hesaplamak; ispat ve delil stratejisini (defter ibrazı, bilirkişi) kurmak.

## Soğuk başlangıç (intake)
- Hak sahibinin fiili kaybı/yoksun kalınan kazancı belgelenebiliyor mu?
- Tecavüz edenin satış/üretim hacmine ve kazancına dair veri var mı?
- Lisans uygulaması/emsal lisans bedeli mevcut mu?
- İtibar zedelenmesi (kalitesiz taklit) ve manevi zarar var mı?

## Denetim şeması
1. Maddi tazminat türü: Yoksun kalınan kazanç esas alınır (SMK m.150/2). Davacı, m.151'deki üç hesap yönteminden birini seçer: (a) hak sahibinin elde edemediği gelir, (b) tecavüz edenin elde ettiği kazanç, (c) emsal/varsayımsal lisans bedeli.
2. FSEK tazminatı: Mali hak ihlalinde sözleşme yapılsaydı istenebilecek bedelin üç katına kadar (FSEK m.68/1); ayrıca m.70/2 maddi, m.70/1 manevi tazminat. SMK ve FSEK aynı fiilde yarışırsa mükerrer tahsil olmaz.
3. İtibar tazminatı: Markanın/eserin kötü/uygunsuz kullanımı itibarı zedelemişse ek tazminat (SMK m.150/3).
4. İspat ve defter ibrazı: Tecavüz edenin kazancının hesabı için ticari defter ve kayıtların ibrazı talep edilir (HMK m.219-222; TTK ilgili hükümleri). Sunmama, davacı lehine değerlendirme doğurabilir.
5. Bilirkişi: Mali müşavir/sektör bilirkişisi ile hesap yapılır; bilirkişiye yöneltilecek sorular netleştirilir. İspat yükü zarar ve illiyette davacıda; kazanç verisi davalının elindeyse ibraz mekanizması işletilir.
6. Faiz ve zamanaşımı: Tazminat alacağına temerrüt faizi; haksız fiil zamanaşımı TBK m.72 (2/10 yıl), süregelen ihlalde her gün yenilenir.

## Çıktı modülleri
- Tazminat yöntemi seçim ve gerekçe notu (SMK m.151).
- Defter ibrazı ve bilirkişi soru taslağı.
- Faiz ve zamanaşımı değerlendirmesi.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
