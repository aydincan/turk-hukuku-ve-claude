---
name: istem-yorumu-koruma-kapsami
description: "Patentin koruma kapsamının ne olduğu, bir ürün/usulün istemlerin içine girip girmediği, eşdeğerlerin değerlendirilmesi gerektiğinde kullanılır; tecavüz ve hükümsüzlük analizinin teknik çekirdeğidir."
---

# İstem Yorumu ve Koruma Kapsamı

## Görev
İstemleri SMK m.89 uyarınca yorumlayarak patentin koruma kapsamını netleştirmek; incelenen ürün/usulün istemlere literal veya eşdeğerler yoluyla girip girmediğini saptamak.

## Soğuk başlangıç (intake)
1. Bağımsız ve bağımlı istemler neler; metin elde mi?
2. İhtilaflı ürün/usulün teknik özellikleri nedir?
3. İnceleme/itiraz sürecinde istemler daraltıldı mı (dosya geçmişi)?
4. Tarifname ve resimler hangi yorumu destekliyor?

## Denetim şeması
1. **Koruma kapsamının kaynağı (SMK m.89/1).** Koruma istemlerle belirlenir; tarifname ve resimler istemlerin yorumunda kullanılır. İstem dışı, yalnızca tarifnamede yer alan özellik kapsam dışıdır.
2. **İstem ayrıştırması.** Bağımsız istemi özellik kümelerine (öğelere) böl. Bağımlı istemler bağımsız isteme ek özellik getirir; tecavüz için kural olarak bağımsız istemin tüm öğeleri karşılanmalı (öğelerin tümü kuralı).
3. **Literal kapsam.** İhtilaflı ürün/usul, bağımsız istemin her bir öğesini birebir taşıyor mu? Bir öğe eksikse literal tecavüz yok.
4. **Eşdeğerler (SMK m.89/5).** İstemde yazılı öğenin yerine, aynı işlevi esas itibarıyla aynı şekilde gören ve aynı sonucu doğuran eşdeğer öğe konulmuşsa kapsam genişler. Eşdeğer değerlendirmesi başvuru/rüçhan tarihindeki uzmana göre yapılır.
5. **Dosya geçmişiyle sınırlama.** İnceleme/itirazda istemden vazgeçilen unsur sonradan eşdeğer yoluyla geri alınamaz (beyan/sınırlama tutarlılığı). Ara sonuç: kapsam içi mi dışı mı?

## Çıktı modülleri
- Bağımsız istem öğe-öğe haritası.
- Literal kapsam karşılaştırma tablosu (öğe / ürün-usul / eşleşti mi).
- Eşdeğer değerlendirme notu.
- Koruma kapsamı sınırı ve dosya geçmişi uyarısı.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
