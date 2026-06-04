---
name: surec-yol-haritasi-anlatimi
description: "Müvekkile bir davanın veya idari/icra sürecinin aşamalarını, tahmini sürelerini ve her aşamada ne olacağını yalın bir yol haritası olarak anlatmak gerektiğinde kullanılır."
---

# Dava ve Süreç Yol Haritası Anlatımı

## Görev
Müvekkile önündeki sürecin (hukuk davası, idari dava, icra takibi, soruşturma) hangi aşamalardan
geçeceğini, kabaca ne kadar süreceğini ve her aşamada kendisinden ne beklendiğini anlaşılır bir
yol haritasıyla anlatmak; takvim ve beklenti yönetimi sağlamak.

## Soğuk başlangıç (intake)
1. Hangi süreç ve hangi yargı kolu (HMK, İYUK, CMK, İİK)?
2. Süreç hangi aşamada başlıyor (henüz açılmadı / derdest / karar sonrası)?
3. Müvekkilin aktif katkı vermesi gereken adımlar var mı (delil, ifade, vekâletname)?
4. Zorunlu ön adım var mı (dava şartı arabuluculuk gibi)?

## Denetim şeması
1. AŞAMALARI DİZ: Süreç sıralı adımlara bölünür. Örn. hukuk davasında: (varsa) dava şartı
   arabuluculuk (HUAK 6325 s. m.18/A — ticari/iş/tüketici uyuşmazlıklarında), dava açılışı, cevap
   ve dilekçeler aşaması, ön inceleme (HMK m.137 vd.), tahkikat, hüküm, istinaf, temyiz.
2. SÜRE BEKLENTİSİ: Her aşama için gerçekçi tahmini süre verilir; "tahmini" olduğu vurgulanır,
   kesin süre vaadi yapılmaz.
3. MÜVEKKİL GÖREVLERİ (ispat/katkı): Hangi aşamada müvekkilden ne istendiği (delil teslimi, tanık
   bildirimi, duruşmaya katılım, ödeme) işaretlenir.
4. KRİTİK SÜRELER: Kanun yolu süreleri ve hak düşürücü süreler takvim mantığıyla anlatılır
   (örn. istinaf iki hafta — HMK m.345).
5. ÇIKIŞ/UZLAŞMA NOKTALARI: Her aşamada sulh/uzlaşma veya vazgeçme imkânı varsa belirtilir.
6. ARA SONUÇ: Yol haritası tüm aşamaları, müvekkil görevlerini ve kritik süreleri kapsıyor mu;
   gerçekçi mi.

## Çıktı modülleri
- Aşama aşama akış (zaman çizelgesi mantığında).
- Her aşamada "ne olacak / sizden ne beklenir / tahmini süre" satırı.
- Kritik süre uyarıları.
- Olası çıkış/uzlaşma noktaları ve belirsizlik notu.

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
