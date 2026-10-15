---
name: tasinir-rehni-ticari-islem
description: "Taşınır mal, alacak veya işletme varlığının teminat gösterilmesi söz konusu olduğunda; klasik teslime bağlı taşınır rehni ile 6750 sayılı Kanun kapsamında teslimsiz (sicil) rehin ayrımı ve paraya çevirme için kullanılır."
---

# Taşınır Rehni ve Ticari İşlemlerde Taşınır Rehni

## Görev
Taşınır teminat yapılarını kurmak: TMK'daki teslime bağlı taşınır rehni ile 6750 sayılı Ticari İşlemlerde Taşınır Rehni Kanunu kapsamındaki teslimsiz (sicile tescilli) rehni ayırmak; hapis hakkı ve alacak rehnini değerlendirmek.

## Soğuk başlangıç (intake)
- Rehnedilecek değer ne: somut taşınır mal mı, alacak mı, ticari işletme/stok mu?
- Taraflar tacir/esnaf gibi 6750 kapsamına giren kişiler mi?
- Rehinli malın zilyetliği alacaklıya devredilecek mi, yoksa borçluda mı kalacak?
- Borç ödenmediğinde hızlı paraya çevirme isteniyor mu?

## Denetim şeması
1. **Klasik taşınır rehni (TMK m.939 vd.)**: Kural teslime bağlı rehindir; rehin, malın zilyetliğinin alacaklıya (veya üçüncü kişiye) devriyle doğar (m.939). Borçluda kalan teslimsiz rehin geçersizdir (m.939/2).
2. **Alacak ve hak rehni (m.954 vd.)**: Devredilebilen alacak ve haklar rehnedilebilir; senede bağlı alacaklarda senedin teslimi/ciro gerekir.
3. **6750 sayılı Kanun (ticari işlemlerde taşınır rehni)**: Tacir/esnaf vb. arasında, mülkiyeti devretmeden ve teslim olmaksızın taşınır varlıklar (makine, stok, alacak, ticari işletme) Rehinli Taşınır Sicili'ne tescille rehnedilebilir. Aleniyet sicil tescili ile sağlanır.
4. **Lex commissoria yasağı**: Borç ödenmezse alacaklının rehinli malın mülkiyetini doğrudan edinmesini öngören anlaşma kural olarak geçersizdir (m.949 mantığı; 6750'de de sınırlı istisnalarla).
5. **Hapis hakkı (m.950-953)**: Alacaklı, zilyetliğindeki taşınırı, alacağı ile bağlantılı olmak koşuluyla borç ödenene dek alıkoyabilir ve gereğinde paraya çevirebilir.
6. **Paraya çevirme**: Klasik rehinde İİK m.145 vd. (rehnin paraya çevrilmesi); 6750 rehninde Kanun'un öngördüğü usule göre.
7. **Ara sonuç**: Doğru rehin tipi seçimi (teslimli/teslimsiz), aleniyetin sağlanması ve paraya çevirme yolunun belirlenmesi.

## Çıktı modülleri
- Rehin sözleşmesi/tescil başvurusu iskeleti (teslimli veya 6750 sicil).
- Rehin tipi seçim tablosu (zilyetlik, taraf sıfatı, aleniyet).
- Paraya çevirme/icra yolu notu.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
