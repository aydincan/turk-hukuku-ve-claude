---
name: bilisim-suclari-tck-243-245
description: "Yetkisiz erişim, sistemi engelleme/bozma, veri yok etme/değiştirme veya banka-kredi kartı kötüye kullanımı gibi bir bilişim suçunun unsurlarını ve nitelikli hallerini denetlemek, şikâyet/savunma stratejisi kurmak gerektiğinde kullanılır."
---

# Bilişim Suçları (TCK 243-245)

## Görev
Somut fiili TCK'nın bilişim alanındaki suç tipleriyle altlamak; unsurları, nitelikli halleri, içtimaı ve şikâyet/dava stratejisini belirlemek.

## Soğuk başlangıç (intake)
1. Fiil tam olarak ne? (sisteme girme, kalma, engelleme, veri silme/değiştirme, kart kullanımı?)
2. Yetki var mıydı? (rıza, erişim hakkı, görev sınırı aşıldı mı?)
3. Bir zarar/menfaat doğdu mu? (haksız çıkar, sistemde bozulma, veri kaybı?)
4. Mağdur/şüpheli ve elimizdeki deliller neler?

## Denetim şeması
1. **TCK m.243 — sisteme hukuka aykırı girme.** Bir bilişim sisteminin bütününe veya bir kısmına hukuka aykırı olarak girmek ya da orada kalmaya devam etmek. Temel suç için sistem içindeki verileri ele geçirmek/zarar vermek şart değildir; m.243/2 bedeli karşılığı yararlanılan sistemlerde indirim, m.243/3 verilerin yok olması/değişmesi halinde ağırlaştırma, m.243/4 sistem içeriği bedelsiz yararlanılabilen sistemler için özel hüküm öngörür.
2. **TCK m.244 — engelleme, bozma, verileri yok etme/değiştirme.** Sistemin işleyişini engelleme/bozma (f.1) ile verileri bozma, yok etme, değiştirme, erişilmez kılma, sisteme veri yerleştirme veya var olanı başka yere gönderme (f.2). Banka, kredi kurumu veya kamu kurumu aleyhine işlenmesi ağırlaştırıcıdır (f.3). Fiil başka suç oluşturmuyorsa bu maddeler uygulanır (tali norm karakteri).
3. **TCK m.245 — banka/kredi kartının kötüye kullanılması.** Başkasına ait kartı ele geçirip/elde bulundurup kullanma (f.1), sahte kart üretme/satma/kabul etme (f.2), sahte kartla yarar sağlama (f.3). m.245/A yasak cihaz/program bulundurma. Etkin pişmanlık ve şikâyete bağlılık halleri (akrabalar arası) gözetilir.
4. **İspat ve içtima.** Kast aranır; taksirle işlenemez. Aynı fiil dolandırıcılık (m.158/1-f) veya kişisel verilere ilişkin suçları (m.135-140) da oluşturabilir; gerçek/görünüşte içtima ayrımı yapılır. İspat yükü iddia makamındadır; failin kimliği IP, log ve adli bilişim raporuyla bağlanır.
5. **Ara sonuç.** Hangi madde(ler), nitelikli hal, içtima ilişkisi ve soruşturma/savunma ekseni netleştirilir.

## Çıktı modülleri
- Suç vasfı analizi (madde-fıkra, unsur tablosu, nitelikli haller).
- Şikâyet dilekçesi / savunma iskeleti.
- Delil-fiil bağlama notu ve içtima değerlendirmesi.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
