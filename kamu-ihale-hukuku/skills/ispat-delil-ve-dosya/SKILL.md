---
name: ispat-delil-ve-dosya
description: "İhale uyuşmazlığında hangi belgenin ne için delil olduğunu, EKAP ve ihale işlem dosyasından hangi kayıtların temin edileceğini ve ispat yükünün kimde olduğunu belirlemek gerektiğinde kullanılır."
---

# İspat, Delil ve İhale Dosyası

## Görev
İhale uyuşmazlığında iddiayı destekleyecek belge ve kayıtları (ihale işlem dosyası, EKAP kayıtları, teklif zarfı, tutanaklar) belirlemek; ispat yükünün dağılımını ve delil temin yollarını ortaya koymak.

## Soğuk başlangıç (intake)
1. İddianın özü ne (yeterlik, değerlendirme, aşırı düşük, eşit muamele ihlali)?
2. Elinde hangi belgeler var; eksik olan kritik belge hangisi?
3. İhale işlem dosyasına/EKAP kayıtlarına erişim sağlandı mı?
4. Karşı tarafın/diğer isteklilerin teklif bilgisine ihtiyaç var mı?

## Denetim şeması
1. **Delil türleri:** İhale dokümanı, teklif mektubu ve eki belgeler, geçici teminat, ihale komisyon kararı, kesinleşen ihale kararı bildirimi, tutanaklar (zarf açma, değerlendirme), zeyilname, açıklama yazıları temel yazılı delillerdir.
2. **EKAP ve işlem dosyası:** Elektronik Kamu Alımları Platformu (EKAP) üzerindeki kayıtlar ve ihale işlem dosyası temin edilir; idareden bilgi/belge talebi (saydamlık ilkesi, m.5) ve gerekirse mahkemece celp yoluna gidilir.
3. **İspat yükü:** Kural olarak işlemi tesis eden idare dayandığı sebebi ve belgeyi ortaya koyar; yeterliğini/teklifinin uygunluğunu iddia eden istekli ise ilgili belgeyi sunmuş olmalıdır. Aşırı düşük açıklamasında ispat yükü açıklamayı sunan isteklidedir.
4. **Gizlilik dengesi (m.5, m.61):** Diğer isteklilerin ticari sır niteliğindeki bilgileri korunur; itirazen şikâyette KİK dosya üzerinden inceleme yapar.
5. **Ara sonuç:** İddia-delil eşleştirmesi yapılır; eksik delil için temin yolu (idareden talep, EKAP, mahkeme celbi) planlanır.

İspat yükü: Yukarıdaki dağılıma göre her iddia somut belgeye bağlanır.

## Çıktı modülleri
- İddia-delil eşleştirme tablosu.
- Eksik belge ve temin yolu listesi.
- EKAP/işlem dosyası kayıt dizini.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
