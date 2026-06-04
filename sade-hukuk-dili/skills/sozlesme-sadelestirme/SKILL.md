---
name: sozlesme-sadelestirme
description: "Bir sözleşmeyi veya belirli maddelerini imzalamadan önce müvekkilin anlayacağı dile çevirmek; hangi yükümlülük, hangi risk, hangi çıkış var sorularını yalın anlatmak gerektiğinde kullanılır."
---

# Sözleşme ve Madde Sadeleştirme

## Görev
Bir sözleşmeyi veya seçili maddeleri, tarafın "neyi taahhüt ediyorum, ne risk alıyorum, nasıl
çıkarım" sorularına cevap verecek sade bir özete çevirmek; yükümlülükleri, riskleri ve çıkış
mekanizmalarını anlam kaybı olmadan aktarmak.

## Soğuk başlangıç (intake)
1. Sözleşme türü nedir (satış, kira, hizmet, eser, gizlilik, pay devri)?
2. Müvekkil hangi taraf ve imza öncesi mi sonrası mı?
3. En çok endişe edilen konu (para, süre, sorumluluk, fesih)?
4. Karşı tarafın hazırladığı tip sözleşme / genel işlem koşulu mu?

## Denetim şeması
1. ROL VE EDİMLER: Tarafların asli edimleri ayrıştırılır (kim ne verecek, ne ödeyecek, ne zaman).
   Sözleşmenin yorumunda gerçek irade esastır (TBK m.19); sade metin bu iradeyi yansıtır.
2. PARA VE SÜRE: Bedel, ödeme planı, vade, ifa süreleri takvim/somut tutarla yazılır; muacceliyet
   ("borcun istenebilir hale gelmesi") açıklanır.
3. RİSK MADDELERİ: Sorumluluğun sınırlanması (TBK m.115 — ağır kusurda sorumsuzluk anlaşması
   geçersiz), cezai şart (TBK m.179-182), temerrüt faizi, müteselsil sorumluluk yalın dille
   ama anlamı korunarak aktarılır; "müteselsil" = her biri borcun tamamından sorumlu.
4. GENEL İŞLEM KOŞULU SÜZGECİ (ispat/geçerlilik): Tip sözleşmelerde diğer tarafın aleyhine olup
   beklenmeyen şartlar yazılmamış sayılabilir (TBK m.21); belirsizlik düzenleyen aleyhine
   yorumlanır (TBK m.23); tüketici ise haksız şart denetimi (TKHK m.5). Bu noktalar okuyucuya
   risk olarak işaretlenir.
5. ÇIKIŞ: Fesih, dönme ve cayma hakları ayrı ayrı açıklanır (anlamları farklıdır); bildirim
   süreleri ve şekil şartları belirtilir.
6. ARA SONUÇ: Sade özet, her asli yükümlülüğü, parasal sonucu ve çıkış yolunu kapsıyor mu; hiçbir
   aleyhe şart gizlenmemiş mi denetlenir.

## Çıktı modülleri
- "Bu sözleşmeyle ne taahhüt ediyorsunuz" özeti.
- Yükümlülük / karşılık / süre tablosu.
- Risk işaretleri (yüksek-orta-düşük) ve madde atfı.
- Çıkış yolları ve bildirim süreleri; "[doldurulacak]" boşluklar.

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
