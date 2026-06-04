---
name: yazilim-veritabani-internet
description: "Bilgisayar programı, veri tabanı veya çevrimiçi paylaşılan içerik üzerindeki telif sorunlarını çözmek gerektiğinde; yazılımın eser niteliği, dekompilasyon istisnası, veri tabanı korumasi ve internette umuma iletim/aracı sorumluluğunu değerlendirmek için kullanılır."
---

# Yazılım, Veri Tabanı ve İnternet İçeriği

## Görev
Bilgisayar programları, veri tabanları ve çevrimiçi içerik özelinde telif korumasının kapsamını, özel istisnaları ve internet ihlallerinde sorumluluk zincirini değerlendirmek.

## Soğuk başlangıç (intake)
- Konu yazılım kodu, arayüz, veri tabanı yapısı/içeriği mi yoksa web içeriği mi?
- Kod/içerik kim tarafından, iş ilişkisi içinde mi üretildi?
- İhlal kopyalama, tersine mühendislik, lisans aşımı mı; yoksa internette paylaşım mı?
- Platform/aracı hizmet sağlayıcı mı, içerik sağlayıcı mı sorumlu tutuluyor?

## Denetim şeması
1. Yazılımın eser niteliği: Bilgisayar programları ilim-edebiyat eseri olarak korunur (m.2/1); koruma ifade biçimine (kaynak/amaç kod) yöneliktir, fikir-algoritma-arayüz işlevi olarak korunmaz. Hazırlık tasarımları da kapsama girer.
2. Yazılıma özgü istisnalar (m.38): Yedekleme, hata düzeltme ve birlikte çalışabilirlik için sınırlı dekompilasyon (tersine mühendislik) belirli şartlarla serbesttir; bunların ötesi ihlaldir. Çalışan eserinde mali haklar işverene aittir (m.18/2).
3. Veri tabanı: Eser niteliğindeki (seçme/düzenlemede hususiyet) veri tabanı m.6/11 kapsamında korunur; içerik tek tek korunmasa da derlemedeki yaratıcı seçim korunur. Salt yatırıma dayalı sui generis koruma ile karıştırma.
4. İnternette umuma iletim: İçeriğin çevrimiçi erişime sunulması m.25 kapsamında işaret-ses-görüntü nakli/umuma iletim ve erişilebilir kılma hakkını ilgilendirir; izinsiz yükleme ihlaldir.
5. Aracı sorumluluğu: Yer/erişim/içerik sağlayıcı ayrımı (5651 sayılı Kanun) ile FSEK ihlali birlikte değerlendirilir; uyar-kaldır mekanizması ve aracıya bildirim süreci kontrol edilir. Asıl fail içerik sağlayıcıdır; aracının sorumluluğu bildirim sonrası harekete geçmemeye bağlanır.
6. Ara sonuç: Koruma kapsamı, uygulanan istisna ve sorumlu süje (içerik/aracı) belirlenir.

İspat yükü: kod/içerik benzerliği ve erişimi davacı (genelde bilirkişi/kaynak kod karşılaştırması ile); istisna/lisans savunmasını davalı ispatlar.

## Çıktı modülleri
- Yazılım/veri tabanı koruma kapsamı ve istisna notu.
- İnternet ihlali sorumluluk zinciri (içerik/aracı, uyar-kaldır).
- Kaynak kod karşılaştırması/bilirkişi talep önerisi.

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
