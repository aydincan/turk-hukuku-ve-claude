---
name: calisan-bulusu
description: "Bir çalışanın iş ilişkisi sırasında yaptığı buluşun hakkının kime ait olduğu, bildirim, hak talebi ve bedel sorunları gündeme geldiğinde kullanılır; işveren-çalışan dengesi ve şirket içi süreç tasarımı için temel beceridir."
---

# Çalışan Buluşları ve Hizmet Buluşu

## Görev
SMK m.113-120 çerçevesinde hizmet buluşu/serbest buluş ayrımını yapmak, bildirim ve hak talebi sürecini kurmak, çalışana ödenecek bedeli ve uyuşmazlık yolunu belirlemek.

## Soğuk başlangıç (intake)
1. Buluşu yapan kim; iş sözleşmesi/üniversite/kamu görevlisi statüsü ne?
2. Buluş iş yükümlülükleri kapsamında mı, işyeri deneyim/çalışmalarına mı dayanıyor?
3. Çalışan buluşu işverene yazılı bildirdi mi; işveren hak talebinde bulundu mu?
4. Bedel/karşılık konusunda anlaşma veya değerlendirme yapıldı mı?

## Denetim şeması
1. **Niteleme (SMK m.113).** Hizmet buluşu: çalışanın yükümlülüğü gereği gerçekleştirdiği ya da işyerinin deneyim ve çalışmalarına dayanan buluş. Bunun dışındakiler serbest buluştur. Ara sonuç: hizmet mi serbest mi?
2. **Bildirim (SMK m.114).** Çalışan, hizmet buluşunu gecikmeksizin yazılı olarak işverene bildirir; bildirim içeriği yönetmelikte belirlenir. Bildirimin yapılış/eksiklik sonuçlarını kontrol et.
3. **İşverenin hak talebi (SMK m.115).** İşveren tam veya kısmi hak talep edebilir; talep bildirimden itibaren süresinde yapılmazsa buluş serbest buluş niteliği kazanır. Tam hak talebinde buluş üzerindeki haklar işverene geçer.
4. **Bedel (SMK m.115/3 ve ilgili hükümler).** Tam/kısmi hak talebinde çalışana makul bedel ödenir; bedelin belirlenmesinde buluşun ekonomik değeri, çalışanın işteki konumu ve işletmenin payı esas alınır.
5. **Serbest buluş ve yükümlülük (SMK m.117-118).** Çalışan serbest buluşu da işverene bildirmek ve kanunda öngörülen hallerde öncelikli kullanım teklifinde bulunmakla yükümlü olabilir.
6. **Uyuşmazlık.** Bedel ve nitelik uyuşmazlıkları için tahkim/uzlaşma ve dava yolu; üniversite mensubu buluşları için özel rejim (SMK m.121) ayrıca değerlendirilir.

## Çıktı modülleri
- Hizmet/serbest buluş nitelemesi gerekçesi.
- Bildirim ve hak talebi zaman çizelgesi.
- Bedel değerlendirme çerçevesi.
- Sözleşme/iç yönetmelik için süreç ve şablon önerisi.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
