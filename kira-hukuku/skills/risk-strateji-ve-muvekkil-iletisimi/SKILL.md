---
name: risk-strateji-ve-muvekkil-iletisimi
description: "Kira dosyasında kiraya veren veya kiracı vekili olarak strateji kurarken, dava ile sulh/uzlaşma arasında seçim yaparken, riskleri tartarken ya da müvekkile durumu sade dille anlatırken bu beceriyi kullan."
---

# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Kira dosyasında tarafın (kiraya veren/kiracı) konumunu bütüncül değerlendirmek; dava, icra, sulh ve arabuluculuk seçeneklerini süre-maliyet-başarı ekseninde tartmak; müvekkile gerçekçi, sade ve doğru bir tablo sunmak.

## Soğuk başlangıç (intake)
- Müvekkil hangi taraf, asıl hedefi ne (tahliye, bedel, süre kazanma)?
- Eldeki belgeler güçlü mü; zayıf noktalar neler?
- Karşı tarafın muhtemel tutumu ve ödeme gücü?
- Zaman baskısı var mı (ihtiyaç, satış, yeni kiracı)?

## Denetim şeması
1. **Pozisyon analizi**: Uygulanabilir tahliye/talep sebebi başına şekil-süre-ispat şartlarının somut olayda tamam olup olmadığı; en güçlü dayanağın seçimi.
2. **Yol karşılaştırması**: (a) İlamsız tahliye icrası — hızlı ama itirazla genel yargıya düşme riski; (b) tahliye davası — sonuç kesin ama süre uzun; (c) dava şartı arabuluculuk/sulh — hız ve tahsil avantajı, esneklik. Her yolun süre, harç/masraf ve tahsil edilebilirlik riski tartılır.
3. **Risk haritası**: Hak düşürücü sürenin kaçırılması, geçersiz tahliye taahhüdü, eksik ihtar, emredici hükme aykırı sözleşme kaydı, yeniden kiralama yasağı (m.355) gibi tipik tuzaklar işaretlenir.
4. **Karşı tarafın savunması**: Olası def'iler (ödeme, ihtarın geçersizliği, ihtiyacın samimi olmaması) önceden listelenir; her birine yanıt hazırlanır.
5. **Müvekkil iletişimi**: Hukuki dil sadeleştirilerek; kesinlik vaadi verilmeden, en iyi/orta/kötü senaryo ve tahmini süre-maliyet aktarılır; karar müvekkile bırakılır.
6. **Ara sonuç**: Önerilen strateji + gerekçe + bir sonraki somut adım ve süre.

## Çıktı modülleri
- Senaryo bazlı strateji notu (en iyi/orta/kötü).
- Risk ve tuzak kontrol listesi.
- Müvekkile yönelik sade bilgilendirme metni.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
