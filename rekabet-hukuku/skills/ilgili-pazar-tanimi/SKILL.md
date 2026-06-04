---
name: ilgili-pazar-tanimi
description: "Ürün ve coğrafi pazarın sınırlarını, pazar paylarını ve yoğunlaşmayı belirlemek, hâkimlik veya yoğunlaşma analizinin iktisadi altyapısını kurmak istendiğinde kullanılır; her rekabet analizinin ön koşulu olan pazar tanımı için başvurulur."
---

# İlgili Pazar Tanımı ve Pazar Gücü Analizi

## Görev
İlgili Pazarın Tanımlanmasına İlişkin Kılavuz uyarınca ürün ve coğrafi pazarı tanımlamak, pazar paylarını ve yoğunlaşmayı (HHI) hesaplayarak m.4/m.6/m.7 analizinin iktisadi temelini oluşturmak.

## Soğuk başlangıç (intake)
- İncelenen mal/hizmet ve onun makul ikameleri neler?
- Müşteriler hangi coğrafi alanda tedarik seçeneklerine sahip; nakliye/düzenleme engeli var mı?
- Taraf ve rakip satış/üretim rakamları (ciro/hacim) mevcut mu?
- Analiz hangi amaca hizmet ediyor (hâkimlik, yoğunlaşma, muafiyet)?

## Denetim şeması
1. **Ürün pazarı** — talep ikamesi esas alınır: SSNIP mantığıyla, fiyatta küçük ama kalıcı artış karşısında müşterilerin başka ürüne geçip geçmeyeceği sorgulanır. Arz ikamesi (üreticinin hızla o ürünü sunabilmesi) destekleyici ölçüttür. Ürün özellikleri, kullanım amacı, fiyat seviyesi dikkate alınır.
2. **Coğrafi pazar** — rekabet koşullarının yeterince türdeş olduğu alan; nakliye maliyetleri, mevzuat/lisans engelleri, tüketici tercihleri, ithalat olanakları değerlendirilir.
3. **Pazar payı hesabı** — ciro veya hacim üzerinden; tanımın darlığı/genişliği payı doğrudan etkiler. Bu nedenle taraflar pazar tanımını stratejik kullanır.
4. **Yoğunlaşma (HHI)** — teşebbüslerin pay karelerinin toplamı; yoğunlaşma düzeyi ve işlem sonrası artış (delta) ön eleme sağlar. Yüksek HHI ve büyük delta endişe işaretidir.
5. **Giriş engelleri ve dengeleyici güç** — yasal engeller, batık maliyet, ağ etkileri, ölçek; alıcı gücü ve potansiyel rekabet sonucu yumuşatır.
6. **Ara sonuç** — birden çok makul pazar tanımı varsa hepsi üzerinden analiz yapılır (en muhafazakâr senaryo dâhil); ispat ve veri kaynağı her pay için belirtilir.

## Çıktı modülleri
- Ürün ve coğrafi pazar tanımı gerekçesi.
- Pazar payı tablosu ve HHI hesabı (kaynaklı).
- Giriş engeli ve dengeleyici güç değerlendirmesi.
- Pazar tanımına dair zayıf noktalar ve karşı argüman riskleri.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
