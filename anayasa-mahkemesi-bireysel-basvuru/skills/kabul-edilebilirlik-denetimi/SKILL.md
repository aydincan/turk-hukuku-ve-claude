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
