---
name: temsil-ve-yetkisiz-temsil
description: "Bir kişinin başkası adına işlem yaptığı, temsil yetkisinin varlığı/kapsamı tartışmalı olduğu veya yetkisiz temsil ile yapılan işlemin akıbeti sorulduğunda kullanılır."
---

# Temsil ve Yetkisiz Temsil

## Görev
Bir işlemin temsilci eliyle geçerli yapılıp yapılmadığını, yetkinin kapsamını ve yetkisiz temsilde işlemin akıbetini belirlemek.

## Soğuk başlangıç (intake)
- İşlemi yapan kişi kimin adına ve hangi yetkiyle hareket etti?
- Temsil yetkisi nasıl verildi (vekâletname, ticari temsil, kanun)?
- Yetki işlem anında mevcut, kapsamı yeterli miydi; sonradan sona ermiş mi?
- Karşı taraf temsilcinin yetkisine iyiniyetle güvendi mi?

## Denetim şeması
1. Doğrudan/dolaylı temsil: TBK m.40 — doğrudan temsilde hukuki sonuçlar temsil olunana ait olur; temsilcinin başkası adına hareket ettiğini bildirmesi veya karşı tarafça anlaşılması gerekir.
2. Yetkinin kaynağı ve kapsamı: İradi temsilde yetki belgesi/vekâletname; kapsam yorumu dar/geniş. Olağan işler için verilen yetki olağanüstü tasarrufları (bağışlama, kefalet, taşınmaz devri) kapsamaz — özel yetki gerekir.
3. Yetkinin sona ermesi: m.42-45 — azil, istifa, ölüme/ehliyetsizliğe bağlı son bulma; iyiniyetli üçüncü kişilerin korunması (m.45). Yetki belgesinin geri verilmemesinden doğan sorumluluk (m.44).
4. Yetkisiz temsil: m.46-47 — temsil olunan icazet verirse işlem baştan itibaren onu bağlar; icazet vermezse işlem onu bağlamaz, yetkisiz temsilci karşı tarafın menfi zararından (icazet vermezse) veya müspet zarardan (kusurluysa) sorumlu olur (m.47).
5. Temsilcinin kendisiyle işlem yapması/çıkar çatışması: kural olarak geçersiz, izin/icazet ile geçerli.
6. İspat yükü: Yetkinin varlığını ve kapsamını işleme dayanan taraf ispatlar.

## Çıktı modülleri
- Yetki kapsamı ve geçerlilik analizi.
- İcazet/ret beyanı taslağı iskeleti.
- Yetkisiz temsilde sorumluluk ve rücu şeması.

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
