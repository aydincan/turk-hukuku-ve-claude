---
name: sikayet-ve-itirazen-sikayet
description: "İhale sürecindeki bir işleme karşı idareye şikâyet ve Kamu İhale Kurumuna itirazen şikâyet başvurusunun süre, şekil ve içerik yönünden hazırlanması gerektiğinde kullanılacak temel usul becerisidir."
---

# Şikâyet ve İtirazen Şikâyet (KİK Yolu)

## Görev
İhale işlemlerine karşı zorunlu idari başvuru yolunu (idareye şikâyet → KİK'e itirazen şikâyet) süre ve şekil şartlarına uygun kurmak; başvuru ehliyeti ve menfaat ilişkisini denetlemek.

## Soğuk başlangıç (intake)
1. Şikâyete konu işlem ne ve hangi tarihte öğrenildi/bildirildi?
2. Başvuran istekli/istekli olabilecek/aday sıfatını taşıyor mu (menfaat)?
3. İdareye şikâyet yapıldı mı, idare cevap verdi mi/sustu mu?
4. Başvuru bedeli yatırıldı mı; itirazen şikâyet dilekçesi süresinde mi?

## Denetim şeması
1. **Şikâyet (m.55):** İhale sürecindeki işlem/eylemlere karşı, hukuka aykırılığın farkına varıldığı veya farkına varılması gereken tarihten itibaren 10 gün içinde idareye yazılı şikâyet edilir. Sözleşme imzalanmadan başvurulmalıdır. İdare 10 gün içinde gerekçeli karar verir.
2. **İtirazen şikâyet (m.56):** İdarenin kararına veya 10 günlük süre içinde karar vermemesine (zımni ret) karşı, tebliğ/sürenin bitiminden itibaren 10 gün içinde KİK'e itirazen şikâyet edilir. Başvuru bedeli (m.53'e göre, güncel tutar) yatırılır.
3. **Ehliyet-menfaat:** Başvuran, ihaleye teklif veren istekli ya da istekli olabilecek/aday sıfatıyla menfaat ilişkisini taşımalıdır. Doküman aykırılığına itirazda istekli olabilecekler de başvurabilir.
4. **KİK kararı:** Kurul düzeltici işlem, ihalenin iptali veya itirazen şikâyetin reddine karar verir. Karar, ilgili idare ve tarafları bağlar.
5. **Dava aşaması:** KİK kararına karşı Ankara idare mahkemelerinde 2577 sayılı İYUK'a göre iptal davası açılır; süre kararın tebliğinden itibaren 30 gündür.
6. **Ara sonuç:** Süre hak düşürücüdür; kaçırılan başvuru esasa girilmeden reddedilir.

İspat yükü: Başvuran iddiasını belge ve doküman atfıyla somutlaştırır.

## Çıktı modülleri
- Süre takvimi (öğrenme → şikâyet → idare cevabı → itirazen şikâyet → dava).
- Şikâyet/itirazen şikâyet dilekçe taslağı (talep + gerekçe + dayanak).
- Ehliyet/menfaat değerlendirme notu.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
