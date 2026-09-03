---
name: btk-yaptirim-savunma
description: "BTK tarafından verilen idari para cezası, yetkilendirme iptali, faaliyet durdurma gibi yaptırımlara ve bant genişliği daraltma kararlarına karşı savunma ve iptal davası hazırlığı gerektiğinde kullanılır."
---

# BTK İdari Yaptırımları ve Savunma

## Görev
BTK kaynaklı idari yaptırımlara (para cezası, yetkilendirme iptali, faaliyet durdurma, sosyal ağ tedbirleri) karşı yazılı savunma, idari başvuru ve iptal davası stratejisini kurmak; usul ve esas sakatlıklarını tespit etmek.

## Soğuk başlangıç (intake)
1. Yaptırımın türü ve dayanağı (5809/5651 hangi madde, hangi yönetmelik ihlali)?
2. Savunma istem yazısı/tebligat tarihi ve verilen süre nedir?
3. İhlal iddiasının somut konusu ve BTK'nın delili nedir?
4. Daha önce ihtar/savunma alındı mı, tekerrür/kademeli yaptırım var mı?

## Denetim şeması
1. **Dayanak ve oran**: 5809 m.60-63 (elektronik haberleşme yaptırımları) veya 5651 ilgili hükümleri — yaptırım türü, para cezasının hesap usulü, üst sınır ve oransallık. Ara sonuç: uygulanan yaptırım türü/oranı dayanakla uyumlu mu.
2. **Usul denetimi**: Savunma hakkının tanınması, makul süre, gerekçe ve bilgi/belgeye erişim; idari işlemde yetki ve şekil unsuru. Usul sakatlığı tek başına iptal sebebi olabilir.
3. **Esas denetimi**: İhlalin maddi olarak gerçekleşip gerçekleşmediği; teknik/yükümlülük ihlali iddiası karşı delil ve uzman raporuyla çürütülür. İhlali idare ispatlar; ancak müvekkil lehine vakıaları (uyum, mücbir sebep) belgeleyin.
4. **Ölçülülük ve eşit muamele**: Kademeli yaptırımda (özellikle sosyal ağ rejiminde reklam yasağı/bant daraltma) ölçülülük, benzer ihlallere uygulanan yaptırımlarla karşılaştırma ve ifade özgürlüğü etkisi.
5. **Dava yolu**: BTK yaptırımı idari işlem olduğundan İYUK m.7 (kural 60 gün) içinde iptal davası; m.27 yürütmenin durdurulması istemi tahsil/iptal/erişim kısıtı sonuçlarını dondurmak için kritik. Görevli yargı yeri idari yargıdır.

İlkesel içtihat için karararama.danistay.gov.tr (özellikle 13. Daire), temel hak boyutunda kararlarbilgibankasi.anayasa.gov.tr taranır; künye [doğrulanacak] işaretlenir, esas/karar no uydurulmaz.

## Çıktı modülleri
- BTK savunma yazısı taslağı (usul + esas).
- İptal davası dilekçesi ve YD istemi iskeleti.
- Sakatlık ve karşı delil tablosu.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
