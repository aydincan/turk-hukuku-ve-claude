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
