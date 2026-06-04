---
name: ticari-elektronik-ileti-iys
description: "SMS, e-posta veya arama yoluyla gönderilen ticari iletilerde onay, ret hakkı ve İleti Yönetim Sistemi (İYS) yükümlülüklerinin denetlenmesi ya da bir yaptırım/şikâyet savunması hazırlanması gerektiğinde kullanılır."
---

# Ticari Elektronik İleti ve İYS Uyumu

## Görev
6563 m.6-7 ve Ticari Elektronik İleti Yönetmeliği kapsamında ticari iletilerin onay, içerik, ret hakkı ve İYS (İleti Yönetim Sistemi) yükümlülüklerine uygunluğunu denetlemek; aykırılık halinde yaptırım riskini veya savunmayı kurmak.

## Soğuk başlangıç (intake)
- İleti türü ne: SMS, e-posta, sesli arama, anlık mesaj?
- Alıcı tüketici mi tacir/esnaf mı? (tacirlere önceden onay gerekmeyebilir)
- Onay nasıl alındı, İYS'ye kayıtlı mı, tarih/kanal kaydı var mı?
- İletilerde gönderici kimliği ve kolay ret imkânı yer alıyor mu?

## Denetim şeması
1. Onay kuralı (6563 m.6): ticari elektronik ileti, alıcılardan önceden onay alınarak gönderilir. Onayın yazılı ya da her türlü elektronik iletişim araçlarıyla alınması mümkündür; ispat yükü hizmet sağlayıcıdadır.
2. Tacir/esnaf istisnası (m.6/3): alıcının tacir veya esnaf olması halinde önceden onay aranmaksızın ileti gönderilebilir; ancak ret hakkı saklıdır.
3. İçerik ve ret (6563 m.7): iletide hizmet sağlayıcının tanıtıcı bilgileri ile iletinin niteliği (tanıtım, kampanya vb.) yer alır; alıcı dilediğinde, ücretsiz ve kolayca reddedebilir; ret bildirimi alındığında 3 iş günü içinde ileti durdurulur.
4. İYS yükümlülüğü: onaylar ve ret bildirimleri İleti Yönetim Sistemi'ne kaydedilir; İYS'de kaydı olmayan onaya dayanılarak gönderim yapılamaz. İYS üzerinden alıcı onay/ret durumunu sorgulayabilir.
5. Yaptırım: aykırılıkta 6563 m.12 uyarınca idari para cezası uygulanır; abonelik/kişisel veri boyutu varsa KVKK ile yarışma değerlendirilir.
İspat yükü: onayın varlığı ve İYS kaydı sağlayıcıdadır; ret talebinin gereği gibi işlendiği belgelenir.

## Çıktı modülleri
- İleti uyum kontrol listesi (onay-içerik-ret-İYS).
- Şikâyet savunması veya aykırılık tespit notu.
- Onay metni ve ret mekanizması taslağı.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
