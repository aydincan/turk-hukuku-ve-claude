---
name: aidat-ve-ortak-gider
description: "Ortak gider ve avans aidatının belirlenmesi, tahsili, ödemeyen malike karşı icra takibi ve gecikme tazminatı ile işletme projesine itiraz gündeme geldiğinde; gider paylaşım esasları, kanuni ipotek ve takip yolunu kurmak için kullanılır."
---

# Aidat, Ortak Gider ve İşletme Projesi

## Görev
Anagayrimenkulün ortak giderlerine ve işletme avansına katılma borcunu belirlemek; ödemeyen malike karşı tahsil yollarını (icra takibi, dava, kanuni ipotek) kurmak; işletme projesine itirazı değerlendirmek.

## Soğuk başlangıç (intake)
- Talep edilen alacak hangi döneme ait; işletme projesi/bütçe kabul edilmiş mi?
- Gider türü genel ortak gider mi (m.20/b) yoksa kullanıma/arsa payına bağlı özel gider mi?
- Borçlu kat maliki mi, kiracı mı; borçtan müteselsil sorumlu olan kim?
- Gecikme süresi ne kadar; gecikme tazminatı işletilmiş mi?

## Denetim şeması
1. **Katılma borcunun kaynağı (KMK m.20)**: Kat malikleri, aksine sözleşme olmadıkça: (a) kapıcı, kaloriferci, bekçi, bahçıvan ve yönetici giderleri ile yönetim için toplanacak avansa **eşit olarak**; (b) anagayrimenkulün sigortası ve bütün ortak yerlerin bakım, koruma, güçlendirme ve onarım giderlerine **arsa payları oranında** katılır (m.20/1-a,b).
2. **İşletme projesi (m.37)**: Yönetici, bir işletme projesi (tahmini gelir-gider ve her malike düşen pay) hazırlar; karara bağlanır ya da işletme projesi maliklere tebliğ edilir. Tebliğden itibaren **7 gün** içinde itiraz edilmezse proje kesinleşir ve **İİK m.68 anlamında belge** (ilam niteliğinde sayılan belge) hâline gelir.
3. **Temerrüt ve gecikme tazminatı (m.20/2)**: Gider/avans payını ödemeyen malik, gecikilen günler için aylık **yüzde beş (%5)** hesabıyla gecikme tazminatı öder. Bu, sözleşmesel cezadan bağımsız kanuni bir yaptırımdır.
4. **Müteselsil sorumluluk**: Bağımsız bölümün kiracısı/intifa hakkı sahibi de işletme giderlerinden malikle birlikte müteselsilen sorumlu olabilir (m.22/1 — kiracının sorumluluğu kira borcuyla sınırlı). Bağımsız bölümü sonradan iktisap eden, eski malikle birlikte ödenmeyen giderlerden sorumludur (m.22/1).
5. **Kanuni ipotek hakkı (m.22/2)**: Gider/avans payını ödemeyen malikin bağımsız bölümü üzerinde, diğer kat malikleri lehine **kanuni ipotek hakkı** tescil ettirilebilir; yöneticinin de bu yetkisi vardır.
6. **Takip yolu**: Kesinleşmiş işletme projesi/karar defterindeki gider tablosu ile ilamsız icra (İİK m.42 vd.) veya m.68 belgesine dayalı takip; itiraz edilirse itirazın iptali (İİK m.67) ya da kaldırılması (m.68).
7. **Ara sonuç**: Geçerli işletme projesi + gider tablosu → takip; itiraz → itirazın iptali; teminat için kanuni ipotek.

## Çıktı modülleri
- Gider paylaşım hesap tablosu (eşit / arsa payı oranlı; m.20/a-b).
- İcra takip talebi ve %5 gecikme tazminatı hesabı.
- İşletme projesine itiraz veya itirazın iptali dilekçe iskeleti.
- Kanuni ipotek tescili başvuru notu (m.22/2).

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
