---
name: dilekce-sadelestirme
description: "Bir dava dilekçesini, cevap dilekçesini, istinaf/temyiz layihasını veya savunmayı müvekkilin anlayacağı sade Türkçeye çevirmek; talep sonucunu, vakıaları ve hukuki sebepleri yalın anlatmak gerektiğinde kullanılır."
---

# Dilekçe ve Layiha Sadeleştirme

## Görev
Dava/cevap dilekçesi, replik-düplik, istinaf veya temyiz layihasını; vakıa-hukuki sebep-talep
sonucu mimarisini bozmadan, müvekkilin "bu dilekçede ne diyoruz, ne istiyoruz" sorusuna net
cevap verecek sade bir metne çevirmek.

## Soğuk başlangıç (intake)
1. Hangi dilekçe ve hangi taraf adına (davacı/davalı/sanık/müşteki)?
2. Yargı kolu nedir (HMK 6100, CMK 5271, İYUK 2577)?
3. Okuyucu müvekkil mi, yoksa hukukçu olmayan bir karar verici mi?
4. Vurgulanması istenen talep veya risk var mı?

## Denetim şeması
1. İSKELETİ ÇIKAR: Dilekçenin üç ana ekseni ayrıştırılır — vakıalar, hukuki sebepler, talep
   sonucu (HMK m.119 dava dilekçesinin zorunlu unsurları; cevap için m.129). Sade metin bu
   üçlüyü "neler oldu / hangi kurala dayanıyoruz / ne istiyoruz" başlıklarına oturtur.
2. TALEP SONUCUNU ÖNE AL: Hukukçu metni gerekçeyle başlatır; sade metin sonuçla (ne istiyoruz)
   başlar, gerekçeyi sonra verir. Talep sonucu birebir korunur, daraltılıp genişletilmez.
3. USULİ SÜZGEÇ (ispat/süre): İçinde süre bağlı bir işlem varsa (istinaf süresi HMK m.345 –
   iki hafta; temyiz HMK m.361 – iki hafta; cevap süresi m.127 – iki hafta) bu süreler takvim
   tarihiyle açıkça yazılır, çünkü müvekkil için kritik sonuçtur.
4. DELİL BAĞINI KORU: "Hangi iddiayı hangi delille gösteriyoruz" ilişkisi sadeleştirmede
   düşürülmez; ispat yükünün kimde olduğu yalın dille belirtilir.
5. ARA SONUÇ: Sade metin, dilekçenin talep sonucunu ve dayanağını eksiksiz yansıtıyor mu;
   hiçbir hukuki sebep veya delil atlanmış mı kontrol edilir.
6. İSTİSNA: Dilekçenin kendisi mahkemeye verilen bağlayıcı metindir; sade versiyon yalnızca
   müvekkili bilgilendirir, dosyaya sunulmaz.

## Çıktı modülleri
- "Bu dilekçede özetle" bölümü (3-5 cümle).
- Ne istiyoruz / Neden / Hangi delillerle tablosu.
- Kritik süreler ve sonraki adımlar (takvim tarihli).
- Korunan teknik terimler sözlüğü ve asıl dilekçeye yönlendirme notu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
