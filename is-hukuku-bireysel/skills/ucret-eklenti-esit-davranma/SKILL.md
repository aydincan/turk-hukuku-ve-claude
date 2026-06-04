---
name: ucret-eklenti-esit-davranma
description: "Ödenmeyen ücret, prim, ikramiye, AGİ ve eşit davranma (ayrımcılık) tazminatı tartışıldığında; ücretin tespiti, gecikme faizi, ücret kesintisi sınırları ve eşitlik ilkesi ihlalini değerlendirmek için kullan."
---

# Ücret, Ücret Ekleri ve Eşit Davranma

## Görev
Ücret ve eklerinin ödenip ödenmediğini, miktarını ve eşit davranma ilkesine aykırılığı denetlemek; doğan alacak ve tazminatları belirlemek.

## Soğuk başlangıç (intake)
1. Kararlaştırılan ve fiilen ödenen ücret nedir; bordro ile banka kaydı uyuşuyor mu?
2. Prim, ikramiye, sosyal yardım gibi ekler düzenli mi?
3. Ücret kesintisi/avans mahsubu yapıldı mı?
4. Aynı işi yapan emsallere kıyasla farklı muamele iddiası var mı?

## Denetim şeması
1. **Ücretin korunması (m.32):** Ücret en geç ayda bir, kural olarak banka aracılığıyla ödenir. Ücret nitelikli alacaklarda zamanaşımı **5 yıl**. Ödenmeyen ücret işçiye haklı fesih hakkı verir (m.24/II-e) ve gününde ödenmezse iş görmekten kaçınma hakkı doğabilir (m.34).
2. **Ücretin ispatı:** Bordro imzalı ve ihtirazi kayıtsızsa aksini işçi yazılı delille çürütmelidir. Miktar çekişmeliyse meslek odası/sendika emsal ücret araştırması yapılır.
3. **Ücret kesintisi sınırları (m.38):** İşveren disiplin cezası dışında ücretten kesinti yapamaz; toplu sözleşme/sözleşme dayanağı ve ayda iki günlük ücreti aşmama sınırı vardır.
4. **Asgari ücret ve AGİ:** Ücret asgari ücretin altında olamaz; AGİ ayrı kalemdir (güncel mevzuat ve uygulama değişiklikleri [doğrulanacak]).
5. **Eşit davranma (m.5):** İşveren biyolojik/cinsiyet, dil, ırk, din vb. sebeplerle ayrım yapamaz; esaslı sebep olmadıkça tam-kısmi süreli ve belirli-belirsiz süreliyi farklı işleme tabi tutamaz. İhlalde işçi, dört aya kadar ücreti tutarında **ayrımcılık tazminatı** ve yoksun bırakıldığı haklar talep edebilir. İhlali işçi ortaya koyar, ayrım olmadığını işveren ispatlar.

## Çıktı modülleri
- Ücret/ek tespit tablosu ve eksik ödeme kalemleri.
- Faiz ve zamanaşımı değerlendirmesi.
- Eşit davranma ihlali değerlendirmesi ve tazminat öngörüsü.
- İspat stratejisi notu.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
