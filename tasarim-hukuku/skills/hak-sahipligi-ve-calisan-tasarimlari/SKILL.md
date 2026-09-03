---
name: hak-sahipligi-ve-calisan-tasarimlari
description: "Tasarımcının kim olduğu, çalışan/sipariş üzerine yapılan tasarımlarda hakkın kime ait olduğu ve gerçek hak sahipliği davasının SMK m.70-73 çerçevesinde çözülmesi; tasarım üzerindeki mülkiyetin ihtilaflı olduğu veya istihdam/sözleşme ilişkisinden doğan haklarda kullanılır."
---

# Hak Sahipliği ve Çalışan Tasarımları

## Görev
Tasarım üzerindeki hakkın gerçek sahibini belirlemek: tasarımcı kimdir, çalışan/sipariş/ortaklık ilişkisinde hak kime aittir ve gerçek hak sahipliği davası nasıl kurulur.

## Soğuk başlangıç (intake)
1. Tasarımı fiilen kim yaptı (gerçek kişi tasarımcı)?
2. Tasarım bir iş/hizmet sözleşmesi kapsamında mı, sipariş üzerine mi, bağımsız mı yapıldı?
3. Sicilde kim hak sahibi görünüyor; başvuruyu kim yaptı?
4. Tasarımcının adının belirtilme (manevi) hakkı talep ediliyor mu?

## Denetim şeması
1. Tasarımcı ilkesi (SMK m.70): Tasarım hakkı, tasarımı yapan tasarımcıya veya halefine aittir. Birden fazla tasarımcı varsa hak müştereken doğar.
2. Çalışan tasarımları (SMK m.73): İşçinin işini görürken veya işverenin talimatıyla yaptığı tasarımların hakkı, aksi sözleşmede kararlaştırılmadıkça işverene aittir. İşçinin bedel/manevi hak talepleri (ad belirtilmesi) saklıdır; SMK ve yönetmelikteki bildirim/karşılık esaslarını uygulayın.
3. Sipariş/vekâlet ilişkisi: Sipariş üzerine yapılan tasarımlarda hak, sözleşmeye göre belirlenir; sözleşme yoksa SMK m.73 mantığı ve TBK eser/vekâlet hükümleri birlikte değerlendirilir.
4. Gerçek hak sahipliği davası (SMK m.71): Tasarım, hak sahibi olmayan kişi tarafından tescil ettirilmişse, gerçek hak sahibi tasarımın kendisine devrini veya hükümsüzlüğünü dava edebilir. Bu sebebi yalnız gerçek hak sahibi/halefi ileri sürebilir (m.77/1-b ile bağlantılı).
5. Manevi hak (SMK m.72): Tasarımcının, tasarımcı olarak belirtilme hakkı vardır; bu hak devredilemez.
6. Ara sonuç: Gerçek hak sahibi, sicil durumu, dava yolu (devir/hükümsüzlük) ve manevi hak durumu net yazılır.

## Çıktı modülleri
- Hak sahipliği zinciri (tasarımcı → işveren/sipariş veren → sicil) tablosu.
- Çalışan/sipariş sözleşmesi madde önerileri (hak devri, bedel, ad belirtme).
- Gerçek hak sahipliği davası iskeleti ve talep türü.

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
