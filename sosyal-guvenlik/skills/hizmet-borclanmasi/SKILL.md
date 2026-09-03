---
name: hizmet-borclanmasi
description: "Askerlik, doğum, yurtdışı çalışma, doktora/avukat stajı gibi sürelerin borçlanılarak prim günü kazanılması ve emeklilik koşulunun tamamlanması istendiğinde kullanılır."
---

# Hizmet Borçlanması (Askerlik, Doğum, Yurtdışı)

## Görev
Borçlanılabilir sürelerin tespiti, borçlanma tutarının hesabı ve borçlanmanın emeklilik koşuluna etkisini değerlendirmek.

## Soğuk başlangıç (intake)
- Hangi süre borçlanılmak isteniyor: askerlik, doğum, yurtdışı çalışma, staj, ücretsiz izin mi?
- Kişinin halen veya geçmişte sigortalılığı var mı? (Bazı borçlanmalar mevcut sigortalılık şartına bağlı.)
- Borçlanmanın amacı eksik prim gününü tamamlamak mı, emeklilik tarihini öne almak mı?
- Yurtdışı borçlanmasında hangi ülke, hangi belgeler mevcut?

## Denetim şeması
1. Borçlanılabilir süreler — 5510 m.41: Askerlik, doğum (en fazla üç çocuk için, çocuk başına azami süre ve doğum sonrası çalışmama şartı), ücretsiz izin, doktora/uzmanlık, avukatlık stajı vb. sayılı haller.
2. Doğum borçlanması koşulu: Doğumdan önce tescilli sigortalılık ve doğum sonrası çalışılmamış olma; çocuğun yaşaması şartları aranır.
3. Yurtdışı borçlanması — 3201 sayılı Kanun: Yurtdışında geçen çalışma/ev hanımlığı süreleri; başvuru, döviz cinsinden tutar ve aylık bağlamada özel kurallar.
4. Tutar — m.41: Borçlanılan sürenin günü, seçilen prime esas kazanç (alt-üst sınır arası) üzerinden prim oranıyla hesaplanır; süresinde ödenmezse borçlanma geçersiz olur.
5. Etki: Borçlanılan süre prim gününe ve duruma göre sigortalılık süresine eklenir; ancak ilk sigortalılık tarihini geriye götürüp götürmediği (kademe avantajı) ayrıca incelenir. Ara sonuç: kazanılacak gün ve emeklilik koşuluna etkisi. İspat: askerlik terhis belgesi, doğum kaydı, yurtdışı hizmet belgesi.

## Çıktı modülleri
- Borçlanılabilir süre ve koşul kontrol listesi.
- Borçlanma tutarı tahmini (seçilen PEK senaryolarıyla).
- Emeklilik koşuluna katkı analizi.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
