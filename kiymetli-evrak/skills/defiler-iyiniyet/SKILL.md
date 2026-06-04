---
name: defiler-iyiniyet
description: "Kambiyo senedinde ileri sürülebilecek mutlak ve kişisel def'ileri ayırmak, iyiniyetli hamile karşı def'i sınırlamasını uygulamak; borçlunun savunma imkânlarını veya hamilin def'isiz konumunu değerlendirirken kullanılır."
---

# Def'iler ve İyiniyetli Hamilin Korunması

## Görev
Kambiyo borçlusunun hamile karşı ileri sürebileceği def'ileri tasnif etmek; senetten anlaşılan/herkese karşı ileri sürülen def'iler ile kişisel def'ileri ayırmak ve iyiniyetli hamile karşı kişisel def'i yasağını uygulamak.

## Soğuk başlangıç (intake)
- Borçlunun iddiası senedin geçerliliğine mi (şekil, ehliyet, sahtelik) yoksa temel ilişkiye mi (ödeme, bedelsizlik, anlaşmaya aykırı doldurma) dayanıyor?
- Hamil, def'inin dayandığı kişiyle doğrudan taraf mı, yoksa ciro yoluyla mı edindi?
- Hamilin senedi edinirken borçluya zarar verme kastı (kötüniyet) iddiası var mı?
- Senet tahsil cirosuyla mı geçti?

## Denetim şeması
1. Mutlak (senetten anlaşılan/herkese karşı) def'iler: şekil eksikliği, zamanaşımı, sahtelik, ehliyetsizlik, senet metnindeki kayıtlar — bunlar her hamile karşı ileri sürülebilir.
2. Kişisel (def'iler): temel ilişkiden doğan def'iler (ödeme, takas, bedelsizlik, anlaşmaya aykırı doldurma) yalnızca doğrudan taraf olunan hamile karşı ileri sürülür.
3. İyiniyetli hamil koruması: TTK m.687 — senedi devralırken borçlunun zararına hareket etmediyse, önceki hamillerle borçlu arasındaki kişisel def'iler kendisine karşı ileri sürülemez. Kötüniyet veya ağır kusur ispatlanırsa koruma kalkar; ispat yükü def'iyi ileri süren borçludadır.
4. Tahsil cirosu istisnası: tahsil cirosuyla edinen hamil temsilci olduğundan, borçlu cirantaya karşı sahip olduğu def'ileri bu hamile de ileri sürebilir (m.688).
5. Bağımsızlık ilkesi: bir imzanın geçersizliği diğer kambiyo taahhütlerini etkilemez (m.677); borçlu yalnızca kendi taahhüdüne ilişkin def'iyi ileri sürebilir.
6. Ara sonuç: def'inin türü ve hamilin iyiniyeti belirlendiğinde, savunmanın o hamile karşı dinlenip dinlenmeyeceği sonuçlanır.

## Çıktı modülleri
- Def'i tasnif tablosu (mutlak/kişisel + dayanak + muhatap hamil).
- İyiniyet/kötüniyet değerlendirme notu (ispat yükü dahil).
- Borçlu savunma dilekçesi veya hamil için def'isizlik argümanı taslağı.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
