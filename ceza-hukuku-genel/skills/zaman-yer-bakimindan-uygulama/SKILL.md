---
name: zaman-yer-bakimindan-uygulama
description: "Kanunların zaman bakımından uygulanması (lehe kanun) ile yer bakımından uygulanması (Türkiye'de/yurt dışında işlenen suçlar) sorunlarını çözmek gerektiğinde kullanılır."
---

# Zaman ve Yer Bakımından Uygulama

## Görev
Hangi ceza normunun zaman (lehe kanun) ve yer (mülkilik/şahsilik) bakımından uygulanacağını belirlemek; özellikle suç tarihi ile karar tarihi arasında değişen mevzuatta lehe hükmü saptamak.

## Soğuk başlangıç (intake)
- Suç tarihi ile karar/inceleme tarihi arasında ilgili norm değişti mi?
- Suç Türkiye'de mi, yurt dışında mı işlendi; fail ve mağdurun vatandaşlığı?
- İnfaz rejimini etkileyen bir değişiklik var mı?
- Suç birden çok ülkede mi gerçekleşti (hareket/netice farklı yerlerde mi)?

## Denetim şeması
1. **Kanunilik (m.2):** İşlendiği zaman kanunda suç sayılmayan fiil cezalandırılamaz; aleyhe kıyas ve geriye yürüme yasaktır.
2. **Lehe kanun (m.7/1-2):** Suçun işlendiği ve sonraki zaman dilimlerindeki normlar arasında failin lehine olan uygulanır; kesinleşmiş hükümlerde dahi infazı ve sonuçlarını etkileyen lehe değişiklik gözetilir. Ara sonuç: hangi metin failin lehine?
3. **Karşılaştırma yöntemi:** Lehe tespit soyut değil, somut olaya uygulanan sonuç üzerinden yapılır; karma uygulama yapılmaz, bir bütün olarak lehe olan metin seçilir.
4. **Mülkilik (m.8):** Türkiye'de işlenen suçlarda Türk kanunu uygulanır; hareket veya netice Türkiye'de gerçekleşmişse suç Türkiye'de işlenmiş sayılır.
5. **Yurt dışında işlenen suçlar (m.9-13):** Vatandaş (m.11) ve yabancı (m.12) tarafından işlenen suçlar, koruma ve evrensellik ilkeleri (m.13); yabancı ülkede mahkûmiyetin etkisi ve non bis in idem (m.9).
6. **Cezadan mahsup (m.16):** Yurt dışında gözaltı/tutukluluk/hükümlülük sürelerinin mahsubu.

## Çıktı modülleri
- Lehe kanun karşılaştırma tablosu (eski/yeni metin, somut sonuç).
- Yer bakımından uygulama yetki analizi.
- Mahsup ve non bis in idem notu.
- Eksik bilgi ve `[doğrulanacak]` içtihat ihtiyacı.

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
