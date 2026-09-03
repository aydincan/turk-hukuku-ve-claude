---
name: grev-ve-lokavt
description: "Kanuni grev ve lokavt karar/uygulama usulunu, grev yasaklarini ve ertelemeyi, kanun disi grevin sonuclarini ele alir; grev karari alma, grev yasagi/erteleme veya kanun disi grev iddiasi durumlarinda kullanilir."
---

# Grev ve Lokavt Hukuku

## Görev
Kanuni grev/lokavt kararının alınması, uygulanması, yasak ve erteleme rejimi ile kanun dışı grevin hukuki sonuçlarını denetlemek. En yüksek riskli aşamadır; usul hatası fesih ve tazminat doğurur.

## Soğuk başlangıç (intake)
- Arabuluculuk tutanağı tutuldu mu, tarihi nedir?
- İşkolu/işyeri grev yasağı kapsamında mı (örn. can/mal güvenliği, bankacılık, kamu hizmeti)?
- Grev kararı alındı mı, ilan ve uygulama tarihleri nedir?
- Bir erteleme kararı söz konusu mu?

## Denetim şeması
1. **Kanuni grev şartı:** 6356 m.58-60 — grev ancak menfaat uyuşmazlığında, arabuluculuk aşaması tüketildikten ve uyuşmazlık tutanağı tebliğinden itibaren **60 gün** içinde alınan kararla, **6 işgünü** önce karşı tarafa bildirilerek uygulanabilir. Bu unsurlar yoksa grev kanun dışıdır.
2. **Lokavt:** 6356 m.60 — işverenin kanuni grev kararına karşı uygulayabileceği savunma aracı; benzer usul ve sürelere tabidir.
3. **Grev yasakları:** 6356 m.62 — can ve mal kurtarma, cenaze/mezarlık, şehir suyu-elektrik-gaz-petrol üretim/dağıtımı, bankacılık (sınırlı), hastaneler, itfaiye gibi işlerde/yerlerde grev ve lokavt yasaktır; bu uyuşmazlıklar **yüksek hakem kuruluna** gider (m.51).
4. **Grev erteleme:** 6356 m.63 — genel sağlığı veya millî güvenliği bozucu nitelikteki grev/lokavt, Cumhurbaşkanı kararıyla **60 gün** ertelenebilir; erteleme sonunda anlaşma yoksa uyuşmazlık YHK'ye gider.
5. **Kanun dışı grev sonuçları:** 6356 m.64-67 — kanun dışı grevde işveren, iş sözleşmelerini haklı nedenle feshedebilir; sendika ve işçiler zarardan sorumlu olabilir. Grev oylaması (m.61) yapılabileceği unutulmaz.

İspat: tutanak tarihleri, ilan ve bildirim belgeleri, oylama tutanağı belirleyicidir.

## Çıktı modülleri
- Grev/lokavt usul ve süre kontrol listesi (60 gün karar, 6 işgünü bildirim).
- Grev yasağı / erteleme değerlendirme notu.
- Kanun dışı grev risk ve sonuç analizi.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
