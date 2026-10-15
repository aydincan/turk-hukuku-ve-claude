---
name: idari-basvuru-ve-merci-tecavuzu
description: "Dava öncesi üst makama başvuru, zorunlu idari başvuru yolları, zımni ret kavramı ve idari merci tecavüzü değerlendirilirken kullanılır; bir işleme doğrudan dava açılabilir mi yoksa önce idareye başvurulmalı mı sorusunda başvurulur."
---

# İdari Başvuru, Zımni Ret ve Merci Tecavüzü

## Görev
Dava açılmadan önce idareye başvurunun zorunlu mu ihtiyari mi olduğunu, zımni ret sürelerini ve merci tecavüzünün sonuçlarını belirleyerek davanın usulden reddini önlemek.

## Soğuk başlangıç (intake)
- İlgili mevzuat, dava öncesi zorunlu bir idari başvuru (itiraz) öngörüyor mu?
- İlgili idareye yapılmış bir başvuru var mı; başvuru tarihi ve cevap durumu?
- İdare hiç cevap vermedi mi (zımni ret) yoksa açık ret mi verdi?
- Başvuru dava açma süresi içinde mi yapıldı?

## Denetim şeması
1. **İhtiyari başvuru ve sürenin durması** (İYUK m.11): İlgililer dava açma süresi içinde, işlemi yapan veya üst makama başvurarak işlemin kaldırılması/geri alınması/değiştirilmesini isteyebilir. Bu başvuru işlemeye başlamış dava süresini **durdurur**.
2. **Zımni ret** (İYUK m.10): İlgililerin idareye yaptıkları başvurulara **60 gün** içinde cevap verilmezse istek reddedilmiş (zımni ret) sayılır; bu sürenin bitiminden itibaren dava açma süresi işler. İdare 60 gün geçtikten sonra cevap verirse, cevap tarihinden itibaren dava süresi yeniden işlemeye başlar.
3. **m.11 zımni reddi**: m.11 başvurusuna 30 gün (özel kanunda farklı süre yoksa) içinde cevap verilmezse istek reddedilmiş sayılır ve durmuş olan dava süresi kaldığı yerden işlemeye devam eder.
4. **Zorunlu idari başvuru / merci tecavüzü** (İYUK m.15/1-e): Mevzuat dava açmadan önce tüketilmesi zorunlu bir başvuru yolu öngörmüşse (ör. bazı vergi/gümrük itirazları, kamu ihalesinde KİK'e itirazen şikâyet), bu yol tüketilmeden açılan dava **merci tecavüzü** nedeniyle reddedilir ve dilekçe ilgili mercie tevdi olunur.
5. **İspat yükü**: Başvuru ve tebliğ tarihlerini ispat ilgilidedir; başvurunun kayıtlı/iadeli yapılması önerilir.
6. **Ara sonuç**: Başvurunun ihtiyari mi zorunlu mu olduğu ayrımı, hem süre hesabını hem de merci tecavüzü riskini doğrudan etkiler; tereddütte zorunlu yol varsayımıyla hareket güvenlidir.

## Çıktı modülleri
- Başvuru türü (ihtiyari/zorunlu) tespiti
- Zımni ret ve süre etkisi hesabı
- Merci tecavüzü riski ve gerekli başvuru taslağı

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
