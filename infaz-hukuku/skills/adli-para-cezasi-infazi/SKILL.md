---
name: adli-para-cezasi-infazi
description: "Adli para cezasının ödenmesi, taksitlendirme, kamuya yararlı işe çevirme ve ödenmemesi hâlinde hapse çevrilmesini değerlendirmek gerektiğinde kullanılır."
---

# Adli Para Cezasının İnfazı ve Hapse Çevirme

## Görev
Adli para cezasının infaz seçeneklerini ve ödenmemesi hâlinde hapse çevrilme riskini 5275 m.106 ekseninde yönetmek.

## Soğuk başlangıç (intake)
- Adli para cezasının toplam tutarı nedir; ödeme emri tebliğ edildi mi?
- Hükümlünün ödeme gücü ve taksit talebi var mı?
- Daha önce kısmi ödeme yapıldı mı?
- Ceza, hapisten çevrilmiş adli para cezası mı yoksa doğrudan mı (hapse iade kuralı farkı)?

## Denetim şeması
1. Ödeme süreci: kesinleşen adli para cezası tebliğ edilen ödeme emriyle istenir; süresinde ödenmezse Cumhuriyet savcılığınca tahsil/çevirme işlemleri başlar (5275 m.106).
2. Taksitlendirme: hükümlünün talebiyle, kanunda öngörülen koşullarda taksitlendirme mümkündür; bir taksitin ödenmemesi kalanın muacceliyetine yol açabilir. Ara sonuç: ödeme planı uygunluğu.
3. Kamuya yararlı işe çevirme: ödenmeyen para cezası, hükümlünün rızası ve uygunluk hâlinde kamuya yararlı bir işte çalıştırmaya çevrilebilir (5275 m.106). İspat: çalışma uygunluğu ve denetimli serbestlik müdürlüğü değerlendirmesi.
4. Hapse çevirme: ödenmeyen ve çevrilemeyen para cezası, kanunda öngörülen hesaba göre hapse çevrilir; ancak doğrudan hükmedilen adli para cezasında ödendiğinde hükümlü serbest bırakılır. Çevrilen hapis için üst sınır ve hesap kuralları kontrol edilir.
5. İtiraz: çevirme/infaz işlemine karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
6. Ara sonuç: ödeme/taksit/çevirme seçeneği + hapse çevrilme riski.

## Çıktı modülleri
- Ödeme seçenekleri tablosu.
- Hapse çevirme hesabı taslağı.
- Taksit veya kamuya yararlı işe çevirme talep dilekçesi tetiği.

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
