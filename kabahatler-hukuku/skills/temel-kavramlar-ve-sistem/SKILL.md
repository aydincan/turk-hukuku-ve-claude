---
name: temel-kavramlar-ve-sistem
description: "Kabahat ile suç ayrımını, idari yaptırım türlerini, kanunilik ve 5326 sayılı Kanunun genel-özel kanun ilişkisini netleştirmek; bir yaptırımın hangi rejime tabi olduğunu en baştan doğru saptamak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Önündeki haksızlığın kabahat mi suç mu olduğunu, uygulanan yaptırımın türünü ve hangi kanun rejimine (5326 genel + özel kanun) tabi olduğunu belirleyip doğru yargı yolunu işaret etmek.

## Soğuk başlangıç (intake)
- Yaptırımı hangi idare/merci verdi ve dayanak madde nedir (özel kanun + 5326)?
- Yaptırım idari para cezası mı, idari tedbir mi (ruhsat iptali, mülkiyetin kamuya geçirilmesi, faaliyet durdurma)?
- Karar bir tutanağa mı, idari işleme mi dayanıyor; tebliğ/tefhim tarihi nedir?
- Aynı fiil ayrıca adli soruşturmaya da konu mu (suç-kabahat içtiması)?

## Denetim şeması
1. **Kabahat-suç ayrımı:** Yaptırım idari nitelikteyse (idari para cezası/idari tedbir) kabahat rejimi; adli para cezası/hapis söz konusuysa ceza yargılaması. 5326 m.2 kabahati, m.16 yaptırım türlerini gösterir. Adli sicile işlememe, hapse çevrilememe kabahatin tipik sonuçlarıdır.
2. **Kanunilik süzgeci (5326 m.4):** Kabahatin tanımı ve yaptırımın kanunda veya kanunun açıkça verdiği yetkiye dayanan düzenlemede gösterilmesi gerekir. Salt yönetmelikle ihdas edilen, kanuni dayanağı olmayan yaptırım sakattır.
3. **Genel-özel kanun (5326 m.3):** Özel kanundaki kabahat hükmü esastır; tanım/miktar/usul orada düzenlenmemişse 5326 genel hükümleri uygulanır. Bu ilişki, başvuru yolu ve süreyi de etkiler.
4. **Yaptırım türü ve yetkili merci (5326 m.22-24):** İdari para cezası kural olarak ilgili idarenin yetkili organınca verilir; bazı tedbirler ve haller mahkeme/Cumhuriyet savcısı kararını gerektirir.
5. **Yargı yolu nitelendirmesi:** İdari yaptırım kararına karşı kural olarak **sulh ceza hâkimliği** yetkilidir (5326 m.27). Yaptırım daha geniş bir idari işlemin parçasıysa idari yargı görevli olabilir; ara sonuç olarak yargı yolunu netleştir.

## Çıktı modülleri
- Nitelendirme notu (kabahat mi/suç mu, yaptırım türü).
- Dayanak madde tablosu (özel kanun + 5326 ilgili maddeleri).
- Yargı yolu ve yetkili merci tespiti, başvuru süresi uyarısı.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
