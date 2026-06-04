---
name: ozel-kanun-kabahatleri
description: "Trafik, belediye-zabıta, tütün, çevre, gıda, iş sağlığı gibi özel kanunlardaki kabahatlerde özel hüküm ile 5326 genel hükümleri arasındaki ilişkiyi kurmak ve sektöre özgü usulü uygulamak gerektiğinde kullanılır."
---

# Özel Kanun Kabahatleri ve Sektörel Uygulama

## Görev
Özel kanunla düzenlenmiş bir kabahatte (KTK, belediye/zabıta, tütün, çevre vb.), özel hükmün önceliğini ve 5326 genel hükümlerinin tamamlayıcı uygulamasını kurarak doğru usulü işletmek.

## Soğuk başlangıç (intake)
- Hangi özel kanun ve hangi madde uygulanmış?
- Özel kanun başvuru yolunu/süreyi ayrıca düzenlemiş mi?
- Yaptırımı veren idare özel kanunda yetkili kılınmış mı?
- Tutanak/karar özel kanunun aradığı şekil şartlarını taşıyor mu?

## Denetim şeması
1. **Genel-özel ilişkisi (5326 m.3):** Tanım, miktar ve usul özel kanunda varsa o uygulanır; boşluk kalan her noktada 5326 genel hükümleri (kast-taksir m.9, içtima m.15, zamanaşımı m.20-21, başvuru m.27) tamamlar.
2. **Trafik (2918 KTK):** İdari para cezası tutanağı; başvuru yolu kural olarak sulh ceza hâkimliği (5326 m.27), ancak sürücü belgesi geri alma gibi işlemlerde idari yargı görev ayrımını kontrol et.
3. **Belediye/zabıta (5393, 1608):** Zabıta tutanaklarına dayanan idari yaptırımlar; encümen/belediye yetkisi ve tebligat denetlenir.
4. **Çevre (2872):** İdari para cezaları ve idari tedbirler; bazı işlemler idari yargının görev alanına girebilir (5326 m.27/8 ayrımı belirleyici).
5. **Tütün (4207), gıda, İSG (6331):** Özel kanundaki miktar ve nispi/maktu yapı esas alınır; takdir ölçütleri (5326 m.17/2) gösterilmeli.
6. **Yargı yolu kontrolü:** Özel kanun aksini öngörmedikçe başvuru sulh ceza hâkimliğine; idari işlemle bütünleşen yaptırımlarda idari yargı. Ara sonuç olarak doğru mercii sabitle.

İspat yükü idarede; sektöre özgü teknik tespitlerin (cihaz, numune) usulü ayrıca denetlenir.

## Çıktı modülleri
- Özel kanun + 5326 eşleştirme tablosu.
- Yargı yolu tespiti (sulh ceza mı / idari yargı mı).
- Sektörel şekil-şart kontrol listesi.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
