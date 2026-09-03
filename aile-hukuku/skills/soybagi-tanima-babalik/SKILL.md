---
name: soybagi-tanima-babalik
description: "Çocukla ana-baba arasında soybağının kurulması, reddedilmesi (soybağının reddi), tanıma ve babalık davası ile evlat edinme süreçlerinde, özellikle sıkı hak düşürücü süreler söz konusu olduğunda kullanılır."
---

# Soybağı, Tanıma ve Babalık Davası

## Görev
Çocuk ile ana-baba arasındaki soybağını kurmak veya kaldırmak; babalık karinesi, soybağının reddi, tanıma, babalık davası ve evlat edinme yollarını ve özellikle hak düşürücü süreleri yönetmek.

## Soğuk başlangıç (intake)
1. Çocuğun doğum tarihi ve ana-babanın o tarihteki medeni hali nedir?
2. Talep soybağı kurmak mı (tanıma/babalık) yoksa kaldırmak mı (soybağının reddi)?
3. Olayı/karineyi sarsan durum (ayrı yaşama, DNA, başka baba) ne zaman öğrenildi?
4. Çocuk ergin mi; vasi/kayyım atanması gerekiyor mu?

## Denetim şeması
1. **Soybağının kurulması.** Ana yönünden doğumla (m.282); baba yönünden ana ile evlilik (babalık karinesi m.285), tanıma (m.295) veya hâkim hükmü/babalık davası (m.301) ile. Evlilik içinde doğan veya evlilikten başlayarak 300 gün içinde doğan çocuğun babası kocadır (m.285/1).
2. **Soybağının reddi (m.286-291).** Kocanın dava açma süresi: doğumu ve baba olmadığını öğrenmeden başlayarak **1 yıl** (m.289/1). Çocuğun dava süresi erginlikten itibaren 1 yıl. Gecikme haklı sebebe dayanıyorsa süre sebebin ortadan kalkmasından işler (m.289/3). Karine çürütülürken DNA esastır.
3. **Tanıma ve babalık davası.** Tanıma resmî senet/vasiyetname/nüfus beyanı ile (m.295); tanımanın iptali (m.297-298). Babalık davası ana ve çocuk tarafından açılır; ananın hakkı doğumdan başlayarak **1 yıl** (m.303). Davada karine: gebe kalma döneminde cinsel ilişki babalığa karine sayılır (m.302).
4. **Evlat edinme.** Küçüğün evlat edinilmesi (m.305 vd.: bir yıl bakım, küçüğün yararı, en az 30 yaş veya 18 yıl evlilik vb.); ergin/kısıtlının evlat edinilmesi (m.313). Hâkim kararıyla kurulur.
5. **Ara sonuç.** Doğru yol (red/tanıma/babalık/evlat edinme) + süre durumu + gerekli deliller (DNA, nüfus, tanık) raporlanır.

## Çıktı modülleri
- Soybağı durum şeması ve uygulanacak dava türü.
- Hak düşürücü süre takvimi ve gecikme mazereti değerlendirmesi.
- Dava dilekçesi için taraf, talep ve delil (DNA tespiti talebi dahil) listesi.

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
