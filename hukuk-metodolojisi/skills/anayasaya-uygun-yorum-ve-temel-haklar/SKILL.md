---
name: anayasaya-uygun-yorum-ve-temel-haklar
description: "Bir kanun hükmü temel hak ve özgürlükleri etkilediğinde ya da birden çok okumaya açık olduğunda; hükmü Anayasa ve AİHS ile uyumlu biçimde yorumlamak ve gerekirse itiraz/başvuru yolunu değerlendirmek için kullanılır."
---

# Anayasaya ve AİHS'e Uygun Yorum

## Görev
Temel hak alanına dokunan bir kanun hükmünü Anayasa ve AİHS ile uyumlu biçimde yorumlamak, sınırlama rejimini ölçülülükle denetlemek ve gerektiğinde AYM yolunu işaretlemek.

## Soğuk başlangıç (intake)
- Hangi temel hak etkileniyor (ifade, mülkiyet, adil yargılanma, özel hayat...)?
- Hükmün birden çok okuması var mı; biri Anayasa'ya uygun mu?
- Sınırlama kanunla mı yapılmış; öngörülebilir mi?
- Konu AİHS kapsamında mı (m.90/5 devreye girer mi)?

## Denetim şeması
1. **Anayasaya uygun yorum ilkesi** — Bir kanun hem Anayasa'ya aykırı hem uygun okunabiliyorsa, hükmü iptal etmeden önce Anayasa'ya uygun yorum tercih edilir (norm korunur, sonuç anayasal sınıra çekilir). Anayasa m.11: Anayasa bağlayıcı ve üstündür.
2. **AİHS üstünlüğü** — Anayasa m.90/5: temel hak ve özgürlüklere ilişkin usulüne göre yürürlüğe konmuş sözleşme ile kanun çatışırsa sözleşme esas alınır; AİHM içtihadı yorum ölçüsü olur.
3. **Sınırlama rejimi — Anayasa m.13** — Temel hak ancak (i) kanunla, (ii) hakkın özüne dokunmadan, (iii) Anayasa'da öngörülen sebeplerle, (iv) demokratik toplum düzeninin gereklerine ve (v) ölçülülük ilkesine uygun olarak sınırlanabilir.
4. **Ölçülülük testi** — Elverişlilik (araç amaca uygun mu), gereklilik (daha az sınırlayıcı yol var mı), orantılılık (yük ile amaç dengeli mi). Üç alt ölçütten biri sağlanmazsa sınırlama Anayasa'ya aykırıdır.
5. **Yol seçimi** — Davada uygulanacak kanunun Anayasa'ya aykırılığı ciddi ise itiraz yolu (Anayasa m.152) ile AYM'ye başvuru; kesinleşmiş ihlalde bireysel başvuru (m.148, ayrı eklenti). AYM kararları bağlayıcıdır (m.153).

## Çıktı modülleri
- Etkilenen hak + hükmün rakip okumaları.
- Anayasaya uygun yorum sonucu.
- m.13 sınırlama ve ölçülülük denetimi tablosu.
- Yol önerisi (yorum / itiraz / başvuru) + `[doğrulanacak]` AYM/AİHM künyesi.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
