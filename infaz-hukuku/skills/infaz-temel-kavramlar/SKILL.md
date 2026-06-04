---
name: infaz-temel-kavramlar
description: "İnfaz hukukunun temel kavramlarını, kesinleşmiş ilamın infaz kabiliyetini, hapis ile adli para cezası infazı ayrımını ve infaz türlerinin sistematiğini netleştirmek gerektiğinde kullanılır."
---

# İnfaz Hukuku Temel Kavramlar ve Sistematik

## Görev
Bir ceza ilamının infaz boyutunu sistematik biçimde çerçevelemek: hangi ceza türünün, hangi rejimle, hangi kanun maddesine göre infaz edileceğini ve infaz sürecinin haritasını çıkarmak.

## Soğuk başlangıç (intake)
- Elinde kesinleşmiş bir ilam var mı; kesinleşme tarihi nedir?
- Ceza türü ne: hapis mi, adli para cezası mı, güvenlik tedbiri mi?
- Suç tarihi ve suç tipi nedir (oranları etkiler)?
- Birden fazla ilam/içtima var mı; hükümlü tutuklu/firari mi?
- İlam infaza verilmiş mi, çağrı kâğıdı tebliğ edilmiş mi?

## Denetim şeması
1. İnfaz kabiliyeti: İnfaz yalnızca kesinleşmiş ve infaz edilebilir bir ilama dayanır (5275 m.4). Kesinleşmemiş veya HAGB'li (CMK m.231) bir hüküm doğrudan infaz edilmez; HAGB'de denetim süresi rejimi işler. Ara sonuç: ilam infaz kabiliyeti taşıyor mu?
2. Ceza türünü ayır:
   - Hapis cezası: 5275 m.19 vd. çağrı, m.14 açık/kapalı kurum rejimi.
   - Adli para cezası: 5275 m.106; ödenmezse hapse çevrilir, ancak kamuya yararlı işe çevirme ve taksitlendirme imkânları değerlendirilir.
   - Güvenlik tedbiri: TCK m.53 (hak yoksunlukları), m.54-55 (müsadere) infaz boyutu.
3. Rejim seçimi: kısa süreli hapis cezası ise TCK m.50 seçenek yaptırımları ve m.51 erteleme uygulanmış mı kontrol et; bunlar infaz tarzını kökten değiştirir.
4. İspat yükü: infaz lehine talepte (mahsup, denetimli serbestlik) dayanak belgeleri hükümlü tarafı sunar; infaz hesabı resen Cumhuriyet savcılığınca yapılır.
5. Ara sonuç: ceza türü + rejim + dayanak madde üçlüsü netleşince infaz takvimi kurulabilir.

## Çıktı modülleri
- İnfaz haritası tablosu (ceza türü, dayanak madde, rejim, sorumlu makam).
- Eksik belge ve doğrulanacak nokta listesi.
- Bir sonraki uzman beceriye yönlendirme (hesap, koşullu salıverilme, başvuru).

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
