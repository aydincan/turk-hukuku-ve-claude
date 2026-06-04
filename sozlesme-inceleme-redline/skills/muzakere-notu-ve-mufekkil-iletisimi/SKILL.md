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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
