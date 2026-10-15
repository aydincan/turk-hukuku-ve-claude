---
name: sure-zamanasimi-telekom
description: "BTK dava açma süresi, 5651 erişim engelleme ve içerik kaldırma başvuru-itiraz süreleri, sosyal ağ başvuru yanıt süreleri, abonelik ve idari para cezası zamanaşımı gibi tüm süre hesapları yapılırken kullanılır."
---

# Telekom-Bilişimde Süreler ve Zamanaşımı

## Görev
Bir telekom/internet dosyasındaki tüm süreleri tek tabloda toplamak; hak düşürücü süre, dava/itiraz süresi ve zamanaşımını ayırarak süre kaçırma riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Hangi işlem/olay için süre soruluyor (BTK işlemi, içerik kararı, başvuru yanıtı, alacak, ceza)?
2. Başlangıç tarihi nedir (tebliğ, öğrenme, başvuru, ihlal)?
3. Süreyi durduran/keser bir başvuru/işlem yapıldı mı?
4. Olay tarihindeki yürürlük hali hangisi (5651 ve BTK mevzuatı sık değişir)?

## Denetim şeması
1. **İdari dava süresi**: BTK işlemlerine karşı İYUK m.7 — kural 60 gün; özel kanunda farklı süre varsa o uygulanır. İdari başvuru (İYUK m.11) süreyi durdurur; ret/zımni retle yeniden işler.
2. **5651 içerik süreleri**: Erişim engelleme/içerik çıkarma kararına karşı CMK m.268 itiraz süresi; m.9'da hâkimin karar verme süresi (24 saat) ve kararın yerine getirilme süresi (kural 4 saat); m.9/A'da BTK'nın 4 saat içinde sonuçlandırma rejimi izlenir.
3. **Sosyal ağ başvuru süreleri**: İçerik kaldırma başvurularını yanıtlama süresi (kural 48 saat) ve şeffaflık raporu dönemleri; kaçırılan yanıt yaptırım doğurur, durmaz.
4. **İdari para cezası zamanaşımı**: 5809/5651 özel hükmü öncelikli; genel kabahat rejiminde 5326 s.K. soruşturma/yerine getirme zamanaşımı tamamlayıcıdır.
5. **Sözleşmesel/tüketici zamanaşımı**: Abonelik alacaklarında TBK m.147 (bazı periyodik edimlerde 5 yıl) ve genel m.146 (10 yıl); tüketici işleminde 6502 özel süreleri; haksız fiilde TBK m.72. Faiz ve fatura alacaklarında tür ayrımı yapılır.

Tüm süreler başlangıç tarihi + dayanak madde + hak düşürücü/zamanaşımı ayrımı ile yazılır; tereddütte en kısa süreye göre hareket edilir.

## Çıktı modülleri
- Konsolide süre takvimi tablosu (olay/dayanak/son gün).
- Durma-kesilme notları.
- Kritik süre uyarı listesi (özellikle kısa içerik ve itiraz süreleri).

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
