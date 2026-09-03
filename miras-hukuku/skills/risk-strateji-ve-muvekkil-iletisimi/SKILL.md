---
name: risk-strateji-ve-muvekkil-iletisimi
description: "Miras dosyasında dava açmadan önce başarı şansı, maliyet, süre ve sulh seçeneklerini tartmak; aile içi uyuşmazlıkta strateji belirlemek ve müvekkile sade, gerçekçi bilgilendirme yapmak gerektiğinde kullanılır."
---

# Risk, Strateji ve Müvekkil İletişimi

## Görev
Miras uyuşmazlığında dava/sulh kararını, başarı olasılığını, maliyet-süre dengesini ve aile dinamiklerini değerlendirip müvekkile anlaşılır bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin önceliği: maksimum pay mı, hız mı, ilişkiyi korumak mı?
- Karşı tarafla anlaşma ihtimali var mı? (aynı aile içi mi?)
- Eldeki delillerin gücü ve zayıf noktalar neler?
- Süre baskısı var mı? (ret 3 ay, tenkis 1 yıl gibi)
- Terekenin değeri dava maliyetini (harç, bilirkişi, vekâlet) karşılıyor mu?

## Denetim şeması
1. **Talep-delil-süre üçlüsünü tart:** Her talebin hukuki dayanağı (örn. tenkis m.560, muvazaa TBK m.19), ispat yükü ve hak düşürücü süre durumu netleştirilir; süresi kaçan talep elenir.
2. **Başarı olasılığı:** Delil gücü, yerleşik içtihat eğilimi (karararama.yargitay.gov.tr — künyeler doğrulanarak), karşı savunma senaryoları. Terditli kurgu (önce muvazaa, sonra tenkis) riski dağıtır.
3. **Maliyet-fayda:** Nispi harç (taşınmazda dava değeri üzerinden), bilirkişi ve keşif gideri, yargılama süresi (yıllarla ölçülen). Beklenen net kazanç ile karşılaştırılır.
4. **Alternatif çözüm:** Miras paylaşımı uyuşmazlıkları arabuluculuğa elverişlidir (HUAK m.1/2 kapsamı); aile içi onarıcı bir sulh çoğu zaman uzun davadan üstündür. Paylaşma sözleşmesi (m.676) ile çözüm değerlendirilir.
5. **İletişim disiplini:** Müvekkile süre riskleri yazılı bildirilir; gerçekçi olmayan beklenti düzeltilir; karar müvekkilindir, hukukçu seçenekleri ve olasılıkları sunar. Çıkar çatışması (birden çok mirasçının temsili) taranır.
6. **Ara sonuç:** önerilen strateji, alternatif senaryolar, müvekkil onayına sunulacak karar noktaları.

## Çıktı modülleri
- Risk haritası (talep / olasılık / maliyet / süre)
- Strateji notu (dava / sulh / terditli kurgu)
- Müvekkile sade dilde bilgilendirme metni
- Sulh/paylaşma teklifi taslağı ve müzakere notu

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
