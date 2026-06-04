---
name: yz-sozlesmeleri-risk-dagitimi
description: "Yapay zekâ modeli geliştirme, lisanslama, API kullanımı, SaaS veya entegrasyon sözleşmeleri hazırlanırken ya da incelenirken sorumluluk, veri kullanımı, fikri mülkiyet, performans garantisi ve tazminat maddeleri tasarlandığında kullanılır."
---

# Yapay Zekâ Sözleşmeleri ve Sözleşmesel Risk Dağıtımı

## Görev
Yapay zekâ geliştirme/lisans/SaaS/API sözleşmelerinde tarafların risk, veri, fikri mülkiyet ve sorumluluk dengesini TBK çerçevesinde tasarlamak veya incelemek; eksik, asimetrik veya geçersiz şartları tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: model geliştirme/eser, lisans, API/SaaS abonelik, entegrasyon/danışmanlık?
2. Müvekkil hangi taraf: sağlayıcı mı, kullanan/alıcı mı?
3. Eğitim/girdi/çıktı verisi kime ait, modeli iyileştirmede kullanılıyor mu?
4. Çıktı üzerinde fikri hak kime; ticari sır ve KVKK boyutu var mı?

## Denetim şeması
1. **Konu ve tip tayini**: Eser/geliştirme ağırlıklıysa TBK eser sözleşmesi (m.470 vd.) ve ayıba karşı tekeffül; sürekli hizmet/lisans ise hizmet/atipik sözleşme. Ara sonuç: hangi tip ve emredici hükümler.
2. **Veri ve KVKK maddeleri**: Girdi verisinin model eğitiminde kullanımı için açık yetki; veri işleyen sıfatı doğuyorsa KVKK m.12 uyumlu veri işleme sözleşmesi ve m.9 aktarım taahhütleri. Eksikse uyum açığı.
3. **Fikri mülkiyet**: Çıktı ve modelin hak sahipliği, lisans kapsamı, üçüncü kişi açık kaynak/lisans uyumu (FSEK/SMK). "Çıktı üzerinde hak garanti edilemez" gerçeğini sözleşmeye yansıt.
4. **Performans ve sorumluluk**: SLA, doğruluk/halüsinasyon riskine ilişkin garanti sınırları; sorumluluk sınırlaması maddeleri TBK m.115 (ağır kusur/kasıtta geçersizlik) ve genel işlem koşulu denetimi (m.20-25) süzgecinden geçirilir.
5. **Tazminat/rücu**: Üçüncü kişi taleplerinde tazmin (indemnity), veri ihlali ve fikri hak ihlali için tahsis; cezai şart ve fesih.

Emredici hüküm ve tüketici işlemi varsa 6502 TKHK ek denetimi. İçtihat künyesini [doğrulanacak] işaretle.

## Çıktı modülleri
- Risk maddesi haritası (veri/IP/sorumluluk/SLA).
- Redline ve alternatif lafız önerileri.
- Müzakere notu ve risk skoru.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
