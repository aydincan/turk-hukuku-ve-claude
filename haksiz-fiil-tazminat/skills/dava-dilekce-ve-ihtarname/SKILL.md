---
name: dava-dilekce-ve-ihtarname
description: "Tazminat talebi için ihtarname, dava dilekçesi veya talep sonucu taslağı hazırlanması istendiğinde; vakıa-hukuki sebep-talep mimarisini kurmak için kullanılır."
---

# Dava Dilekçesi ve İhtarname Taslağı

## Görev
Haksız fiil tazminatı için HMK m.119'a uygun dava dilekçesi, dava öncesi ihtarname ve talep sonucu taslağı üretmek; vakıa-hukuki sebep-talep mimarisini kurmak ve delilleri vakıalara bağlamak. Eksik/belirsiz veriler `[doldurulacak]` yer tutucularıyla işaretlenir.

## Soğuk başlangıç (intake)
- Taraf bilgileri, olayın özeti ve talep edilen kalemler (maddi/manevi, tutar) nedir?
- Hangi sorumluluk normu dayanak (m.49 / objektif sorumluluk)?
- Faiz türü ve başlangıç tarihi ne istenecek?
- Eldeki deliller ve henüz toplanmamış olanlar neler?

## Denetim şeması
1. **İhtarname (dava öncesi).** Olay-zarar-talep özetlenir, belirli süre verilir, temerrüt ve faiz başlangıcı için ihtarın tarihi/içeriği netleştirilir; noterden keşide önerilir. Zamanaşımını kesmez ama temerrüt için önemlidir.
2. **Dilekçe zorunlu unsurları (HMK m.119).** Mahkeme, taraflar ve adresler, dava konusu/değeri, açık vakıalar, dayanılan hukuki sebepler, her vakıanın hangi delille ispatlanacağı, açık talep sonucu, imza.
3. **Vakıa-altlama.** Maddi olay kronolojik ve sade anlatılır; her vakıa haksız fiil unsuruyla (fiil, hukuka aykırılık, kusur, zarar, illiyet) eşleştirilir; gereksiz hukuki tartışma vakıa bölümüne taşınmaz.
4. **Hukuki sebepler.** TBK m.49 (ve varsa m.66-71 objektif sorumluluk), zarar kalemleri için m.51-56, gerekiyorsa TMK m.24-25; usul için HMK ve yetki m.16.
5. **Talep sonucu.** Kalem bazlı (maddi/manevi) tutar; belirsiz alacaksa HMK m.107 ifadesi; faiz türü-başlangıcı; yargılama gideri ve vekâlet ücreti.
6. **Ara sonuç.** Delil listesi vakıalara bağlanır; eksik veriler `[doldurulacak]` ile, doğrulama bekleyen içtihat `[doğrulanacak]` ile işaretlenir; uydurma karar numarası yazılmaz.

## Çıktı modülleri
- İhtarname taslağı (süre + temerrüt unsurları).
- HMK m.119 yapılı dava dilekçesi iskeleti.
- Talep sonucu ve delil listesi taslağı.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
