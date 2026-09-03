---
name: vekalet-sozlesmesi-ve-ucret
description: "Müvekkil ile avukatlık sözleşmesi kurulurken, ücret ve masraf yapısı belirlenirken veya ücret uyuşmazlığı, azil-istifa halinde ücret hesabı yapılırken kullanılır."
---

# Avukatlık Sözleşmesi ve Vekâlet Ücreti

## Görev
Avukat-müvekkil ilişkisinin maddi çerçevesini kurmak: işin kapsamı, ücret tipi, masraf paylaşımı, azil/istifa halinde ücretin akıbeti ve karşı taraf vekâlet ücretini sözleşmeye doğru yansıtmak.

## Soğuk başlangıç (intake)
1. İş ne (dava/danışmanlık/işlem) ve değeri belirli mi?
2. Ücret nasıl kurgulanacak: maktu, nispi (değer üzerinden), saatlik, başarıya bağlı kısım?
3. Masraflar (harç, gider avansı, bilirkişi, yol) kim öder, avans alınacak mı?
4. İlişki şu an mı kuruluyor, yoksa süren bir işte azil/istifa mı söz konusu?

## Denetim şeması
1. **Sözleşmenin kurulması (1136 m.163)**: Avukatlık sözleşmesi serbestçe düzenlenir ancak yazılı olması ispat ve uyuşmazlık önleme açısından esastır. Kapsam (hangi dava/işlem, hangi aşamalar — istinaf/temyiz dahil mi) açıkça yazılır.
2. **Ücretin belirlenmesi (1136 m.164)**: Ücret sözleşme ile kararlaştırılır. Dava değerinin %25'ini aşan başarıya bağlı (nispi) kısım sınırlarına ve Avukatlık Asgari Ücret Tarifesi tabanına dikkat edilir; tarife altı geçersizdir, sözleşme yoksa tarife uygulanır.
3. **Karşı taraf vekâlet ücreti (1136 m.164/son)**: Yargılama gideri olarak hükmedilen vekâlet ücreti, aksi yazılmadıkça avukata aittir; bu kalem müvekkille ödenecek ücretten ayrıdır, sözleşmede netleştirilir.
4. **Masraf ve avans**: Harç/gider avansı (HMK m.120) ve masraflar müvekkile aittir; alınacak avans ve mahsup düzeni yazılır.
5. **Azil ve istifa (1136 m.174)**: Haklı sebep olmadan azil halinde ücretin tamamı; haksız istifada ücret talep edilemeyebilir. Hapis hakkı (m.166) ile dosya/evrak üzerinde ücret alacağı güvencesi değerlendirilir.
6. **Ara sonuç**: Kapsam + ücret tipi + masraf + sona erme senaryoları sözleşmede karşılanmışsa metin tamamdır.

## Çıktı modülleri
- Avukatlık sözleşmesi taslağı (kapsam, ücret, masraf, fesih/azil maddeleri).
- Ücret hesap tablosu (maktu/nispi/saatlik senaryoları).
- Azil/istifa halinde ücret değerlendirme notu.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
