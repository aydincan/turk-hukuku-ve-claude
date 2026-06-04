---
name: kurumsal-siber-guvenlik-yukumlulukleri
description: "Bir kurumun siber güvenlik ve veri güvenliği yükümlülüklerini (KVKK m.12 teknik-idari tedbirler, sektörel düzenlemeler, politika ve sözleşme mimarisi) değerlendirmek ve uyum boşluğunu çıkarmak gerektiğinde kullanılır."
---

# Kurumsal Siber Güvenlik Yükümlülükleri ve Uyum

## Görev
Kurumun siber/veri güvenliği hukuki yükümlülüklerini saptamak; politika, teknik-idari tedbir ve sözleşme mimarisindeki boşlukları çıkarıp uyum yol haritası kurmak.

## Soğuk başlangıç (intake)
1. Kurumun faaliyeti ve sektörü ne? (banka/ödeme, sağlık, telekom, e-ticaret, genel?)
2. Hangi ve ne kadar kişisel veri işleniyor, işleyen/bulut kullanılıyor mu?
3. Mevcut politika, olay müdahale planı, log yönetimi var mı?
4. Tetikleyici ne? (denetim, ihlal sonrası, yatırım/due diligence, proaktif uyum?)

## Denetim şeması
1. **Genel veri güvenliği (KVKK m.12).** Veri sorumlusu, kişisel verilerin hukuka aykırı işlenmesini ve erişilmesini önlemek ile muhafazasını sağlamak üzere uygun **teknik ve idari tedbirleri** almakla yükümlüdür; işleyen ile müştereken sorumludur. Tedbirlerin alındığını ispat yükü kurumdadır. Eksiklik m.18 idari para cezası ve ihlal halinde ağırlaştırılmış sorumluluk doğurur.
2. **Sektörel katman.** Bankacılık/ödeme (BDDK, 6493 ve bilgi sistemleri düzenlemeleri), elektronik haberleşme (BTK/5809 ve ağ güvenliği), kritik altyapı düzenlemeleri ve varsa kurumun tabi olduğu özel rejim eklenir. TS ISO/IEC 27001 ve ilgili standartlar uyum ölçütü olarak referans alınır (sözleşme/idari beklenti düzeyinde).
3. **Belge ve süreç denetimi.** Veri envanteri, saklama-imha politikası, erişim yönetimi, log kayıtları, olay müdahale ve iş sürekliliği planı, sızma testi/zafiyet yönetimi, farkındalık eğitimleri kontrol edilir.
4. **Sözleşme mimarisi.** Veri işleyen sözleşmeleri, gizlilik ve güvenlik taahhütleri, SLA/güvenlik ekleri, sorumluluk sınırlamaları (TBK çerçevesinde geçerlilik), yurt dışı aktarım şartları denetlenir.
5. **Ara sonuç.** Yükümlülük-mevcut durum karşılaştırmasıyla **uyum boşluğu** ve öncelik/risk sıralaması çıkarılır.

## Çıktı modülleri
- Yükümlülük envanteri (genel KVKK + sektörel + standart).
- Uyum boşluğu raporu (boşluk, risk, öncelik, aksiyon).
- Politika/sözleşme eki şablon önerileri.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
