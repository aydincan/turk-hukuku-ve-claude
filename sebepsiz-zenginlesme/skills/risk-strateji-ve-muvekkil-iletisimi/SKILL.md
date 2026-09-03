---
name: risk-strateji-ve-muvekkil-iletisimi
description: "Sebepsiz zenginleşme uyuşmazlığında dava/sulh seçeneklerini tartmak, kazanma olasılığı ve maliyet-fayda analizi yapmak ve müvekkile anlaşılır bir yol haritası sunmak gerektiğinde kullanılır."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
İade uyuşmazlığında hukuki pozisyonu gerçekçi tartmak; talep seçimi, süre ve ispat zayıflıklarını öne koymak; dava/sulh/ihtar seçeneklerini maliyet-fayda ekseninde değerlendirip müvekkile sade ve dürüst bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (parayı geri almak, aynen iade, ilişkiyi tasfiye etmek)?
- Eldeki delillerin gücü ve karşı tarafın muhtemel savunması (bağışlama, geçerli sebep, zamanaşımı)?
- Zaman baskısı (yaklaşan iki/on yıllık süre)?
- Risk iştahı ve bütçe (harç, vekâlet ücreti, bilirkişi)?

## Denetim şeması
1. **Pozisyon analizi.** Dört unsuru (m.77) ve seçilen tipi delil gücüyle altla; en zayıf halkayı belirle. Tipik zayıflıklar: haklı sebebin yokluğunun ispatı, yanılarak ödemenin (m.78) ispatı, öğrenme tarihinin (m.82) belirsizliği, karşı tarafın bağışlama savunması.
2. **Talep ve süre stratejisi.** Yarışan talep (istihkak/sözleşme/haksız fiil) varsa süre ve miktar avantajına göre birincil talebi, sebepsiz zenginleşmeyi yedek (terditli) kur. Zamanaşımı yakınsa derhal kesen işlem (dava/takip) planla.
3. **Senaryo matrisi.** En iyi/orta/en kötü sonuç; kazanma olasılığı kaba bant (yüksek/orta/düşük) olarak verilir, kesin oran vaadinden kaçınılır. Karşı tarafın m.79 (elden çıkma) ve m.81 (ahlaka aykırılık) savunmaları değerlendirilir.
4. **Maliyet-fayda.** Tahmini harç/giderler, yargılama süresi (istinaf/temyiz dahil), tahsil kabiliyeti (karşı tarafın ödeme gücü). İade miktarı ölçü olduğundan, faiz ve semere kalemleriyle gerçek getiri hesaplanır.
5. **Strateji seçimi.** İhtar → (gerekirse) arabuluculuk → dava sıralaması; ihtiyati haciz (İİK m.257) gereği değerlendirilir; sulh için makul aralık ve kozlar (zamanaşımı riski, ispat zorluğu) belirlenir.
6. **Müvekkil iletişimi.** Sonuç sade Türkçe ile; seçeneklerin artı/eksisi, önerilen adım ve varsayımlar/`[doğrulanacak]` veriler açıkça yazılır. Kesin kazanç taahhüdü verilmez. Ara sonuç: önerilen yol + gerekçe + sonraki adım listesi.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti.
- Müvekkile sade bilgilendirme notu ve aksiyon planı.

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
