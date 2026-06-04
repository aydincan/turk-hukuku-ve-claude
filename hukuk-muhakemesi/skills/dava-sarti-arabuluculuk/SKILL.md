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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
