---
name: lisanssiz-uretim-oztuketim
description: "Çatı GES, kendi tüketimini karşılayan tesisler, mahsuplaşma ve lisanssız üretim eşikleri ile bağlantı başvuruları söz konusu olduğunda ve lisanssız üretim uyuşmazlıklarında kullanılır."
---

# Lisanssız Üretim ve Öz Tüketim

## Görev
Lisans almaksızın üretim yapma rejiminin (özellikle çatı/cephe GES ve öz tüketim) koşullarını, başvuru sürecini ve mahsuplaşma/ihtiyaç fazlası satış esaslarını denetlemek.

## Soğuk başlangıç (intake)
1. Tesis tipi ve kurulu güç; tüketim tesisiyle ilişkisi nedir?
2. Başvuru ilgili şebeke işletmecisine (dağıtım/OSB) yapıldı mı?
3. Üretim, tüketimi karşılamaya mı yönelik, ihtiyaç fazlası satış var mı?
4. Bağlantı görüşü/çağrı mektubu alındı mı?

## Denetim şeması
1. **Rejim ve eşik**: 6446 m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği — lisans ve şirket kurma muafiyeti kapsamı ve güç sınırları. Ara sonuç: faaliyet lisanssız rejime giriyor mu.
2. **Tüketim bağı**: Öz tüketim esası; üretim tesisinin bir tüketim tesisiyle ilişkilendirilmesi ve aynı dağıtım bölgesi/ölçüm noktası koşulları. Bağ kurulamıyorsa rejim dışı kalınır.
3. **Başvuru ve bağlantı**: Şebeke işletmecisine başvuru, teknik değerlendirme, bağlantı görüşü ve çağrı mektubu; kapasite tahsisi sınırlı olduğundan ret gerekçeleri (trafo/fider kapasitesi) teknik veriyle sınanır.
4. **Mahsuplaşma ve ihtiyaç fazlası**: Aylık mahsuplaşma esasları ve ihtiyaç fazlası enerjinin görevli tedarik şirketince satın alınması; bedel ve süre yönetmelik/ilgili dönem tarifesine göre belirlenir (tarih kilidi).
5. **İhlal sonuçları**: Lisanssız sınırın aşılması veya öz tüketim koşulunun kaybı lisanslı faaliyet sayılarak yaptırım riski doğurur.

Şebeke işletmecisinin ret işlemine karşı önce idari başvuru/şikâyet, ardından duruma göre adli veya idari yargı yolu değerlendirilir.

## Çıktı modülleri
- Lisanssız uygunluk ve eşik kontrol notu.
- Bağlantı başvuru/itiraz dilekçesi taslağı.
- Mahsuplaşma ve ihtiyaç fazlası satış hesap özeti.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
