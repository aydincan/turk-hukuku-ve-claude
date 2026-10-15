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
