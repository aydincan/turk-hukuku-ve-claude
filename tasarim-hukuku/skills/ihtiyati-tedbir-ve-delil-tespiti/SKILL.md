---
name: ihtiyati-tedbir-ve-delil-tespiti
description: "Tasarım uyuşmazlıklarında tecavüzün durdurulması/önlenmesi için ihtiyati tedbir ve delillerin kaybolmadan tespiti taleplerinin hazırlanması; hızlı müdahale, fuar baskını veya ürünün piyasadan çekilmesi gibi acil korumalar gerektiğinde kullanılır."
---

# İhtiyati Tedbir ve Delil Tespiti

## Görev
Esas dava açılmadan veya dava sürerken hakkı korumak: tecavüz fiilini durduran/önleyen ihtiyati tedbir ile, kaybolması/değişmesi muhtemel delillerin tespitini sağlamak. Fuar, ihale, sezon ürünü gibi zaman-kritik durumlarda belirleyicidir.

## Soğuk başlangıç (intake)
1. Acil tehlike ne (fuarda sergileme, toplu satış, ihaleye teklif, ürünün tükenmesi)?
2. Korunan hakkın geçerliliği ve sicil durumu güçlü mü (tedbirde yaklaşık ispat gerekir)?
3. Hangi delil kaybolabilir (numune, üretim kayıtları, stok, dijital kayıt)?
4. Karşı tarafın adresi/ürünü tespit edilebilir mi (keşif/bilirkişi için)?

## Denetim şeması
1. İhtiyati tedbir dayanağı (SMK m.159, HMK m.389 vd.): Tasarım sahibi, tecavüz veya yakın tehlike hâlinde üretimin/satışın durdurulması, ürünlere el konulması, teminat gibi tedbirler isteyebilir. Yaklaşık ispat (HMK m.390/3) yeterlidir; hakkın varlığı ve tecavüz/tehlike yaklaşık olarak gösterilir.
2. Teminat (HMK m.392): Tedbir kural olarak teminata bağlanır; haksız tedbir tazminat sorumluluğu doğurur (HMK m.399). Teminat tutarı ve istisnaları değerlendirin.
3. Tedbirin kapsamı: Üretim/satış/ithalat yasağı, gümrükte durdurma (SMK m.159 ve gümrük mevzuatı), ürünlere/araçlara el koyma, fuarda standdan çekme. Orantılılığı gerekçelendirin.
4. Esas dava süresi (HMK m.397/1): Dava açılmadan alınan tedbirde, tedbir kararının uygulanmasından itibaren 2 hafta içinde esas dava açılmalı; aksi hâlde tedbir kendiliğinden kalkar.
5. Delil tespiti (HMK m.400 vd.): Numune alma, üretim/stok/defter incelemesi, bilirkişiyle keşif; ileride elde edilmesi zorlaşacak deliller için ayrı veya tedbirle birlikte talep edilir.
6. Görev/yetki: FSHHM; tedbir esas davaya bakacak veya en yakın/uygun mahkemeden istenir (HMK m.390/1).

## Çıktı modülleri
- İhtiyati tedbir dilekçesi iskeleti (yaklaşık ispat, talep, teminat görüşü).
- Delil tespiti talebi ve tespit edilecek delil listesi.
- 2 haftalık esas dava süresi takvimi ve haksız tedbir riski notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
