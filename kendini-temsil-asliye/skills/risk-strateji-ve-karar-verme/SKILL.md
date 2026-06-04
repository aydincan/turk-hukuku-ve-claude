---
name: risk-strateji-ve-karar-verme
description: "Kullanıcı dava açmaya değer mi, sulh mü daha iyi, kazanma şansı ve maliyet-fayda dengesi nedir gibi stratejik kararlar vermek istediğinde kullanılır."
---

# Risk Değerlendirmesi ve Dava Stratejisi

## Görev
Tarafın dava açmadan önce gerçekçi bir maliyet-fayda ve kazanma ihtimali değerlendirmesi yapmasını sağlamak; sulh, arabuluculuk ve dava seçeneklerini tartmak.

## Soğuk başlangıç (intake)
- Talebinizin parasal değeri ve elinizdeki delilin gücü nedir?
- Karşı tarafın ödeme gücü/tahsil kabiliyeti var mı?
- Zaman ve duygusal maliyeti üstlenmeye hazır mısınız?
- Sulh için kabul edebileceğiniz asgari nedir?
- Süre/zamanaşımı baskısı var mı?

## Denetim şeması
1. **Hukuki güç analizi:** İddianın hukuki dayanağı (madde) + her vakıanın delille desteklenme oranı değerlendirilir. Senetle ispat zorunluluğu (HMK m.200) gibi engeller kazanma ihtimalini düşürebilir.
2. **Tahsil riski:** Davayı kazanmak ile alacağı tahsil etmek farklıdır; karşı tarafın malvarlığı/icra kabiliyeti yoksa lehe karar kâğıt üstünde kalabilir. İcra ve haciz ihtimali baştan değerlendirilir.
3. **Maliyet-fayda:** Harç + avans + zaman + (kaybetme halinde) karşı taraf giderleri (HMK m.326) toplam riski oluşturur; bu, beklenen kazanca karşı tartılır.
4. **Sulh/arabuluculuk:** Çoğu uyuşmazlıkta arabuluculuk zaten dava şartıdır; erken ve gerçekçi sulh, zaman ve gider tasarrufu sağlar. Sulh sınırı (BATNA — en iyi alternatif) baştan belirlenir.
5. **Süre baskısı:** Zamanaşımı/hak düşürücü süre yaklaşıyorsa, müzakere uzasa bile davayı/takibi açıp süreyi kesmek gerekebilir (TBK m.154).
6. **Ara sonuç:** Hukuki güç + tahsil + maliyet + süre dengesine göre dava/sulh/vazgeçme yönünde gerekçeli öneri oluşturulur.

## Çıktı modülleri
- Kazanma ihtimali ve tahsil riski özeti (zayıf-orta-güçlü).
- Maliyet-fayda tablosu ve sulh eşiği (BATNA) önerisi.
- Strateji tavsiyesi (dava aç / önce müzakere / vazgeç) gerekçeleriyle.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
