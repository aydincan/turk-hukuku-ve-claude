---
name: fesih-denetim-semasi
description: "Bir işçinin iş sözleşmesinin feshi planlanıyor veya yapılmış feshin hukuka uygunluğu değerlendirilecekse, geçerli/haklı sebep, usul ve son çare ilkesini adım adım denetlemek için kullanılır."
---

# Fesih Denetim Şeması (Geçerli ve Haklı Sebep)

## Görev
İşveren feshini, iş güvencesi rejimi içinde ayakta kalacak biçimde planlamak veya yapılmış bir feshin işe iade/usulsüzlük riskini ölçmek. Esas + usul + ispat üçlüsünü birlikte denetlemek.

## Soğuk başlangıç (intake)
1. İşyerinde 30+ işçi var mı, işçinin kıdemi 6 ayı geçti mi (iş güvencesi kapsamı)?
2. Fesih sebebi davranış mı, yetersizlik/performans mı, işletme gereği mi, yoksa ahlak ve iyiniyete aykırılık (m.25/II) mı?
3. Olaydan bu yana kaç gün geçti (6 işgünü/m.26)?
4. Yazılı bildirim ve savunma alındı mı, daha hafif tedbir mümkün müydü?

## Denetim şeması
1. **Güvence kapsamı (m.18)**: 30+ işçi, 6 ay kıdem, belirsiz süreli ve işveren vekili olmama → kapsamdaysa **geçerli sebep ve usul** zorunlu.
2. **Sebep tipi**: (a) Geçerli sebep (m.18) = yetersizlik/davranış/işletme gereği; (b) Haklı/derhal sebep (m.25) = sağlık, ahlak ve iyiniyete aykırılık, zorlayıcı sebep. Sebep gerçek, ciddi ve fesihle orantılı olmalı.
3. **Usul (m.19)**: Fesih **yazılı** ve **sebep açıkça** belirtilmeli; m.18 sebepli fesihte (ve içtihaden m.25/II davranışlarda) işçinin **savunması** alınmalı. Savunma alınmadan davranış sebepli fesih usulsüzdür.
4. **Süre (m.26)**: Ahlak ve iyiniyete aykırılık sebepleri, öğrenmeden itibaren **6 işgünü** ve her halde 1 yıl içinde kullanılmalı; geçmesi haklı feshi düşürür.
5. **Son çare (ultima ratio)**: Özellikle işletme gereği ve performansta uyarı/yer değişikliği/eğitim gibi daha hafif yol tüketilmeli (içtihat — `[doğrulanacak]`, karararama.yargitay.gov.tr).
6. **İspat (m.20/2)**: Feshin geçerli/haklı sebebe dayandığını **işveren** ispatlar; eldeki tutanak/ihtar/savunma yeterli mi kontrol et.
7. **Ara sonuç**: Eksik usul → usulsüz/geçersiz fesih; işe iade + boşta geçen süre ücreti + işe başlatmama tazminatı riski.

## Çıktı modülleri
- Fesih risk değerlendirme tablosu (esas/usul/süre/ispat skoru).
- Eksik adım listesi ve giderme önerisi.
- Fesih bildirimi taslağı veya feshi erteleme/alternatif tedbir önerisi.

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
