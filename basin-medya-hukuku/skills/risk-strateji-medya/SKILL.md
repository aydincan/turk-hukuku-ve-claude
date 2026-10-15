---
name: risk-strateji-medya
description: "Yayın öncesi hukuki risk denetimi, müvekkilin medya kuruluşu veya mağdur olmasına göre strateji ve müzakere-sulh seçeneklerini değerlendirmek gerektiğinde kullanılır."
---

# Risk Yönetimi ve Strateji

## Görev
Yayın öncesi/sonrası hukuki riski haritalamak, müvekkilin konumuna (yayıncı/mağdur) göre strateji belirlemek, sulh ve müzakere ile dava arasında seçim yapmak.

## Soğuk başlangıç (intake)
1. Müvekkil yayıncı/medya kuruluşu mu, mağdur mu?
2. Yayın henüz yapılmadı mı (önleyici denetim), yapıldı mı (zarar yönetimi)?
3. Hedef: itibar onarımı, tazminat, içeriğin kaldırılması, yargısal zafer?
4. Kamuoyu/medya etkisi (Streisand etkisi) riski var mı?

## Denetim şeması
1. **Yayıncı tarafı (önleyici)**: Yayın öncesi gerçeklik, kaynak güvenilirliği, kamu yararı, öz-biçim dengesi ve KVKK uyumu denetlenir. Riskli ifadeler için değer yargısı/maddi vakıa ayrımı netleştirilir, hukuka uygunluk dayanağı belgelenir.
2. **Mağdur tarafı**: Yol kombinasyonu seçilir (cevap-düzeltme + içerik kaldırma + tazminat + ceza şikâyeti). Hızlı sonuç için 5651 m.9 ve cevap-düzeltme; tatmin için tazminat önceliklenir.
3. **Sulh-müzakere**: Özür/düzeltme yayımı, içeriğin çıkarılması ve makul tazminatla erken çözüm değerlendirilir; özellikle Streisand etkisi riskinde dava maliyeti tartılır.
4. **Maliyet-fayda**: Yargılama süresi, ispat zorluğu, tazminat takdir aralığı ve itibar etkisi birlikte değerlendirilir.
5. **Ara sonuç**: Konuma göre öncelikli yol ve yedek plan belirlenir; süre disiplini korunur.

## Çıktı modülleri
- Risk haritası (olasılık/etki)
- Yayıncı için yayın öncesi kontrol listesi
- Strateji seçenekleri ve sulh-müzakere notu

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
