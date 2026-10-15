---
name: delil-ispat-baglama
description: "Vakıaları doğru delillere bağlamak; ispat yükü, senetle ispat zorunluluğu, delil listesi ve delil tespiti taleplerini kurmak gerektiğinde kullanılır."
---

# Delil, İspat ve Delillerin Bağlanması

## Görev
Vakıaları kabul edilebilir delillerle desteklemek; ispat yükünü doğru dağıtmak; senetle ispat sınırlarını gözetmek ve delil listesini dilekçeye sağlam bağlamak. Somutlaştırılmamış delil dikkate alınmaz (HMK m.194).

## Soğuk başlangıç (intake)
- Hangi vakıa hangi delille ispatlanacak?
- Senet/yazılı delil var mı, yoksa tanık mı dayanılacak?
- Karşı tarafın elindeki belgeler gerekli mi (ibraz)?
- Delil tespiti veya bilirkişi gerekiyor mu?

## Denetim şeması
1. İspat yükü (HMK m.190; TMK m.6): Bir hakkın varlığını iddia eden, dayandığı vakıayı ispatla yükümlüdür. Karşı ispat ve aksini ispat ayrımını gözetin.
2. Delil türleri (HMK m.187 vd.): Kesin deliller (senet, yemin, kesin hüküm) ve takdiri deliller (tanık, bilirkişi, keşif, uzman görüşü). Her vakıaya en güçlü delili eşleyin.
3. Senetle ispat zorunluluğu (HMK m.200-201): Belirli tutarı aşan hukuki işlemler senetle ispatlanır; senede karşı tanık kural olarak dinlenmez. İstisnalar (m.203): yakın hısımlar, delil başlangıcı, örf-adet.
4. Belge ibrazı ve delil tespiti: Karşı taraftaki/üçüncü kişideki belge için ibraz (HMK m.219-222); kaybolma riski varsa delil tespiti (m.400-406). Fikri-sınai uyuşmazlıkta ihtiyati tedbirle birlikte.
5. Somutlaştırma (HMK m.194): Hangi delilin hangi vakıa için sunulduğunu açıkça yazın; tanıkla ispatı caiz olmayan vakıada tanık göstermeyin. Ara sonuç: vakıa-delil eşleşmesi tamsa delil listesi kapanır.

## Çıktı modülleri
- Vakıa-delil eşleşme tablosu
- Delil listesi (senet/tanık/bilirkişi/keşif)
- Senetle ispat sınırı uyarısı
- Delil tespiti/ibraz talebi taslağı

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
