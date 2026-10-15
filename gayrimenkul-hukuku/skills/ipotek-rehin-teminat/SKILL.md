---
name: ipotek-rehin-teminat
description: "Bir taşınmaz kredi/alacak için teminat gösterildiğinde, ipotek kurulurken ya da borç ödenmeyip ipoteğin paraya çevrilmesi veya fekki gerektiğinde; anapara/üst sınır ipoteği, derece ve takip yolu için kullanılır."
---

# İpotek Tesisi, Derecesi ve Paraya Çevrilmesi

## Görev
Taşınmaz teminat ilişkisini kurmak ve yönetmek: ipoteğin geçerli tesisi, kapsamı, derecesi ve borç ödenmediğinde paraya çevrilmesi (icra) yolunu belirlemek; alacak sona erince fek (terkin) talebini değerlendirmek.

## Soğuk başlangıç (intake)
- Teminat altına alınan alacak mevcut ve belirli mi (anapara), yoksa doğacak/değişken mi (cari kredi → üst sınır)?
- İpotek hangi taşınmaz, hangi derecede; önceki/sonraki rehinler var mı?
- Borç muaccel ve ödenmedi mi; talep paraya çevirme mi, fek mi?
- Taşınmaz maliki ile borçlu aynı kişi mi (üçüncü kişi rehni var mı)?

## Denetim şeması
1. **Türler**: Taşınmaz rehni ipotek, ipotekli borç senedi ve irat senedi olarak kurulabilir (TMK m.881); uygulamada ipotek esastır.
2. **Anapara/üst sınır ipoteği (m.851)**: Mevcut ve belirli alacak için anapara ipoteği; doğacak veya tutarı belirsiz alacak için belirli azami meblağ (limit) üzerinden üst sınır ipoteği. Faiz ve giderlerin kapsamı bu ayrıma göre değişir.
3. **Kuruluş**: İpotek, tapu sicil müdürlüğünde resmî senet ve tescille doğar; rehin yükü taşınmazın bütünleyici parça ve eklentilerini de kapsar (m.862).
4. **Sıra/derece (m.870-871)**: Rehinler derece sistemine tabidir; sabit dereceler ilkesi ve boşalan dereceden yararlanma kayda göre belirlenir.
5. **Paraya çevirme**: Borç ödenmezse alacaklı, ipoteğin paraya çevrilmesi yoluyla takip başlatır (İİK m.145 vd.); ipotek bir ilama veya ilam niteliğindeki belgeye dayanıyorsa ilamlı, aksi hâlde ilamsız takip yolu izlenir. Doğrudan mülkiyet edinme (lex commissoria) yasaktır (TMK m.873/2).
6. **Fek/terkin (m.883)**: Alacak son bulunca malik ipoteğin terkinini isteyebilir; alacaklı yanaşmazsa fek davası açılır.
7. **Ara sonuç**: Geçerli kuruluş ve kapsamın tespiti; ihtilafta ya paraya çevirme takibi ya da fek davası.

## Çıktı modülleri
- İpotek tesis/fek talebi ve resmî senet kontrol listesi.
- Anapara/üst sınır ipoteği nitelendirme notu (faiz-gider kapsamı, derece).
- Rehnin paraya çevrilmesi takibine geçiş notu (İİK m.145 vd.).

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
