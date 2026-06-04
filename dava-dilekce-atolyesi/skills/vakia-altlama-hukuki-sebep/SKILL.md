---
name: vakia-altlama-hukuki-sebep
description: "Olayı hukuken anlamlı vakıalara ayırmak, her vakıayı delile ve doğru kanun maddesine altlamak, hukuki sebepleri eksiksiz dökmek gerektiğinde kullanılır."
---

# Vakıa Tespiti ve Hukuki Altlama

## Görev
Ham olayı hukuken anlamlı, numaralı ve kronolojik vakıalara ayırmak; her vakıayı bir delile bağlamak ve doğru norma altlamak. Layihanın ikna gücü, vakıa-norm eşleşmesinin sağlamlığından gelir.

## Soğuk başlangıç (intake)
- Olayın kronolojisi nedir (tarih, taraf, eylem)?
- Hangi haklar ve borçlar doğdu, ihlal edildi?
- Hangi vakıa hangi belgeyle/tanıkla ispatlanacak?
- Karşı tarafın itiraz edebileceği vakıalar hangileri?

## Denetim şeması
1. Vakıa ayrıştırma: Olayı tek tek maddi vakıalara bölün; hukuki nitelendirmeyi (ör. temerrüt) vakıadan ayrı tutun. Numaralandırın; her vakıa bir cümle.
2. İspat yükü dağıtımı (HMK m.190; TMK m.6): Her bir vakıayı iddia eden taraf ispatla yükümlüdür. Karine ve ikrarları (HMK m.188) belirleyin; ikrar edilen vakıa ispat gerektirmez.
3. Altlama: Her vakıa grubunu somut norma bağlayın. Örnek: ödeme yapılmaması → borçlu temerrüdü TBK m.117; sözleşmeye aykırılık → TBK m.112; haksız fiil → TBK m.49 (fiil, hukuka aykırılık, kusur, zarar, illiyet); ayıplı mal → TBK m.219 vd. veya TKHK m.8 vd.
4. Hukuki sebepler bütünü: HMK m.119/1-g uyarınca hukuki sebepleri yazın; hâkim hukuku re'sen uygular (iura novit curia) fakat dayanak normları açıkça belirtmek savunma ve istinaf açısından korur.
5. Çelişki taraması: Vakıalar arası ve vakıa-delil arası çelişkileri işaretleyin. Ara sonuç: her vakıanın delili ve normu varsa talep sonucuna geçilir; boşluk varsa `[delil eki]` yer tutucusu ve eksik listesi.

## Çıktı modülleri
- Numaralı kronolojik vakıa listesi
- Vakıa → delil → norm altlama tablosu
- İspat yükü dağıtımı notu
- Eksik vakıa/delil ve çelişki listesi

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
