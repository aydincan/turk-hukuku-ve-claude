---
name: metodoloji-dayanak-denetimi
description: "Raporun ulaştığı sonuca hangi yöntem, kabul, varsayım ve veriyle vardığını; gerekçenin denetlenebilir olup olmadığını ve kabullerin dosya gerçeğiyle örtüşüp örtüşmediğini incelemek istendiğinde kullanılır."
---

# Metodoloji ve Bilimsel Dayanak Denetimi

## Görev
Raporun "neden böyle sonuca varıldı" sorusuna verdiği yanıtı denetlemek: yöntem, kabul, varsayım ve veri kaynağı açık mı, dosya verisiyle örtüşüyor mu, sonuç gerekçeyle bağlanmış mı (HMK m.279)?

## Soğuk başlangıç (intake)
- Rapor hangi yöntemi/standardı kullandığını açıkça söylüyor mu?
- Kabuller ve varsayımlar dosyadaki hangi veriye dayanıyor?
- Bilirkişi keşif/inceleme yapmış mı; yoksa eksik veriyle mi çalışmış?
- Sonuç ile gerekçe arasında izlenebilir bir mantık zinciri var mı?

## Denetim şeması
1. **Gerekçe zorunluluğu (HMK m.279):** Rapor; inceleme konusu, gerekçe ve sonuçtan oluşur; bilirkişi kanaatini gerekçeleriyle açıklar. Gerekçesiz "kanaatimce" türü ifadeler denetlenemez; başlı başına itiraz sebebidir.
2. **Yöntem şeffaflığı:** Kullanılan teknik standart, formül veya yöntem adıyla belirtilmeli; "tecrübeye dayanarak" gibi soyut dayanak yetersizdir. Yöntem tekrar uygulandığında aynı sonuca götürebilmeli.
3. **Kabul-veri örtüşmesi:** Her kritik kabul, dosyadaki belge/delile çıpalanır. Dosyada olmayan veya çelişen bir varsayıma dayanan sonuç sakattır. Eksik veriyle çalışılmışsa, eksiğin sonucu nasıl etkilediği gösterilir.
4. **Sonuç-gerekçe bağı:** Gerekçeden mantıken çıkmayan sonuç (atlama/gediği) işaretlenir.
5. **Ara sonuç:** Yöntem eksik açıklanmış ama düzeltilebilir → **ek rapor**; yöntem temelden hatalı veya bilimsel dayanağı yok → **yeni bilirkişi/heyet** (HMK m.281). Karşı uzman mütalaası yöntem eleştirisini güçlendirir.

## Çıktı modülleri
- Yöntem-kabul-veri-sonuç izleme zinciri çıktısı.
- Dosyayla çelişen veya dayanaksız kabullerin listesi.
- Metodolojik itiraz paragrafı taslağı (madde atıflı).
- Karşı uzman görüşüyle desteklenecek noktaların notu.

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
