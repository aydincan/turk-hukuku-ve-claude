---
name: ispat-delil-medya
description: "Basın-medya davalarında yayın içeriğinin tespiti, dijital delilin toplanması ve korunması, gerçeklik ve kamu yararının ispatı söz konusu olduğunda kullanılır."
---

# İspat ve Delil (Medya Uyuşmazlıkları)

## Görev
Yayın içeriğini güvenilir biçimde tespit ve sabitlemek, dijital delili kaybolmadan toplamak, ispat yükünü doğru dağıtmak ve gerçeklik/kamu yararı savunmasını delillendirmek.

## Soğuk başlangıç (intake)
1. İhlal eden içerik hâlâ erişilebilir mi; kaybolma riski var mı?
2. İçeriğin yayın tarihi ve değişiklik geçmişi belgelenebilir mi?
3. İddianın gerçekliğini destekleyen kaynak/belge var mı?
4. Tanık, ekran görüntüsü, noter tespiti mevcut mu?

## Denetim şeması
1. **İçeriğin sabitlenmesi**: Online içerik için ekran görüntüsü yeterli olmayabilir; noter tespiti, web arşivi (arşiv hizmeti) ve HMK m.400 vd. delil tespiti yoluna başvurulur. İçeriğin silinme riski varsa acil delil tespiti istenir.
2. **Dijital delil**: Bütünlük ve değişmezlik için meta veriler, URL, tarih damgası korunur; mümkünse adli bilişim raporu alınır.
3. **İspat yükü dağılımı (TMK m.6)**: Davacı saldırıyı ve zararı; davalı hukuka uygunluk sebebini (gerçeklik, kamu yararı, rıza) ispatlar. Değer yargısında yeterli olgusal temelin varlığı yayıncıdan beklenir.
4. **Gerçekliğin ispatı**: Maddi vakıa iddiasında, yayıncı görünür gerçeklik ve özen ölçütünü karşıladığını belgeyle ortaya koyar.
5. **Bilirkişi**: Teknik içerik, dijital delil veya zarar hesabı için bilirkişi incelemesi (HMK m.266) gerekebilir.
6. **Ara sonuç**: Deliller güvenli biçimde sabitlenmiş ve ispat yükü doğru dağıtılmışsa davada konum sağlamlaşır.

## Çıktı modülleri
- Delil sabitleme kontrol listesi (noter/arşiv/adli bilişim)
- İspat yükü dağılım tablosu
- Delil tespiti talebi dilekçesi iskeleti

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
