---
name: patent-tasarim-tecavuz
description: "Patent, faydalı model veya tasarım hakkına tecavüz iddiasında istem/görünüm karşılaştırması, koruma kapsamı ve eşdeğerler doktrini ile yenilik-ayırt edicilik değerlendirmesi gerektiğinde kullanılır."
---

# Patent ve Tasarım Tecavüz Denetimi

## Görev
Patent/faydalı model veya tasarım hakkına tecavüz iddiasını koruma kapsamı (istem yorumu yahut tescilli görünüm) çerçevesinde teknik karşılaştırma ile denetlemek.

## Soğuk başlangıç (intake)
- Hak patent mi, faydalı model mi, tasarım mı; tescil no ve koruma süresi nedir?
- İhlal iddia edilen ürün/sürecin teknik özellikleri/görünümü nedir?
- Patentte bağımsız istemler nelerdir; tasarımda tescilli görseller hangileri?
- Hükümsüzlük (yenilik/buluş basamağı eksikliği) karşı iddiası var mı?

## Denetim şeması
1. Koruma kapsamı (patent): Kapsam istemlerle belirlenir; tarifname ve resimler yorumda kullanılır (SMK m.89). Bağımsız istemin tüm unsurları ürün/süreçte varsa birebir tecavüz; eşdeğerler doktrini (m.89/5) ile fonksiyon-yol-sonuç özdeşliği değerlendirilir.
2. Faydalı model: Buluş basamağı aranmaz (SMK m.142); tecavüz incelemesi istem temelli aynı mantıkla yapılır.
3. Tasarım: Koruma tescilli görünümle sınırlıdır; tecavüz, bilgilenmiş kullanıcıda aynı genel izlenimi yaratıp yaratmadığına göre belirlenir (SMK m.55-56, m.81). Seçenek özgürlüğü ölçütü dikkate alınır.
4. Hükümsüzlük savunması: Patentte yenilik/buluş basamağı/sanayiye uygulanabilirlik eksikliği (SMK m.138 atfıyla m.82-83); tasarımda yenilik ve ayırt edici nitelik eksikliği (m.77 atfıyla m.56). Tekniğin bilinen durumu delillerle (önceki yayın, kullanım) ortaya konur. İspat yükü hükümsüzlüğü ileri sürende.
5. Bilirkişi: Teknik karşılaştırma için uzman bilirkişi şarttır; istem haritalama tablosu hazırlanır.
6. Ara sonuç: Tecavüz sabit ve hak geçerliyse SMK m.149-151 talepleri kurgulanır; çalışan buluşu/ön kullanım hakkı (m.87) ayrıca tartılır.

## Çıktı modülleri
- İstem haritalama / görünüm karşılaştırma tablosu.
- Hükümsüzlük risk değerlendirmesi.
- Bilirkişi sorularının taslağı.

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
