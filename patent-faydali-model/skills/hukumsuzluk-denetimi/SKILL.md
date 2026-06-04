---
name: hukumsuzluk-denetimi
description: "Bir patentin/faydalı modelin hükümsüz kılınması ya da tecavüz davasında geçersizlik savunması gündeme geldiğinde kullanılır; sebep envanteri ve geçmişe etkili sonuçların değerlendirilmesi için temel beceridir."
---

# Patent ve Faydalı Model Hükümsüzlüğü

## Görev
SMK m.138 hükümsüzlük sebeplerini envanterlemek, dava şartlarını ve husumet ilişkisini kurmak, hükümsüzlüğün SMK m.139 geçmişe etkili sonuçlarını değerlendirmek.

## Soğuk başlangıç (intake)
1. Hangi sebep ileri sürülüyor: yenilik/buluş basamağı yokluğu, yetersiz açıklama, kapsam aşımı, gasp?
2. Elde yeni prior art belgesi var mı; tarihi başvuru/rüçhandan önce mi?
3. Talep eden kimin menfaati var; gerçek hak sahibi iddiası mı?
4. Patentin verdiği zarar/lisans/tecavüz davası var mı (menfaat için)?

## Denetim şeması
1. **Sebepler (SMK m.138/1).** (a) m.82-83 patentlenebilirlik şartının yokluğu (yenilik, buluş basamağı, sanayiye uygulanabilirlik); (b) buluşun yeterince açık ve tam tarif edilmemesi (m.92/4); (c) konunun başvuru kapsamını aşması; (d) patent sahibinin gerçek hak sahibi olmaması (gasp). Ara sonuç: hangi sebep(ler) somut olayda var?
2. **Kısmî hükümsüzlük (SMK m.138/6).** Sebep istemlerin bir kısmına ilişkinse yalnızca o istemler iptal edilir; patent sahibine istem sınırlandırma imkânı tanınır.
3. **Husumet ve menfaat.** Hükümsüzlük davasını menfaati olanlar açabilir; gasp sebebine dayalı hükümsüzlüğü yalnızca gerçek hak sahibi ileri sürebilir (m.138/2-3).
4. **Süre ve sonuç (SMK m.139).** Hükümsüzlük kararı geçmişe etkilidir; koruma baştan doğmamış sayılır. Ancak kesinleşmiş tecavüz kararları, ödenmiş tazminat ve uygulanmış lisans bedellerinde dengeleme (m.139/2-3) ve iyiniyetin korunması değerlendirilir.
5. **Def'i olarak ileri sürme.** Tecavüz davasında hükümsüzlük bir def'i/karşı dava olarak ileri sürülebilir; FSHM'de birlikte görülebilir.

## Çıktı modülleri
- Hükümsüzlük sebebi envanteri (madde-bent eşlemeli).
- Prior art / açıklama / kapsam analizi özeti.
- Kısmî hükümsüzlük ve istem sınırlandırma senaryosu.
- Geçmişe etkili sonuç ve dengeleme uyarısı.

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
