---
name: imar-dava-dilekce-ve-yd
description: "İmar uyuşmazlığında iptal veya tam yargı dilekçesi, yürütmenin durdurulması talebi ya da idari başvuru/itiraz dilekçesi hazırlanacağında; vakıa-hukuki sebep-talep mimarisi ve YD koşulları sorulduğunda kullanılır."
---

# İmar Davası Dilekçesi ve Yürütmenin Durdurulması

## Görev
İmar uyuşmazlığına uygun, İYUK formatında dava/başvuru dilekçesi üretmek; yürütmenin durdurulması talebini gerekçeli kurmak.

## Soğuk başlangıç (intake)
- Dava türü iptal mi, tam yargı mı, ikisi birlikte mi?
- Dava konusu işlem ve tarafları (davalı idare) net mi?
- Süre durumu uygun mu, YD talebi gerekiyor mu?
- Eldeki belgeler ve talep edilen sonuç (iptal/tazminat tutarı) ne?

## Denetim şeması
1. **Dava türü ve taraf (İYUK m.2)**: İptal davası (yetki-şekil-sebep-konu-maksat sakatlığı) mı, tam yargı (tazminat/el atma) mı belirlenir; davalı idare doğru gösterilir (işlemi tesis eden makam). Husumet hatası ret riskidir.
2. **Dilekçe mimarisi (İYUK m.3)**: Taraflar, konu, **tebliğ/öğrenme tarihi**, vakıalar (olay kronolojisi), hukuki sebepler (3194 ilgili maddeleri + İYUK + Anayasa m.35), deliller ve net **talep sonucu** (iptal / tazminat miktarı / YD). Her vakıa bir delile bağlanır.
3. **Yürütmenin durdurulması (İYUK m.27)**: İki koşul birlikte: **(a) işlemin açıkça hukuka aykırılığı ve (b) telafisi güç/imkânsız zarar.** Yıkım, inşaatın başlaması, parselin elden çıkması gibi geri dönülemez sonuçlar zarar koşulunu, üst plana/yönetmeliğe aykırılık hukuka aykırılık koşulunu somutlaştırır. Gerekçe iki koşulu da ayrı ayrı işlemelidir.
4. **İspat yükü kurgusu**: İşlemin hukuka uygunluğunu idare savunur; davacı sakatlığı ve menfaat ihlalini somut delille gösterir. Bilirkişi/keşif talebi dilekçede istenir.
5. **Yer tutucu disiplini**: Bilinmeyen veriler `[doldurulacak]` ile bırakılır; uydurma tarih/sayı/karar yazılmaz. İçtihat gerekiyorsa ilkesel atıf + `[doğrulanacak]` ve karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynak notu.
6. **Ara sonuç**: Süre, husumet ve talep sonucu son kez kontrol edilir; harç/gider ve ekler listesi tamamlanır.

## Çıktı modülleri
- İYUK formatlı dava dilekçesi iskeleti (vakıa-sebep-talep).
- YD talebi gerekçe bloğu (iki koşul ayrı).
- Delil listesi ve bilirkişi/keşif talep paragrafı.
- Üst makama başvuru/itiraz dilekçesi alternatifi.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
