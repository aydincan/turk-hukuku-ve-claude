---
name: uyap-evrak-yonetimi
description: "UYAP üzerinden gelen evrakı, e-tebligatları ve dosya dökümlerini düzenli bir evrak listesine bağlamak, tebliğ tarihlerini ve evrak bütünlüğünü doğrulamak gerektiğinde kullan."
---

# UYAP ve Evrak Yönetimi

## Görev
UYAP'tan gelen evrakı, e-tebligatları ve dosya safahatını numaralı, tarihli ve sayfa referanslı bir evrak listesine dönüştürmek; tebliğ tarihlerini ve evrak bütünlüğünü doğrulayarak süre takvimini beslemek.

## Soğuk başlangıç (intake)
- Elinde UYAP safahat dökümü, e-tebligat kayıtları veya taranmış evrak var mı?
- Hangi evrakın tebliğ tarihi kritik (karar, bilirkişi raporu, dava dilekçesi)?
- Evrak numaralandırılmış/sayfalanmış mı?
- Eksik veya okunaksız belge var mı?

## Denetim şeması
1. Evrak envanteri: her belgeye sıra no, tarih, tür, gönderen/alıcı ve sayfa aralığı ver; safahat dökümüyle eşleştir. Eksik sıra varsa [doldurulacak].
2. Tebliğ doğrulama: e-tebligatta tebliğ tarihi muhatabın elektronik adrese ulaşmasından itibaren beşinci günün sonu sayılır (7201 sayılı Tebligat Kanunu m.7/a); bu tarihi süre takvimine tetikleyici olarak aktar.
3. Bütünlük kontrolü: eki olduğu belirtilen ama dosyada bulunmayan ekler, imzasız/okunaksız sayfalar ayrı not.
4. Süre köprüsü: tebliğ tarihi belirlenen her evrak için tetiklediği süre (cevap, itiraz, kanun yolu) Süre Takvimi becerisine devredilir; çift kayıt önlenir.
5. Ara sonuç: numaralı evrak listesi + doğrulanmış tebliğ tarihleri + eksik/okunaksız liste. Tarihler UYAP kaydından alınır; tahmin edilmez.

## Çıktı modülleri
- Numaralı evrak listesi (no, tarih, tür, taraf, sayfa).
- Tebliğ tarihi doğrulama tablosu.
- Eksik/okunaksız evrak ve eklerin listesi.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
