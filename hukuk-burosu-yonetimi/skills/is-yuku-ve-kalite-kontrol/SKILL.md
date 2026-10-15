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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
