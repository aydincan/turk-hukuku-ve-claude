---
name: kiyas-evleviyet-aksiyle-kanit
description: "İki olayın benzerliği nedeniyle bir kuralın taşınıp taşınmayacağı, ya da kuralın yalnızca metindeki hâlle sınırlı olup olmadığı tartışıldığında mantıksal yorum argümanlarını doğru seçmek için kullanılır."
---

# Kıyas, Evleviyet ve Aksiyle Kanıt

## Görev
Bir hükmün metinde sayılmayan bir olaya uygulanıp uygulanmayacağını, klasik yorum/boşluk doldurma argümanları (analoji, *a fortiori*, *a contrario*) arasından doğrusunu seçerek gerekçelendirmek.

## Soğuk başlangıç (intake)
- Eldeki olay, kuralın düzenlediği olaya hangi yönden benziyor; benzerlik kuralın amacı bakımından mı yoksa yüzeysel mi?
- Kanun bir liste/sayım mı yapıyor (tahdidi mi, tadadi mi)?
- Alan kıyasa açık mı (özel hukuk) yoksa kapalı mı (ceza TCK m.2, vergi, istisna hükümleri, emredici sınırlamalar)?
- Rakip taraf hangi argümanı (a contrario) öne sürüyor?

## Denetim şeması
1. **Kıyas (analoji)** — Şartlar: (i) kanunda doğrudan hüküm yok; (ii) düzenlenen olay ile eldeki olay, kuralın amacı (ratio) bakımından özsel olarak benzer; (iii) farklı muameleyi haklı kılan bir ayrım yok. Sağlanırsa kuralın hukuki sonucu eldeki olaya taşınır. Tek olaya değil, bir ilkeye dayanan kıyas "hukuk kıyası"dır.
2. **Evleviyet (a fortiori)** — *A maiore ad minus*: çok için geçerli olan, evleviyetle az için de geçerlidir (yetki/hak hâlleri). *A minore ad maius*: az için yasak olan, çok için evleviyetle yasaktır (yasak/yük hâlleri). Amaç ölçeği aynı yönde işlemelidir.
3. **Aksiyle kanıt (a contrario)** — Kanun bir hâli düzenleyip diğerini bilinçle dışarıda bıraktıysa, dışarıdakine zıt sonuç bağlanır. Ancak susmanın "bilinçli tercih" mi yoksa "boşluk" mu olduğu önce belirlenmelidir; yanlış a contrario, boşluğu örter.
4. **Çatışma çözümü** — Aynı olayda kıyas ve a contrario ters sonuç verir; tercih, normun amacına (teleolojik) göre yapılır. İstisna ve sınırlayıcı hükümler dar yorumlanır, kural kıyasa kapalıdır (*exceptiones non sunt extendendae*).
5. **Yasak alan kontrolü** — Ceza (TCK m.2), vergi ve idari yaptırımlarda aleyhe kıyas ve kıyasa varan genişletici yorum yasaktır; bu alanda yalnızca lehe/teknik kıyas tartışılabilir.

## Çıktı modülleri
- Benzerlik analizi tablosu (ratio temelli).
- Seçilen argüman + neden diğerinin reddedildiği.
- Yasak alan uyarısı (gerekiyorsa).
- İlkesel içtihat atfı, künye `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
