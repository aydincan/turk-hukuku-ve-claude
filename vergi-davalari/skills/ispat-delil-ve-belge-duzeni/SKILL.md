---
name: ispat-delil-ve-belge-duzeni
description: "Vergi uyuşmazlığında ispat yükünün dağılımını, ekonomik yaklaşım ilkesini ve defter-belge-banka kayıtları gibi delillerin değerlendirilmesini ele almak için kullanılır."
---

# İspat, Delil ve Belge Düzeni

## Görev
Vergi uyuşmazlığında ispat yükünün taraflar arasında nasıl dağıldığını belirlemek; ekonomik yaklaşım ve ispat serbestisi çerçevesinde delilleri (defter, belge, banka, POS, sözleşme) değerlendirip savunmaya bağlamak.

## Soğuk başlangıç (intake)
1. İdare iddiasını hangi tespite dayandırıyor (inceleme raporu, karşıt inceleme, bilgi formu)?
2. Mükellef defter ve belgeleri tam mı; banka/POS/stok kayıtları mevcut mu?
3. Uyuşmazlık sahte belge, kayıt dışı hasılat mı yoksa nitelendirme/yorum farkı mı?
4. Hangi belgeler eksik veya çelişkili?

## Denetim şeması
1. **Genel ilke.** VUK m.3/B — vergilendirmede vergiyi doğuran olay ve muamelelerin **gerçek mahiyeti** esastır; ispat serbesttir, ancak **yemin** delil olamaz. İktisadi, ticari ve teknik icaplara uymayan veya olayın özelliğine göre normal olmayan durumu iddia eden ispatla yükümlüdür.
2. **İspat yükünün dağılımı.** Matrah farkını/ziyaı iddia eden idare somut tespit getirmekle; bu tespite karşı çıkan mükellef karşı delil sunmakla yükümlü. Sahte belge iddiasında idarenin somut delili (düzenleyen hakkında tespit, ödeme-emtia hareketi yokluğu) ile mükellefin gerçeklik delili (ödeme, taşıma, stok) karşılaştırılır.
3. **Defter ve belgenin ispat gücü.** Usulüne uygun tutulan defterler sahibi lehine de delil olabilir; ibraz edilmeyen defter re'sen tarh sebebidir (VUK m.30). İbraz mücbir sebep (VUK m.13) varsa farklı değerlendirilir.
4. **Tamamlayıcı deliller.** Banka kayıtları, POS, sözleşme, irsaliye, randıman/karşılaştırma analizleri delil olarak sunulur; çelişkiler giderilir veya idare aleyhine kullanılır.
5. **Bilirkişi.** Hesap ve teknik konularda bilirkişi incelemesi talep edilir; rapordaki metodoloji ve dayanak denetlenir. Ara sonuç: hangi vakıanın kim tarafından ispatlanması gerektiği ve mevcut delilin yeterliliği belirlenir.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa / yükümlü taraf / mevcut delil).
- Delil dizini ve eksik/çelişki listesi.
- Bilirkişi/karşı delil talep notu.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
