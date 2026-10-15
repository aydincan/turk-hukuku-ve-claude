---
name: sgk-eczane-sozlesme-kesinti
description: "Eczane ile SGK arasındaki protokol, reçete kesintileri, cezai şart, MEDULA provizyonu ve sözleşme feshi uyuşmazlıklarında itiraz kademeleri ve dava yolunu kurmak için kullanılır."
---

# SGK-Eczane Protokolü ve Kesinti Uyuşmazlıkları

## Görev
Eczacı-SGK arasındaki ilaç temin protokolünden doğan kesinti, cezai şart ve fesih uyuşmazlıklarında doğru itiraz kademesini ve yargı yolunu belirlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık reçete kesintisi mi, cezai şart mı, sözleşmenin feshi/sözleşme dışı bırakma mı?
- Eczacı ile SGK arasında imzalanan protokol/sözleşme yürürlükte mi; protokoldeki itiraz kademeleri kullanıldı mı?
- Kesinti gerekçesi: reçete/fatura uyumsuzluğu, mükerrer, MEDULA/provizyon hatası, kural ihlali mi?
- Tebliğ/kesinti tarihi ve itiraz süreleri?

## Denetim şeması
1. **İlişkinin niteliği.** SGK-eczacı protokolü idari sözleşme tartışmalıdır; uygulamada kesinti ve cezai şart uyuşmazlıklarında görevli yargı yeri içtihatla şekillenir — güncel görev içtihadı karararama.danistay.gov.tr ve karararama.yargitay.gov.tr üzerinden teyit edilmelidir [doğrulanacak].
2. **İtiraz kademesi.** Önce protokolde öngörülen itiraz komisyonu/kademesi tüketilir. Ara sonuç: idari/sözleşmesel başvuru yolu tamamlandı mı?
3. **Esas denetimi.** Kesintinin dayanağı SUT ve protokol kuralı; reçete-fatura örneklemi, MEDULA kayıtları delil olur. İspat: SGK kesinti sebebini; eczacı reçetenin usulüne uygunluğunu (hekim onayı, ICD, doz) gösterir.
4. **Cezai şart.** Protokoldeki cezai şartın TBK m.182 vd. çerçevesinde fahiş olup olmadığı, tenkis imkânı (sözleşmesel ilişki kabul edilirse) değerlendirilir.
5. **Fesih/sözleşme dışı bırakma.** Süreli/süresiz fesih sebebi, ölçülülük ve eczacının savunma hakkı; iptal/menfi tespit veya alacak davası seçimi ilişkinin niteliğine göre yapılır.

## Çıktı modülleri
- İtiraz kademesi ve görevli yargı yolu notu.
- Kesinti kalemi bazında itiraz/dava cetveli.
- İtiraz dilekçesi veya dava dilekçesi iskeleti [doldurulacak].

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
