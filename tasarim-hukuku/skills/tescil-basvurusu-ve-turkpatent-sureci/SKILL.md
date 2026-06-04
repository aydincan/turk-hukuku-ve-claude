---
name: tescil-basvurusu-ve-turkpatent-sureci
description: "TÜRKPATENT nezdinde tasarım tescil başvurusunun hazırlanması, görsel anlatım ve sınıflandırma, yayın-itiraz aşaması ve yenileme takviminin yönetilmesi; bir tasarımın tescil ettirilmesi veya başvuru sürecindeki sorunların çözülmesi gerektiğinde kullanılır."
---

# Tescil Başvurusu ve TÜRKPATENT Süreci

## Görev
Tasarımı tescile götüren idari süreci uçtan uca yönetmek: başvuru içeriği, görsel anlatım kalitesi, çoklu başvuru, yayın-itiraz aşaması ve koruma süresinin korunması (yenileme).

## Soğuk başlangıç (intake)
1. Tek bir tasarım mı, çoklu başvuru mu (aynı sınıfa ait birden çok tasarım)?
2. Görseller/çizimler tasarımı tüm yönleriyle gösteriyor mu; renk/talep edilmeyen unsur var mı?
3. Rüçhan talep edilecek mi (önceki bir başvuru veya sergi rüçhanı)?
4. Ürün Locarno sınıflandırmasında hangi sınıfa girer?
5. Kamuya sunma yapıldıysa 12 aylık süre içinde miyiz?

## Denetim şeması
1. Başvuru unsurları (SMK m.61; Yönetmelik): Başvuru formu, tasarımın görsel anlatımı, ürün adı/Locarno sınıfı, tasarımcı bilgisi, varsa rüçhan belgesi. Görsel anlatım korumanın kapsamını belirler; eksik/çelişkili görsel koruma alanını daraltır.
2. Çoklu başvuru (SMK m.61/3): Aynı alt sınıfa giren birden çok tasarım tek başvuruda toplanabilir; maliyet ve yönetim avantajı sağlar.
3. Yenilik incelemesi (SMK m.64): TÜRKPATENT şekli inceleme ve sınırlı yenilik incelemesi yapar; ayırt edicilik kural olarak resen derinlemesine incelenmez, itiraza bırakılır.
4. Yayım ve itiraz (SMK m.66-67): Tasarım Bülteni'nde yayımlanır; üçüncü kişiler yayımdan itibaren 3 ay içinde TÜRKPATENT'e itiraz edebilir (yenilik/ayırt edicilik/hak sahipliği/koruma dışı). İtirazlar YİDD (Yeniden İnceleme ve Değerlendirme Dairesi) tarafından karara bağlanır.
5. YİDD kararına karşı dava (SMK m.67/son): Nihai karara karşı, kararın tebliğinden itibaren 2 ay içinde Ankara FSHHM'de iptal davası açılır.
6. Koruma süresi ve yenileme (SMK m.69): Başvuru tarihinden 5 yıl; 5'er yıllık dönemlerle azami 25 yıl. Yenileme süresini ve ek süreyi (sürşarjla) takvime bağlayın; süre kaçarsa koruma düşer.

## Çıktı modülleri
- Başvuru dosyası kontrol listesi (görsel, sınıf, rüçhan, tasarımcı beyanı).
- Yayın-itiraz-dava takvimi (3 ay itiraz, 2 ay YİDD iptal davası).
- Yenileme takvimi (5/10/15/20 yıl tetik tarihleri).

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
