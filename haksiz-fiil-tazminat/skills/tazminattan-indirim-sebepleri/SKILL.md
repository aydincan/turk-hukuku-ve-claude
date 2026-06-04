---
name: tazminattan-indirim-sebepleri
description: "Karşı taraf zarar görenin kendi kusurunu, zararı ağırlaştıran davranışını veya failin az kusurunu ileri sürerek tazminatın azaltılmasını istediğinde; indirim sebeplerini değerlendirmek için kullanılır."
---

# Tazminattan İndirim Sebepleri

## Görev
TBK m.52'deki indirim sebeplerini (zarar görenin kendi kusuru/müterafik kusur, durumu ağırlaştırması, rıza) ve m.51'in kusur-zarar dengesini denetleyerek tazminat miktarının hakkaniyetle azaltılıp azaltılmayacağını belirlemek. İndirim, sorumluluğu kaldırmaz; miktarı düşürür.

## Soğuk başlangıç (intake)
- Zarar gören kendi davranışıyla zarara katkıda bulundu mu (örn. emniyet kemeri, talimata aykırılık)?
- Zarar görenin zararı azaltma yükümünü ihmal ettiği bir durum var mı?
- Failin kusuru hafif mi; tazminat onu yoksulluğa düşürür mü?
- Zarar görenin rızası ya da riski göze alması söz konusu mu?

## Denetim şeması
1. **Müterafik (birlikte) kusur (m.52/1).** Zarar gören kendi kusuruyla zararın doğmasına/artmasına yol açmışsa hâkim tazminatı indirir; katkı oranı somut olarak belirlenir.
2. **Zararı azaltma yükümü.** Zarar gören, makul önlemlerle zararı azaltabilecekken kaçınmışsa artan kısımdan sorumlu tutulmaz (dürüstlük kuralı TMK m.2 ile birlikte değerlendirilir).
3. **Durumu ağırlaştıran davranış.** Zarar görenin zararı genişleten eylemleri indirim sebebidir; illiyeti tümden kesiyorsa sorumluluk kalkar.
4. **Hafif kusur ve yoksulluk (m.52/2).** Fail hafif kusurluysa ve tazminat onu yoksulluğa düşürecekse, hakkaniyet gerektiriyorsa hâkim tazminatı indirebilir; bu istisnai bir denkleştirmedir.
5. **Rıza ve riski göze alma.** Geçerli rıza aykırılığı kaldırabilir (m.63); kısmî/örtülü rıza ise indirim sebebi olabilir.
6. **Ara sonuç ve ispat.** İndirim sebeplerini ileri süren ve katkı oranını ispatlayan taraf (genelde davalı) yükü taşır (TMK m.6). İndirim oranı gerekçelendirilir; kalan tazminat miktarı netleştirilir.

## Çıktı modülleri
- İndirim sebepleri kontrol listesi (sebep + katkı oranı + dayanak).
- Müterafik kusur değerlendirme notu.
- Net tazminat etkisi hesabı (indirim öncesi/sonrası).

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
