---
name: dava-gorev-yetki-ve-ispat
description: "Borçlar hukukundan doğan bir uyuşmazlık yargıya taşınırken görevli-yetkili mahkeme, dava türü, dava şartı arabuluculuk ve ispat yükünün planlanması gerektiğinde kullanılır."
---

# Dava, Görev-Yetki ve İspat Stratejisi

## Görev
Borç ilişkisinden doğan uyuşmazlıkta doğru dava türünü, görevli-yetkili mahkemeyi, zorunlu arabuluculuğu ve ispat planını belirlemek.

## Soğuk başlangıç (intake)
- Talep ne: alacak/tazminat, tespit, sözleşmenin iptali/feshi, menfi tespit?
- Taraflar tacir mi; uyuşmazlık ticari iş mi?
- Dava değeri ve konusu ne (görev için)?
- Elde hangi deliller var (senet, fatura, tanık, bilirkişi gereği)?

## Denetim şeması
1. Görev: Genel görevli mahkeme asliye hukuk mahkemesidir (HMK m.2); dava değerine bakılmaksızın. Ticari işlerde asliye ticaret mahkemesi (TTK m.4-5); tüketici işlemlerinde tüketici mahkemesi (6502 s.K. m.73), kira ve bazı uyuşmazlıklarda sulh hukuk (HMK m.4).
2. Yetki: Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davalarda sözleşmenin ifa yeri (HMK m.10); haksız fiilde ek yetki (HMK m.16). Kesin yetki hâllerine ve yetki sözleşmesine (HMK m.17, tacirler arası) dikkat.
3. Dava şartı arabuluculuk: Ticari davalarda konusu alacak/tazminat olan uyuşmazlıklar (TTK m.5/A), tüketici davalarının bir kısmı (6502 s.K. m.73/A) ve kira uyuşmazlıkları zorunlu arabuluculuğa tabidir; arabulucuya başvurulmadan açılan dava usulden reddedilir.
4. Dava türü seçimi: Eda, tespit (HMK m.106), belirsiz alacak (HMK m.107) ve kısmi dava (HMK m.109); faiz başlangıcı ve talep sonucu doğru kurulmalı.
5. İspat: Senetle ispat zorunluluğu ve istisnaları (HMK m.200-203), kesin/takdiri deliller, ispat yükü TMK m.6 ve TBK özel kuralları (kusur karinesi m.112, ifa ispatı borçluda).
6. Ara sonuç: Yetkili-görevli mahkeme, başvurulacak ön şart ve delil listesi.

## Çıktı modülleri
- Görev-yetki ve arabuluculuk yol haritası.
- Dava türü ve talep sonucu önerisi (faiz dâhil).
- İspat planı ve delil-vakıa eşleştirme tablosu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
