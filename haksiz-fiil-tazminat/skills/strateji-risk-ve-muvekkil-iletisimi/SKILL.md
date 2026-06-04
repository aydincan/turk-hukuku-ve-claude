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
