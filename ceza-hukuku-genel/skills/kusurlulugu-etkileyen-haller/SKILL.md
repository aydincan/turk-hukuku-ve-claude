---
name: kusurlulugu-etkileyen-haller
description: "Yaş küçüklüğü, akıl hastalığı, haksız tahrik, cebir-tehdit, zorunluluk ve hata gibi kusurluluğu etkileyen hâlleri ve sonuçlarını değerlendirmek gerektiğinde kullanılır."
---

# Kusurluluğu Kaldıran ve Azaltan Hâller

## Görev
Tipik ve hukuka aykırı bir fiilde failin kusurunun bulunup bulunmadığını; kusuru kaldıran ya da azaltan hâlleri (TCK m.28-34) ve sonuçlarını saptamak.

## Soğuk başlangıç (intake)
- Failin suç tarihindeki yaşı ve akli durumu nedir?
- Faili harekete geçiren haksız bir fiil/provokasyon var mıydı?
- Cebir, tehdit veya karşı konulamaz tehlike etkisi söz konusu muydu?
- Fail fiilin niteliğinde ya da hukuka uygunluk sebebinin şartlarında yanılmış mıydı?

## Denetim şeması
1. **Yaş küçüklüğü (m.31):** 0-12 yaş ceza sorumluluğu yok; 12-15 yaş için algılama/yönlendirme yeteneği araştırılır ve indirilir; 15-18 yaş için indirim uygulanır.
2. **Akıl hastalığı (m.32):** Algılama veya davranışlarını yönlendirme yeteneğini ortadan kaldıran akıl hastalığında ceza verilmez, güvenlik tedbiri uygulanır (m.57); kısmen azaltan hâlde indirimli ceza.
3. **Sağır ve dilsizlik (m.33), geçici nedenler/alkol-uyuşturucu (m.34):** Yaş gruplarına paralel rejim; iradi alınan alkol/uyuşturucunun etkisi kusuru kaldırmaz.
4. **Cebir, şiddet, tehdit (m.28) ve zorunluluk (m.25/2):** Karşı konulamaz cebir/ağır tehdit altında işlenen fiilde kusur bulunmaz; bu hâlde fiili icbar eden fail sayılır. Ara sonuç: irade tümüyle baskı altında mıydı?
5. **Haksız tahrik (m.29):** Haksız bir fiilin doğurduğu hiddet/şiddetli elem etkisiyle işlenen suçta ceza indirilir; tahrikin haksızlığı ve fiille orantısı denetlenir.
6. **Hata (m.30):** Maddi unsurlarda hata kastı kaldırır; hukuka uygunluk sebebinin maddi şartlarında kaçınılmaz hata kusuru kaldırır; haksızlık yanılgısı kaçınılmazsa ceza verilmez. Ara sonuç: hata kaçınılabilir miydi?

## Çıktı modülleri
- Hâl bazlı sonuç tablosu (cezasızlık / indirim / güvenlik tedbiri).
- Rapor ihtiyacı notu (ATK/sağlık kurulu, sosyal inceleme raporu).
- Tahrik/hata için olay-madde altlaması.
- Strateji ve eksik delil listesi.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
