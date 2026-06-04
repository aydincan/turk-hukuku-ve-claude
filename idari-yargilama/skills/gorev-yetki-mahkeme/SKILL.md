---
name: gorev-yetki-mahkeme
description: "Davanın idare mahkemesi, vergi mahkemesi yoksa ilk derece Danıştay'da görüleceğinin ve hangi yer mahkemesinin yetkili olduğunun belirlenmesinde kullanılır; yetki itirazı, gönderme kararı ve Danıştay ilk derece görevleri tartışmalı olduğunda başvurulur."
---

# Görevli ve Yetkili Mahkemenin Belirlenmesi

## Görev
Davanın hangi ilk derece merciinde (idare mahkemesi, vergi mahkemesi veya ilk derece Danıştay) ve hangi yer mahkemesinde açılacağını belirlemek; yetkisizlik/görevsizlik halinde doğru usulü uygulamak.

## Soğuk başlangıç (intake)
- Uyuşmazlık vergi/gümrük/benzeri mali yükümlülükle mi ilgili?
- İşlem bir bakanlık/düzenleyici kurumun ülke geneli düzenleyici işlemi mi?
- İşlemi tesis eden idarenin bulunduğu yer ile işlemin uygulandığı yer neresi?
- Taşınmaza, kamu görevlisine veya tam yargıya ilişkin özel yetki kuralı var mı?

## Denetim şeması
1. **Görev — idare/vergi mahkemesi ayrımı** (2576 sayılı K. m.5-6): Vergi, resim, harç ve benzeri mali yükümlülükler ile bunların zam ve cezalarına ilişkin davalar **vergi mahkemesinde**; bunun dışındaki genel idari uyuşmazlıklar **idare mahkemesinde** görülür.
2. **İlk derece Danıştay görevi** (2575 sayılı K. m.24): Bakanlar Kurulu/Cumhurbaşkanı kararları, bakanlıkların düzenleyici işlemleri (yönetmelik vb.) ve kanunda sayılan ülke düzeyindeki işlemler ilk derece olarak Danıştay'da dava edilir.
3. **Yer yetkisi — genel kural** (İYUK m.32): Aksine hüküm yoksa yetkili mahkeme, dava konusu işlemi yapan **idari merciin bulunduğu yer** mahkemesidir.
4. **Özel yetki kuralları** (İYUK m.33-36): Kamu görevlilerine ilişkin işlemlerde görevlinin son görev yaptığı yer (m.33); taşınmaz mallara ilişkin davalarda taşınmazın bulunduğu yer (m.34); taşınır mallar ve tam yargı davalarında zararı doğuran işlem/eylemin yapıldığı yer veya ilgilinin ikametgâhı (m.35-36) gibi özel kurallar genel kurala önceliklidir.
5. **Görevsizlik/yetkisizlik** (İYUK m.15/1-a, m.43): Görev/yetki yönünden dava reddedilir ve dosya görevli/yetkili mahkemeye gönderilir; aynı yargı kolunda gönderme kararı verilir.
6. **Ara sonuç**: İki ayrı yer mahkemesi arasında yetki uyuşmazlığı çıkarsa bölge idare mahkemesi/Danıştay merci tayini ile çözer.

## Çıktı modülleri
- Görev (idare/vergi/Danıştay) tespiti
- Yetkili yer mahkemesi ve dayanak madde
- Yanlış mahkemeye açılma riski için gönderme senaryosu

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
