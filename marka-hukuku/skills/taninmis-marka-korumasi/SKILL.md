---
name: taninmis-marka-korumasi
description: "Markanın tanınmışlık düzeyi ve sınıf-aşırı koruması tartışmalıysa veya tanınmış marka taklidi/sulandırma iddiası varsa; m.6/4-5 ile Paris 1. mük. 6. md. korumasını denetlemek için kullanılır."
---

# Tanınmış Marka Koruması

## Görev
Bir markanın tanınmışlığını ve buna bağlı genişletilmiş korumayı SMK m.6/4 (Paris Sözleşmesi 1. mük. 6. md. anlamında tanınmış marka) ve m.6/5 (Türkiye'de ulaşılan tanınmışlık düzeyi nedeniyle farklı mal/hizmette koruma) çerçevesinde değerlendirmek. Tanınmışlık, normal karıştırılma sınırlarını aşan koruma sağlar.

## Soğuk başlangıç (intake)
- Marka hangi mal/hizmette, hangi coğrafyada ne kadar tanınıyor?
- Tanınmışlığa ilişkin somut delil var mı (pazar payı, tanıtım, süre, tüketici anketi)?
- İhtilaflı kullanım aynı sınıfta mı, farklı sınıfta mı?
- Haksız yarar/itibara veya ayırt ediciliğe zarar somut mu?

## Denetim şeması
1. **Tanınmışlık türü.** m.6/4 Paris kapsamı tanınmış marka (tescilsiz dahi olabilir) ile m.6/5 Türkiye'de ulaşılmış tanınmışlık ayrımı yapılır.
2. **Tanınmışlık ispatı.** İlgili tüketici kesimindeki bilinirlik; kullanım süresi-yoğunluğu, coğrafi yaygınlık, tanıtım yatırımı, pazar payı, TÜRKPATENT tanınmış marka siciline kayıt (karine değil, delil) değerlendirilir.
3. **m.6/4 (aynı/benzer mal).** Tanınmış markayla aynı/benzer mal-hizmette karıştırılma ihtimali; tescilsiz tanınmış marka da bu kapsamda korunur.
4. **m.6/5 (farklı mal).** Üç koşuldan biri: (i) tanınmış markanın itibarından haksız yarar sağlama, (ii) itibarına zarar, (iii) ayırt edici karakterinin zedelenmesi (sulandırma). Koşul ispatlanamazsa farklı sınıf koruması doğmaz.
5. **Sınır.** Tanınmışlık her sınıfa otomatik koruma vermez; haklı sebep (m.6/5) ve dürüst kullanım savunması değerlendirilir.

## Çıktı modülleri
- Tanınmışlık delil dosyası kontrol listesi.
- m.6/4 mü m.6/5 mi belirleme notu ve koşul altlaması.
- Sınıf-aşırı koruma kapsamı değerlendirmesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
