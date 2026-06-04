---
name: kisilere-karsi-suclar
description: "Kasten/taksirle yaralama, öldürme, tehdit, şantaj, cebir ve kişiyi hürriyetinden yoksun kılma gibi kişi varlığına yönelik suçların unsurlarını ve nitelikli hallerini denetlemek gerektiğinde kullanılır."
---

# Kişilere Karşı Suçlar (Yaralama, Tehdit, Hürriyet)

## Görev
Hayata, vücut dokunulmazlığına ve hürriyete karşı suçlarda tipiklik unsurlarını, nitelikli halleri ve cezayı etkileyen halleri madde metniyle altlamak.

## Soğuk başlangıç (intake)
- Yaralanma var mı; basit tıbbi müdahaleyle giderilebilir mi, kemik kırığı/çıkığı veya yaşamsal tehlike var mı?
- Fiil kasten mi taksirle mi (trafik, iş kazası vb.) gerçekleşti?
- Tehdit/cebir varsa neyle, hangi içerikle yapıldı; silah kullanıldı mı?
- Mağdur belli bir süre serbestçe hareket edemedi mi?

## Denetim şeması
1. Kasten yaralama (TCK m.86): Hareket + vücutta acı/sağlık bozulması neticesi + kast. Basit tıbbi müdahaleyle giderilebilirse m.86/2 (şikâyete bağlı). Nitelikli haller m.86/3 (silahla, kamu görevlisine karşı, canavarca hisle). Neticesi sebebiyle ağırlaşmış yaralama m.87 (duyu/organ kaybı, kemik kırığı m.87/3, çocuk düşürme, ölüm m.87/4).
2. Taksirle yaralama (TCK m.89): Dikkat-özen yükümlülüğü ihlali, öngörülebilir netice; bilinçli taksir (m.22/3) cezayı artırır. Kural olarak şikâyete bağlı; bilinçli taksir hali şikâyet aranmaz.
3. Kasten öldürme (TCK m.81) ve nitelikli halleri (m.82: tasarlama, canavarca, kan gütme, töre saiki, kamu görevlisine karşı). Ölümle yaralanma sınırı: failin kastının yöne(l)imi ve eylemin elverişliliği (kast-taksir ayrımı m.21-22) belirleyicidir.
4. Tehdit (TCK m.106): Bir kötülüğün gerçekleştirileceğinin bildirilmesi; malvarlığına yönelikse alt sınır farklı. Silahla/birden fazla kişiyle m.106/2 nitelikli. Şantaj m.107, cebir m.108 ile sınırı çiz.
5. Hürriyetten yoksun kılma (TCK m.109): Kişinin hareket serbestisinin hukuka aykırı kısıtlanması; cebir/tehditle, kamu görevlisi tarafından veya cinsel amaçla nitelikli hal. Etkin pişmanlık m.110.
6. Ispat yükü ve ara sonuç: ATK/adli rapor yaralanmanın derecesini belirler; tehditte içerik ve mağdur üzerindeki etki delillendirilmeli. Hangi maddenin hangi fıkrasının uygulanacağını ve şikâyet/uzlaştırma durumunu sonuçlandır.

## Çıktı modülleri
- Unsur altlama tablosu (fiil, netice, manevi unsur, nitelikli hal) madde atıflı.
- Adli rapor değerlendirme notu (yaralanmanın hukuki nitelendirmesi).
- Şikâyet/uzlaştırma ve olası ceza aralığı özeti.

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
