---
name: strateji-risk-ve-muvekkil-iletisimi
description: "Tazminat dosyasında dava açma, sulh veya bekleme arasında karar verirken; pozisyonun gücünü, maliyet-faydayı ve tahsil riskini değerlendirip müvekkile sade bir yol haritası sunmak için kullanılır."
---

# Strateji, Risk ve Müvekkil İletişimi

## Görev
Haksız fiil dosyasında pozisyonu değerlendirmek, dava/sulh/bekleme seçeneklerini maliyet-fayda ve tahsil riski üzerinden tartmak ve müvekkile sade Türkçe ile gerekçeli bir yol haritası sunmak. Kesin kazanç vaadi verilmez; varsayımlar açıkça yazılır.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (tazminat tahsili, ilkesel sonuç, hızlı çözüm)?
- Delillerin gücü ve karşı tarafın muhtemel savunması (hukuka uygunluk, müterafik kusur, zamanaşımı)?
- Zaman baskısı (yaklaşan zamanaşımı/öğrenme süresi)?
- Karşı tarafın ödeme gücü ve müvekkilin risk-bütçe iştahı?

## Denetim şeması
1. **Pozisyon analizi.** Beş unsuru ve indirim sebeplerini delil gücüyle altla; zayıf halkayı (örn. illiyet ispatı, öğrenme tarihi belirsizliği) belirginleştir. Kusursuz sorumluluk normunun varlığı pozisyonu güçlendirir.
2. **Senaryo matrisi.** En iyi/orta/en kötü sonuç ve kazanma olasılığı kaba bant (yüksek/orta/düşük) olarak; kesin oran vaadinden kaçınılır. İndirim ve müterafik kusur etkisi tahmini tutara yansıtılır.
3. **Maliyet-fayda.** Nispi harç, bilirkişi/aktüer gideri, yargılama süresi (istinaf/temyiz), tahsil kabiliyeti (karşı tarafın/sigortanın ödeme gücü). Düşük tutarlı/yüksek belirsizlikli işte sulh öne alınır.
4. **Süre ve usul riski.** Yakın zamanaşımı (m.72), görev-yetki hatası, dava türü seçimi gibi riskler önceliklenir; gerekirse ihtiyati haciz/tedbir (İİK m.257; HMK m.389) değerlendirilir.
5. **Strateji seçimi.** İhtarname → müzakere/sulh → dava sıralaması; sigortacıya doğrudan başvuru imkânı; delil tespiti ihtiyacı (HMK m.400). Sulh için makul aralık ve kozlar belirlenir.
6. **Müvekkil iletişimi.** Hukuki sonuç sade Türkçe ile; seçeneklerin artı/eksisi, önerilen adım ve varsayımlar açık yazılır; `[doğrulanacak]` veriler ve kesin kazanç taahhüdü verilmediği belirtilir. Ara sonuç: önerilen yol + gerekçe + sonraki adımlar.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti (sulh aralığı dahil).
- Müvekkile sade bilgilendirme notu ve aksiyon planı.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
