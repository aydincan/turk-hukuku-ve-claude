---
name: sureler-zamanasimi
description: "Tıbbi sorumluluk talebinde hangi zamanaşımı süresinin (sözleşme, haksız fiil, idari, cezai) işlediğini ve başlangıç anını hesaplamak için kullanılır; rejim seçiminin tazminat hakkına etkisini ortaya koyar."
---

# Süreler ve Zamanaşımı

## Görev
Talebin hangi zamanaşımına tabi olduğunu, sürelerin başlangıç anını ve kesilme/durma hâllerini hesaplamak; en lehe rejimi tespit etmek.

## Soğuk başlangıç (intake)
1. Hukuki sebep sözleşme mi, haksız fiil mi, idari mi, cezai mi?
2. Zararın ve failin öğrenildiği tarih nedir?
3. Olay üzerinden kaç yıl geçti?
4. Daha ağır cezayı gerektiren bir suç söz konusu mu (ceza zamanaşımı)?

## Denetim şeması
1. **Sözleşmesel sorumluluk (vekâlet)**: Kural olarak TBK m.146 — 10 yıllık genel zamanaşımı. Sözleşme rejimi davacı için süre avantajı sağlar.
2. **Haksız fiil**: TBK m.72 — fiil ve failin öğrenilmesinden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanır (uzamış zamanaşımı).
3. **İdari (tam yargı)**: İYUK m.13 — zararın öğrenilmesinden itibaren 1 yıl ve her hâlde olaydan itibaren 5 yıl içinde idareye başvuru; dava süreleri İYUK m.7.
4. **Cezai**: Dava zamanaşımı TCK m.66; taksirle öldürme/yaralamada suçun cezasına göre değişir. Şikâyete bağlı yaralamada TCK m.73 — 6 ay şikâyet süresi.
5. **Başlangıç anı sorunu**: Geç ortaya çıkan zararlarda (gizli sakatlık) öğrenme anı kritiktir; objektif öğrenme aranır.
6. **Ara sonuç**: Birden çok rejim varsa davacı için en uzun olan seçilir; zamanaşımı def'i karşı tarafça ileri sürülmedikçe re'sen dikkate alınmaz.

## Çıktı modülleri
- Rejim bazlı zamanaşımı tablosu (süre + başlangıç)
- En lehe süre seçimi gerekçesi
- Kesilme/durma ve başvuru takvimi
- Süre riski uyarısı (kritik tarih)

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
