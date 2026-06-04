---
name: ilgili-kisi-basvuru-sureci-denetimi
description: "Kuruluşun ilgili kişi başvurularını karşılama prosedürünün m.13 ve Başvuru Tebliği'ne uygunluğu, 30 günlük yanıt süresine riayet ve şikâyete geçiş riski denetlenirken kullanılır."
---

# İlgili Kişi Başvuru Süreci Denetimi

## Görev
Kuruluşun m.11 haklarına dayanan başvuruları nasıl karşıladığını denetlemek: başvuru kanalları, kimlik doğrulama, 30 günlük yanıt süresi, gerekçeli ret usulü ve Kurul'a şikâyete geçişin önlenmesi açısından sürecin sağlamlığını ölçmek.

## Soğuk başlangıç (intake)
1. İlgili kişi başvurusu için ilan edilmiş bir kanal/form var mı (web, KEP, yazılı)?
2. Gelen başvuruyu kim alıyor, kim yanıtlıyor; sorumlu birim belli mi?
3. Başvuru–yanıt süreleri kayıt altında mı; geçmişte süre aşımı yaşandı mı?
4. Ret kararları gerekçelendiriliyor mu?

## Denetim şeması
1. **Kanal ve usul (m.13, Başvuru Tebliği)**: Başvuru yazılı veya Kurul'un belirlediği yöntemlerle (KEP, güvenli elektronik imza, kayıtlı e-posta vb.) yapılır; kuruluş bu kanalları ilan etmiş ve işler tutmuş olmalı.
2. **Kimlik doğrulama**: Başvuranın ilgili kişi olduğunun doğrulanması gerekir; aşırı bilgi talebi ise ölçülülük ihlali olur — denge denetlenir.
3. **Yanıt süresi**: Talep en kısa sürede ve en geç 30 gün içinde sonuçlandırılır. İşlemin maliyeti varsa Kurul tarifesi uygulanır; süre aşımı doğrudan şikâyet ve yaptırım riskidir.
4. **Gerekçeli ret**: Ret kararı gerekçesiz olamaz; m.11 haklarından hangisinin neden reddedildiği açıklanmalı.
5. **Şikâyete geçiş (m.14)**: Ret, eksik yanıt veya 30 günde yanıtsızlık halinde ilgili kişi, öğrenmeden itibaren 30 ve her hâlde başvurudan itibaren 60 gün içinde Kurul'a şikâyet edebilir. Veri sorumlusuna başvuru, şikâyet için zorunlu ön şarttır.
6. **Ara sonuç**: Süresinde, gerekçeli ve kayıtlı yanıt, hem şikâyeti hem yaptırımı önler.

İspat yükü: Başvurunun süresinde ve gereği gibi yanıtlandığını veri sorumlusu yanıt kayıtlarıyla ispatlar.

## Çıktı modülleri
- Başvuru süreci uygunluk kontrol listesi ve süre takip cetveli.
- Standart başvuru formu ve gerekçeli yanıt (kabul/ret) şablonları.
- Süre aşımı/şikâyet riski uyarı raporu.

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
