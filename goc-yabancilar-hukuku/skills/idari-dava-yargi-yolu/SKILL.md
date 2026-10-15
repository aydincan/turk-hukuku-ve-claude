---
name: idari-dava-yargi-yolu
description: "Göç İdaresi veya Bakanlık işlemine (ikamet ret, sınır dışı, çalışma izni ret, vatandaşlık ret) karşı dava açılacağında; görevli-yetkili mahkemeyi, süreyi ve yürütmenin durdurulmasını saptamak için kullanılır."
---

# İdari Dava ve Yargı Yolu

## Görev
Göç ve yabancılar alanındaki idari işlemlere karşı doğru yargı yolunu, görevli-yetkili mahkemeyi ve süreyi belirlemek; iptal davası ve yürütmenin durdurulması stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem türü nedir (ikamet, sınır dışı, gözetim, çalışma izni, vatandaşlık)?
2. İşlemin tebliğ/öğrenme tarihi nedir?
3. İdari itiraz/komisyon yolu öngörülmüş mü, tüketildi mi?
4. Yabancı gözetim altında mı, yürütmenin acilen durdurulması gerekiyor mu?

## Denetim şeması
1. **Yargı yolu ayrımı**: Çoğu işlem idari yargı (İYUK m.2 iptal davası). İstisna: idari gözetim kararına karşı **sulh ceza hâkimliği** (YUKK m.57/6); ceza irtibatlı (göçmen kaçakçılığı TCK m.79, insan ticareti m.80) konular adli yargı.
2. **Görev ve yetki**: İdare mahkemesi görevli; sınır dışı kararına karşı dava tek hâkimli idare mahkemesinde görülür (YUKK m.53). Yetki, işlemi tesis eden idarenin/yabancının bulunduğu yer üzerinden İYUK m.32-33 ile belirlenir.
3. **Süreler**: Genel iptal davası süresi İYUK m.7 — 60 gün; sınır dışı kararına karşı YUKK m.53'teki özel kısa süre; idari gözetime karşı m.57'deki süre. Süreler işlemden işleme değişir, her dosyada ayrı hesaplanır.
4. **Dava şartları**: İYUK m.2 — ehliyet ve menfaat (yabancı ya da vekili), kesin/yürütülebilir işlem, süre. İdari merci tecavüzü (m.15) ve idari başvuru yolları kontrol edilir.
5. **Yürütmenin durdurulması**: İYUK m.27 — açıkça hukuka aykırılık + telafisi güç/imkânsız zarar; sınır dışıda zaten dava işlemi durdurabilir, çalışma/ikamette YD ayrıca talep edilir.
**Ara sonuç**: Tek bir görevli-yetkili mahkeme, kesin bir son gün ve YD gerekçesi netleştirilir.

## Çıktı modülleri
- Yargı yolu/görev-yetki/süre karar tablosu.
- İptal davası dilekçesi iskeleti (işlem-vakıa-hukuki sebep-YD-talep).
- Süre takvimi ve kanun yolları (istinaf/temyiz) notu.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
