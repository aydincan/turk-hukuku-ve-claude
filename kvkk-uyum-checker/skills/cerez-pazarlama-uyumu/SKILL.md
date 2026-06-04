---
name: cerez-pazarlama-uyumu
description: "Web sitesi çerezleri, çerez aydınlatması ve ticari elektronik ileti (İYS) süreçlerinin KVKK ve ilgili mevzuata uygunluğu denetlenirken kullanılır."
---

# Çerez ve Pazarlama Uyumu Denetimi

## Görev
İki yüksek görünürlüklü uyum alanını denetlemek: (1) web sitesi/uygulama çerezlerinin ve çerez aydınlatmasının KVKK m.5/m.10 ve Kurul Çerez Rehberi'ne uygunluğu; (2) ticari elektronik ileti gönderiminin 6563 sayılı Kanun ve İYS (İleti Yönetim Sistemi) düzeninde olup olmadığı.

## Soğuk başlangıç (intake)
1. Sitede hangi çerezler var (zorunlu, analitik, pazarlama, üçüncü taraf)?
2. Çerez aydınlatma/rıza arayüzü var mı; ön işaretli kutu veya "kabul et" zorlaması var mı?
3. Pazarlama iletisi (SMS, e-posta, arama) gönderiliyor mu; alıcı onayı nasıl alındı?
4. İYS kaydı ve onay yönetimi yapılıyor mu?

## Denetim şeması
1. **Çerez tasnifi**: Zorunlu (işlevsel) çerezler için rıza aranmaz; analitik ve pazarlama/üçüncü taraf çerezler için açık rıza ve aydınlatma gerekir (Kurul Çerez Rehberi). Tüm çerezleri tek "kabul" altında toplayan banner kırmızı bulgudur.
2. **Rıza geçerliliği (m.3/1-a)**: Çerez rızası özgür, belirli ve bilgilendirilmiş olmalı; ön işaretli kutu, "kabul etmeden devam edemezsin" (cookie wall) ve reddi zorlaştıran tasarım geçersizdir.
3. **Aydınlatma (m.10)**: Çerez politikası; çerez türü, amacı, süresi, üçüncü taraf alıcıları ve hakların kullanımını içermeli.
4. **Ticari elektronik ileti (6563)**: İleti için önceden onay esastır (esnaf/tacir istisnaları ve mevcut müşteri sınırlı istisnası ayrı değerlendirilir); her iletide kolay ret (opt-out) imkânı bulunmalı.
5. **İYS kontrolü**: Onaylar İYS'ye yüklenmeli ve ret talepleri İYS üzerinden işlenmeli; İYS dışı gönderim yaptırım riskidir.
6. **Ara sonuç**: Çerez ihlali KVKK m.18, ileti ihlali 6563 idari para cezası kapsamındadır; iki rejim paralel işler.

İspat yükü: Çerez rızasının ve ileti onayının geçerli alındığını veri sorumlusu/gönderen kayıt ve İYS verisiyle ispatlar.

## Çıktı modülleri
- Çerez envanteri ve tasnif tablosu (zorunlu/rızaya tabi).
- Çerez banner ve politika uygunluk bulgu listesi.
- İYS onay/ret yönetimi ve ticari ileti uygunluk raporu.

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
