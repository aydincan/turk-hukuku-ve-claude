---
name: borclu-temerrudu
description: "Borçlunun borcunu zamanında ifa etmemesi, temerrüt faizi, gecikme tazminatı ve karşılıklı sözleşmelerde dönme/aynen ifa/tazminat seçeneklerinin değerlendirilmesi gerektiğinde kullanılır."
---

# Borçlu Temerrüdü ve Seçimlik Haklar

## Görev
Borçlunun temerrüde düşüp düşmediğini, ihtar ve süre şartlarını, temerrüt faizini ve karşılıklı sözleşmelerde alacaklının seçimlik haklarını belirlemek.

## Soğuk başlangıç (intake)
- Borç muaccel mi; alacaklı borçluyu ihtar etti mi?
- Sözleşmede kesin vade var mı (ihtar gereksiz hâl)?
- Edim para borcu mu; faiz oranı kararlaştırıldı mı?
- Alacaklı aynen ifada mı ısrar ediyor, yoksa dönme/fesih mi istiyor?

## Denetim şeması
1. Temerrüt şartları: TBK m.117 — muaccel borç + alacaklının ihtarı. İhtar gerekmeyen hâller (m.117/f.2): kesin vade kararlaştırılmış, ihtarın faydasızlığı, borçlunun ifadan kaçınacağını bildirmesi, haksız fiil/sebepsiz zenginleşme bazı hâlleri.
2. Genel sonuçlar: m.118 — borçlu beklenmedik hâlden de sorumlu olur (sorumluluğun ağırlaşması). Gecikme tazminatı.
3. Para borçlarında: m.120 — temerrüt faizi; sözleşmede oran yoksa 3095 s.K. uygulanır. Aşkın zarar (munzam zarar) m.122; ticari işlerde TTK m.8-9 faiz rejimi.
4. Karşılıklı borç yükleyen sözleşmelerde seçimlik haklar: m.123-126 — alacaklı uygun süre verir (m.123; gereksiz olduğu hâller m.124). Süre sonunda: ya aynen ifa + gecikme tazminatı, ya ifadan vazgeçip müspet zarar (olumlu zarar) tazmini, ya da sözleşmeden dönüp menfi zarar (olumsuz zarar) tazmini (m.125). Sürekli edimli sözleşmelerde dönme yerine fesih (m.126).
5. Müspet/menfi zarar ayrımı: Dönmede menfi zarar (sözleşme hiç yapılmasaydı durumu), ifadan vazgeçmede müspet zarar (sözleşme ifa edilseydi durumu).
6. İspat yükü: Temerrüdü ve zararı alacaklı; kusursuzluğu ve mücbir sebebi borçlu ispatlar.

## Çıktı modülleri
- Temerrüt oluşum analizi (ihtar/kesin vade kontrolü).
- Süre verme ihtarnamesi taslağı iskeleti.
- Seçimlik hak ve zarar kalemleri (müspet/menfi) tablosu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
