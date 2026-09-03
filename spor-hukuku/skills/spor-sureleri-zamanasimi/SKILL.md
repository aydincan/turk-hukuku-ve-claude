---
name: spor-sureleri-zamanasimi
description: "Disiplin, itiraz, tahkim, CAS ve sözleşmesel alacaklarda süre rejimini ve zamanaşımını hesaplamak, hak kaybını önlemek için süre takvimi çıkarmak gerektiğinde kullanın."
---

# Spor Hukukunda Süreler, Hak Düşürücü Süreler ve Zamanaşımı

## Görev
Spor uyuşmazlıklarında geçerli süre rejimini doğru kurmak; itiraz, tahkim, CAS ve sözleşmesel alacak süreleri ile hak düşürücü süreleri ayırmak ve geriye sayımlı bir süre takvimi üretmektir.

## Soğuk başlangıç (intake)
1. Hangi işlem için süre soruluyor (disiplin itirazı, tahkim, CAS, alacak davası)?
2. Tebliğ/öğrenme tarihi nedir; tebligat usulü ne (elektronik, federasyon bildirimi)?
3. Federasyon ve uygulanacak talimat hangisi?
4. Sözleşmesel alacak mı, ceza/idari karar mı?
5. Süre içinde herhangi bir başvuru yapıldı mı?

## Denetim şeması
1. **Süre türü**: Disiplin ve tahkim başvuru süreleri kural olarak **hak düşürücü** süredir; durmaz, kesilmez ve resen dikkate alınır. Sözleşmesel alacaklarda **zamanaşımı** (TBK) işler; def'i olarak ileri sürülür.
2. **Başlangıç anı**: Sürenin tebliğ mi, öğrenme mi, yoksa kararın kesinleşmesiyle mi başladığı talimat metninden tespit edilir; tebligatın usulüne uygunluğu kontrol edilir.
3. **Talimat sürelerinin önceliği**: Federasyon disiplin/itiraz/tahkim süreleri ilgili talimatta düzenlenir ve genelde günlerle ölçülür; metin ve yürürlük tarihi mutlaka doğrulanır (talimat sık değişir).
4. **CAS süresi**: Milletlerarası boyutta CAS başvuru süresi, ilgili federasyon kuralının atıf yaptığı süredir; kaçırılması başvuruyu reddettirir.
5. **Sözleşmesel zamanaşımı**: Sporcu ücret/prim alacaklarında TBK genel ve özel zamanaşımı süreleri uygulanır; alacağın niteliğine göre süre belirlenir.
6. **Ara sonuç**: Her işlem için son gün, kalan gün ve risk seviyesi tabloya yazılır.

## Çıktı modülleri
- Süre takvimi tablosu (işlem → başlangıç → son gün → kalan gün)
- Hak düşürücü/zamanaşımı ayrım notu
- Acil aksiyon uyarısı
- Talimat/süre doğrulama notu `[doğrulanacak]`

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
