---
name: temel-kavramlar-ve-sistem
description: "Bir telekom veya internet dosyasını konu (operatör düzenlemesi 5809 mu, internet içeriği 5651 mi) ve katman (düzenleyici-idari, sözleşmesel, yargısal) ekseninde konumlandırıp doğru kanun, yönetmelik ve mercii belirlemek gerektiğinde kullanılır."
---

# Telekom-Bilişim Temel Kavramlar ve Sistematik

## Görev
Dosyayı doğru düzenleme rejimine ve hukuki katmana oturtmak; uygulanacak kanunu (5809 EHK / 5651 / kesişen 6698-6563), ilgili ikincil mevzuatı ve görevli mercii (BTK, sulh ceza hâkimliği, idari yargı, adli yargı) hızlıca tespit ederek sonraki uzman becerilere doğru giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Konu elektronik haberleşme sektörü mü (operatör/işletmeci, abonelik, frekans, numara) yoksa internet içeriği/sorumluluk mu?
2. Müvekkilin sıfatı: işletmeci/operatör, içerik sağlayıcı, yer/erişim sağlayıcı, sosyal ağ sağlayıcı, abone/son kullanıcı, mağdur?
3. Uyuşmazlık türü: BTK düzenleyici/yaptırım işlemi, abonelik/tüketici, erişim engelleme/içerik çıkarma, arabağlantı/erişim, veri/gizlilik mi?
4. Bir karar/işlem tebliğ edildi mi (BTK yaptırımı, sulh ceza kararı, BTK bildirimi); tebliğ/öğrenme tarihi nedir?
5. Olay tarihi ve dolayısıyla yürürlükteki mevzuat versiyonu hangisi?

## Denetim şeması
1. **Rejim tespiti**: Sektör düzenlemesi için 5809 EHK ve BTK ikincil mevzuatı; internet içeriği için 5651; ticari ileti/aracılık kesişiminde 6563; veri boyutunda 6698. Bir olgu birden çok rejimi ilgilendirebilir (ör. abone trafik verisi: hem 5809 m.51 hem KVKK). Ara sonuç: uygulanacak norm seti.
2. **Sağlayıcı/aktör sıfatı**: 5651 m.2 tanımlarıyla içerik/yer/erişim/toplu kullanım/sosyal ağ ayrımı; 5809 kapsamında işletmeci yetkilendirme türü (bildirim/kullanım hakkı, m.8-9). Sıfat sorumluluk rejimini belirler.
3. **Katman ayrımı**: (a) Düzenleyici uyum — BTK kurul kararı/yönetmelik, yetkilendirme; (b) Sözleşmesel — abonelik (m.50), arabağlantı/erişim, hizmet; (c) Yargısal — erişim engelleme/içerik (sulh ceza hâkimliği), BTK işlemi (idari yargı), özel hukuk (adli yargı).
4. **Görev-yetki ve süre**: BTK işlemi → İYUK m.7 (kural 60 gün); 5651 erişim engelleme → sulh ceza hâkimliği ve CMK m.267 itiraz; abonelik tüketici işlemi → 6502 tüketici hakem heyeti/mahkemesi.
5. **Tarih kilidi**: 5651 ve BTK mevzuatının sık değiştiği gözetilerek olay tarihindeki yürürlük hali ve süre eşikleri sabitlenmeden değerlendirme yapılmaz.

## Çıktı modülleri
- Dosya konumlandırma notu (rejim + sağlayıcı sıfatı + katman + uygulanacak norm seti).
- Görevli merci ve süre uyarısı.
- Hangi uzman beceriye geçileceğine dair yönlendirme.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
