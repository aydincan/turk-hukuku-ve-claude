---
name: mobbing-esit-davranma-ayrimcilik
description: "İşyerinde ayrımcılık, eşit davranma borcu, mobbing/psikolojik taciz iddiası veya bu iddiaları önleyecek süreç tasarımı gündeme geldiğinde kullanılır."
---

# Eşit Davranma, Ayrımcılık ve Mobbing Riski

## Görev
İşverenin eşit davranma borcuna uyumunu sağlamak; ayrımcılık ve mobbing (psikolojik taciz) iddialarını değerlendirmek ve önleyici şikâyet/soruşturma mekanizması kurmak; ispat yükü dağılımını doğru yönetmek.

## Soğuk başlangıç (intake)
1. İddia ne (ücret/terfide ayrımcılık, sendikal ayrım, sistematik yıldırma)?
2. Karşılaştırılabilir emsal çalışan ve farklı muamele somut mu?
3. Davranış süreklilik/sistematiklik taşıyor mu (mobbing ölçütü)?
4. İşyerinde şikâyet/etik hattı ve soruşturma süreci var mı?

## Denetim şeması
1. **Eşit davranma (4857 m.5)**: İşveren, esaslı sebep olmadıkça çalışanlara eşit davranmak zorunda; ihlalde işçi **4 aya kadar ücret tutarında** ayrımcılık tazminatı ve yoksun kaldığı haklarını isteyebilir.
2. **İspat yükü (m.5/son)**: İşçi ayrımcılığı **güçlü olasılıkla** ortaya koyarsa, böyle bir muamelenin olmadığını **işveren** ispatlar. Bu yüzden objektif kriter belgesi şart.
3. **Mobbing**: Yargı, sistematik, süreklilik arz eden, yıldırma kastlı davranışları mobbing sayar; tazminat TBK haksız fiil/kişilik hakkı (TBK m.49, m.58; TMK m.24-25) ve işverenin gözetme borcu (TBK m.417) temelinde değerlendirilir.
4. **İşverenin önleme yükümlülüğü (TBK m.417)**: İşçinin kişiliğini koruma ve sağlıklı ortam sağlama borcu; şikâyeti soruşturmamak başlı başına sorumluluk doğurur.
5. **Süreç tasarımı**: Yazılı şikâyet kanalı, tarafsız soruşturma, tanık beyanı ve karar tutanağı; misilleme yasağı.
6. **Ara sonuç**: Kriter belgesi ve soruşturma kaydı yoksa işveren ispat yükü altında ezilir; tazminat + manevi tazminat riski.

## Çıktı modülleri
- Şikâyet ve iç soruşturma prosedürü taslağı.
- Ayrımcılık/mobbing risk değerlendirme notu.
- Objektif terfi/ücret kriteri çerçevesi.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
