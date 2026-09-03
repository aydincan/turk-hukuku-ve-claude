---
name: senet-iptali-zayi
description: "Kaybolan, çalınan veya yok olan kıymetli evrakın iptali davasını ve ödemeden men kararını yürütmek; senedi elinden çıkan hak sahibinin hakkını koruması gerektiğinde kullanılır."
---

# Senedin Zıyaı ve İptali

## Görev
Elden çıkan (kayıp, çalıntı, yok olmuş) kıymetli evrakın iptali yoluyla hak sahibinin korunmasını sağlamak; ödemeden men tedbiri, ilan ve iptal kararı sürecini yürütmek.

## Soğuk başlangıç (intake)
- Senet hangi tip (çek, bono, poliçe, nama/hamiline) ve nasıl elden çıktı (kayıp/çalıntı/imha)?
- Senedi en son elinde bulunduran kim; senet içeriği (bedel, vade, taraflar) belgelenebiliyor mu?
- Senet henüz ödenmedi mi; muhatap/borçlu kim?
- Acil ödemeden men tedbiri gerekiyor mu?

## Denetim şeması
1. İptal kabiliyeti: kambiyo senetleri ve kıymetli evrak zıyaı halinde mahkemeden iptaline karar verilmesi istenebilir (TTK m.651 vd. genel; kambiyoda poliçe için m.757-765, çek için m.818 yollamasıyla uygulanır).
2. Yetkili/görevli mahkeme: kural olarak ödeme yeri veya senedin tedavül ettiği yer asliye ticaret mahkemesi; talep, senedi elinde bulunduranın bilinmemesi haliyle iptal davası olarak açılır.
3. Ödemeden men tedbiri: hak sahibinin istemi üzerine mahkeme borçluya/muhataba senet bedelini ödemekten men eden tedbir kararı verir (TTK m.758); böylece senet eline geçen üçüncü kişiye ödeme engellenir.
4. İlan ve süre: mahkeme, senedi getirmesi için hamile uygun süre vererek ilan yapar (m.759 vd.); süre içinde senet ibraz edilmezse iptaline karar verilir.
5. İptal kararının etkisi: iptal kararıyla hak sahibi, senet olmadan da hakkını borçludan talep edebilir veya yeni senet düzenlenmesini isteyebilir (m.763).
6. Ara sonuç: senet iyiniyetli üçüncü kişiye geçmişse onun korunan iktisabı (m.687) ile hak sahibinin iptal talebi karşı karşıya gelir; bu durumda iyiniyet ve devir zinciri ayrıca incelenir.

## Çıktı modülleri
- Ödemeden men tedbiri talepli iptal dilekçesi taslağı.
- Senet kimlik kartı (tip/bedel/vade/taraf [doldurulacak]).
- İlan ve süre takvimi notu.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
