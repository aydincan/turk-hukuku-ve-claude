---
name: ispat-ve-delil
description: "Tüketici uyuşmazlığında ispat yükünün kimde olduğunu, hangi delillerin gerektiğini ve karinelerin nasıl kullanılacağını planlamak gerektiğinde; özellikle ayıp, haksız şart ve masraf iadelerinde kullanılır."
---

# İspat ve Delil Stratejisi

## Görev
Tüketici uyuşmazlığında ispat yükünü doğru dağıtmak, lehe karineleri kullanmak, gerekli delilleri belirlemek ve delil bağlama mimarisini kurmak.

## Soğuk başlangıç (intake)
- İspatlanması gereken çekirdek vakıa ne (ayıbın varlığı, masrafın tahsili, şartın müzakere edilmediği)?
- Elde hangi belgeler var (fatura, sözleşme, ekran görüntüsü, yazışma, ödeme dekontu)?
- Teknik bir tespit gerekiyor mu (bilirkişi, servis raporu)?
- Karşı tarafın elinde tutulan belge var mı (sözleşme nüshası, hesap dökümü)?

## Denetim şeması
1. **Genel kural (TMK m.6):** Kanunda aksi öngörülmedikçe, iddiasını dayandırdığı olguyu ispat yükü iddia eden taraftadır.
2. **Ayıpta karine (TKHK m.10):** Teslimden itibaren altı ay içinde ortaya çıkan ayıp teslim anında var sayılır; bu süre içinde ispat satıcıdadır. Altı aydan sonra ayıbın varlığını ve eskiden geldiğini tüketici ispatlar; malın ayıpsız olduğunun ispatı ise satıcıya aittir (m.10/2).
3. **Haksız şartta karine (TKHK m.5/3):** Standart sözleşmedeki şartın müzakere edildiğini ispat satıcı/sağlayıcıya düşer; tüketici şartın matbu olduğunu göstermesi yeterlidir.
4. **Masraf/ücret iadesinde:** Tahsil edilen masrafın hizmet karşılığı ve hukuken öngörülmüş olduğunu ispat, bunu alan bankaya/sağlayıcıya aittir.
5. **Delil türleri (HMK m.199 vd.):** Senet (sözleşme, fatura), elektronik veri (e-posta, SMS, sipariş kaydı), tanık, bilirkişi, keşif. Tüketici işlemlerinde basit usulün esnekliği ve dosyaya hâkim somut delil önemlidir.
6. **Belge istetme (HMK m.219-220):** Sözleşme nüshası, hesap dökümü gibi karşı taraf veya üçüncü kişide bulunan belgeler için ibraz talebi; ibraz edilmezse aleyhe sonuç değerlendirmesi.
7. **Ara sonuç:** Hangi vakıayı kim ispatlayacak, hangi delil hangi vakıayı bağlıyor, bilirkişi gerekli mi?

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa → taraf → delil).
- Delil/belge ihtiyaç listesi ve eksik tespiti.
- Bilirkişi/servis raporu talep notu.
- Karşı tarafa belge ibraz talebi taslağı.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
