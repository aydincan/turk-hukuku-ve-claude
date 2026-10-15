---
name: ispat-ve-delil
description: "Sosyal güvenlik uyuşmazlığında hangi delilin neyi ispatladığı, SGK kayıtları, bordro, tanık ve bilirkişi raporunun değeri ile re'sen araştırma ilkesinin uygulanması gerektiğinde kullanılır."
---

# İspat ve Delil Yönetimi

## Görev
Uyuşmazlık türüne göre ispat yükünü dağıtmak, mevcut ve getirtilebilecek delilleri değerlendirmek ve delil stratejisini kurmak.

## Soğuk başlangıç (intake)
- İspatlanması gereken vakıa ne (çalışma olgusu, kazanç miktarı, kusur, maluliyet)?
- Elde hangi belgeler var (hizmet dökümü, bordro, işe giriş bildirgesi, sağlık raporu)?
- Tanık var mı; bordro tanığı mı komşu işyeri tanığı mı?
- Bilirkişi/sağlık kurulu raporu gerekiyor mu?

## Denetim şeması
1. İspat yükü — TMK m.6 ve özel kurallar: Kural olarak iddia eden ispatla yükümlü; ancak hizmet tespiti gibi kamu düzenine ilişkin davalarda hâkim re'sen araştırma yapar (HMK genel ilkeleriyle birlikte).
2. Resmi/yazılı delil önceliği: SGK hizmet dökümü, işyeri sicil dosyası, dönem bordroları, işe giriş bildirgesi, müfettiş raporu; bunlar aksi ispatlanana dek güçlü karinedir.
3. Tanık delili: Çalışma olgusunun ispatında bordro tanıkları (aynı dönem aynı işyerinde bildirilmiş kişiler) önceliklidir; salt komşu işyeri tanığıyla sonuç güçlü destekleyici delil gerektirir.
4. Bilirkişi/sağlık kurulu: Kusur oranı, maluliyet derecesi, prim/PEK hesabı bilirkişi ve Kurum sağlık kurulu/ATK raporlarıyla saptanır; rapora itiraz ve ek rapor talebi disiplinli yürütülür.
5. Çelişki yönetimi: Belge ile tanık, raporlar arası çelişkiler işaretlenir; gerekirse yeniden inceleme istenir. Ara sonuç: her vakıa için delil eşleşmesi ve eksik delil listesi.

## Çıktı modülleri
- Vakıa-delil eşleştirme matrisi.
- Getirtilecek belge ve tanık listesi.
- Bilirkişi/sağlık kurulu raporuna itiraz noktaları.

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
