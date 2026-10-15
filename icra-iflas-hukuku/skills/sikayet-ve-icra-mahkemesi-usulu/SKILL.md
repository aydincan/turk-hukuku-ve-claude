---
name: sikayet-ve-icra-mahkemesi-usulu
description: "İcra dairesinin işlemlerine karşı kanuna aykırılık veya hadiseye uygunsuzluk nedeniyle icra mahkemesine şikâyet etmek; süreli-süresiz şikâyet ayrımını ve icra memuru muamelelerini denetlemek gerektiğinde kullanılır."
---

# Şikâyet ve İcra Mahkemesi Usulü

## Görev
İcra/iflas dairesinin işlemlerine karşı şikâyet yolunu (m.16-18) doğru kullanmak; itiraz ile şikâyeti ayırmak; süreli ve süresiz şikâyet hallerini ve icra mahkemesinin inceleme usulünü yönetmek.

## Soğuk başlangıç (intake)
- Şikâyet konusu işlem ne; kanuna mı aykırı, hadiseye mi uygunsuz?
- İşlem öğrenildi/tebliğ edildi mi (7 günlük süre)?
- İddia kamu düzeniyle mi ilgili (süresiz şikâyet)?
- İşlem itiraz konusu mu, yoksa şikâyet konusu mu?

## Denetim şeması
1. **İtiraz/şikâyet ayrımı**: Borca/imzaya itiraz alacağın esasına yöneliktir ve icra dairesine/icra mahkemesine yapılır; şikâyet ise dairenin **işleminin** kanuna/usule aykırılığına yöneliktir (m.16).
2. **Süreli şikâyet (m.16/I)**: İşlemin öğrenilmesinden itibaren 7 gün içinde icra mahkemesine yapılır.
3. **Süresiz şikâyet (m.16/II)**: Bir hakkın yerine getirilmemesi/sebepsiz sürüncemede bırakılması ve kamu düzenine aykırı işlemler (ör. kambiyo vasfı eksikliği, haczedilmezlik gibi kamu düzeni ilgili haller) süreye bağlı olmaksızın şikâyet edilebilir.
4. **İnceleme usulü (m.18)**: İcra mahkemesi kural olarak basit yargılama usulüyle, çoğu kez evrak üzerinden ve duruşmasız inceler; aksi belirtilmedikçe taraflar çağrılmaz.
5. **Sonuç**: Şikâyet kabul edilirse işlem iptal/düzeltme/yapılması yönünde karar verilir (m.17); karar kanun yoluna (istinaf) tabi olabilir.
6. **Ara sonuç**: Doğru yol (itiraz mı şikâyet mi), süre durumu ve beklenen karar belirlenir.

## Çıktı modülleri
- İtiraz/şikâyet ayrım notu.
- Şikâyet dilekçesi taslağı (süreli/süresiz dayanağıyla).
- İnceleme usulü ve kanun yolu öngörüsü.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
