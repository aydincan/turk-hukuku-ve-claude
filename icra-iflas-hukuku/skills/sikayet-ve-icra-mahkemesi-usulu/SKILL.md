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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
