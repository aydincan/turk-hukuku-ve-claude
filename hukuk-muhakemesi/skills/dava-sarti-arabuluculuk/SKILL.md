---
name: dava-sarti-arabuluculuk
description: "Bir uyuşmazlıkta dava açmadan önce zorunlu (dava şartı) arabuluculuğa başvurulması gerekip gerekmediğini saptamak; ticari, iş, tüketici ve genişleyen kapsam, son tutanak ve dava şartı eksikliğinin sonucu için."
---

# Dava Şartı Arabuluculuk Kapsam Denetimi

## Görev
Dava açılmadan önce zorunlu arabuluculuk gerekip gerekmediğini belirlemek; gerekiyorsa son tutanağı dava şartı olarak dosyaya bağlamak, gerekmiyorsa boşa süreç işletilmesini önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık türü ne? (ticari alacak, işçi-işveren, tüketici, kira, ortaklığın giderilmesi?)
- Talep konusu para alacağı/tazminat mı, yoksa kapsam dışı bir talep mi?
- Daha önce arabuluculuğa başvuruldu mu, son tutanak var mı?
- Karşı tarafa ulaşılabiliyor mu (anlaşamama tutanağı seçeneği)?

## Denetim şeması
1. **Ticari uyuşmazlıklar** (TTK m.5/A): Konusu bir miktar paranın ödenmesi olan alacak ve tazminat talepleri bakımından dava şartı arabuluculuk; dava açmadan son tutanak alınmalıdır.
2. **İş uyuşmazlıkları** (7036 sayılı İş Mahkemeleri Kanunu m.3): İşçi-işveren arasındaki kıdem/ihbar/fazla mesai gibi alacak ve işe iade taleplerinde dava şartı arabuluculuk; **iş kazası/meslek hastalığından kaynaklanan maddi-manevi tazminat** istisnası kontrol edilir.
3. **Tüketici uyuşmazlıkları** (6502 sayılı Kanun): Belirli parasal sınır üstündeki tüketici uyuşmazlıklarında dava şartı arabuluculuk; hakem heyeti zorunluluğu olan alt sınır ayrıca kontrol edilir.
4. **Genişleyen kapsam**: Kira ilişkisinden doğan uyuşmazlıklar, taşınır/taşınmaz ortaklığının giderilmesi, komşuluk hukuku ve kat mülkiyetinden doğan belirli uyuşmazlıklar da kademeli olarak dava şartı arabuluculuk kapsamına alınmıştır — **güncel kapsam ve yürürlük tarihleri mevzuattan teyit edilir.**
5. **Sonuç** (dava şartı): Kapsamdaki uyuşmazlıkta son tutanak (anlaşma/anlaşamama) dosyaya konmadan dava açılırsa, dava **usulden reddedilir** (HMK m.115; ilgili özel hükümler). Karşı tarafın katılmaması durumunda anlaşamama tutanağı dava şartını karşılar.
6. **Süre etkisi**: Arabuluculuğa başvuru, zamanaşımını durdurur ve hak düşürücü süreyi işlemekten alıkoyar; bu koruma esastır.

Ara sonuç: "Kapsamda mı + hangi norm + son tutanak gerekli mi + zamanaşımı etkisi" özeti.

## Çıktı modülleri
- Kapsam kararı (norm atıflı, istisna kontrollü).
- Eksik son tutanak halinde usulden ret uyarısı.
- Başvurunun zamanaşımı/hak düşürücü süreye etkisi notu.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
