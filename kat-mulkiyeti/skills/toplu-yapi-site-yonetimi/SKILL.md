---
name: toplu-yapi-site-yonetimi
description: "Birden çok bağımsız yapıdan oluşan sitelerde blok/ada/toplu yapı kurullarının oluşumu, yetki paylaşımı, ortak gider katılımı ve birden çok yapıyı ilgilendiren kararlar gündeme geldiğinde; KMK m.66-74 toplu yapı rejimini kurmak için kullanılır."
---

# Toplu Yapı (Site) Yönetimi ve Ortak Gider Rejimi

## Görev
Birden çok yapıyı kapsayan toplu yapılarda (siteler) yönetim katmanlarını ve ortak gider paylaşımını doğru kurmak: blok kat malikleri kurulu, blok arası/ada ve toplu yapı kurullarının yetkilerini ayırmak; hangi giderin hangi katmana ait olduğunu belirlemek.

## Soğuk başlangıç (intake)
- Site tek parselde mi yoksa birden çok parsel/ada üzerinde mi; tapuda toplu yapı şerhi var mı?
- Kaç blok/yapı var; her blokun ayrı yöneticisi mi, tek site yönetimi mi?
- Uyuşmazlık tek bloku mu, blok arası ortak yeri mi (yol, sosyal tesis, havuz), yoksa tüm siteyi mi ilgilendiriyor?
- Toplu yapı yönetim planı düzenlenmiş ve tescilli mi?

## Denetim şeması
1. **Toplu yapı kavramı (KMK m.66)**: Toplu yapı, bir veya birden çok imar parseli üzerinde, belli bir onaylı yerleşim planına göre yapılan altyapı tesisleri, ortak kullanım yerleri, sosyal tesis ve hizmetlerle bunların yönetimi bakımından birbiriyle bağlantılı birden çok yapıyı ifade eder.
2. **Yönetim planının kapsamı (m.70)**: Toplu yapı kapsamındaki bütün yapı ve ortak yerler için **tek bir yönetim planı** düzenlenir; bu plan bütün kat maliklerini bağlar ve değiştirilmesi için **beşte dört (4/5)** çoğunluk gerekir.
3. **Yönetim organları (m.69, m.73)**: (a) Her yapı için **blok kat malikleri kurulu**; (b) birden çok yapının ortak yerleri için o yapıların **blok kat malikleri kurullarının** oluşturduğu kurul; (c) bütün siteyi ilgilendiren konular için **toplu yapı temsilciler kurulu** (her blok yöneticisinin/temsilcisinin katıldığı). Her katman kendi yetki alanında karar alır.
4. **Gider paylaşımı (m.72)**: Bir bloka özgü giderler o blok malikleri arasında; birden çok yapının ortak yerine ilişkin giderler ilgili yapı malikleri arasında; bütün siteye ait genel giderler (örn. çevre güvenliği, ana yol, sosyal tesis) yönetim planındaki esaslara göre paylaştırılır. Katılım, KMK m.20 esaslarıyla uyumlu kurulur.
5. **Geçiş ve uyum (Geçici/Ek hükümler)**: Eski "site" düzenlemeleri toplu yapı hükümlerine uyumlaştırılır; mevcut yönetim planları m.66-74'e göre yeniden düzenlenebilir.
6. **Ara sonuç**: Uyuşmazlığın ait olduğu yönetim katmanını ve gider havuzunu belirle; yetkili kurul ve karar nisabını ona göre uygula.

## Çıktı modülleri
- Yönetim katmanı/yetki haritası (blok / ada / toplu yapı kurulu).
- Gider havuzu ve paylaşım tablosu (blok / ortak / genel).
- Toplu yapı yönetim planı uyum/değişiklik (4/5) notu.

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
