---
name: ispat-delil-bilirkisi
description: "Tıbbi uyuşmazlıkta ispat yükünün dağılımını, hangi delillerin toplanacağını ve ATK/bilirkişi raporlarının nasıl denetleneceğini belirlemek için kullanılır."
---

# İspat, Delil ve Bilirkişi/ATK Raporu

## Görev
İspat yükünün taraflar arasında dağılımını saptamak, dosyaya kazandırılacak delilleri planlamak ve bilirkişi/ATK raporunu metodolojik olarak denetlemek.

## Soğuk başlangıç (intake)
1. Tartışmalı vakıa kusur mu, illiyet mi, aydınlatma mı, zarar miktarı mı?
2. Tıbbi kayıtlar (epikriz, ameliyat notu, onam formu, tetkikler) tam mı?
3. Dosyada hangi raporlar var (ATK, üniversite, özel bilirkişi)?
4. Tanık (ekip, refakatçi) ve uzmanlık dalı belli mi?

## Denetim şeması
1. **İspat yükü dağılımı**: Genel kural TMK m.6 — iddia eden ispatla yükümlüdür. Davacı kusur, illiyet ve zararı; hekim/hastane ise aydınlatma ve onamın varlığını ispatlar. Sözleşmesel sorumlulukta kusursuzluk ispatı borçludadır (TBK m.112).
2. **Delil toplama**: Tıbbi kayıtların eksiksiz celbi (HMK m.219-220 belge ibrazı), tedavi gören kurum dosyası, onam belgeleri, görüntüleme/laboratuvar verileri, tanık.
3. **Bilirkişi/ATK**: HMK m.266 vd. uyarınca özel/teknik bilgi gerektiren konularda bilirkişiye başvuru; sağlık uyuşmazlıklarında ATK İhtisas Kurulları sık başvurulur. Hâkim raporla bağlı değildir.
4. **Rapor denetimi**: Görevlendirme kapsamına uygunluk, dayanak vakıaların doğruluğu, metodolojinin açıklığı, sonuç-gerekçe tutarlılığı, çelişki ve maddi hata kontrolü.
5. **İtiraz / ek rapor**: Çelişki veya eksiklik varsa gerekçeli itiraz, ek rapor, üniversiteden veya farklı kuruldan yeni rapor talebi (HMK m.281).
6. **Ara sonuç**: Belirleyici teknik sorun raporla çözülür; rapor yetersizse hüküm bozma sebebidir.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa bazlı)
- Delil toplama ve celp listesi
- Bilirkişi/ATK rapor denetim kontrol listesi
- Gerekçeli rapor itiraz taslağı (yer tutuculu)

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
