---
name: hizmet-saglayici-yukumlulukleri
description: "Bir e-ticaret sitesinin veya satıcının 6563 kapsamındaki bilgi verme, sözleşme öncesi bilgilendirme ve sipariş sürecine ilişkin yükümlülüklerini denetlemek veya kurmak gerektiğinde kullanılır."
---

# Hizmet Sağlayıcı Bilgi ve Sipariş Yükümlülükleri

## Görev
6563 sayılı Kanun kapsamında hizmet sağlayıcının (kendi mal/hizmetini elektronik ortamda sunan) bilgi verme, sözleşme öncesi bilgilendirme ve sipariş akışına ilişkin yükümlülüklerini denetlemek; eksiklikleri ve yaptırım riskini tespit etmek.

## Soğuk başlangıç (intake)
- Sitede/uygulamada iletişim ve kimlik bilgileri (unvan, MERSIS, adres, e-posta) görünür mü?
- Sipariş öncesi teknik adımlar, sözleşme metninin saklanıp saklanmayacağı, hata düzeltme imkânı belirtiliyor mu?
- Sipariş sonrası teyit (onay) gönderiliyor mu?
- Karşı taraf tüketici mi tacir mi? (yükümlülüklerin kapsamı değişir)

## Denetim şeması
1. Bilgi verme yükümlülüğü (6563 m.3): hizmet sağlayıcının güncel tanıtıcı bilgilerini (ad/unvan, MERSIS no, iletişim, ETBİS bilgileri) elektronik ortamda kolay erişilebilir biçimde bulundurması zorunludur. Eksiklik m.12 idari para cezası riskidir.
2. Sözleşme öncesi bilgilendirme (6563 m.4): sözleşmenin kurulması için izlenecek teknik adımlar, sözleşme metninin saklanıp saklanmayacağı ve sonradan erişim imkânı, veri giriş hatalarının belirlenmesi ve düzeltilmesine ilişkin teknik araçlar bildirilir. Tacirler/esnaf ile aksi kararlaştırılabilir (m.4/2).
3. Sipariş (6563 m.5): sipariş veren kişinin ödeme yükümlülüğü altına girdiği açıkça gösterilir; sipariş alındığının gecikmeksizin elektronik iletişim araçlarıyla teyidi yapılır; sipariş ve teyitler taraflarca gecikmesiz erişilebilir tutulur. Hata düzeltme imkânı sağlanır.
4. Tüketici ise: 6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği'ndeki ön bilgilendirme katmanı ek olarak uygulanır (bkz. mesafeli-sozlesmeler becerisi).
5. İspat yükü: bilgilendirmenin yapıldığını ve teyitlerin gönderildiğini sağlayıcı ispatlar (log, kayıt, ekran görüntüsü).
Ara sonuç: her madde için "uygun / eksik / riskli" notu ve giderme önerisi.

## Çıktı modülleri
- Yükümlülük kontrol listesi (m.3-4-5 bazında).
- Eksiklik ve idari para cezası risk notu.
- Sipariş akışı düzeltme tavsiyesi.

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
