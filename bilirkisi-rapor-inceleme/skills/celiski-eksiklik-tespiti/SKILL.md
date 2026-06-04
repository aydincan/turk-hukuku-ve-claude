---
name: celiski-eksiklik-tespiti
description: "Rapor içi çelişkileri, dosyadaki diğer deliller veya önceki raporlarla çelişkileri ve sorulduğu hâlde yanıtsız kalan hususları sistematik biçimde ortaya çıkarmak istendiğinde kullanılır."
---

# Çelişki ve Eksiklik Tespiti

## Görev
Raporu hem kendi içinde hem dosyanın bütünüyle karşılaştırarak tutarsızlık ve boşlukları çıkarmak; bunları ek rapor veya yeni heyet talebine gerekçe yapmak.

## Soğuk başlangıç (intake)
- Dosyada birden fazla bilirkişi raporu/uzman mütalaası var mı?
- Rapor, kendi içinde farklı yerlerde farklı sayı/sonuç veriyor mu?
- Tanık beyanı, keşif tutanağı, belge gibi delillerle rapor çelişiyor mu?
- Hangi soru fiilen yanıtsız kalmış?

## Denetim şeması
1. **Rapor içi çelişki:** Gövde, tablo ve sonuç bölümleri arasındaki sayısal/mantıksal tutarsızlıklar işaretlenir. Aynı kalemin farklı yerlerde farklı çıkması denetlenebilirliği bozar (HMK m.279).
2. **Dosya delilleriyle çelişki:** Rapordaki kabuller; belge, tanık, keşif tutanağı ve kayıtlarla karşılaştırılır. Delille çelişen kabul, sonucu sakatlar; çelişki dosya sayfasıyla çıpalanır.
3. **Raporlar arası çelişki:** Birden fazla rapor varsa hangi noktada ayrıştıkları ve hangisinin dayanağının güçlü olduğu gösterilir; hâkim raporları serbestçe takdir eder (HMK m.282), bu yüzden çelişkinin giderilmesi istenir.
4. **Eksik yanıt:** Görevlendirme sorularından yanıtsız kalanlar listelenir (HMK m.273 ile bağ).
5. **Ara sonuç:** Giderilebilir çelişki/eksik → **ek rapor**; raporlar arası esaslı ve giderilemeyen çelişki → **yeni/üçüncü heyet** talebi (HMK m.281). Her çelişki "rapordaki ifade vs. çelişen kaynak" biçiminde karşılıklı sunulur.

## Çıktı modülleri
- Çelişki matrisi (rapordaki ifade / çelişen kaynak / sayfa / etki).
- Yanıtsız kalan görevlendirme sorularının listesi.
- Raporlar arası ayrışma haritası.
- Çelişki temelli itiraz ve talep paragrafı taslağı.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
