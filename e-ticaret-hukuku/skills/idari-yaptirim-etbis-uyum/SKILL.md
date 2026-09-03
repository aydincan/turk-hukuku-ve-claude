---
name: idari-yaptirim-etbis-uyum
description: "6563 kapsamında idari para cezası, ETBİS kayıt yükümlülüğü, ETAHS lisansı veya Ticaret Bakanlığı denetim/yaptırımına ilişkin bir durumun değerlendirilmesi ya da itiraz hazırlanması gerektiğinde kullanılır."
---

# İdari Yaptırım, ETBİS ve Lisans Uyumu

## Görev
6563 sayılı Kanun ve yönetmelikleri kapsamında ETBİS kaydı, ETAHS lisansı ve idari para cezalarına ilişkin uyumu denetlemek; verilen idari yaptırıma karşı itiraz/dava stratejisini kurmak.

## Soğuk başlangıç (intake)
- Müvekkil ETBİS'e kayıtlı mı; faaliyet türü kayıt kapsamında mı?
- Bir idari yaptırım kararı tebliğ edildi mi; dayanağı hangi madde?
- ETAHS ise net işlem hacmi lisans eşiğini aşıyor mu, lisans alındı mı?
- Tebliğ tarihi ve itiraz süresi ne durumda?

## Denetim şeması
1. ETBİS (6563 m.11): hizmet sağlayıcı ve aracı hizmet sağlayıcılar, Bakanlıkça belirlenen kapsamda Elektronik Ticaret Bilgi Sistemi'ne kayıt ve bildirim yapar; kayıtsızlık idari yaptırım sebebidir.
2. Lisans (ETAHS): belirli net işlem hacmi eşiğini aşan elektronik ticaret aracı hizmet sağlayıcılar Bakanlıktan lisans almak ve lisans bedeli ödemekle yükümlüdür; reklam/indirim bütçesi sınırlarına uyulur.
3. İdari para cezaları (6563 m.12): bilgi verme, ticari ileti, ETBİS, aracı yükümlülükleri ve lisans ihlallerine bağlı kademeli idari para cezaları ile faaliyet durdurma/erişim engelleme tedbirleri öngörülür; ceza miktarları her yıl yeniden değerleme oranıyla güncellenir.
4. Yaptırıma karşı yol: idari yaptırım kararının niteliğine göre başvuru mercii belirlenir; idari para cezası niteliğindeki kararlara karşı 2577 sayılı İYUK uyarınca idari yargı yolu (iptal davası) ya da ilgili özel başvuru yolu değerlendirilir; süreler kaçırılmaz.
5. Savunma ekseni: yetki-şekil-sebep-konu-maksat denetimi; tebligat usulü, oransızlık ve maddi hata itirazları.
İspat yükü: yükümlülüğün yerine getirildiğini müvekkil belgelerle ortaya koyar.

## Çıktı modülleri
- ETBİS/lisans uyum kontrol listesi.
- Yaptırım risk ve süre takvimi.
- İtiraz/iptal dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
