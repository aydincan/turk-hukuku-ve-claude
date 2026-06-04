---
name: hukumsuzluk-davasi
description: "Tescilli tasarımın SMK m.77 sebepleriyle hükümsüzlüğünün talep edilmesi veya savunulması; yenilik/ayırt edicilik yokluğu, hak sahipliği veya koruma dışılık iddialarının dava yapısına oturtulması gerektiğinde kullanılır."
---

# Hükümsüzlük Davası

## Görev
Tescilli tasarımı geçmişe etkili biçimde ortadan kaldırmak (veya savunmak): hükümsüzlük sebeplerini, husumeti, ispat yükünü ve sonuçlarını yönetmek. Çoğu kez tecavüz davasında karşı dava/savunma olarak kullanılır.

## Soğuk başlangıç (intake)
1. Hangi sebebe dayanılıyor: yenilik yokluğu, ayırt edicilik yokluğu, koruma dışılık, hak sahipliği, kötü niyet?
2. Önceki tasarım(lar) ve tarihleri elimizde mi (yenilik/ayırt edicilik için)?
3. Tasarım hâlen sicilde geçerli mi; koruma süresi devam ediyor mu?
4. Hükümsüzlüğü kim talep ediyor (menfaati olan kişi / Cumhuriyet savcısı / hak sahibi)?

## Denetim şeması
1. Hükümsüzlük sebepleri (SMK m.77/1): (a) m.55-59'daki koruma şartlarının bulunmaması (yenilik/ayırt edicilik yokluğu, koruma dışı görünüm), (b) gerçek hak sahibinin başkası olması (m.77/1-b; bu sebebi yalnız hak sahibi ileri sürebilir), (c) sonraki tasarımın önceki bir hakla çatışması, (ç) kötü niyetli tescil.
2. Husumet ve menfaat (SMK m.77/2-3): Menfaati olanlar, Cumhuriyet savcısı veya ilgili kamu kurumları dava açabilir; hak sahipliği sebebini ise yalnız gerçek hak sahibi/halefi ileri sürür. Dava sicildeki tasarım sahibine yöneltilir; sicilde hak sahibi görünenler de davaya dâhil edilir.
3. İspat yükü: Yenilik/ayırt edicilik yokluğunu ileri süren davacı, önceki tasarımı ve kamuya sunma tarihini ispatla yükümlüdür. Tasarım sahibi grace period (m.58/3) gibi def'ileri ileri sürebilir.
4. Kısmi hükümsüzlük (SMK m.77/5): Çoklu tasarımlarda yalnız bir kısmı için, ya da değişiklikle korunabilirlik sağlanabiliyorsa kısmi hükümsüzlük mümkündür.
5. Sonuç (SMK m.79): Hükümsüzlük kararı geçmişe etkilidir (ex tunc); tasarım hiç doğmamış sayılır. Kesinleşen karar herkese karşı hüküm doğurur ve sicilden terkin edilir. Kesinleşmiş ve uygulanmış tecavüz kararları, iyiniyetle yapılmış sözleşmeler gibi istisnalar saklıdır.
6. Görev/yetki: FSHHM (yoksa görevlendirilen asliye hukuk); yetki SMK m.156 ve HMK genel kuralları.

## Çıktı modülleri
- Hükümsüzlük dava dilekçesi iskeleti (sebep, önceki tasarım delilleri, talep).
- Önceki tasarım karşılaştırma tablosu ve ispat planı.
- Sonuç ve sicil terkini ile istisnalar notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
