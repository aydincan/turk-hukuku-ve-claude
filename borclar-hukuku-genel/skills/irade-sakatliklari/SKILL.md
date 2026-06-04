---
name: irade-sakatliklari
description: "Bir tarafın yanılarak, aldatılarak veya korkutularak sözleşme yaptığını ileri sürdüğü ve iptal hakkı ile sürelerin değerlendirilmesi gerektiği hâllerde kullanılır."
---

# İrade Sakatlıkları — Hata, Hile, Korkutma

## Görev
Sözleşme iradesinin hata, hile veya korkutma ile sakatlanıp sakatlanmadığını, iptal hakkını, süresini ve tazminat sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Taraf neye dayanarak iradesinin sakat olduğunu söylüyor: yanılma mı, aldatılma mı, baskı mı?
- Yanılma esaslı mı (sözleşmenin niteliği, karşı taraf, miktar, temel vasıf)?
- Aldatma/korkutma karşı taraftan mı, üçüncü kişiden mi geldi?
- Sakatlığın öğrenildiği/ortadan kalktığı tarih nedir (bir yıllık süre için)?

## Denetim şeması
1. Hata (yanılma): TBK m.30-35. Esaslı yanılma türleri m.31 (sözleşmenin niteliği, karşı taraf kimliği, miktar) ve temel vasıfta yanılma m.32; saik yanılması kural olarak esaslı değildir. İletmede yanılma m.33. Dürüstlük kuralına aykırı şekilde iptal hakkı kullanılamaz (m.34); yanılan kusurluysa tazminatla yükümlüdür (m.35).
2. Hile (aldatma): m.36 — esaslı olmayan yanılmaya yol açsa bile iptal sağlar. Üçüncü kişinin hilesinde karşı taraf bilmiyor/bilmesi gerekmiyorsa sözleşme ayakta kalır (m.36/f.2).
3. Korkutma (ikrah): m.37-38 — ağır ve yakın bir tehlike, kişi veya yakınına yönelik; haklı korku yaratacak ciddiyette. Üçüncü kişinin korkutmasında iyiniyetli karşı tarafa tazminat gerekebilir (m.38/f.2).
4. İptal beyanı ve süre: m.39 — sakatlığın öğrenildiği veya korkutmanın etkisinin kalktığı andan itibaren bir yıl içinde diğer tarafa bildirilerek; aksi hâlde sözleşmeye icazet verilmiş sayılır. Bu hak bozucu yenilik doğuran haktır.
5. İspat yükü: Sakatlığı ileri süren unsurları ve süreyi koruduğunu ispatlar.
6. Ara sonuç: İptal hakkı var mı, süre içinde mi, tazminat yükümlülüğü doğuyor mu?

## Çıktı modülleri
- Sakatlık türü ve esaslılık değerlendirmesi.
- İptal beyanı/ihtarname taslağı iskeleti (süre uyarısıyla).
- İptal hâlinde iade ve tazminat sonuç şeması.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
