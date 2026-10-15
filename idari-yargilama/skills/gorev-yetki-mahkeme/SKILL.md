---
name: gorev-yetki-mahkeme
description: "Davanın idare mahkemesi, vergi mahkemesi yoksa ilk derece Danıştay'da görüleceğinin ve hangi yer mahkemesinin yetkili olduğunun belirlenmesinde kullanılır; yetki itirazı, gönderme kararı ve Danıştay ilk derece görevleri tartışmalı olduğunda başvurulur."
---

# Görevli ve Yetkili Mahkemenin Belirlenmesi

## Görev
Davanın hangi ilk derece merciinde (idare mahkemesi, vergi mahkemesi veya ilk derece Danıştay) ve hangi yer mahkemesinde açılacağını belirlemek; yetkisizlik/görevsizlik halinde doğru usulü uygulamak.

## Soğuk başlangıç (intake)
- Uyuşmazlık vergi/gümrük/benzeri mali yükümlülükle mi ilgili?
- İşlem bir bakanlık/düzenleyici kurumun ülke geneli düzenleyici işlemi mi?
- İşlemi tesis eden idarenin bulunduğu yer ile işlemin uygulandığı yer neresi?
- Taşınmaza, kamu görevlisine veya tam yargıya ilişkin özel yetki kuralı var mı?

## Denetim şeması
1. **Görev — idare/vergi mahkemesi ayrımı** (2576 sayılı K. m.5-6): Vergi, resim, harç ve benzeri mali yükümlülükler ile bunların zam ve cezalarına ilişkin davalar **vergi mahkemesinde**; bunun dışındaki genel idari uyuşmazlıklar **idare mahkemesinde** görülür.
2. **İlk derece Danıştay görevi** (2575 sayılı K. m.24): Bakanlar Kurulu/Cumhurbaşkanı kararları, bakanlıkların düzenleyici işlemleri (yönetmelik vb.) ve kanunda sayılan ülke düzeyindeki işlemler ilk derece olarak Danıştay'da dava edilir.
3. **Yer yetkisi — genel kural** (İYUK m.32): Aksine hüküm yoksa yetkili mahkeme, dava konusu işlemi yapan **idari merciin bulunduğu yer** mahkemesidir.
4. **Özel yetki kuralları** (İYUK m.33-36): Kamu görevlilerine ilişkin işlemlerde görevlinin son görev yaptığı yer (m.33); taşınmaz mallara ilişkin davalarda taşınmazın bulunduğu yer (m.34); taşınır mallar ve tam yargı davalarında zararı doğuran işlem/eylemin yapıldığı yer veya ilgilinin ikametgâhı (m.35-36) gibi özel kurallar genel kurala önceliklidir.
5. **Görevsizlik/yetkisizlik** (İYUK m.15/1-a, m.43): Görev/yetki yönünden dava reddedilir ve dosya görevli/yetkili mahkemeye gönderilir; aynı yargı kolunda gönderme kararı verilir.
6. **Ara sonuç**: İki ayrı yer mahkemesi arasında yetki uyuşmazlığı çıkarsa bölge idare mahkemesi/Danıştay merci tayini ile çözer.

## Çıktı modülleri
- Görev (idare/vergi/Danıştay) tespiti
- Yetkili yer mahkemesi ve dayanak madde
- Yanlış mahkemeye açılma riski için gönderme senaryosu

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
