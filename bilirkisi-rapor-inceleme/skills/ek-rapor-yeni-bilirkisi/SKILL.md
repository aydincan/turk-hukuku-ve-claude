---
name: ek-rapor-yeni-bilirkisi
description: "Bir kusurun ek raporla giderilebilir mi yoksa yeni bilirkişi/heyet mi gerektirdiği ayrımını yapmak ve bu doğrultuda en isabetli usulî talebi gerekçelendirmek istendiğinde kullanılır."
---

# Ek Rapor ve Yeni Bilirkişi Talebi Stratejisi

## Görev
Tespit edilen her kusur için "tamamlama mı, ikame mi" kararını vermek: eksik/belirsizlik ek raporla; yöntem hatası, esaslı çelişki veya tarafsızlık kusuru yeni bilirkişi/heyetle ele alınır (HMK m.281).

## Soğuk başlangıç (intake)
- Kusur eksiklik/belirsizlik mi, yoksa yöntem/tarafsızlık temelli mi?
- Aynı bilirkişi düzeltirse güven verir mi, yoksa yenisi mi gerekli?
- Dosyada birden fazla çelişen rapor var mı (üçüncü heyet ihtiyacı)?
- Talebin yargılamayı uzatma maliyeti kabul edilebilir mi?

## Denetim şeması
1. **Eksiklik/belirsizlik testi (HMK m.281):** Hususlar eksik/belirsizse veya tamamlanması gerekiyorsa, kural olarak aynı bilirkişiden **ek rapor** istenir. Hesap hataları, yanıtsız sorular ve tamamlanabilir veriler bu kapsamdadır.
2. **Yöntem/güven testi:** Kusur yöntemin temelinde veya bilirkişinin objektifliğindeyse (6754 s.K. m.3), tamamlama yetmez; **yeni bilirkişi/heyet** seçimi istenir.
3. **Çelişki yoğunluğu:** Birden fazla rapor esaslı ve giderilemez biçimde çelişiyorsa, çelişkiyi giderecek **yeni/üçüncü heyet** talebi gerekçelendirilir; hâkim raporları serbestçe takdir eder (HMK m.282).
4. **Maliyet-fayda:** Yeni heyet yargılamayı uzatır ve gider doğurur; bu nedenle ikame talebi yalnızca tamamlama yetersizse tercih edilir, gerekçesi güçlü tutulur.
5. **Ara sonuç:** Her kusur "ek rapor / yeni heyet / üçüncü heyet" etiketiyle ve dayanağıyla sınıflandırılır; karma talep (bazı kalemlerde ek rapor, bir kalemde yeni heyet) mümkündür.

## Çıktı modülleri
- Kusur-yol eşleştirme tablosu (ek rapor / yeni heyet / üçüncü heyet + gerekçe).
- Ek rapor için bilirkişiye sorulacak ilave sorular listesi.
- Yeni bilirkişi talebinin gerekçe paragrafı.
- Yargılama süresi ve gider etkisine ilişkin kısa risk notu.

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
