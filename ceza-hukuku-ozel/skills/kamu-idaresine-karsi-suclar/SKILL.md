---
name: kamu-idaresine-karsi-suclar
description: "Kamu görevlilerinin işlediği zimmet, irtikâp, rüşvet ve görevi kötüye kullanma suçlarının unsurlarını, görevli sıfatını ve etkin pişmanlığı değerlendirmek gerektiğinde kullanılır."
---

# Kamu İdaresine Karşı Suçlar (Zimmet, Rüşvet, Görevi Kötüye Kullanma)

## Görev
Kamu görevlilerinin görevle bağlantılı suçlarında fail sıfatını, fiilin niteliğini ve görevi kötüye kullanma ile özel suçlar arasındaki sınırı madde metniyle belirlemek.

## Soğuk başlangıç (intake)
- Fail kamu görevlisi mi (TCK m.6/1-c anlamında)?
- Fiil zilyetliği görev nedeniyle devredilmiş malın mal edinilmesi mi, menfaat temini mi, görevin gereklerine aykırılık mı?
- Bir menfaat anlaşması (rüşvet) var mı, yoksa görevlinin baskısıyla mağdurdan menfaat mi sağlandı (irtikâp)?
- Bir kamu zararı veya kişilerin mağduriyeti/haksız menfaati doğdu mu?

## Denetim şeması
1. Fail sıfatı: Bu suçlar özgü suçtur; fail kamu görevlisi olmalıdır (TCK m.6). Sıfat yoksa zimmet yerine güveni kötüye kullanma (m.155) gündeme gelebilir.
2. Zimmet (TCK m.247): Görevi nedeniyle zilyetliği devredilen veya koruma ile görevlendirilen malın mal edinilmesi. Suçun açığa çıkmamasını sağlamaya yönelik hileli davranış nitelikli hal (m.247/2). Kullanma zimmeti daha az ceza (m.247/3). Etkin pişmanlıkla iade m.248.
3. İrtikâp (TCK m.250): Görevin sağladığı nüfuzun kötüye kullanılarak kişinin hataya düşürülmesi veya icbar yoluyla menfaat sağlanması/vaadi alınması. İcbar/ikna/hatadan yararlanma biçimlerini ayır.
4. Rüşvet (TCK m.252): Görevin gereklerine aykırı veya uygun bir iş için kamu görevlisi ile iş sahibi arasında menfaat anlaşması; veren ve alan ayrı cezalandırılır. Etkin pişmanlık m.254 (durumu bildirme şartları farklı).
5. Görevi kötüye kullanma (TCK m.257): Tamamlayıcı/ikincil suç. Görevin gereklerine aykırı hareketle kişilerin mağduriyeti, kamu zararı veya haksız menfaat doğması şarttır; daha özel bir suç (zimmet, rüşvet, irtikâp) oluşuyorsa m.257 uygulanmaz.
6. Ara sonuç: Fail sıfatı tespiti + uygulanacak özel suç veya tamamlayıcı m.257 + etkin pişmanlık imkânı + soruşturma izni (4483 sayılı Kanun) gerekip gerekmediği.

## Çıktı modülleri
- Fail sıfatı ve suç tipi belirleme notu (madde atıflı).
- Zimmet/rüşvet/irtikâp/m.257 sınır ayrımı.
- Etkin pişmanlık ve soruşturma izni süreç notu.

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
