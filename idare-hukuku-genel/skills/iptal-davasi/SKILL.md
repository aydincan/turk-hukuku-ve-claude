---
name: iptal-davasi
description: "Hukuka aykırı bir idari işlemin iptali için dava şartlarını, ehliyet-menfaat ilişkisini, süreyi ve esas sebeplerini kurgulamak amacıyla kullanılır; idari işleme karşı dava açılacağında temel beceridir."
---

# İptal Davası Stratejisi

## Görev
İdari işlemin iptali için davayı baştan sona kurgulamak: dava şartları, ehliyet ve menfaat, süre, görev-yetki ve esas iptal sebepleri. İYUK m.2/1-a çerçevesinde iptal davasının iskeletini üretir.

## Soğuk başlangıç (intake)
1. Dava edilecek kesin/yürütülebilir bir işlem var mı; tebliğ/öğrenme tarihi nedir?
2. Müvekkilin işlemle ihlal edilen kişisel, güncel ve meşru menfaati nedir?
3. İYUK m.11 üst makama başvuru yapıldı/yapılacak mı; zımni ret oluştu mu?
4. İşlem bireysel mi düzenleyici mi (yönetmelik/genelge)?

## Denetim şeması
1. **Dava türü.** İptal davası: yetki, şekil, sebep, konu, maksat yönünden hukuka aykırı işlemin iptali (İYUK m.2/1-a). Menfaat ihlali yeterlidir; subjektif hak şart değildir.
2. **Ehliyet ve menfaat.** Davacının işlemle kişisel, güncel ve meşru bir menfaat ilişkisi bulunmalı. Düzenleyici işlemlerde menfaat daha geniş yorumlanır.
3. **Süre.** Genel dava açma süresi 60 gün (İYUK m.7/1); tebliğ/ilan/öğrenme tarihinden işler. İYUK m.11 başvurusu süreyi durdurur; 60 gün sessizlik zımni rettir (m.10/m.11). Düzenleyici işlemde hem düzenlemeye hem uygulama işlemine karşı dava imkânı (m.7/4).
4. **Görev ve yetki.** Kural olarak idare mahkemesi; ilk derecede Danıştay'da görülecek işlemler (2575 sayılı K. ile belirli düzenleyici işlemler) ayrıdır. Yer yönünden yetki İYUK m.32 vd. (işlemi yapan idarenin bulunduğu yer kuralı ve özel yetki kuralları).
5. **Esas sebepler.** Beş unsur denetiminden (bkz. unsur denetimi becerisi) çıkan aykırılıkları hukuki sebep olarak diz; her birini madde ve delille bağla.
6. **Yürütmenin durdurulması.** İYUK m.27/2: telafisi güç veya imkânsız zarar **ve** açık hukuka aykırılık koşullarını birlikte gerekçelendir.
7. **Ara sonuç.** Dava şartları karşılanıyorsa esas sebeplerle iptal talebi; karşılanmıyorsa eksik giderme yolu (m.11 başvurusu, süre, ehliyet düzeltimi).

## Çıktı modülleri
- Dava şartları kontrol listesi (süre, ehliyet, menfaat, görev, yetki).
- İptal sebepleri ile madde/delil eşleşmesi.
- Yürütmenin durdurulması gerekçesi taslağı.
- Dilekçe için talep sonucu önerisi.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
