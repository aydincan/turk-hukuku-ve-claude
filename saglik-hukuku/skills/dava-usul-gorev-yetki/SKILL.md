---
name: dava-usul-gorev-yetki
description: "Tıbbi uyuşmazlıkta hangi mahkemenin görevli ve yetkili olduğunu, hangi dava türünün açılacağını ve dava şartlarını belirlemek için kullanılır; adli/idari yargı ayrımını çözer."
---

# Dava, Usul ve Görev-Yetki

## Görev
Tıbbi uyuşmazlıkta doğru yargı kolu, görevli/yetkili mahkeme, dava türü ve dava şartlarını (özellikle arabuluculuk) saptamak.

## Soğuk başlangıç (intake)
1. Davalı kim: hekim, özel hastane, kamu idaresi, sigorta?
2. Müdahale kamu mu özel sağlık kuruluşunda mı yapıldı?
3. Talep tazminat mı, şikâyet mi, hizmet kusuru mu?
4. Zarar tarihi ve varsa öğrenme tarihi?

## Denetim şeması
1. **Yargı kolu**: Özel hastane/muayenehane → adli yargı. Kamu hastanesi → idari yargı (tam yargı davası, İYUK m.2, m.12-13). Hekime karşı kişisel dava 3359 Ek m.18 nedeniyle kural olarak idareye yöneltilir.
2. **Görevli mahkeme (adli)**: Hasta-özel hastane ilişkisi çoğu kez tüketici işlemi sayılır → Tüketici Mahkemesi (6502). Tacir/şirket taraf veya tüketici niteliği yoksa Asliye Hukuk. Ceza yönü için Asliye Ceza.
3. **Dava şartı arabuluculuk**: Tüketici ve ticari uyuşmazlık niteliğine göre 6325/6502 kapsamında zorunlu arabuluculuk gündeme gelir; idari davada uygulanmaz.
4. **İdari yolun ön şartı**: Tam yargı davasından önce İYUK m.13 uyarınca idareye başvuru ve süreler.
5. **Yetki**: HMK m.6 (davalı yerleşim yeri), haksız fiilde HMK m.16 (haksız fiilin işlendiği/zararın doğduğu yer). İdari davada İYUK m.33 vd.
6. **Dava şartları**: HMK m.114-115 (görev, yetki kesin ise, hukuki yarar, taraf ehliyeti). Ara sonuç: yanlış yargı kolunda açılan dava görevsizlik/yargı yolu reddi ile sonuçlanır.

## Çıktı modülleri
- Yargı kolu ve görevli/yetkili mahkeme tespiti
- Dava türü ve dava şartı kontrol listesi
- Arabuluculuk zorunluluğu değerlendirmesi
- Husumet (doğru davalı) tablosu

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
