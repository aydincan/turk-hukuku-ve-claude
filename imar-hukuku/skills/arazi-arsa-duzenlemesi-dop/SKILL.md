---
name: arazi-arsa-duzenlemesi-dop
description: "İmar uygulaması, parselasyon, düzenleme ortaklık payı (DOP) kesintisi, dağıtım ve tahsis işlemlerine itiraz veya iptal davası gündeme geldiğinde; eşit/eşdeğer dağıtım ilkesi ve DOP oranı sorulduğunda kullanılır."
---

# Arazi ve Arsa Düzenlemesi (m.18 / DOP)

## Görev
İmar uygulaması (parselasyon) ve DOP işlemlerinin hukuka uygunluğunu denetlemek; eşit dağıtım ve kamu payı dengesini kontrol ederek iptal davasını kurmak.

## Soğuk başlangıç (intake)
- Uygulama hangi imar planına dayanıyor, encümen/onay kararı tarihi ne?
- Müvekkilin eski parseli ile tahsis edilen yeni parsel(ler) neler?
- DOP oranı kaç, hangi kamu tesisleri için kesildi?
- Dağıtımda değer kaybı, başka bölgeye tahsis veya eşitsizlik var mı?

## Denetim şeması
1. **Uygulamanın dayanağı (3194 m.18)**: Düzenlemenin **onaylı uygulama imar planına** dayanması zorunludur; plansız m.18 uygulaması yapılamaz. Plan-uygulama bağı ilk denetim noktasıdır.
2. **DOP kesintisi**: Düzenlemeye giren taşınmazlardan, düzenleme ile oluşan değer artışı karşılığında ve **kanunda belirlenen üst oran** dahilinde, bedelsiz olarak düzenleme ortaklık payı kesilir; DOP yalnızca m.18'de sayılan kamusal hizmet alanları için kullanılabilir. Oranın ve kullanım amacının yasallığı denetlenir.
3. **Eşit/eşdeğer dağıtım ilkesi**: Maliklerin yeni parsellere mümkün olduğunca **eski parseline yakın ve eşdeğer** biçimde tahsisi esastır; başka bölgeye savrulma, değer kaybı, hisseli hale getirme eşitlik denetiminden geçirilir.
4. **Mükerrer DOP yasağı**: Aynı taşınmazdan ikinci kez DOP kesilemez (daha önce kesinti yapılmışsa); bu husus tapu kaydı ve önceki uygulamalarla doğrulanır.
5. **İspat ve bilirkişi**: Harita mühendisi/şehir plancısı bilirkişi, dağıtım cetvelleri, parselasyon paftaları, değerleme; ispat yükü idarenin işlemin hukuka uygunluğunu, davacının somut zararını göstermesi şeklinde paylaşılır.
6. **Süre ve ara sonuç**: Parselasyon işlemi ilan edilir; İYUK m.7'de 60 günde iptal davası açılır. DOP oranı, dağıtım veya plan-uygulama bağı sakatsa iptal + gerekirse YD. İlkesel Danıştay atfı `[doğrulanacak]`.

## Çıktı modülleri
- DOP oranı ve kullanım amacı denetim notu.
- Eski-yeni parsel eşdeğerlik karşılaştırması.
- Mükerrer DOP/değer kaybı kontrol listesi.
- Parselasyon iptali dilekçe iskeleti ve bilirkişi soruları.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
