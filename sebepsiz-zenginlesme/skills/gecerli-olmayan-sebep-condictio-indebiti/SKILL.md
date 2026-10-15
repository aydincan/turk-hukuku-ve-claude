---
name: gecerli-olmayan-sebep-condictio-indebiti
description: "Borç olmadığı halde veya geçersiz bir sözleşmeye dayanarak yapılan ödeme/edimin geri istenmesi söz konusu olduğunda; hata ile ödeme ve isteyerek ödeme ayrımını çözmek için kullanılır."
---

# Geçerli Olmayan Sebep — Borçlanılmayanın İfası

## Görev
Hiç var olmayan veya geçersiz/iptal edilmiş bir borca dayanarak yapılan edimin iadesini TBK m.77/2 ve m.78 çerçevesinde denetlemek; "yanılarak ödeme" ile "borçlu olmadığını bilerek ödeme" ayrımını netleştirmek, çünkü ikincisi iadeyi kapatır.

## Soğuk başlangıç (intake)
- Ödeme/edim hangi borca dayanıyordu; o borç hiç var mıydı, geçersiz miydi, iptal mi edildi?
- Ödeyen, ödeme anında borçlu olmadığını biliyor muydu, yanılarak mı ödedi?
- Çifte ödeme, fazla ödeme, baştan geçersiz sözleşme gibi tipik bir durum var mı?
- Borç zamanaşımına uğramış mıydı veya ahlaki bir ödev miydi?

## Denetim şeması
1. **Geçersiz/yok borç tespiti.** Sözleşme kesin hükümsüz (TBK m.27), iptal edilmiş (irade sakatlığı m.39), şekil eksik (m.12) veya borç hiç doğmamışsa, ona dayalı ifa sebepsizdir (m.77/2).
2. **Yanılarak ödeme şartı (m.78/1).** Borçlanmadığı şeyi ifa eden, ancak **yanılarak** (borçlu olduğunu sanarak) ödediğini ispat ederse geri isteyebilir. Bu kuruma özgü ek ispat yüküdür.
3. **İsteyerek ödeme engeli (m.78/1).** Ödeyen, ödeme anında borçlu olmadığını **biliyorsa**, ödediğini geri isteyemez (bilinçli ifa bağışlama/ibra gibi yorumlanır). Baskı altında/ihtirazi kayıtla ödeme bu engelin dışındadır.
4. **İstisnalar (m.78/2).** Zamanaşımına uğramış borcun ifası ve ahlaki ödevin yerine getirilmesi geri istenemez; bunlar geçerli sebep sayılır.
5. **İade kapsamı.** Para ise anapara; semere/faiz için zenginleşenin iyiniyeti m.79'a göre belirlenir. Geçersiz sözleşmede karşılıklı ifalar varsa her iki tarafın iadesi birlikte (tasfiye) ele alınır.
6. **İspat ve ara sonuç.** Borcun yokluğunu ve yanılgıyı ödeyen; bilerek ödendiğini iade borçlusu ileri sürer ve ispatlar. Ara sonuç: iade hakkı var/yok + kapsam + faiz başlangıcı.

## Çıktı modülleri
- Geçersizlik + yanılgı altlama notu.
- İade talebi/ihtarname taslağı (ihtirazi kayıt vurgusuyla).
- İsteyerek ödeme engeli risk değerlendirmesi.

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
