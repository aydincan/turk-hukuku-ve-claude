---
name: hukumsuzluk-iptal-davalari
description: "Bir marka, patent veya tasarımın geçersiz kılınması (hükümsüzlük) yahut markanın kullanılmama/jenerikleşme nedeniyle iptali iddialarında şartları ve idari/adli yol ayrımını değerlendirmek gerektiğinde kullanılır."
---

# Hükümsüzlük ve İptal Davaları

## Görev
Tescilli bir hakkın hükümsüzlüğü veya iptali talebini, sebep ve usul yönünden SMK çerçevesinde denetlemek; idari iptal yetkisi geçişini gözetmek.

## Soğuk başlangıç (intake)
- Hangi hak hedefleniyor (marka, patent, tasarım) ve tescil no nedir?
- Sebep mutlak/nispi ret sebebi mi, kullanmama mı, yenilik eksikliği mi?
- Davacının menfaati/sıfatı var mı; nispi sebepte itiraz/önceki hak sahipliği var mı?
- Hak kaç yıldır tescilli; sessiz kalma yoluyla hak kaybı (m.25/6) gündemde mi?

## Denetim şeması
1. Marka hükümsüzlüğü: Mutlak ret sebepleri (SMK m.5) ve nispi ret sebepleri (m.6) hükümsüzlük sebebidir (m.25). Menfaati olanlar dava açabilir; nispi sebeplerde önceki hak sahibi. Sessiz kalma (m.25/6 — 5 yıl) ve kötüniyet istisnası tartılır.
2. Marka iptali: Kullanmama (m.9 — kesintisiz 5 yıl ciddi kullanmama), jenerik hâle gelme, yanıltıcılık (m.26). İptal yetkisi geçiş süreciyle TÜRKPATENT'e bırakılmıştır (m.26 ve geçici m.4); bu süreçte idari/adli yol doğru seçilir.
3. Patent hükümsüzlüğü: Patentlenebilirlik şartlarının yokluğu, yetersiz açıklama, kapsam aşımı, gerçek hak sahipliği (SMK m.138). Tekniğin bilinen durumu delili.
4. Tasarım hükümsüzlüğü: Yenilik ve ayırt edici nitelik eksikliği, kamu düzeni, hak sahipliği (SMK m.77). Önceki tasarım/yayın delili.
5. İspat ve etki: Hükümsüzlük sebebini ileri süren ispatla yükümlü (HMK m.190). Hükümsüzlük kararı geçmişe etkilidir (SMK m.157/ilgili hükümler), iptal kural olarak ileriye etkili (m.27).
6. Ara sonuç: Hükümsüzlük genellikle tecavüz davasına karşı def'i veya karşı dava olarak gelir; süre, sıfat ve idari aşama tamamlanmadan dava reddi riski izlenir.

## Çıktı modülleri
- Hükümsüzlük/iptal sebebi haritası (madde atıflı).
- İdari (TÜRKPATENT) - adli yol seçim notu.
- Sıfat, süre ve sessiz kalma kontrol listesi.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
