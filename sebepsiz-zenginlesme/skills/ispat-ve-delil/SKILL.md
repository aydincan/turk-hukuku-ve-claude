---
name: ispat-ve-delil
description: "Sebepsiz zenginleşme davasında hangi vakıanın kim tarafından ve hangi delille ispatlanacağını, özellikle haklı sebebin yokluğu ve yanılarak ödeme noktalarında ispat yükünü belirlemek gerektiğinde kullanılır."
---

# İspat ve Delil

## Görev
İade davasında ispat yükünü TMK m.6 ve TBK m.77-79 özel kurallarına göre dağıtmak, senetle ispat zorunluluğunu (HMK m.200 vd.) uygulamak ve delil planı kurmak. Bu kurumda ispat yükünün dağılımı sonucu tayin edicidir.

## Soğuk başlangıç (intake)
- İspatı gereken vakıa ne (kazandırma, zenginleşme miktarı, sebebin yokluğu, yanılgı, iyiniyet)?
- Yazılı dayanak var mı (banka dekontu, makbuz, geçersiz sözleşme metni, e-posta)?
- İade konusunun değeri senetle ispat sınırını aşıyor mu?
- Karşı taraf bağışlama veya geçerli sebep iddia ediyor mu?

## Denetim şeması
1. **Genel yük (TMK m.6).** İade isteyen; (a) kendi malvarlığından/emeğinden bir kayma olduğunu, (b) karşı tarafın zenginleştiğini ve miktarını, (c) bu kaymanın **haklı sebebe dayanmadığını** ispatlar. Sebebin yokluğu (olumsuz vakıa) ispatı, olağan yaşam deneyimi ve karşı tarafın somutlaştırma yüküyle hafifletilir.
2. **Yanılarak ödeme (m.78).** Borçlanmadığını ödeyen, yanılgısını da ispatlar; karşı taraf "bilerek ödedi" diyorsa bunu o ileri sürer ve ispatlar.
3. **İyiniyet ve elden çıkma (m.79).** Zenginleşmenin elden çıktığını ve kendi iyiniyetini iade borçlusu ispatlar (kapsamı daraltan vakıa lehinedir). Kötüniyet/öngörü iddiasını iade alacaklısı ortaya koyar.
4. **Senetle ispat (HMK m.200-201).** Belirlenen parasal sınırı (her yıl güncellenen tutar; `[doğrulanacak]`) aşan hukuki işlemler senetle ispatlanır; senede karşı tanık kural olarak dinlenmez. Bağışlama iddiası gibi savunmalar bu kurala tâbidir.
5. **Delil-vakıa eşlemesi.** Ödeme → dekont/makbuz; geçersiz sözleşme → metin + geçersizlik vakıaları; kullanım yararı/rayiç değer → bilirkişi/keşif; öğrenme tarihi (zamanaşımı) → yazışma/ihtarname. Ticari defterler HMK m.222 ile sahibi lehine/aleyhine delil.
6. **Ara sonuç.** Vakıa-yük-delil matrisi ve eksik delil listesi çıkarılır; gerekirse delil tespiti (HMK m.400) veya bilirkişi talebi planlanır.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu.
- Senetle ispat/istisna değerlendirme notu.
- Bilirkişi/delil tespiti talebi taslağı.

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
