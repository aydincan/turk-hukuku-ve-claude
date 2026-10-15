---
name: kabul-edilebilirlik-denetimi
description: "Başvurunun komisyonca/bölümce kabul edilebilir bulunup bulunmayacağı, açıkça dayanaktan yoksunluk, önemli zarar ve diğer ret sebepleri değerlendirilirken; esasa geçmeden önceki eşiği geçmek için kullanılır."
---

# Kabul Edilebilirlik Denetimi

## Görev
Başvurunun 6216 m.48 ve İçtüzük süzgeçlerinden geçip geçmeyeceğini önceden öngörmek; kabul edilemezlik risklerini tespit edip başvuruyu güçlendirmek veya gereksiz başvurudan caydırmak.

## Soğuk başlangıç (intake)
- Şikâyet konusu hangi anayasal hakka dayandırılıyor; açık bir anayasal mesele var mı?
- Başvurucunun katlandığı zarar önemli/anlamlı mı, yoksa önemsiz mi?
- Başvuru formundaki olay, deliller ve ihlal gerekçeleri tam mı?
- Daha önce aynı konuda AYM kararı var mı (mükerrerlik)?

## Denetim şeması
1. Anayasal/kişisel yetki — m.45-46: konu, kişi ve zaman bakımından yetki yeniden teyit edilir; eksikse usulden ret.
2. Açıkça dayanaktan yoksunluk — m.48/2: ihlal iddiası temellendirilmemişse, salt kanun yolu şikâyetiyse veya hak ihlali görünür biçimde yoksa başvuru reddedilir. Başvurucu, ihlali "ilk bakışta savunulabilir" (arguable) düzeyde ortaya koymalıdır.
3. Önemli zarar (anayasal önem) ölçütü — başvurucunun önemli bir zarara uğramadığı, anayasal ve kişisel önemi bulunmayan başvurular kabul edilemez bulunabilir; istisna, genel yarar veya ilkesel mesele varlığında değerlendirilir.
4. Mükerrerlik / derdestlik — daha önce esastan karara bağlanmış aynı başvuru veya başka uluslararası mercide derdest aynı şikâyet ret sebebidir.
5. Süre ve şekil — İçtüzük m.64'teki otuz günlük süre ve m.59 vd. başvuru formu şartları; eksiklik varsa giderme süresi tanınır, giderilmezse ret.

İspat yükü: kabul edilebilirlik eşiğini geçecek temellendirme başvurucudadır; AYM resen de inceler.

Ara sonuç: her ret sebebi için "geçti / riskli / geçemez" etiketi ve gerekçe çıkarılır.

## Çıktı modülleri
- Kabul edilebilirlik kontrol listesi (madde madde geçti/riskli/red).
- Açıkça dayanaktan yoksunluk riski analizi ve güçlendirme önerileri.
- Önemli zarar ve mükerrerlik notu.
- Eksiklik giderme uyarıları.

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
