---
name: verbis-kayit
description: "Veri sorumlusunun VERBİS'e kayıt yükümlülüğü bulunup bulunmadığı, istisnalar ve kayıt içeriği değerlendirilirken; sicil kaydı oluşturulur veya güncellenirken kullanılır."
---

# VERBİS Kayıt ve Sicil Yükümlülüğü

## Görev
KVKK m.16 ve Veri Sorumluları Sicili Hakkında Yönetmelik uyarınca müvekkilin VERBİS kayıt yükümlülüğünü, istisnalarını ve kayıt içeriğini belirlemek; eksik/yanlış kayıttan doğan yaptırım riskini yönetmek.

## Soğuk başlangıç (intake)
1. Veri sorumlusunun yıllık çalışan sayısı ve mali bilanço toplamı nedir?
2. Ana faaliyeti özel nitelikli veri işlemeyi gerektiriyor mu?
3. Yurt dışında yerleşik veri sorumlusu mu (bu halde sayısal eşik aranmaz)?
4. Halihazırda bir VERBİS kaydı var mı, güncel mi?

## Denetim şeması
1. **Yükümlülük ilkesi — m.16/2**: Kişisel veri işleyen gerçek/tüzel kişi veri sorumluları, işlemeye başlamadan önce Sicile kaydolmak zorundadır.
2. **İstisnalar**: Kurul, işlenen verinin niteliği, sayısı, faaliyetin hukuki sebebi ve güvenlik tedbirleri gibi ölçütlerle istisna belirleyebilir. Yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı belirlenen eşiğin altında olan ve ana faaliyeti özel nitelikli veri işleme olmayan veri sorumluları için kayıt istisnası öngörülmüştür (Kurul kararıyla belirlenen güncel eşikler [doğrulanacak — kvkk.gov.tr]).
3. **Kayıt içeriği**: Veri sorumlusu kimliği, irtibat kişisi, işleme amaçları, veri kategorileri, alıcı grupları, yurt dışına aktarım, azami saklama süreleri ve alınan teknik-idari tedbirler. Kayıt, fiili işleme envanteriyle tutarlı olmalıdır.
4. **İrtibat kişisi**: Türkiye'de yerleşik tüzel kişiler için irtibat kişisi atanır; bu kişi temsilci/veri koruma görevlisi değildir, yalnızca Kurul ve ilgili kişilerle iletişimi sağlar.
5. **Ara sonuç**: Kayıt yükümlülüğüne aykırılık m.18/1-ç kapsamında idari para cezası gerektirir; istisna iddiası belgeyle desteklenmelidir.

İspat yükü: İstisnadan yararlandığını veri sorumlusu (çalışan sayısı/bilanço belgeleriyle) ispatlar.

## Çıktı modülleri
- VERBİS yükümlülük/istisna değerlendirme notu.
- Sicile işlenecek envanter özeti tablosu.
- Güncelleme gerektiren değişiklikler kontrol listesi.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
