---
name: yeterlik-ve-teklif-degerlendirme
description: "Bir teklifin değerlendirme dışı bırakılması, ihale dışı bırakma veya yeterlik belgelerinin (iş deneyim, mali yeterlik, geçici teminat) eksikliği tartışıldığında başvurulacak değerlendirme denetimi becerisidir."
---

# Yeterlik ve Teklif Değerlendirme

## Görev
Tekliflerin değerlendirilmesinde isteklinin yeterlik kriterlerini sağlayıp sağlamadığını, değerlendirme dışı bırakma veya ihale dışı bırakma kararının hukuka uygunluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Hangi belge eksik/uygunsuz görülerek teklif değerlendirme dışı bırakıldı?
2. Eksiklik bilgi tamamlatma kapsamında mı, yoksa esasa ilişkin mi (m.37)?
3. İş deneyim belgesi, mali yeterlik oranları, geçici teminat uygun mu (m.10, m.33-34)?
4. İhale dışı bırakma sebebi (m.10 son fıkra) somut belgeyle mi dayandırıldı?

## Denetim şeması
1. **Geçici teminat (m.33-34):** Teklif edilen bedelin %3'ünden az olmamak üzere; uygun olmayan/eksik teminat değerlendirme dışı bırakma sebebidir, tamamlatılamaz.
2. **Yeterlik kriterleri (m.10):** Ekonomik-mali yeterlik (banka referansı, bilanço/iş hacmi oranları) ve mesleki-teknik yeterlik (iş deneyim belgesi, kapasite, kalite belgeleri) sağlanmalı. İş deneyim oranları işin türüne göre (yapımda asgari oranlar) kontrol edilir.
3. **İhale dışı bırakma (m.10 son fıkra):** İflas, tasfiye, vergi/SGK borcu, m.17 yasak fiil, ihale tarihinden önceki belirli süre içinde mahkûmiyet gibi durumlar somut belgeyle ortaya konur.
4. **Bilgi/belge tamamlatma (m.37, ilgili Yönetmelik):** Teklifin esasını değiştirmeyen, sunulan belgelerdeki bilgi eksiklikleri tamamlatılabilir; teklif fiyatını veya teklifin esasını etkileyen eksiklik tamamlatılamaz, bu ayrım iptal davalarının düğüm noktasıdır.
5. **Eşit muamele:** Bir istekliye tanınan tamamlatma imkânı diğerine de tanınmalıdır (m.5). Çelişkili uygulama iptal sebebidir.
6. **Ara sonuç:** Karar hukuka aykırıysa kesinleşen ihale kararının bildiriminden itibaren 10 gün içinde şikâyet edilir.

İspat yükü: Yeterliğini iddia eden istekli belgeyi sunmuş olmalı; idare ret sebebini gerekçeli açıklar.

## Çıktı modülleri
- Belge bazlı yeterlik kontrol tablosu.
- Tamamlatılabilir/tamamlatılamaz ayrım analizi.
- Eşit muamele karşılaştırma notu.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
