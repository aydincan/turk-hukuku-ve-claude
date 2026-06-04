---
name: marka-tecavuzu-ve-onleme
description: "İzinsiz kullanım, taklit, iltibas veya benzer işaretle marka hakkına saldırı söz konusuysa; m.29 tecavüz hallerini ve m.149-150 dava taleplerini denetlemek için kullanılır."
---

# Marka Hakkına Tecavüz ve Önleme

## Görev
Tescilli marka hakkına yönelik saldırıyı SMK m.29 (tecavüz sayılan haller) ve m.7 (yasaklama yetkisi) çerçevesinde tespit etmek; m.149-150 kapsamında tecavüzün önlenmesi/durdurulması/kaldırılması ve sonuçlarının giderilmesi taleplerini kurmak.

## Soğuk başlangıç (intake)
- Marka tescilli mi; tecavüz iddiası hangi mal/hizmette?
- Karşı tarafın kullanımı aynı işaret-aynı mal mı, benzer mi (iltibas)?
- Karşı tarafın kendi tescili/önceki hakkı/dürüst kullanım savunması var mı?
- Tecavüz devam ediyor mu (tedbir aciliyeti)?

## Denetim şeması
1. **Hakkın varlığı.** Geçerli ve devam eden marka tescili; kapsamı (mal/hizmet ve işaret) m.7'ye göre belirlenir.
2. **Tecavüz halleri (m.29).** İzinsiz kullanım (m.7 ihlali); markayı taklit; tecavüz yoluyla kullanılan ürünleri satma/dağıtma/ticari amaçla elde bulundurma; izinsiz lisans/devir. Marka sahibinin izninin yokluğu esastır.
3. **İltibas ve karıştırılma.** Aynı işaret-aynı mal doğrudan; benzer işaret-benzer mal hâlinde karıştırılma ihtimali (m.7/2) aranır.
4. **Savunmalar.** Karşı tarafın geçerli tescili (tescilli markanın kullanımı tek başına savunma değildir; hükümsüzlük gündeme gelir), dürüst kullanım (m.7/5), hakkın tüketilmesi (m.152), önceye dayalı hak.
5. **Talepler (m.149).** Tecavüzün tespiti, men'i (önlenmesi), ref'i (giderilmesi), ürünlere el konulması/imhası, üretim araçlarına el konulması, kararın ilanı; ayrıca tazminat (ayrı şema).
6. **İhtiyati tedbir (m.159).** Tecavüzün durdurulması/önlenmesi için yargılama öncesi/sırasında tedbir; teminat ve aciliyet değerlendirilir.

## Çıktı modülleri
- Tecavüz hali-madde eşleştirmesi ve delil listesi.
- Talepler kataloğu (tespit/men/ref/imha/ilan).
- İhtiyati tedbir gerekçe taslağı; ihtarname iskeleti.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
