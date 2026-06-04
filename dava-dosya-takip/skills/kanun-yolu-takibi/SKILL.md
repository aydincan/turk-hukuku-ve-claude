---
name: kanun-yolu-takibi
description: "Karar sonrası istinaf ve temyiz yollarının açık olup olmadığını, süreleri, kesinlik sınırlarını ve dilekçe gereklerini izlemek gerektiğinde kullan."
---

# Kanun Yolu Takibi (İstinaf ve Temyiz)

## Görev
Verilen kararın hangi kanun yoluna tabi olduğunu, süresini, kesinlik sınırını ve başvuru gereklerini takvime bağlamak; kanun yolu hakkının süre veya parasal sınır nedeniyle kaybını önlemek.

## Soğuk başlangıç (intake)
- Karar hangi mahkemeden ve ne zaman tebliğ edildi?
- Karar miktarı/değeri ne (kesinlik sınırı kontrolü için)?
- Hukuk, ceza, icra yoksa idari karar mı?
- Aleyhe olan kısım ve başvuru sebepleri belirlendi mi?

## Denetim şeması
1. Yol tespiti: ilk derece kararına istinaf (BAM), istinaf kararına temyiz (Yargıtay/Danıştay). Hukukta istinaf süresi 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361); cezada istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291); idaride istinaf/temyiz süreleri İYUK m.45-46.
2. Kesinlik sınırı: parasal sınır altında istinaf/temyiz kapalı olabilir (HMK m.341 istinaf, m.362 temyiz kesinlik sınırları; her yıl güncellenir → sınır [doğrulanacak]). Sınırı yıl bazında doğrulat.
3. Başlangıç: süre tebliğ ile başlar; gerekçeli karar tebliğ edilmemişse süre işlemeye başlamaz, bu durumu not et.
4. Dilekçe gereği: istinaf/temyiz dilekçesinde sebeplerin gösterilmesi (HMK m.342, m.364); harç ve gider yatırma şartı (eksiklik halinde başvurudan vazgeçilmiş sayılma riski).
5. Ara sonuç: hangi yol açık, son gün, parasal sınır durumu ve hazırlanacak dilekçe. Tarih ve miktar evraktan alınır; sınır değerleri doğrulanmak üzere işaretlenir.

## Çıktı modülleri
- Kanun yolu takvimi (yol, süre, son gün, kesinlik durumu).
- Kesinlik sınırı doğrulama notu ([doğrulanacak]).
- Başvuru dilekçesi gerekleri çek-listesi.

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
