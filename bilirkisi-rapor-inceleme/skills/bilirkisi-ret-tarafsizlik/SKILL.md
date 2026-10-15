---
name: bilirkisi-ret-tarafsizlik
description: "Bilirkişinin tarafsızlığından şüphe edilen, hâkimin reddi sebeplerine benzer durumların bulunduğu veya bilirkişinin yasak işlerle uğraştığı hâllerde ret talebi ve tarafsızlık itirazı hazırlamak istendiğinde kullanılır."
---

# Bilirkişinin Reddi ve Tarafsızlık Denetimi

## Görev
Bilirkişinin kişisel tarafsızlığını ve bağımsızlığını denetlemek; HMK'nın hâkimin reddine ilişkin sebeplerinin bilirkişiye uygulanması yoluyla (HMK m.272) ret talebi ya da rapora itibar edilmemesi itirazı kurmak.

## Soğuk başlangıç (intake)
- Bilirkişinin taraflarla akrabalık, husumet, menfaat veya iş ilişkisi var mı?
- Bilirkişi daha önce aynı işte taraflardan biri için görüş/danışmanlık vermiş mi?
- Ret sebebi ne zaman ve nasıl öğrenildi (süre yönünden)?
- Tarafsızlık şüphesini somutlaştıran belge/olgu nedir?

## Denetim şeması
1. **Ret rejimine yollama (HMK m.272):** Hâkimin reddini gerektiren sebepler bilirkişi için de ret sebebidir; bilirkişi ayrıca kendisini reddedebilecek sebepleri bildirmekle yükümlüdür. Sebepler HMK m.34-36 ölçütleriyle değerlendirilir.
2. **Tarafsızlık ve etik (6754 s.K. m.3):** Bilirkişi bağımsızlık, tarafsızlık ve objektiflik ilkelerine tabidir; menfaat çatışması veya taraf lehine eğilim ret/itiraz sebebidir.
3. **Süre ve usul:** Ret sebebi öğrenildikten sonra gecikmeksizin, ilgili usul kuralları çerçevesinde ileri sürülür; sebep dilekçede somut olgularla gösterilir (soyut şüphe yetmez).
4. **Yasak işler/devir (HMK m.277):** Görevin başkasına yaptırılması bağımsızlık ihlali olarak ayrıca ileri sürülür.
5. **Ara sonuç:** Ret kabul edilirse yeni bilirkişi atanır; ret süresi geçmiş veya reddi gerektirmeyen ama tarafsızlığı zedeleyen durumda rapora itibar edilmemesi/yeni heyet talep edilir (HMK m.281, m.282).

## Çıktı modülleri
- Ret sebebi-olgu-dayanak eşleştirmesi.
- Ret dilekçesi iskeleti (HMK m.272 atıflı, somut olgularla).
- Süre değerlendirmesi ve sunum yolu notu.
- Alternatif olarak tarafsızlık temelli esasa itiraz paragrafı.

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
