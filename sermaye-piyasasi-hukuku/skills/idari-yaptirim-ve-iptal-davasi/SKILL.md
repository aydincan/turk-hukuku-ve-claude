---
name: idari-yaptirim-ve-iptal-davasi
description: "Sermaye Piyasası Kurulu'nun idari para cezası, tedbir ve menfaat iadesi kararlarına karşı savunma, idari yargıda iptal davası ve yürütmenin durdurulması gerektiğinde kullanılır."
---

# SPK İdari Yaptırımları ve İptal Davası

## Görev
Kurul'un idari yaptırım kararını (idari para cezası, tedbir, menfaat iadesi) SPK m.92-104 ve İYUK çerçevesinde denetlemek; iptal davası ve yürütmenin durdurulması stratejisini kurmak.

## Soğuk başlangıç (intake)
- Yaptırımın türü ve dayanağı: hangi SPK maddesi/tebliğ ihlali gerekçe gösterildi?
- Karar ne zaman tebliğ edildi; dava açma süresi işliyor mu?
- Savunma alındı mı, usule uygun bildirim yapıldı mı; menfaat iadesi (m.104) var mı?
- Müvekkil gerçek kişi yönetici mi, ihraççı/kurum mu?

## Denetim şeması
1. **Yaptırım türü ve dayanak:** Kararın idari para cezası (m.103), tedbir (m.96-99) veya menfaat iadesi (m.104) niteliği ve dayanak maddesi belirlenir; ölçülülük (Anayasa m.13) test edilir.
2. **Usul denetimi:** Kurul kararının yetki, şekil, sebep, konu, maksat unsurları (idari işlem unsurları); savunma hakkı tanınması ve gerekçe yeterliliği incelenir. Usul sakatlığı tek başına iptal sebebidir.
3. **Esas denetimi:** İhlal fiilinin sabit olup olmadığı, isnat ile delil arasındaki bağ, cezanın alt-üst sınır ve tekerrür uygulaması denetlenir; ispat yükü ihlali iddia eden idarededir.
4. **Yargı yolu ve süre:** İptal davası idari yargıda açılır (İYUK m.2, m.7); dava açma süresi tebliğden itibaren işler, hak düşürücüdür; yürütmenin durdurulması (İYUK m.27) telafisi güç zarar ve açık hukuka aykırılık koşullarıyla talep edilir. Ara sonuç: süre takvimi ve YD talebi netleşir.
5. **Cezai eksenle ilişki:** Aynı fiil için cezai süreç (m.106-107) ayrı yürür; idari ve cezai sonuçların birbirini etkilemesi değerlendirilir.

## Çıktı modülleri
- Yaptırım kararı unsur denetim tablosu
- İptal sebepleri (usul + esas) listesi
- Dava açma süresi ve YD takvimi
- İptal/iddia dilekçesi iskeleti ([doldurulacak] yer tutucularıyla)

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
