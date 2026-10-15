---
name: risk-ve-uyum-stratejisi
description: "İhraççı, yönetici veya yatırım kuruluşu için sermaye piyasası mevzuatına uyum, yaptırım/cezai risk haritası, içsel bilgi yönetimi ve önleyici politika tasarımı gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Uyum Stratejisi

## Görev
İhraççı/yönetici/yatırım kuruluşu için sermaye piyasası risklerini haritalamak; idari ve cezai sorumluluk olasılıklarını tartmak; önleyici uyum politikaları önermek.

## Soğuk başlangıç (intake)
- Müvekkil kim: ihraççı, yönetim kurulu üyesi, yatırım kuruluşu, ortak mı?
- Risk konusu: kamuyu aydınlatma, içsel bilgi yönetimi, çağrı, ilişkili taraf işlemleri mi?
- Geçmişte Kurul incelemesi/yaptırımı veya devam eden işlem var mı?
- Amaç önleyici uyum mu, devam eden bir riske müdahale mi?

## Denetim şeması
1. **Risk envanteri:** Faaliyet türüne göre yükümlülükler listelenir: özel durum açıklamaları (SPK m.15), finansal raporlama (m.14), içsel bilgi erişen listesi, ilişkili taraf/örtülü kazanç aktarımı (m.21), geri alım (m.22), çağrı (m.25-26).
2. **Olasılık-etki tartımı:** Her risk için ihlal olasılığı ve sonucu (idari para cezası m.103, menfaat iadesi m.104, tedbir m.96-99, cezai sorumluluk m.106-107) değerlendirilir; ölçülülük ve tekerrür etkisi gözetilir. Ara sonuç: öncelikli riskler sıralanır.
3. **İçsel bilgi yönetimi:** Bilgi bariyerleri, içsel bilgiye erişen listesi, açıklama/erteleme prosedürü ve işlem yasağı pencereleri tasarlanır; yöneticilerin kişisel işlemleri için kurallar konur.
4. **Sözleşmesel dağıtım:** Aracılık, danışmanlık ve M&A işlemlerinde sorumluluk ve tazminat klozları (TBK çerçevesinde) ile bilgi/beyan yükümlülükleri dengelenir.
5. **Belgeleme:** Tüm karar ve gerekçelerin yazılı/iz bırakacak şekilde tutulması; ispat ve savunma için bu kayıtların kritikliği vurgulanır.

## Çıktı modülleri
- Risk haritası (olasılık-etki matrisi)
- İçsel bilgi yönetim politikası iskeleti
- Uyum kontrol listesi ve sorumluluk dağıtım önerisi
- Öncelikli eylem planı

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
