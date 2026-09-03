---
name: is-yuku-ve-kalite-kontrol
description: "Büroda dosyaların avukatlara dağıtımı, kapasite planlaması, iş yükü dengelemesi ve çıktı kalitesinin gözden geçirilmesi (peer review) süreçleri kurgulanırken kullanılır."
---

# İş Yükü Dağılımı ve Kalite Kontrol

## Görev
Dosya ve görevleri ekip içinde dengeli ve uzmanlığa uygun dağıtmak; kapasiteyi izlemek; çıktıların (dilekçe, sözleşme, mütalaa) büroyu terk etmeden önce kalite kontrolünden geçmesini sağlamak.

## Soğuk başlangıç (intake)
1. Ekipte kaç avukat/stajyer var, uzmanlık alanları ve mevcut yükleri ne?
2. Dağıtılacak iş(ler)in türü, aciliyeti ve karmaşıklık düzeyi nedir?
3. Yaklaşan kritik süreler ve duruşmalar hangi tarihlerde yoğunlaşıyor?
4. Kalite kontrol için mevcut bir gözden geçirme (review) akışı var mı?

## Denetim şeması
1. **Yetkinlik eşleştirmesi**: İş, uzmanlık ve deneyime göre atanır; karmaşık/yüksek riskli iş daha kıdemli avukata, çift kontrol gerektirenlere ikinci göz atanır (özen — TBK m.506).
2. **Kapasite ve süre dengesi**: Mevcut yük ve yaklaşan süreler birlikte değerlendirilir; süre çakışmaları görünür kılınır, darboğaz tarihleri için erken müdahale planlanır.
3. **Çıkar çatışması teyidi**: Atama öncesi ilgili avukatın o işte çatışması olmadığı doğrulanır (1136 m.38).
4. **Kalite kontrol katmanı**: Her büro-dışı çıktı için kontrol listesi — doğru taraf/mahkeme, talep sonucu vakıalarla uyumlu mu, süre içinde mi, madde atıfları teyit edildi mi, gizli/yanlış bilgi sızıyor mu.
5. **Sorumluluk izi**: Hazırlayan ve gözden geçiren ayrı kaydedilir; revizyon notları saklanır.
6. **Ara sonuç**: Uygun atama + kapasite teyidi + tamamlanmış kalite kontrolü ile iş "teslime hazır" sayılır.

## Çıktı modülleri
- İş yükü/atama tablosu (avukat, dosya, aciliyet, kapasite durumu).
- Yaklaşan süre/duruşma yoğunluk takvimi.
- Çıktı kalite kontrol listesi (dilekçe/sözleşme/mütalaa için).

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
