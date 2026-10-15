---
name: muzakere-notu-ve-mufekkil-iletisimi
description: "İnceleme bulgularını önceliklendirilmiş bir müzakere stratejisine ve müvekkilin anlayacağı sade bir özete dönüştürmek gerektiğinde kullanılır."
---

# Müzakere Notu ve Müvekkil İletişimi

## Görev
Madde madde inceleme ve redline çıktısını, önceliklendirilmiş bir müzakere stratejisine ve müvekkile sunulacak sade, karar verdirici bir özete dönüştürmek.

## Soğuk başlangıç (intake)
- Müvekkilin işlemden ana hedefi ve risk iştahı ne?
- Müzakerede pazarlık gücü kimde; zaman baskısı var mı?
- Hangi talepler "olmazsa olmaz", hangileri "isterse" düzeyinde?
- Müvekkilin teknik hukuk bilgisi ne düzeyde (dil sadeliği için)?

## Denetim şeması
1. **Öncelik matrisi**: Bulgular "deal-breaker / yüksek öncelik pazarlık / düşük öncelik / kabul" olarak sıralanır; her birine anchor ve fallback bağlanır.
2. **Taviz haritası**: Müvekkilin verebileceği tavizler ile karşılığında alınacak kazanımlar eşleştirilir (paket pazarlık mantığı).
3. **Gerekçe zırhı**: Her talep için müzakere masasında kullanılacak gerekçe — emredici dayanak (TBK m.27, m.115, m.182), "market standard" veya karşılıklılık argümanı.
4. **Risk-karar bağlama**: Müvekkile her kritik madde için "kabul edersen şu risk, reddedersen şu sonuç" netliğiyle karar seçeneği sunulur.
5. **Sade dil süzgeci**: Hukuki doğruluk korunarak teknik terimler açıklanır; tablo ve madde işaretleriyle özetlenir.
6. **İmza öncesi kontrol**: Son metin değişiklikleri, açık kalan `[doldurulacak]` alanlar, vekâlet/yetki teyidi ve nüsha düzeni hatırlatılır.

## Çıktı modülleri
- Önceliklendirilmiş müzakere notu (talep / gerekçe / fallback / öncelik).
- Müvekkile tek sayfalık sade özet ve karar seçenekleri.
- İmza öncesi son kontrol listesi.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
