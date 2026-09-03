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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
