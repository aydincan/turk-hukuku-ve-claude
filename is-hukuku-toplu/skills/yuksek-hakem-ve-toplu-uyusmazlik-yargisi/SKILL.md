---
name: yuksek-hakem-ve-toplu-uyusmazlik-yargisi
description: "Grev yasagi veya erteleme hallerinde Yuksek Hakem Kuruluna basvuruyu, kurulun TIS yerine gecen kararini ve toplu hak uyusmazliklarinin yargi yolunu ele alir; YHK sureci veya TIS yorum davasi gerektiginde kullanilir."
---

# Yüksek Hakem Kurulu ve Toplu Uyuşmazlık Yargısı

## Görev
Grevin yasak veya ertelenmiş olduğu menfaat uyuşmazlıklarında Yüksek Hakem Kurulu (YHK) yolunu, kurulun TİS hükmündeki kararını ve toplu hak uyuşmazlıklarının yargısal çözümünü yönetmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık grev yasağı kapsamında mı veya erteleme mi yapıldı?
- Arabuluculuk/erteleme süreci tamamlandı mı?
- Sorun yeni TİS şartı mı (menfaat) yoksa mevcut TİS yorumu mu (hak)?
- Tarafların YHK'ye başvuru iradesi/zorunluluğu var mı?

## Denetim şeması
1. **YHK'ye başvuru halleri:** 6356 m.51 — grev ve lokavtın yasak olduğu uyuşmazlıklarda, arabuluculukta anlaşma sağlanamazsa taraflardan biri YHK'ye başvurur; grevin ertelendiği ve erteleme sonunda anlaşma olmayan hallerde de YHK devreye girer (m.63 yollamasıyla).
2. **Kurulun kararı:** YHK kararı **kesindir ve toplu iş sözleşmesi hükmündedir**; tarafları normatif olarak bağlar. Bu nedenle YHK aşaması fiilen TİS'in içeriğini belirler.
3. **Toplu hak uyuşmazlığı yargısı:** TİS'in yorumu, uygulanması veya ihlalinden doğan uyuşmazlık hak uyuşmazlığıdır → **İş Mahkemesi** görevlidir (7036 sayılı Kanun m.5). Bu davalarda TİS m.36 ışığında normatif/borç doğurucu hüküm ayrımı yapılır.
4. **Yetki itirazı ve diğer davalar:** Yetki tespitine itiraz (6356 m.43), TİS'in tarafı sıfatının tespiti, sendikal tazminat davaları da İş Mahkemesinde görülür; kararlara karşı istinaf (BAM) ve sınırlı temyiz yolu işler.
5. **Ara sonuç:** Menfaat uyuşmazlığı + grev yasağı/erteleme = YHK; mevcut TİS'ten doğan anlaşmazlık = İş Mahkemesi.

İçtihat için karararama.yargitay.gov.tr (9./22. HD, HGK); künyeler `[doğrulanacak]`.

## Çıktı modülleri
- Yol ayrımı şeması (YHK mı, İş Mahkemesi mi).
- YHK başvuru dilekçesi iskeleti.
- TİS yorum davası dava planı (vakıa-hüküm-talep).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
