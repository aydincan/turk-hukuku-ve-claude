---
name: celiski-eksiklik-tespiti
description: "Rapor içi çelişkileri, dosyadaki diğer deliller veya önceki raporlarla çelişkileri ve sorulduğu hâlde yanıtsız kalan hususları sistematik biçimde ortaya çıkarmak istendiğinde kullanılır."
---

# Çelişki ve Eksiklik Tespiti

## Görev
Raporu hem kendi içinde hem dosyanın bütünüyle karşılaştırarak tutarsızlık ve boşlukları çıkarmak; bunları ek rapor veya yeni heyet talebine gerekçe yapmak.

## Soğuk başlangıç (intake)
- Dosyada birden fazla bilirkişi raporu/uzman mütalaası var mı?
- Rapor, kendi içinde farklı yerlerde farklı sayı/sonuç veriyor mu?
- Tanık beyanı, keşif tutanağı, belge gibi delillerle rapor çelişiyor mu?
- Hangi soru fiilen yanıtsız kalmış?

## Denetim şeması
1. **Rapor içi çelişki:** Gövde, tablo ve sonuç bölümleri arasındaki sayısal/mantıksal tutarsızlıklar işaretlenir. Aynı kalemin farklı yerlerde farklı çıkması denetlenebilirliği bozar (HMK m.279).
2. **Dosya delilleriyle çelişki:** Rapordaki kabuller; belge, tanık, keşif tutanağı ve kayıtlarla karşılaştırılır. Delille çelişen kabul, sonucu sakatlar; çelişki dosya sayfasıyla çıpalanır.
3. **Raporlar arası çelişki:** Birden fazla rapor varsa hangi noktada ayrıştıkları ve hangisinin dayanağının güçlü olduğu gösterilir; hâkim raporları serbestçe takdir eder (HMK m.282), bu yüzden çelişkinin giderilmesi istenir.
4. **Eksik yanıt:** Görevlendirme sorularından yanıtsız kalanlar listelenir (HMK m.273 ile bağ).
5. **Ara sonuç:** Giderilebilir çelişki/eksik → **ek rapor**; raporlar arası esaslı ve giderilemeyen çelişki → **yeni/üçüncü heyet** talebi (HMK m.281). Her çelişki "rapordaki ifade vs. çelişen kaynak" biçiminde karşılıklı sunulur.

## Çıktı modülleri
- Çelişki matrisi (rapordaki ifade / çelişen kaynak / sayfa / etki).
- Yanıtsız kalan görevlendirme sorularının listesi.
- Raporlar arası ayrışma haritası.
- Çelişki temelli itiraz ve talep paragrafı taslağı.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
