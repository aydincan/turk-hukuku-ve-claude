---
name: icra-ve-takip-dosyasi-takibi
description: "Bir ilamlı veya ilamsız icra takibinin aşamasını, itiraz/itirazın iptali sürelerini, haciz ve satış adımlarını izlemek gerektiğinde kullan."
---

# İcra ve Takip Dosyası Takibi

## Görev
İcra takip dosyasının türünü, aşamasını ve kritik sürelerini izleyip haciz-satış-paraya çevirme zincirini takip etmek; itiraz ve süre kaynaklı hak kayıplarını önlemek.

## Soğuk başlangıç (intake)
- Takip türü ne: ilamlı, ilamsız, kambiyo senetlerine özgü, rehnin paraya çevrilmesi?
- Ödeme/icra emri tebliğ edildi mi, tarihi ne?
- Borçlu itiraz etti mi, ettiyse hangi tarihte?
- Haciz uygulandı mı, satış aşamasına gelindi mi?

## Denetim şeması
1. Tür ve aşama: ilamsız takipte ödeme emrine itiraz 7 gün (İİK m.62) → itiraz takibi durdurur → alacaklı itirazın iptali (İİK m.67, 1 yıl) ya da itirazın kaldırılması (İİK m.68) yoluna gider. Kambiyo takibinde itiraz 5 gün ve icra mahkemesine (İİK m.168, m.170).
2. İlamlı takip: ilama dayalı takipte icranın geri bırakılması (İİK m.33) dışında itirazla durmaz; tehir-i icra şartlarını kontrol et.
3. Haciz-satış zinciri: haciz talebi süresi (İİK m.78, ödeme emrinin kesinleşmesinden itibaren), satış isteme süresi (İİK m.106) ve düşme riski (İİK m.110); kıymet takdiri ve satış ilanı.
4. İstihkak ve şikâyet: üçüncü kişi istihkak iddiası (İİK m.96 vd.), icra memuru işlemine şikâyet (İİK m.16, kural 7 gün).
5. Ara sonuç: takibin kesinleşip kesinleşmediği, açık süreler ve sıradaki adım. Tarihler ve tutarlar yalnızca takip dosyasından alınır.

## Çıktı modülleri
- Takip aşaması ve süre takvimi tablosu.
- İtiraz/itirazın iptali/kaldırılması karar ağacı notu.
- Haciz-satış adım takibi ve düşme riski uyarısı.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
