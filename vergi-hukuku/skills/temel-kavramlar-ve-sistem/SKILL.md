---
name: temel-kavramlar-ve-sistem
description: "Vergi türünü, mükellefiyeti, vergiyi doğuran olayı ve uygulanacak katmanı (maddi-usul-icra-yargı) belirlemek; bir vergi dosyasının haritasını çıkarmak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Vergilendirme Sistematiği

## Görev
Vergi uyuşmazlığının ya da danışmanlık sorusunun hangi vergi türüne, hangi mükellefiyete ve hangi hukuki katmana ait olduğunu belirleyip dosyanın yol haritasını kurmak. Bu beceri çoğu vergi işinin giriş süzgecidir.

## Soğuk başlangıç (intake)
1. Hangi vergi türü söz konusu (gelir, kurumlar, KDV, ÖTV, damga, MTV, emlak)?
2. Mükellef gerçek kişi mi, tüzel kişi mi; tam/dar mükellef mi?
3. Vergiyi doğuran olay hangi takvim yılında/dönemde gerçekleşti?
4. Elde bir idari işlem var mı (ihbarname, ödeme emri, ceza), tebliğ tarihi nedir?
5. Amaç tespit mi, savunma mı, planlama mı?

## Denetim şeması
1. **Verginin kanuniliği:** Anayasa m.73 — vergi ancak kanunla konur. Dayanak normu (GVK 193, KVK 5520, KDVK 3065, VUK 213) ve ilgili maddeyi tespit et.
2. **Vergiyi doğuran olay:** VUK m.19 uyarınca olayın vukuu/hukuki durumun tekemmülü anını belirle. Bu an hem zamanaşımının (VUK m.114) hem de uygulanacak oran/mevzuatın referansıdır.
3. **Mükellef ve vergi sorumlusu ayrımı:** VUK m.8 — mükellef vergi borcunu kendi malvarlığından ödeyen; sorumlu, kesip ödeyen (örn. stopaj/tevkifat). Muhatabı doğru belirle.
4. **Ekonomik yaklaşım:** VUK m.3/B — vergilendirmede olayların gerçek mahiyeti esastır; ispat, iktisadi-ticari icaplara uygunlukla değerlendirilir. Muvazaa/peçeleme iddiası burada doğar.
5. **Katman tayini:** Sorun matrah/oran ise maddi hukuk; tarh-tebliğ-ceza-süre ise VUK usul; tahsil-haciz-tecil ise AATUHK; iptal talebi ise İYUK vergi yargısı.
6. **Ara sonuç:** Vergi türü + mükellefiyet + doğuran olay yılı + katman + (varsa) işlem tipi ve tebliğ tarihi tek satırda sabitlenir.

## Çıktı modülleri
- Dosya künyesi tablosu (vergi türü, dönem, mükellef, tutar, işlem tipi, tebliğ tarihi).
- Uygulanacak norm zinciri (kanun > madde > tebliğ > özelge, bağlayıcılık notuyla).
- Katman ve sonraki adım yönlendirmesi (uzlaşma / dava / düzeltme / planlama).
- Açık belirsizlikler ve istenecek belge listesi.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
