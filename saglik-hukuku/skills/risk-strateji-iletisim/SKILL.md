---
name: risk-strateji-iletisim
description: "Tıbbi uyuşmazlıkta hekim, hastane veya hasta tarafının dava başarı şansını, risklerini ve müzakere/sulh seçeneklerini değerlendirmek ve müvekkile sade bir yol haritası sunmak için kullanılır."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Mevcut delil ve hukuki duruma göre tarafın kazanma/kaybetme riskini değerlendirmek, dava-sulh-arabuluculuk seçeneklerini tartmak ve müvekkile anlaşılır bir strateji sunmak.

## Soğuk başlangıç (intake)
1. Temsil edilen taraf kim: hasta/yakını, hekim, hastane, sigorta?
2. Eldeki en güçlü ve en zayıf delil hangisi?
3. Tarafın önceliği: tazminat miktarı, hız, mesleki itibar, ceza riskini bertaraf?
4. Mesleki sorumluluk (zorunlu/ihtiyari) sigortası var mı?

## Denetim şeması
1. **Olgu-hukuk uyumu**: Sorumluluk unsurları (kusur, illiyet, zarar, onam) mevcut delille ne ölçüde karşılanıyor? Her unsur için güç skoru (zayıf/orta/güçlü).
2. **Karşı taraf senaryosu**: Komplikasyon savunması, müterafik kusur (TBK m.52), aydınlatmanın ispatı, zamanaşımı def'i gibi olası savunmalar öngörülür.
3. **Bilirkişi/ATK riski**: Sonuç büyük ölçüde rapora bağlı; rapor lehe/aleyhe çıkma olasılığı strateji belirler.
4. **Sigorta ve rücu**: Hekim mesleki sorumluluk sigortası, kamu hekiminde idarenin rücu riski (3359 Ek m.18) değerlendirilir.
5. **Çözüm yolu seçimi**: Dava, sulh, arabuluculuk; ceza riski varsa savunma stratejisiyle eşgüdüm. Maliyet-fayda ve süre karşılaştırması.
6. **Müvekkil iletişimi**: Sonuç olasılıkları abartısız ve sade dille; garanti verilmez, en iyi/orta/en kötü senaryo sunulur. Ara sonuç: önerilen yol ve gerekçesi.

## Çıktı modülleri
- Unsur bazlı güç skoru tablosu
- Senaryo analizi (en iyi/orta/en kötü)
- Strateji önerisi (dava/sulh/arabuluculuk)
- Müvekkile sade dilde özet ve yapılacaklar listesi

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
