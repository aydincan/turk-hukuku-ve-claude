---
name: ceza-sorumlulugu
description: "Eser, icra, fonogram veya yapım üzerindeki hakların ihlalinin suç oluşturup oluşturmadığını ve şikâyet sürecini değerlendirmek gerektiğinde; FSEK m.71-75 suç tiplerini, şikâyet şartını ve savunmayı kurmak için kullanılır."
---

# Telif Hakkı İhlalinde Ceza Sorumluluğu

## Görev
İhlalin FSEK m.71 vd. anlamında suç oluşturup oluşturmadığını belirlemek, şikâyet sürecini ve cezai savunmayı kurmak.

## Soğuk başlangıç (intake)
- İhlal eylemi nedir (izinsiz çoğaltma, yayma, satışa arz, umuma iletim, ad belirtmeme)?
- Eylem ticari boyutta mı; kazanç/yayma var mı?
- Şikâyet süresi (fiilin ve failin öğrenilmesi) işledi mi?
- Hak sahibi/yetkili meslek birliği şikâyetçi mi?

## Denetim şeması
1. Suç tipi (m.71): Manevi, mali veya bağlantılı hakları ihlal eden eylemler — eseri izinsiz işleme/çoğaltma/yayma/temsil/umuma iletim, ad belirtmeme, eseri başkasının eseri gibi gösterme/intihal, korsanla mücadele kapsamı. Eylemin kanuni tarife birebir uyması (kanunilik, TCK m.2) aranır.
2. Manevi unsur: Kasıt aranır (TCK m.21); taksirle ihlal kural olarak cezalandırılmaz. Hata ve kusurluluk değerlendirilir (TCK m.30).
3. Hukuka uygunluk: Hak sahibinin izni, FSEK m.30-40 istisnaları (şahsen kullanma m.38, iktibas m.35, haber m.37) tipikliği veya hukuka aykırılığı kaldırabilir.
4. Şikâyet ve süre (m.75): Bu suçlar kural olarak şikâyete bağlıdır; şikâyet, fiil ve failin öğrenilmesinden itibaren işleyen süreye tabidir (TCK m.73 — altı ay). Yetkili şikâyetçi (hak sahibi/meslek birliği) ve şikâyetin geri alınması sonuçları değerlendirilir.
5. Görev ve uzlaşma: Fikri ve Sınai Haklar Ceza Mahkemesi (yoksa görevlendirilen ağır ceza/asliye ceza) görevlidir (m.76). Şikâyete bağlı suç olması nedeniyle uzlaştırma (CMK m.253) gündeme gelir.
6. Ara sonuç: Suç var/yok, şikâyet geçerliliği, savunma ekseni ve hukuk davasıyla koordinasyon belirlenir.

İspat yükü: ceza yargılamasında suçun ispatı iddia makamında; şüpheden sanık yararlanır. İzin/istisna savunması ileri sürülür ve değerlendirilir.

## Çıktı modülleri
- Suç tipi ve unsur analizi (m.71, kasıt, hukuka uygunluk).
- Şikâyet süresi ve yetkili şikâyetçi kontrolü.
- Şikâyet/şikâyetten vazgeçme veya savunma dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
