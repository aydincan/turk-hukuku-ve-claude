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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
