---
name: titck-idari-yaptirim-dava
description: "TİTCK tarafından verilen uyarı, faaliyet durdurma, ruhsat askı/iptal ve idari para cezası gibi işlemlere karşı iptal davası ve yürütmenin durdurulması stratejisini kurmak için kullanılır."
---

# TİTCK İdari Yaptırımlarına Karşı Dava

## Görev
TİTCK’nın birel veya düzenleyici işlemine karşı idari yargıda iptal davasını, yürütmenin durdurulması talebini ve gerekçe stratejisini kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: uyarı, faaliyet/tanıtım durdurma, sertifika askısı, ruhsat iptali, idari para cezası, düzenleyici tebliğ/kılavuz mu?
- İşlemin tebliğ tarihi; dava açma süresi durumu?
- İşlemin gerekçesi ve dayanak norm nedir?
- Telafisi güç/imkânsız zarar doğuran etki var mı (tesis kapanması, listeden çıkma)?

## Denetim şeması
1. **İşlem niteliği.** Birel işlem mi düzenleyici işlem mi? Düzenleyici işlemde normlar hiyerarşisi ve süre (İYUK m.7) ayrı değerlendirilir; düzenleyici işlemin uygulanması üzerine de dava açılabilir.
2. **Unsur denetimi.** Yetki (TİTCK’nın 663 sayılı KHK’dan gelen yetkisi), şekil (gerekçe, savunma alma), sebep (denetim bulgusu/bilimsel değerlendirme), konu, maksat. Ara sonuç: hangi unsur sakat?
3. **Süre ve usul.** İYUK m.7 (60 gün); idari para cezasında özel kanun/5326 kontrolü; üst makama başvuru (İYUK m.11) süreyi durdurur. İspat: idare sebep unsurunu somut belgeyle; davacı sakatlığı ortaya koyar.
4. **Yürütmenin durdurulması.** İYUK m.27: açıkça hukuka aykırılık + telafisi güç/imkânsız zarar birlikte gösterilir; ilacın hayati önemi veya işletmenin kapanma riski somutlaştırılır.
5. **Ölçülülük ve eşitlik.** Takdire dayalı yaptırımda elverişlilik-gereklilik-orantılılık ve benzer olaylarla eşit muamele denetlenir; emsal idari işlem/karar karararama.danistay.gov.tr üzerinden araştırılır [doğrulanacak].

## Çıktı modülleri
- İşlem niteliği ve süre tespiti.
- İptal + yürütmeyi durdurma dilekçesi iskeleti [doldurulacak].
- Unsur bazında hukuka aykırılık ve ölçülülük argüman listesi.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
