---
name: esitlik-ve-ayrimcilik
description: "Bir kural veya uygulamanın Anayasa m.10 eşitlik ilkesine veya ayrımcılık yasağına aykırı olup olmadığını değerlendirmek; karşılaştırılabilir durum, farklı muamele ve haklı sebep analizinin gerektiği hallerde kullanılır."
---

# Eşitlik İlkesi ve Ayrımcılık Yasağı

## Görev
Bir norm veya uygulamanın Anayasa m.10 (kanun önünde eşitlik) ve m.13 ile birlikte ayrımcılık yasağına uygunluğunu denetlemek; eşit olanlara eşit, farklı olanlara farklı muamele mantığını somut olaya uygulamak.

## Soğuk başlangıç (intake)
1. Şikâyet konusu farklı muamele kim/hangi grup arasında yapılıyor?
2. Karşılaştırılan durumlar gerçekten benzer (karşılaştırılabilir) mi?
3. Farklı muamelenin dayandığı ölçüt ne (cinsiyet, yaş, statü, ekonomik durum)?
4. Bu ölçüt, AİHS Ek 12 No.lu Protokol / AİHS m.14 kapsamında şüpheli bir kategori mi?

## Denetim şeması
1. **Karşılaştırılabilirlik.** İki durum/grup hukuken benzer konumda mı? Benzer değillerse eşitlik ihlali kural olarak doğmaz; farklı muamele meşru olabilir.
2. **Farklı muamele tespiti.** Aynı durumdakilere farklı, farklı durumdakilere aynı muamele var mı? Doğrudan ve dolaylı ayrımcılık ayrımını gözetin.
3. **Haklı sebep testi.** Farklı muamelenin objektif ve makul bir dayanağı var mı, meşru bir amaca yöneliyor mu? (m.10 ile m.13 birlikte). Ara sonuç: haklı sebep yoksa ayrımcılık vardır.
4. **Ölçülülük.** Haklı sebep varsa dahi, kullanılan ayrım aracı ile amaç arasında orantı bulunmalı; aşırı ya da gereksiz farklılaştırma aykırıdır.
5. **Şüpheli kategoriler.** Cinsiyet, ırk, din gibi ölçütlerde daha sıkı denetim uygulanır; kamu makamının ispat yükü ağırlaşır.
İspat: farklı muameleyi başvurucu gösterir; bunun haklı ve orantılı olduğunu kamu makamı temellendirir. AYM ve AİHM eşitlik içtihadına ilke düzeyinde atıf yapın, künyeyi `[doğrulanacak]` işaretleyin.

## Çıktı modülleri
- Karşılaştırma matrisi (gruplar, muamele farkı, ölçüt, haklı sebep değerlendirmesi).
- Doğrudan/dolaylı ayrımcılık nitelendirmesi ve sonuç.
- Norm denetimi veya bireysel başvuru için eşitlik gerekçesi taslağı.

## Plugin bağlamı

Bu beceri `anayasa-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
