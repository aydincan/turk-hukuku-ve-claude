---
name: temel-kavramlar-ve-sistem
description: "Buluşun patent mi faydalı model mi olarak korunacağı, ulusal/EPC/PCT rejimi, koruma süresi ve uygulanacak normun belirlenmesi gerektiğinde; uyuşmazlığı doğru rejime oturtmak için ilk başvurulacak beceri."
---

# Patent ve Faydalı Model Temel Kavramları ve Sistematik

## Görev
Önündeki teknik korumayı doğru rejime oturtmak: patent mi faydalı model mi, ulusal mı EPC/PCT yoluyla mı geldiği, koruma süresi ve uygulanacak normu (SMK Dördüncü Kitap, SMK Yönetmeliği, EPC/PCT) belirleyip uyuşmazlığın iskeletini kurmak.

## Soğuk başlangıç (intake)
1. Korunan/korunacak konu nedir: ürün mü usul mü; teknik alan ne?
2. Patent mi faydalı model mi; belge verildi mi, başvuru hangi aşamada?
3. Hak ulusal başvurudan mı, PCT ulusal aşamasından mı, yoksa Türkiye'de validasyonlu Avrupa patentinden mi doğuyor?
4. Başvuru/rüçhan tarihi ve kalan koruma süresi nedir?

## Denetim şeması
1. **Rejim tespiti.** Patent SMK m.82 vd. (20 yıl, m.101); faydalı model SMK m.142-145 (10 yıl). Faydalı modelde buluş basamağı aranmaz (m.142/1), ancak usuller, kimyasal/biyolojik maddeler ve eczacılık ürünleri faydalı modelle korunamaz (m.142/3). Ara sonuç: hangi rejim?
2. **Hak kaynağı.** Ulusal patent TPMK; PCT başvurusunun ulusal aşaması; Avrupa patenti EPC m.65 uyarınca çeviri/validasyon ile Türkiye'de ulusal patent hükmü doğurur. Validasyon ve yıllık ücret durumunu sicilden teyit et.
3. **Koruma kapsamının kaynağı.** Koruma istemlerle belirlenir (SMK m.89); tarifname ve resimler yorumda kullanılır. Bağımsız/bağımlı istem ayrımını çıkar.
4. **Süre ve ayakta kalma.** Patent 20, faydalı model 10 yıl; koruma yıllık ücretlerin ödenmesine bağlıdır (SMK m.101). Ödenmeyen ücret hakkı düşürür; ek süre/telafi imkânını kontrol et.
5. **Norm seçimi.** Maddi şartlarda SMK m.82-83; usulde SMK Yönetmeliği; çatışmada özel düzenleme genel kuralı önceler.

## Çıktı modülleri
- Rejim ve uygulanacak norm haritası (patent/faydalı model; ulusal/EPC/PCT).
- Hak kaynağı ve sicil durumu özeti.
- Koruma süresi ve yıllık ücret takvimi uyarısı.
- İstem yapısı (bağımsız/bağımlı) ilk dökümü.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
