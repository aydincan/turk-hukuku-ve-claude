---
name: risk-strateji-muvekkil
description: "Dava açmadan önce ihtarname/cease and desist, tedbir-esas-ceza yol seçimi, kazanma şansı ve maliyet değerlendirmesi ile müvekkile sade dilde risk haritası ve strateji önerisi sunmak gerektiğinde kullanılır."
---

# Risk, Strateji ve Müvekkil İletişimi

## Görev
Uyuşmazlığa girmeden önce hak sahibinin (veya tecavüzle suçlanan tarafın) stratejik konumunu değerlendirmek; ihtar, müzakere, tedbir, dava ve ceza seçenekleri arasında gerekçeli yol önermek ve müvekkile sade dilde aktarmak.

## Soğuk başlangıç (intake)
- Müvekkil hak sahibi mi, tecavüzle suçlanan taraf mı?
- Öncelik hızlı durdurma mı, tazminat mı, ticari ilişkiyi korumak mı?
- Karşı tarafın hükümsüzlük/kullanmama gibi karşı kozları var mı?
- Bütçe, zaman ve kamuoyu/itibar hassasiyeti nedir?

## Denetim şeması
1. Konum tespiti: Hakkın geçerliliği (sicil, kullanım kanıtı), tecavüzün gücü ve karşı tarafın olası savunmaları (kullanmama m.19, hükümsüzlük, önceki hak) birlikte tartılır; zayıf hak üzerine agresif dava tedbir tazminatı riski doğurur.
2. İhtar adımı: Çoğu olayda ihtarname/cease and desist ile durdurma ve müzakere denenir; ihtar, sonraki tedbir talebinde kötüniyeti ve devam eden tecavüzü belgeler. Ancak ihtar, karşı tarafa delil karartma fırsatı verebilir — gizli delil tespiti/tedbir önceliği değerlendirilir.
3. Yol seçimi: (a) sadece hukuk (tedbir+tecavüz+tazminat), (b) ceza eklemek (caydırıcılık, arama), (c) idari yol (hükümsüzlük/iptal için TÜRKPATENT/Ankara FSHM). Maliyet, süre ve kanıt gücü matrisi kurulur.
4. Karşı taraf temsili: Tecavüzle suçlanan müvekkilde önce hakkın geçerliliği ve kullanım kapsamı sorgulanır; hükümsüzlük/kullanmama def'i ile savunma kurgulanır, sulh seçeneği tartılır.
5. Müvekkil iletişimi: Olasılıklar yüzde kesinlik vaadi olmadan; en iyi/orta/kötü senaryo ve tahmini süre-maliyet sade dille sunulur. Karar müvekkilindir; yazılı bilgilendirme alınır.

## Çıktı modülleri
- Risk haritası (hak gücü / tecavüz gücü / karşı koz / senaryo).
- Yol seçimi karşılaştırma tablosu.
- Müvekkile sade dilde strateji notu ve ihtarname taslağı.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
