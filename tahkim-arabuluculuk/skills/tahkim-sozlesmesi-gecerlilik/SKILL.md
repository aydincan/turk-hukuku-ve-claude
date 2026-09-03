---
name: tahkim-sozlesmesi-gecerlilik
description: "Bir tahkim şartı veya tahkim sözleşmesinin geçerliliğini, kapsamını ve ayrılabilirliğini denetlemek; sözleşmeye tahkim klozu yazmak veya karşı tarafın tahkim itirazını değerlendirmek gerektiğinde kullanılır."
---

# Tahkim Sözleşmesi ve Geçerlilik Denetimi

## Görev
Tahkim iradesinin geçerli, yazılı ve kapsam bakımından yeterli olup olmadığını altlamak;
hem mevcut bir klozu denetlemek hem de yeni bir tahkim şartı kaleme almak. Geçersiz veya
patolojik kloz tüm tahkim sürecini riske atar.

## Soğuk başlangıç (intake)
1. Tahkim anlaşmasının metni nedir, asıl sözleşmenin içinde mi ayrı belge mi?
2. Yabancılık unsuru var mı (iç tahkim/MTK ayrımı için)?
3. Tahkim yeri, dili, hakem sayısı ve uygulanacak kurum kuralları belirlenmiş mi?
4. Karşı taraf tahkim itirazında mı bulunuyor yoksa tahkime mi gidiliyor?

## Denetim şeması
1. **Yazılılık**: İç tahkimde **HMK m.412/3**, MTK'da **MTK m.4/2** — yazılı şekil
   şarttır; tahkim şartı içeren belgeye atıf yapan sözleşme de geçerli sayılır.
2. **İrade ve elverişlilik**: Konunun tahkime elverişliliği (**HMK m.408** / **MTK m.1**)
   ve tarafların ehliyeti denetlenir; emredici alanlar dışlanır.
3. **Ayrılabilirlik (separability)**: Asıl sözleşmenin geçersizliği tahkim şartını
   kendiliğinden geçersiz kılmaz (**HMK m.412/4**, **MTK m.4/4**). Bu ilke ayrı altlanır.
4. **Yetki-yetki (competence-competence)**: Hakem kendi yetkisi hakkında karar verebilir
   (**HMK m.422**, **MTK m.7/H**). Mahkemeye tahkim itirazı **ilk itiraz** olarak ileri
   sürülür (**HMK m.116, m.413**).
5. **Patoloji kontrolü**: Belirsiz hakem atama usulü, çelişkili yetki klozları, geçersiz
   kurum atfı tespit edilir; ara sonuçta klozun ayakta kalıp kalmadığı belirtilir.

## Çıktı modülleri
- Geçerlilik denetim tablosu (yazılılık, elverişlilik, ayrılabilirlik, yetki).
- Önerilen/düzeltilmiş tahkim klozu taslağı (yer, dil, hakem sayısı, kurum kuralları
  ve [doldurulacak] yer tutucularıyla).
- Tahkim itirazı veya tahkime başvuru için strateji notu.

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
