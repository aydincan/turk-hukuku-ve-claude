---
name: odeme-emri-ve-tahsilat
description: "6183 sayılı Kanun kapsamında düzenlenen ödeme emrine, hacze, e-hacze ve ihtiyati haciz/tahakkuk işlemlerine karşı tahsil aşamasındaki uyuşmazlıkları çözmek için kullanılır."
---

# Ödeme Emri ve Tahsilat İşlemlerine Karşı Dava

## Görev
Kesinleşmiş ya da kesinleştiği varsayılan kamu alacağının tahsili için çıkarılan ödeme emri ve takip işlemlerine karşı, AATUHK'nın sınırlı itiraz sebepleri çerçevesinde dava kurmak; tahsil aşamasının hukuka uygunluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Ödeme emri size ne zaman tebliğ edildi? Üzerindeki alacağın türü ve dönemi ne?
2. Bu alacağın aslına ilişkin daha önce ihbarname tebliğ edildi mi, dava açıldı mı?
3. İtiraz sebebiniz hangisi: böyle bir borç yok / kısmen ödedim / borç zamanaşımına uğradı?
4. Halihazırda haciz, e-haciz, banka bloke veya ihtiyati haciz uygulandı mı?

## Denetim şeması
1. **Süre — kritik.** AATUHK m.58 — ödeme emrine karşı dava **tebliğden itibaren 7 gün** içinde vergi mahkemesinde açılır. Bu süre, 30 günlük genel vergi davası süresinden farklıdır; karıştırma en sık hata.
2. **Sınırlı itiraz sebepleri.** m.58 — yalnızca "böyle bir borcun olmadığı", "borcun kısmen ödendiği" veya "borcun zamanaşımına uğradığı" ileri sürülebilir. Tarhiyatın esasına (matrah/ceza) ödeme emri aşamasında girilemez; o aşama ihbarname davasında tüketilir.
3. **Önceki aşamayı sorgula.** Ödeme emrinin dayanağı kesinleşmiş mi? İhbarname usulüne uygun tebliğ edilmemişse "böyle bir borç yoktur" kapsamında tarhiyat aşaması canlanabilir; tebligatın geçerliliği (VUK m.93 vd.) denetlenir.
4. **Zamanaşımı.** AATUHK m.102 — tahsil zamanaşımı 5 yıl; m.103 kesilme, m.104 durma halleri kontrol edilir.
5. **Yürütmenin durdurulması.** Ödeme emrine karşı davada İYUK m.27/4'ün otomatik durma etkisi yoktur; teminat ve YD talebi (İYUK m.27) ayrıca istenir. İhtiyati haciz/tahakkuk (AATUHK m.13-20) için ayrı dava ve YD değerlendirilir. Ara sonuç: haciz baskısı varsa teminat gösterilerek YD önceliklendirilir.
6. **Tecil-taksit.** AATUHK m.48 tecil talebi ile dava paralel yürütülebilir; ödeme güçlüğü varsa not düşülür.

## Çıktı modülleri
- 7 günlük süre uyarısı ve itiraz sebebi seçim tablosu.
- Ödeme emrine itiraz dilekçesi iskeleti.
- Teminat + YD talep stratejisi notu.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
