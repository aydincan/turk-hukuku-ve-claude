---
name: dogal-hukuk-ve-adalet
description: "Geçerli bir normun içeriksel adaletsizliği, hukuk-ahlak ilişkisi veya aşırı haksız kanunun bağlayıcılığı tartışıldığında; klasik doğal hukuk ile Radbruch formülünü Türk hukuk devleti (Anayasa m.2) ve dürüstlük (TMK m.2) zeminine oturtmak için kullanın."
---

# Doğal Hukuk, Adalet ve Radbruch Formülü

## Görev
Pozitif olarak geçerli bir normun içeriksel adaleti/meşruiyeti sorununu işlemek; doğal hukuk
geleneğini ve Radbruch formülünü (katlanılmaz adaletsizlik eşiği) Türk hukuk devleti ilkesi
(Anayasa m.2) ve değer ölçütleriyle (TMK m.2-3) bağlantılandırmak.

## Soğuk başlangıç (intake)
- Tartışılan norm geçerli mi, yoksa geçerliliği mi sorgulanıyor (önce pozitivizm becerisine bak)?
- "Adaletsizlik" iddiası hangi değere dayanıyor (insan onuru, eşitlik, orantılılık)?
- Somut bir uyuşmazlıkta mı, yoksa soyut/akademik düzeyde mi soruluyor?
- Temel hak boyutu var mı (Anayasa m.12 vd., AİHS) — adalet iddiası pozitif hakka çevrilebilir mi?

## Denetim şeması
1. **Adalet türünü ayır.** Aristotelesçi dağıtıcı/denkleştirici adalet ile prosedürel adalet
   ayrımını yap; iddianın hangi adalet türüne dayandığını netleştir. "Adaletsiz" yargısı
   ölçütsüz kalmamalı.
2. **Pozitif değer çıpalarını ara.** İçeriksel adalet çoğu zaman pozitif hukukta zaten
   karşılığını bulur: insan onuru ve hukuk devleti (Anayasa m.2), eşitlik (Anayasa m.10),
   ölçülülük (Anayasa m.13), dürüstlük ve hakkın kötüye kullanılması yasağı (TMK m.2). Önce
   bu pozitif kanalları tüket.
3. **Radbruch eşiğini uygula.** Salt adaletsizlik normu geçersiz kılmaz; ancak adaletsizlik
   "katlanılmaz" boyuta ulaşır ve eşitlik bilinçli olarak inkâr edilirse, kanunun "doğru
   olmayan hukuk" olarak geri çekildiği savunulabilir. Bu istisnai eşiği vurgula; günlük
   uyuşmazlığa taşımaktan kaçın.
4. **Yöntemsel çıkış.** Türk hukukunda mahkeme kanunu kendiliğinden "adaletsiz" diye
   uygulamadan bırakamaz; yolu (a) Anayasaya aykırılık iddiasıyla AYM'ye taşıma (somut norm
   denetimi, Anayasa m.152), (b) anayasaya uygun/temel hakka uygun yorum, (c) TMK m.2 ile
   sonucu düzeltmedir. Ara sonuç: adalet itirazı → pozitif kanal.
5. **Dayanak.** Radbruch, Aquinas, Finnis ve Türk hukuk felsefesi külliyatına atıf;
   sayfa [doğrulanacak]. İçtihat zikredilecekse künye teyidi şarttır, aksi halde [doğrulanacak].

## Çıktı modülleri
- Adalet türü ve ölçüt notu.
- Pozitif değer çıpaları haritası (madde atıflarıyla).
- Radbruch eşiği değerlendirmesi (eşiğin altında/üstünde).
- Yöntemsel çıkış önerisi (AYM / uygun yorum / TMK m.2).

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
