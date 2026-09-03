---
name: nafaka-turleri-ve-hesap
description: "Tedbir, yoksulluk ve iştirak nafakası taleplerinin türünü, şartlarını, miktarını ve süresini belirlemek; nafakanın artırımı, azaltımı veya kaldırılması davalarını kurgulamak gerektiğinde kullanılır."
---

# Nafaka Türleri, Şartları ve Hesap

## Görev
Talep edilen nafakayı doğru türe oturtmak (tedbir, yoksulluk, iştirak, yardım), şartlarını denetlemek ve tarafların mali gücüne göre hakkaniyete uygun miktar/süre kurgulamak.

## Soğuk başlangıç (intake)
1. Nafaka kimin için isteniyor: eş için mi, çocuk için mi, üstsoy-altsoy/kardeş için mi?
2. Dava sürüyor mu (tedbir nafakası), boşanma kesinleşti mi (yoksulluk/iştirak)?
3. Tarafların gelirleri, malvarlığı, çocuk sayısı ve özel ihtiyaçları neler?
4. Mevcut nafaka var mı; artırım, azaltım veya kaldırma mı isteniyor?

## Denetim şeması
1. **Tür ayrımı.** Yargılama süresince eş ve çocuk için **tedbir nafakası** (TMK m.169) talep edilir. Boşanma sonrası eş için **yoksulluk nafakası** (m.175): boşanmayla yoksulluğa düşecek taraf, kusuru daha ağır olmamak kaydıyla, süresiz olarak isteyebilir. Çocuk için **iştirak nafakası** (m.182, m.327-330): velayet kendisine verilmeyen taraf, çocuğun bakım-eğitim giderlerine gücü oranında katılır; ergin olana kadar (eğitimi sürüyorsa m.328/2 kapsamında uzayabilir). Akrabalar arası **yardım nafakası** (m.364).
2. **Şart denetimi.** Yoksulluk nafakasında: boşanma yüzünden yoksulluk + talep eden kusurun daha ağır olmaması + nafaka yükümlüsünün gücü. İştirak nafakasında kusur aranmaz; ölçüt çocuğun ihtiyacı ve ana-babanın mali gücüdür.
3. **Miktar/biçim.** Hâkim irat veya toptan ödemeye karar verebilir (m.176/1); irat şeklindeki nafaka ÜFE/uyarlama hükmüyle (m.176/4, m.331) artırılabilir. Yoksulluk nafakası, alacaklının yeniden evlenmesi, ölüm veya fiilen evli gibi yaşama halinde kendiliğinden/dava ile kalkar (m.176/3).
4. **Uyarlama davaları.** Tarafların mali durumunun değişmesi halinde artırım/azaltım/kaldırma (m.176/4, m.331); ispat yükü değişikliği iddia edende.
5. **Ara sonuç.** Tür + şart + miktar/süre + uyarlama imkânı raporlanır.

## Çıktı modülleri
- Nafaka türü-şart-süre tablosu ve hakkaniyet gerekçesi.
- Gelir-gider/ihtiyaç dökümü ile miktar önerisi aralığı.
- Artırım/azaltım/kaldırma dilekçesi için dayanak listesi.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
