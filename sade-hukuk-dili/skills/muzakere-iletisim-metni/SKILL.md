---
name: muzakere-iletisim-metni
description: "Karşı tarafa, kamu kurumuna veya üçüncü kişiye gönderilecek resmi ama anlaşılır bir yazışma, talep veya sulh teklifi metni hazırlamak; tonu ve hukuki pozisyonu koruyarak yalın anlatmak gerektiğinde kullanılır."
---

# Karşı Taraf ve Müzakere İletişim Metni

## Görev
Karşı tarafa, kuruma veya üçüncü kişiye gönderilecek bir yazıyı (talep, sulh teklifi, açıklama,
yanıt) hukuki pozisyonu ve uygun tonu koruyarak anlaşılır, profesyonel ve fazla agresif olmayan
bir dille hazırlamak; iletişimin amacına (anlaşma, baskı, bilgi) göre üslubu ayarlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim (karşı taraf, vekili, kamu kurumu, müşteri)?
2. Amaç ne (sulh, talep, savunma, bilgi verme)?
3. Hukuki pozisyon nedir ve nereye kadar açık edilecek?
4. Yazının ileride delil olma ihtimali var mı (ton ve içerik buna göre)?

## Denetim şeması
1. AMAÇ VE TON: Hedef belirlenir (kapı açık tutan sulh dili mi, net talep mi). Müzakerede aşırı
   sertlik kapatır, aşırı yumuşaklık pozisyon zayıflatır; denge kurulur.
2. POZİSYON KORUMA (ispat/çekince): Yazı ileride aleyhe delil olmamalı; gereksiz ikrar veya hak
   feragati içermez. Sulh görüşmelerinde "haklılığı kabul anlamına gelmez / her türlü hakkımız
   saklıdır (ihtirazi kayıt)" kaydı düşülür.
3. HUKUKİ DAYANAK ÖZÜ: Talep, dayandığı temel norma kısaca bağlanır (madde atfı gerekiyorsa)
   ama karşı tarafa ders verir tonundan kaçınılır.
4. NET TALEP VE SÜRE: Ne istendiği ve hangi süre içinde yanıt beklendiği açıkça yazılır;
   verilen süre makul ve takip edilebilir olmalıdır.
5. GİZLİLİK/UYUM: Müzakere yazışmalarında gizlilik kaydı; meslek kuralları gereği karşı taraf
   vekili varsa doğrudan müvekkille temastan kaçınma (TBB Meslek Kuralları) gözetilir.
6. ARA SONUÇ: Metin amaca hizmet ediyor mu; aleyhe ikrar/feragat içeriyor mu; ton uygun mu.

## Çıktı modülleri
- Resmi başlık ve muhatap.
- Bağlam + net talep + süre.
- İhtirazi kayıt / haklar saklı / gizlilik kaydı.
- Alternatif yumuşak ve sert ton versiyonları (gerekirse).

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
