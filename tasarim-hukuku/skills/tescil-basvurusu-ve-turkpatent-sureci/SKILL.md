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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
