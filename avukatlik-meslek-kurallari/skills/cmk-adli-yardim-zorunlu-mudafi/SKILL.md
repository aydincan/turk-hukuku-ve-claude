---
name: cmk-adli-yardim-zorunlu-mudafi
description: "Baro tarafından CMK kapsamında zorunlu müdafi/vekil görevlendirmesi, adli yardım bürosu atamaları, bu görevlerin reddi ve ücretlendirilmesi söz konusu olduğunda kullanılır."
---

# CMK Müdafiliği, Adli Yardım ve Zorunlu Görevlendirmeler

## Görev
Baro üzerinden yapılan zorunlu müdafi/vekil ve adli yardım görevlendirmelerinin
yükümlülüklerini, reddi mümkün halleri ve ücret-rücu düzenini belirlemek.

## Soğuk başlangıç (intake)
1. Görevlendirme CMK zorunlu müdafilik mi, adli yardım vekilliği mi?
2. Görevi reddetmek için haklı/kanuni sebep var mı (çıkar çatışması, mazeret)?
3. Görev kapsamı hangi aşamayı içeriyor (soruşturma, kovuşturma, kanun yolu)?
4. Ücret CMK tarifesinden mi, adli yardımdan mı talep edilecek?

## Denetim şeması
1. **Görevin kaynağı.** Zorunlu müdafilik CMK m.150 (zorunlu hallerde müdafi tayini) ve
   m.156 (mağdur/vekil) ile baro tarafından atama yoluyla doğar; adli yardım Av. K. m.176-181
   kapsamında baro adli yardım bürosunca yürütülür. Atanan avukat görevi kabul ile yükümlüdür.
2. **Reddedilebilir haller.** Çıkar çatışması (Av. K. m.38), kabul edilemeyecek mazeret veya
   yasal engel halinde görev baroya iade/itiraz yoluyla bırakılabilir; keyfi ret disiplin
   suçudur. Ara sonuç: ret sebebi m.38/mazeret kalıbına uyuyor mu?
3. **Özen yükümü aynıdır.** Zorunlu/ücretsiz görevde de özen, sır ve sadakat yükümü serbest
   vekâletteki ile aynıdır (Av. K. m.34, m.36); savunmanın etkinliği esastır.
4. **Ücret ve giderler.** CMK görevlerinde ücret, ilgili CMK ücret tarifesinden Hazine/baro
   eliyle ödenir; adli yardımda ödeme Av. K. m.180 çerçevesinde yapılır. Davanın kazanılması
   halinde karşı taraftan tahsil ve rücu (Av. K. m.181) gözetilir.
5. **Sona erme.** Vekille temsil veya görevin kalkması halinde görevlendirme sona erer;
   dosya ve bilgi devri yapılır.

## Çıktı modülleri
- Görevin kabul/ret değerlendirmesi ve dayanağı.
- Aşama bazlı yükümlülük ve ücret özeti (CMK / adli yardım ayrımı).
- Görev iadesi/itiraz veya ücret talep dilekçesi taslağı.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
