---
name: basin-ceza-sorumlulugu
description: "Yayın yoluyla hakaret, özel hayatın ihlali, kişisel verilerin yayılması gibi suçlarda ceza sorumluluğu silsilesini, şikâyet ve uzlaştırmayı değerlendirmek gerektiğinde kullanılır."
---

# Basın Yoluyla İşlenen Suçlar ve Ceza Sorumluluğu

## Görev
Yayın içeriğinin TCK suçu oluşturup oluşturmadığını saptamak, 5187 sayılı Kanun m.11 sorumluluk silsilesini uygulamak, şikâyet ve uzlaştırma sürecini yönetmek.

## Soğuk başlangıç (intake)
1. İçerik hangi suçu oluşturabilir (hakaret, özel hayat, veri ihlali)?
2. Mağdur gerçek kişi mi, kamu görevlisi mi; suç görevden mi kaynaklanıyor?
3. Eser sahibi belli mi; sorumlu müdür kim?
4. Yayın tarihi nedir (dava/şikâyet süresi için)?

## Denetim şeması
1. **Suç tipi**: Hakaret TCK m.125 (alenen işlenmesi nitelikli hâl, m.125/IV); kamu görevlisine görevinden dolayı hakaret artırıcı sebep. Özel hayatın gizliliğini ihlal TCK m.134; kişisel verileri hukuka aykırı yayma TCK m.136; haberleşmenin gizliliği m.132.
2. **Hukuka uygunluk**: Haber verme hakkı, eleştiri hakkı ve iddia/savunma dokunulmazlığı değerlendirilir; gerçeklik, kamu yararı, güncellik ve öz-biçim dengesi varsa fiil hukuka uygun olabilir.
3. **Sorumluluk silsilesi (m.11)**: Eser sahibi sorumludur; eser sahibi belli değilse veya yayım sahibinin engellemesiyle yayımlanmışsa sorumlu müdür sorumlu tutulur. Tüzel kişiler için ayrı değerlendirme yapılır.
4. **Şikâyet ve süre**: Hakaret şikâyete bağlıdır; şikâyet süresi fiil ve failin öğrenilmesinden itibaren altı aydır (TCK m.73). Basın Kanunu m.26 dava sürelerini özel olarak düzenler.
5. **Uzlaştırma**: Hakaret uzlaştırmaya tabidir (CMK m.253).
6. **Ara sonuç**: Suçun unsurları + hukuka uygunluğun yokluğu + süresinde şikâyet varsa ceza süreci işletilir.

## Çıktı modülleri
- Suç tipi-unsur altlama tablosu
- Sorumluluk silsilesi şeması
- Şikâyet dilekçesi iskeleti ve süre uyarısı

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
