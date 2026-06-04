---
name: veri-ihlali-mudahale-hazirligi
description: "Kuruluşun veri ihlali müdahale planının varlığı ve yeterliliği denetlenirken, 72 saatlik Kurul bildirim ve ilgili kişi bilgilendirme süreçleri test edilirken kullanılır."
---

# Veri İhlali Müdahale Hazırlığı Denetimi

## Görev
KVKK m.12/5 kapsamında kuruluşun veri ihlaline hazırlığını denetlemek: müdahale planı, ekip ve roller, 72 saatlik Kurul bildirim akışı ve ilgili kişi bilgilendirme mekanizması mevcut ve işler mi? Bu beceri olay anına değil, olaya hazırlığa odaklanır.

## Soğuk başlangıç (intake)
1. Yazılı bir veri ihlali müdahale planı var mı; ekip ve roller (kim karar verir, kim bildirir) tanımlı mı?
2. İhlali tespit eden çalışanın bildirim yapacağı iç kanal belli mi?
3. Daha önce yaşanan ihlal var mı; nasıl yönetildi, kayıt tutuldu mu?
4. 72 saatlik süreyi takip edecek bir mekanizma/şablon hazır mı?

## Denetim şeması
1. **Plan varlığı (m.12)**: Yazılı müdahale planı, eskalasyon zinciri ve karar matrisi olmalı. Plan yoksa veya güncel değilse yüksek risk bulgusu.
2. **Tespit→bildirim akışı**: İhlalin öğrenildiği an süreyi başlatır. Kurul'a bildirim en kısa sürede ve en geç 72 saat içinde, Kurul'un belirlediği form üzerinden yapılır; 72 saat aşılırsa gecikme gerekçesi açıklanmalı. Bu akışın test edilebilir (tatbikatlı) olması beklenir.
3. **İlgili kişi bilgilendirme**: Etkilenen kişiler makul en kısa sürede bilgilendirilir; bilgilendirme metni şablonu hazır olmalı.
4. **Bildirim içeriği**: İhlalin niteliği, etkilenen veri kategorileri ve kişi sayısı, olası sonuçlar, alınan/önerilen tedbirler ve irtibat bilgisi. Eksik içerik ayrı yükümlülük ihlalidir.
5. **Kanıt zinciri**: Loglar ve müdahale kayıtlarının korunacağı düzen kurulmalı; bu kayıtlar hem yaptırım hem tazminat davasında belirleyicidir.
6. **Ara sonuç**: Hazırlıksızlık, ihlal anında 72 saatin aşılmasına ve m.18 ek yaptırımına yol açar.

İspat yükü: Bildirimin süresinde ve usulüne uygun yapıldığını/yapılacağını veri sorumlusu plan ve kayıtlarla ispatlar.

## Çıktı modülleri
- Veri ihlali müdahale planı uygunluk kontrol listesi.
- 72 saat takip cetveli ve Kurul bildirim formu taslağı ([doldurulacak]).
- İlgili kişi bilgilendirme metni şablonu ve eskalasyon karar matrisi.

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
