---
name: ihtiyari-arabuluculuk
description: "Taraf iradesiyle yürütülen, dava şartı olmayan arabuluculukta süreci başlatmak, yürütmek ve anlaşma belgesini icra edilebilir hale getirmek gerektiğinde kullanılır."
---

# İhtiyari Arabuluculuk Süreci

## Görev
HUAK kapsamında ihtiyari arabuluculuk sürecini tasarlamak ve anlaşmayı bağlayıcı/icra
edilebilir hale getirmek; gizlilik ve beyanların kullanılamaması ilkelerini korumak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık tarafların serbestçe tasarruf edebileceği bir konuya mı ilişkin?
2. Taraflar arabuluculuğa başvurmaya istekli mi, arabulucu seçildi mi?
3. Hedef nedir: tam anlaşma, kısmi anlaşma, yoksa müzakere zemini mi?
4. Anlaşma sonrası icra edilebilirlik şerhi gerekiyor mu?

## Denetim şeması
1. **Elverişlilik**: **HUAK m.1/2** — tarafların üzerinde serbestçe tasarruf edebileceği,
   yabancılık unsuru taşıyabilen özel hukuk uyuşmazlıkları. Aile içi şiddet içeren konular
   dışlanır.
2. **İlkeler**: İradilik ve eşitlik (**HUAK m.3**), **gizlilik** (**HUAK m.4**) ve
   arabuluculukta ileri sürülen beyan/belgelerin sonraki davada **delil olarak
   kullanılamaması** (**HUAK m.5**). Bu ilkeler süreç boyunca korunur.
3. **Arabulucunun rolü**: Arabulucu karar veremez, çözüm dayatamaz; tarafları
   buluşturur (**HUAK m.2/b, m.15**). Sicile kayıtlı olmalıdır.
4. **Anlaşma ve icra edilebilirlik**: Anlaşma belgesi düzenlenir; taraflar ve avukatları
   imzaladığı belge **icra edilebilirlik şerhi** niteliğindedir, aksi halde sulh
   hukuk mahkemesinden şerh alınır (**HUAK m.18**). Anlaşılan konular yönünden dava
   açılamaz.
5. **Ara sonuç**: Anlaşma kapsamı, açık kalan konular ve icra yolu.

## Çıktı modülleri
- Arabuluculuk anlaşma belgesi taslağı ([doldurulacak] yer tutucularıyla).
- Gizlilik/beyan kullanılamazlığı uyarı notu.
- İcra edilebilirlik şerhi başvuru rehberi.

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
