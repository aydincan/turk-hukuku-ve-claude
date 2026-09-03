---
name: ihtiyati-tedbir-haciz
description: "Dava öncesi veya sırasında hakkı güvence altına almak için ihtiyati tedbir veya ihtiyati haciz talebini şartları ve teminatıyla kurmak gerektiğinde kullanılır."
---

# İhtiyati Tedbir ve İhtiyati Haciz Talepleri

## Görev
Yargılama sonuna kadar hakkın korunması için geçici hukuki koruma talebini kurmak: HMK'ya göre ihtiyati tedbir, İİK'ya göre para alacaklarında ihtiyati haciz. Şartlar ve teminat doğru kurulmazsa talep reddedilir veya tazminat riski doğar.

## Soğuk başlangıç (intake)
- Korunacak hak para alacağı mı, başka bir hak mı?
- Gecikmede zarar/sakınca doğuyor mu (aciliyet)?
- Haklılık yaklaşık olarak ispatlanabiliyor mu?
- Teminat yatırılabilir mi, muafiyet hâli var mı?

## Denetim şeması
1. Yol ayrımı: Para alacağında kural olarak ihtiyati haciz (İİK m.257); diğer hak ve durumlarda (mevcut durumun korunması, taşınmaza şerh, vb.) ihtiyati tedbir (HMK m.389).
2. İhtiyati tedbir şartları (HMK m.389-390): Hakkın elde edilmesinin önemli ölçüde zorlaşması veya gecikmede sakınca/ciddi zarar; talep edenin hakkı yaklaşık ispat (m.390/3). Tedbir kararı ve kapsamı somut yazılmalı.
3. İhtiyati haciz şartları (İİK m.257): Muaccel (veya istisnaen müeccel) para alacağı; rehinle temin edilmemiş olması; alacağın ve sebebinin yaklaşık ispatı.
4. Teminat: İhtiyati tedbirde HMK m.392, ihtiyati hacizde İİK m.259 — haksız tedbir/haciz nedeniyle doğabilecek zararlar için teminat; istisna ve muafiyetleri kontrol edin.
5. Uygulama ve süre: Tedbirin uygulanması (HMK m.393 — bir hafta içinde icra); ihtiyati hacizde dava açma/takip süresi (İİK m.264 — yedi/bir hafta). Ara sonuç: şart-teminat-süre uygunsa talep hazır; haksız çıkma tazminatı riski (HMK m.399; İİK m.259/son) notlanır.

## Çıktı modülleri
- İhtiyati tedbir/haciz talep dilekçesi taslağı
- Şart denetim listesi (aciliyet, yaklaşık ispat)
- Teminat tutarı/muafiyet notu
- Uygulama ve dava/takip süresi takvimi

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
