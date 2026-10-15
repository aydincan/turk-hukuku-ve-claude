---
name: genel-saglik-sigortasi
description: "GSS kapsamı, tescil, prim borcu, bakmakla yükümlü olunan kişi statüsü ve sağlık yardımlarından yararlanma koşulları söz konusu olduğunda; özellikle GSS borç ve gelir testi uyuşmazlıklarında kullanılır."
---

# Genel Sağlık Sigortası (GSS)

## Görev
Kişinin GSS kapsamını, tescil ve prim yükümlülüğünü, bakmakla yükümlü olunan kişi statüsünü ve sağlık hizmetinden yararlanma hakkını çözümlemek; GSS prim borcuna ilişkin uyuşmazlığı yönetmek.

## Soğuk başlangıç (intake)
- Kişi sigortalı (4/a-b-c) mi, bağımsız GSS'li mi, yoksa bakmakla yükümlü olunan kişi mi?
- GSS prim borcu tebliğ edildi mi; gelir testi yapıldı mı?
- Sağlık hizmetinden yararlanma reddedildi mi (prim borcu/kapsam dışı)?
- Öğrenci, yabancı, vatansız veya uluslararası koruma statüsü var mı?

## Denetim şeması
1. Kapsam — 5510 m.60: GSS'li sayılanlar (sigortalılar, gelir/aylık alanlar, yeşil kart yerine geçen kapsam, ikamet eden yabancılar) belirlenir.
2. Bakmakla yükümlülük — m.3/10 ve m.60: Eş, çocuk ve ana-baba sigortalı üzerinden yararlanma koşulları; bu durumda ayrı GSS tescili gerekmez.
3. Gelir testi — m.60-61: Bağımsız GSS'lide prime esas kazanç, hane içi gelirin asgari ücretin üçte birine göre durumuna göre belirlenir; gelir testi sonucuna SGK'ya itiraz ve dava yolu açıktır.
4. Prim ve borç — m.67 ve m.88: Sağlık yardımından yararlanmada prim borcu olmama koşulu (belirli istisnalar/yapılandırmalar saklı); GSS borçlarında zamanaşımı m.93.
5. Yararlanma — m.67: Müstehaklık koşulları (gün şartı, prim borcu durumu). Ara sonuç: kapsam, borç ve müstehaklık durumu. İspat: SGK tescil/gelir testi kayıtları, hane bilgileri.

## Çıktı modülleri
- GSS kapsam ve statü tespiti.
- Gelir testi sonucuna itiraz/dava değerlendirmesi.
- Prim borcu ve müstehaklık durum notu.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
