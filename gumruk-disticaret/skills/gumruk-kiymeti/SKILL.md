---
name: gumruk-kiymeti
description: "İthalatta gümrük kıymetinin doğru hesaplanması, satış bedeli yönteminin reddi, kıymet artırımı ve buna bağlı ek tahakkuklarda; kıymet ihtilaflarını yöntem hiyerarşisi ve ilave kalemler üzerinden çözmek için kullanılır."
---

# Gümrük Kıymeti Belirleme ve İhtilafları

## Görev
İthal eşyasının gümrük kıymetini 4458 m.23-31 yöntem hiyerarşisine göre belirlemek; idarenin satış bedelini reddedip kıymet artırması veya ilave kalem eklemesi nedeniyle çıkan ek tahakkuk ihtilaflarını çözmek.

## Soğuk başlangıç (intake)
- Beyan edilen kıymet ve ödeme şekli nedir; alıcı-satıcı arasında ilişki var mı?
- Faturaya yansımayan royalti, lisans, komisyon, navlun, sigorta gibi kalemler var mı?
- İdare satış bedelini hangi gerekçeyle reddetti veya hangi referans/emsal kıymeti esas aldı?
- Kıymet araştırması, ek beyan veya sonradan kontrol raporu mevcut mu?

## Denetim şeması
1. Asıl yöntem: Gümrük kıymeti kural olarak satış bedelidir (m.24) — fiilen ödenen veya ödenecek bedel. Bu yöntemin uygulanabilmesi için m.24/3'teki şartlar (kısıtlama yokluğu, ilişkinin fiyatı etkilememesi) aranır.
2. İlaveler (m.27): Alıcı tarafından ödenen ve fiyata dahil olmayan komisyon, ambalaj, royalti/lisans ücreti, Türkiye'ye kadar navlun ve sigorta gibi kalemler kıymete eklenir. Royaltinin "satış şartı" olup olmadığı ayrıca denetlenir.
3. İndirimler (m.28): İthalattan sonraki montaj/nakliye, Türkiye'de ödenen vergiler gibi kalemler ayrıştırılabiliyorsa kıymete dahil edilmez.
4. Yöntem hiyerarşisi: Satış bedeli reddedilirse sırasıyla aynı eşyanın satış bedeli (m.25/a), benzer eşya, indirgeme (tutundurma), hesaplanmış kıymet ve son çare yöntemi (m.25-26) uygulanır. İdare sırayı atlamamalı ve reddi gerekçelendirmelidir.
5. İspat yükü: İdare satış bedelini reddederken somut şüphe ve veri ortaya koymalı; yükümlü beyanın gerçekliğini destekleyen banka ödemesi, sözleşme ve emsal verilerle savunur. Soyut "düşük kıymet" iddiası tek başına yetmez (Danıştay yerleşik içtihadı [doğrulanacak], karararama.danistay.gov.tr).
6. Ara sonuç: Doğru yöntem ve kıymet tabanı belirlenir; ilave/indirim kalemleri hesaplanır; ek tahakkuk farkı ve buna bağlı m.234 cezası değerlendirilir.

## Çıktı modülleri
- Kıymet hesap tablosu (beyan vs. idare farkı, kalem kalem)
- Yöntem reddine karşı gerekçeli itiraz/dava taslağı
- Royalti ve ilişkili kişi analizi notu

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
