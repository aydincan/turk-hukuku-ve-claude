---
name: sureler-ve-basvuru-yollari
description: "İdari işleme karşı dava açma sürelerini, İYUK m.10-11-13 başvurularını, zımni ret rejimini ve sürelerin hesabını çıkarmak için kullanılır; süre kaçırma riskini önlemek üzere her dosyada erken başvurulur."
---

# Süreler, Zamanaşımı ve İdari Başvuru Yolları

## Görev
Dosyadaki tüm idari süreleri ve başvuru yollarını çıkarıp bir takvime dökmek; zımni ret, dava açma süresi ve durdurucu başvuruları doğru hesaplamak. İdare hukukunda hak kaybının en sık sebebi süredir.

## Soğuk başlangıç (intake)
1. İşlemin tebliğ/ilan/öğrenme tarihi tam olarak nedir?
2. İşlem bireysel mi düzenleyici mi; vergi/genel idari mi?
3. İYUK m.11 (üst makam/işlemi yapan makam) başvurusu yapıldı mı, ne zaman?
4. İdareye bir talep yapıldı ve cevapsız mı kaldı (m.10 zımni ret)?

## Denetim şeması
1. **Genel dava açma süresi.** İYUK m.7: Danıştay ve idare mahkemelerinde **60 gün**, vergi mahkemelerinde **30 gün**; tebliğ/ilan/öğrenme tarihini izleyen günden başlar.
2. **Düzenleyici işlem.** İYUK m.7/4: düzenleyici işleme karşı süresi içinde dava açılabileceği gibi, uygulama işlemiyle birlikte de düzenlemeye karşı dava açılabilir.
3. **İdari başvuru ile durma (m.11).** İşlemin kaldırılması/değiştirilmesi için **üst makama veya işlemi yapan makama** başvuru, dava süresini **durdurur**. İdarenin cevabı üzerine kalan süre işler; 60 gün cevapsızlık talebin reddi sayılır.
4. **Zımni ret (m.10).** İlgililerin idareden bir talebine **60 gün** içinde cevap verilmezse talep reddedilmiş sayılır; dava süresi bu sürenin bitiminden işler. Sonradan gelen cevap dava süresini etkilemez (cevaba göre yeni dava hakkı doğabilir).
5. **Eylemde ön başvuru (m.13).** İdari eylemlerden doğan zararlarda dava açmadan önce idareye başvuru zorunludur; eylemin/zararın öğrenilmesinden itibaren **bir yıl** ve her halde **beş yıl** içinde.
6. **Sürelerin hesabı (m.8).** Süreler tebliğ/ilanı izleyen günden başlar, tatil günleri dâhildir; son gün tatile rastlarsa ilk iş günü sonuna uzar. Çalışmaya ara verme (adli tatil) süreyi uzatabilir (m.61).
7. **Ara sonuç.** Tüm süreler için başlangıç-bitiş tarihli takvim ve hangi başvurunun süreyi durdurduğu.

## Çıktı modülleri
- Süre takvimi tablosu (olay → tarih → son gün).
- Zımni ret / m.11 durma senaryosu hesabı.
- Eylemde m.13 ön başvuru uyarısı.
- Süre riskleri kontrol listesi.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
