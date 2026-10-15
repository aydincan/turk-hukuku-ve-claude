---
name: delil-ve-delil-yasaklari
description: "Delillerin toplanması, vicdani değerlendirme ilkesi, hukuka aykırı delil yasağı ve şüpheden sanık yararlanır ilkesi çerçevesinde ispat analizi yapılırken kullanılır."
---

# Delil, İspat ve Delil Yasakları

## Görev
Dosyadaki delilleri elde ediliş ve değerlendirme yönünden tasnif etmek; hukuka aykırı delilleri ayıklamak; ispat gücünü ve şüphe dengesini ortaya koymak.

## Soğuk başlangıç (intake)
- Hangi delil türleri var (beyan, belge, bilirkişi, keşif, dijital, gizli tanık)?
- Her delil hangi usulle elde edildi; karar/onay var mı?
- İddianın dayandığı çekirdek delil hangisi?
- Lehe deliller toplandı/değerlendirildi mi?
- Çelişen deliller arasında nasıl bir denge var?

## Denetim şeması
1. **Serbest delil ve ilke.** Ceza muhakemesinde deliller serbestçe ileri sürülür ve hâkim vicdani kanaatiyle değerlendirir (CMK m.217/1). Ancak bu serbesti hukuka aykırı delille sınırlanır.
2. **Hukuka aykırı delil yasağı.** Yüklenen suç ancak hukuka uygun şekilde elde edilmiş delillerle ispat edilebilir (m.217/2); hukuka aykırı deliller reddolunur (m.206/2-a). Anayasa m.38/6 ve adil yargılanma (Anayasa m.36) bu yasağın temelidir.
3. **Delil tartışması.** Mahkeme, ortaya konulan her delili tartışır; reddedilen delil için gerekçe gösterir (m.206, m.217). Beyan delilinde teyit edici yan delil aranır.
4. **Şüpheden sanık yararlanır.** Mahkûmiyet, kuşkuya yer bırakmayan kesin ve inandırıcı delile dayanmalıdır; giderilemeyen şüphe sanık lehine yorumlanır (in dubio pro reo; Anayasa m.38, m.223/2 uygulaması).
5. **Özel delil tipleri.** Bilirkişi raporu denetlenir (HMK atfı ve CMK m.62 vd.); gizli tanık/koruma altına alınan tanık beyanı tek başına hükme esas alınamaz; dijital delilde bütünlük/zincir denetlenir.
6. **Ara sonuç.** Hukuka aykırı deliller dışlandıktan sonra kalan delil yeterli mi; değilse beraat/CYOK; yeterliyse nitelendirme ve ceza tayini aşamasına geçilir.

## Çıktı modülleri
- Delil envanteri ve hukuka uygunluk/dışlama notu.
- İspat dengesi analizi (lehe/aleyhe, çekirdek delil).
- Delil reddi/dışlama talebi gerekçesi.
- Bilirkişi/dijital delile itiraz noktaları listesi.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
