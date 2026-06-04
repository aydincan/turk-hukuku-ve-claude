---
name: sureler-ve-zamanasimi
description: "Soruşturma zamanaşımı, yerine getirme zamanaşımı, başvuru ve itiraz süreleri ile peşin ödeme süresini birlikte hesaplamak ve bir takvim çıkarmak gerektiğinde kullanılır; süre kaynaklı hak kayıplarını önler."
---

# Süreler ve Zamanaşımı

## Görev
Dosyadaki tüm süreleri (zamanaşımı + usul süreleri) ilk günden doğru hesaplayıp bir takvime bağlamak; resen dikkate alınan zamanaşımı savunmasını kaçırmamak.

## Soğuk başlangıç (intake)
- Kabahatin işlendiği/tamamlandığı tarih nedir?
- İdari yaptırım kararı ne zaman verildi, ne zaman tebliğ edildi?
- Ceza maktu mu nispi mi, tutarı ne (zamanaşımı süresi tutara bağlı)?
- Süreyi durduran/kesen bir işlem (dava, tebligat, ödeme) var mı?

## Denetim şeması
1. **Soruşturma zamanaşımı (5326 m.20):** İdari para cezasını gerektiren kabahatlerde, ceza miktarına göre kademeli süreler (örn. düşük tutarlarda kısa, yüksek tutarlarda daha uzun) öngörülür; süre fiilin işlenmesiyle (kabahat sonuçlu ise sonuçtan) başlar. Bu süre içinde karar verilip ilgiliye tebliğ edilmezse ceza verilemez. Süreleri madde metniyle birebir kontrol et.
2. **Yerine getirme (infaz) zamanaşımı (5326 m.21):** Kesinleşen idari para cezası, ceza miktarına göre belirlenen süre içinde tahsil edilmezse infaz edilemez. Süre kesinleşmeyle başlar.
3. **Başvuru süresi (5326 m.27/1):** Tebliğ/tefhimden itibaren **15 gün**; hak düşürücü.
4. **İtiraz süresi (5326 m.29):** Hâkimlik kararının tebliğinden **7 gün**.
5. **Peşin ödeme süresi (5326 m.17/6):** Tebliğden itibaren süresinde ödemede 1/4 indirim; süreyi kaçırmamak için takvime işle.
6. **Durma/kesilme:** Lehe kanun (5326 m.5 → TCK m.7) ve özel kanunlardaki özel süreler gözden geçirilir; süre hesabında tebligatın geçerliliği (7201) belirleyicidir.

Zamanaşımı, hak düşürücü süreden farklı olarak esasa ilişkindir ve resen incelenir; başvuru/itirazda öncelikle ileri sürülür.

## Çıktı modülleri
- Süre takvimi tablosu (zamanaşımı + usul süreleri, son günleriyle).
- Zamanaşımı savunması notu.
- Risk uyarısı (yaklaşan/geçen süreler).

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
