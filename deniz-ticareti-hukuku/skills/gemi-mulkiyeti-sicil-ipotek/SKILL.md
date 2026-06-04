---
name: gemi-mulkiyeti-sicil-ipotek
description: "Gemi alım-satımı, gemi siciline tescil, gemi mülkiyetinin devri ve gemi ipoteği/kanuni rehin hakları söz konusu olduğunda; geminin ayni hak durumunu, takyidatları ve finansman teminatını incelemek için kullan."
---

# Gemi Mülkiyeti, Sicil ve Gemi İpoteği

## Görev
Geminin ayni hak durumunu (mülkiyet, ipotek, kanuni rehin, haciz şerhi) tespit etmek; mülkiyet devri ve ipotek tesisi işlemlerini denetlemek; finansman ve teminat yapısını kurmak veya zayıflıklarını saptamak.

## Soğuk başlangıç (intake)
- Gemi Türk Gemi Siciline mi yoksa yabancı sicile mi kayıtlı; bayrağı nedir?
- İşlem bir satış mı, ipotek tesisi mi, yoksa takyidat tespiti mi?
- Gemi üzerinde mevcut ipotek, kanuni rehin (gemi alacaklısı hakkı) veya ihtiyati haciz var mı?
- Banka/finansör kim; teminat kapsamı (navlun, sigorta tazminatı) genişletildi mi?

## Denetim şeması
1. **Sicil durumu**: Geminin tescilli olup olmadığını belirle (TTK m.954 vd.). Tescilli gemilerde mülkiyet ve ipotek tapu benzeri sicil ilkelerine tabidir; sicil kaydını ve şerhleri çıkar.
2. **Mülkiyetin devri**: Tescilli gemide mülkiyet devri için yazılı sözleşme ve sicile tescil aranır; tescilsiz gemide zilyetliğin devri esas alınır. Devirde geminin yük ve navlun üzerindeki ilişkilerini ayrıca değerlendir.
3. **Gemi ipoteği**: İpotek ancak tescilli gemi üzerinde, sicile tescille kurulur (TTK m.1014 vd.). İpoteğin kapsamı, derecesi, sabit/üst sınır ipoteği ayrımı ve eklentilere (sigorta tazminatı, navlun) sirayetini denetle.
4. **Kanuni rehin / gemi alacaklısı hakkı**: TTK m.1320 vd. kapsamındaki gemi alacaklısı haklarının ipotekten önce mi sonra mı geldiğini belirle; bu haklar genellikle ipoteğe öncelikli olabilir — teminat değerlemesinde kritik.
5. **İspat ve ara sonuç**: Sicil kaydı ayni hak durumunun temel delilidir; iyiniyetli üçüncü kişinin sicile güveni korunur. Çıktıda takyidat sırasını ve teminatın gerçek değerini gerekçeli olarak ortaya koy.

## Çıktı modülleri
- Sicil/takyidat özeti ve rehin sırası tablosu
- Mülkiyet devri veya ipotek tesisi adım listesi
- Teminat zayıflığı/risk notu ve finansör tavsiyesi

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
