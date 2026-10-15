---
name: beyan-tekefful-ve-tazminat
description: "SPA'daki beyan ve tekeffülleri (R&W) kapsam ve katalog olarak tasarlamak, disclosure letter ile sınırlamak ve ihlal halinde tazminat-sınırlama (cap, basket, süre) mimarisini kurmak için kullanılır."
---

# Beyan ve Tekeffüller ile Tazminat Rejimi

## Görev
Satıcı beyan-tekeffül kataloğunu hazırlamak, disclosure letter ile istisnaları yönetmek ve ihlal halinde tazminat ve sorumluluk sınırlamalarını dengeli kurmak.

## Soğuk başlangıç (intake)
- Müvekkil beyanı veren (satıcı) mı, alan (alıcı) mı?
- Beyanlar imza ve/veya kapanış tarihinde tekrarlanacak mı?
- Disclosure letter (açıklama mektubu) hazırlanacak mı?
- Bilgi standardı (best knowledge / fairly disclosed) nasıl tanımlanacak?

## Denetim şeması
1. **Beyan kataloğu**: Kurumsal yetki, pay mülkiyeti ve takyidatsızlık, finansal tablolar, vergi, iş hukuku, fikri mülkiyet, sözleşmeler, dava, uyum, KVKK başlıklarında temel ve operasyonel beyanlar.
2. **Hukuki nitelik**: Türk hukukunda R&W, satımda ayıba karşı tekeffül (TBK m.219 vd.) ile zapttan sorumluluk (TBK m.214 vd.) mantığına benzer; sözleşmeyle bağımsız bir tazminat (indemnity) borcu olarak da kurulabilir.
3. **Disclosure (açıklama)**: Beyanlar disclosure letter ile sınırlandırılır; açıklanan hususlar ihlal sayılmaz. Genel ve özel açıklamalar ayrılır.
4. **İhlal ve tazminat**: İhlal halinde gerçek zarar TBK m.112 (gereği gibi ifa etmeme) çerçevesinde; hile varsa TBK m.36 ile iptal/tazminat hakları saklıdır ve sözleşmesel sınırlamalar hileyi kapsayamaz.
5. **Sınırlamalar**: Azami sorumluluk (cap), eşik (de minimis / basket), zaman sınırı (genel beyanlar için kısa, vergi/temel beyanlar için uzun), sandbagging düzenlemesi.
6. **İspat yükü**: İhlali ve zarar miktarını talep eden taraf ispatlar (HMK m.190).
7. **Ara sonuç**: Müvekkil satıcı ise sınırlamalar genişletilir; alıcı ise temel beyanlar sınırlama dışı bırakılır.

## Çıktı modülleri
- Beyan-tekeffül kataloğu taslağı
- Disclosure letter şablonu (genel + özel açıklamalar)
- Tazminat ve sınırlama klozları (cap/basket/süre)
- Risk dağılım tablosu

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
