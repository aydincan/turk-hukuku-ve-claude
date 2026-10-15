---
name: abonelik-ve-suregelen-edim
description: "Cep telefonu, internet, dijital platform, spor salonu gibi abonelik sözleşmelerinde tüketicinin her zaman fesih hakkını, bedel iadesini ve taahhüt/cezai şart denetimini değerlendirmek gerektiğinde kullanılır."
---

# Abonelik ve Sürekli Edimli Sözleşmeler

## Görev
Abonelik ve sürekli edimli tüketici sözleşmelerinde tüketicinin fesih hakkını, fesih usulünü, peşin alınan bedelin iadesini ve taahhütlü aboneliklerdeki cezai şart/erken cayma bedeli denetimini altlamak.

## Soğuk başlangıç (intake)
- Abonelik konusu ne (haberleşme, internet, dijital içerik, üyelik) ve süresi belirli mi?
- Taahhüt/kampanya var mı; erken çıkışta bedel öngörülmüş mü?
- Tüketici feshetmek mi istiyor, yoksa fesih engelleniyor mu?
- Peşin ödenen bir bedel var mı, fesih usulü sözleşmede nasıl düzenlenmiş?

## Denetim şeması
1. **Fesih hakkı (TKHK m.52):** Tüketici, belirsiz süreli veya süresi bir yıldan uzun belirli süreli abonelik sözleşmesini herhangi bir gerekçe göstermeden ve cezai şart ödemeden istediği zaman feshedebilir.
2. **Fesih usulü ve kolaylığı (m.52):** Sağlayıcı, aboneliğin kurulduğu yöntemi/araçları ile aynı kolaylıkta fesih imkânı sunmak zorundadır; fesih, talebin ulaşmasından itibaren kısa sürede (Yönetmelikte öngörülen gün) hüküm doğurur.
3. **Bedel iadesi:** Fesih halinde tüketici, ifa edilmemiş kısma ilişkin peşin ödediği bedelin iadesini isteyebilir; kullanılmayan dönem orantılı biçimde geri verilir.
4. **Taahhüt ve cezai şart denetimi:** Taahhütlü aboneliklerde erken fesih bedeli, ancak sağlayıcının sunduğu cihaz/indirim gibi somut bir avantajla orantılıysa ve önceden açıkça bildirilmişse geçerlidir; orantısız ya da müzakere edilmemiş cezai şart m.5 haksız şart denetimine tabidir.
5. **Sektörel mevzuat:** Elektronik haberleşmede BTK düzenlemeleri tamamlayıcıdır; ancak TKHK m.52'nin tüketici lehine emredici fesih hakkı saklıdır.
6. **Ara sonuç:** Fesih hakkı doğmuş mu, erken çıkış bedeli geçerli mi, ne kadar bedel iade edilmeli?

## Çıktı modülleri
- Fesih hakkı ve usul değerlendirmesi.
- Fesih bildirimi taslağı.
- İade edilecek bedel hesabı.
- Cezai şart geçerlilik analizi.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
