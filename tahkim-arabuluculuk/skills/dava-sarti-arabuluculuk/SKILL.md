---
name: dava-sarti-arabuluculuk
description: "İş, ticari, tüketici, kira ve benzeri uyuşmazlıklarda dava açmadan önce zorunlu arabuluculuk başvurusunu yönetmek; kapsam, süre ve son tutanak sonrası dava açma adımını belirlemek gerektiğinde kullanılır."
---

# Dava Şartı (Zorunlu) Arabuluculuk

## Görev
Dava açmadan önce arabuluculuğun zorunlu olduğu uyuşmazlıklarda kapsamı, süreyi ve son
tutanaktan sonraki dava açma penceresini doğru yönetmek. Arabulucuya başvurmadan açılan
dava **usulden reddedilir**; bu beceri o riski engeller.

## Soğuk başlangıç (intake)
1. Uyuşmazlık iş, ticari, tüketici, kira/komşu/kat mülkiyeti gibi zorunlu bir alana mı
   giriyor?
2. Alacak/talep türü nedir (ör. işçilik alacağı, ticari alacak, tahliye)?
3. Daha önce arabuluculuğa başvuruldu mu, son tutanak alındı mı?
4. Anlaşmama halinde dava açma süresi ne zaman doluyor?

## Denetim şeması
1. **Kapsam belirleme**: İş uyuşmazlıkları **7036 m.3** (işçi-işveren alacak/tazminat ve
   işe iade); ticari uyuşmazlıklar **TTK m.5/A** (konusu para alacağı/tazminat olan ticari
   davalar); tüketici **TKHK m.73/A**; kira, taşınır/taşınmaz paylaştırma ve ortaklığın
   giderilmesi, komşu hukuku, kat mülkiyeti **HUAK m.18/B**. İş kazası/meslek hastalığından
   maddi-manevi tazminat ve tespit istisnası gözetilir.
2. **Zamanaşımı/hak düşürücü süre**: Arabuluculuk başvurusu **zamanaşımını durdurur, hak
   düşürücü süreyi işlemez kılar** (**HUAK m.18/A-15**). Bu koruma başvuru tarihinden son
   tutanağa kadar sürer.
3. **Yetki ve atama**: Başvuru, karşı tarafın yerleşim yeri/işin yapıldığı yer adliyesi
   arabuluculuk bürosuna yapılır; arabulucu komisyonca atanır (**HUAK m.18/A**).
4. **Anlaşmama ve dava açma**: Anlaşmama son tutanağının düzenlendiği tarihten itibaren
   **2 hafta** içinde dava açılmalı; aksi halde tekrar arabuluculuk şarttır. Dava
   dilekçesine son tutanağın aslı/örneği eklenmezse mahkeme **1 haftalık kesin süre**
   verir, sunulmazsa dava şartı yokluğundan usulden reddedilir (**HUAK m.18/A-2**).
5. **Ara sonuç**: Kapsam teyidi, süre takvimi ve eksik belge listesi.

## Çıktı modülleri
- Kapsam/istisna kontrol tablosu (alan-madde eşleştirmesi).
- Arabuluculuk başvuru dilekçesi taslağı.
- Son tutanak sonrası 2 haftalık dava açma takvimi ve hatırlatma notu.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
