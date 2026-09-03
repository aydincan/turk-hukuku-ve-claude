---
name: yonetici-sorumlulugu-553
description: "Yönetim kurulu üyeleri, müdürler, kurucular veya denetçiler aleyhine kusurla verdikleri zarardan doğan hukuki sorumluluk, farklılaştırılmış teselsül, ibra ve zamanaşımı (TTK m.549-561) gündeme geldiğinde; sorumluluk davasının unsurlarını ve savunmaları kurmak için kullanılır."
---

# Yönetici ve Kurucu Sorumluluğu (TTK m.553 vd.)

## Görev
Şirkete, pay sahiplerine veya alacaklılara verilen zarardan doğan yönetici/kurucu/denetçi sorumluluğunu unsurlarıyla kurmak veya savunmak; teselsül, ibra ve zamanaşımını işletmek.

## Soğuk başlangıç (intake)
1. Sorumlu tutulan kim (YK üyesi, müdür, kurucu, denetçi) ve hangi fiil?
2. Zarar kimde doğdu: şirkette mi (dolayısıyla pay sahibi/alacaklı), doğrudan pay sahibinde mi?
3. İhlal edilen yükümlülük hangi kanun/sözleşme hükmü; özen/bağlılık ihlali mi (m.369)?
4. İbra kararı var mı; kim, ne zaman, hangi kapsamda?
5. Zararı ve sorumluyu öğrenme tarihi; fiilden bu yana geçen süre?

## Denetim şeması
1. Sorumluluk halleri: kuruluş/sermaye taahhüt belgelerinin gerçeğe aykırılığı, sermaye hakkında yanlış beyan (m.549-551); m.553 genel hüküm — kurucular, YK üyeleri, yöneticiler ve tasfiye memurları kanun ve esas sözleşmeden doğan yükümlülüklerini kusurlarıyla ihlal ederlerse verdikleri zarardan sorumlu.
2. Unsurlar: (i) sıfat, (ii) yükümlülük ihlali (m.369 özen/bağlılık, m.375 devredilemez yetki, ilgili özel hüküm), (iii) kusur, (iv) zarar, (v) illiyet bağı. Kusursuzluğunu ispat eden sorumlu olmaz (m.553/3 — kontrol dışı sebep).
3. Davacı ve zarar türü: Şirket ve pay sahibi (dolayısıyla zararda tazminat şirkete ödenir, m.555); alacaklılar şirketin iflası halinde (m.556). Doğrudan zararda pay sahibi/alacaklı kendi adına.
4. Farklılaştırılmış teselsül: m.557 — birden çok kişi aynı zarardan sorumluysa, kusur ve durumun gereklerine göre teselsül; rücu m.557/2.
5. İbra ve dava: Genel kurul ibrası ibra edilen konularda dava hakkını düşürür (m.558); ibraya olumsuz oy veren/sonradan pay alan için m.558/2; dava açma kararı ve azlık m.559.
6. Zamanaşımı: m.560 — zararı ve sorumluyu öğrenmeden iki yıl, her hâlde fiilden beş yıl; fiil suç oluşturuyor ve TCK'da daha uzun zamanaşımı varsa o uygulanır.
7. Kamu alacağı paralel sorumluluk: VUK m.10, 6183 mük. m.35 (vergi/prim borçları) ayrıca değerlendirilir.

## Çıktı modülleri
- Sorumluluk unsur analizi ve kusur/illiyet değerlendirmesi.
- Sorumluluk davası dilekçesi veya savunma iskeleti (zamanaşımı/ibra def'ileri).
- Teselsül ve rücu haritası.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
