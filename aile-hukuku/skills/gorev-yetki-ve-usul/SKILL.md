---
name: gorev-yetki-ve-usul
description: "Açılacak davanın görevli mahkemesini (aile mahkemesi), yetkili yer mahkemesini, yargılama usulünü, tedbir taleplerini ve harç durumunu belirlemek; istinaf-temyiz yolunu planlamak gerektiğinde kullanılır."
---

# Aile Davalarında Görev, Yetki ve Usul

## Görev
Aile hukuku uyuşmazlığında doğru mahkemeyi, yetkili yeri, yargılama usulünü, geçici hukuki korumayı ve kanun yolu rejimini belirleyerek usuli hataları önlemek.

## Soğuk başlangıç (intake)
1. Talep türü nedir (boşanma, nafaka, velayet, tasfiye, soybağı, koruma)?
2. Tarafların yerleşim yeri ve son birlikte oturdukları yer neresi?
3. Yabancı unsur veya yurt dışında verilmiş karar var mı (tanıma-tenfiz)?
4. Acil tedbir (tedbir nafakası, çocukla kişisel ilişki, 6284) gerekiyor mu?

## Denetim şeması
1. **Görev.** Aile hukukundan doğan dava ve işlerde görevli mahkeme **aile mahkemesidir** (4787 sK. m.4); aile mahkemesi bulunmayan yerlerde asliye hukuk mahkemesi bu sıfatla bakar. Görev kamu düzenindendir, re'sen gözetilir (HMK m.114/1-c, m.115).
2. **Yetki.** Boşanma/ayrılıkta yetkili mahkeme, eşlerden birinin yerleşim yeri veya davadan önce son defa altı aydan beri birlikte oturdukları yer mahkemesidir (TMK m.168). Nafaka davalarında nafaka alacaklısının yerleşim yeri mahkemesi de yetkilidir (HMK m.9 ve özel kural). 6284 başvurusunda mağdurun yerleşim yeri/şiddetin yapıldığı yer aile mahkemesi yetkilidir.
3. **Usul.** Boşanma ve fer'ileri yazılı yargılama usulüne (HMK m.118 vd.); dilekçeler aşaması, ön inceleme (m.137-142), tahkikat sırasıyla işler. Boşanmada hâkim re'sen araştırma ilkesini sınırlı uygular; tarafların üzerinde serbestçe tasarruf edemeyeceği konularda (çocuk, kamu düzeni) re'sen delil toplanabilir.
4. **Geçici hukuki koruma.** Dava süresince eş ve çocuk için tedbir nafakası, velayet, kişisel ilişki ve barınma tedbirleri (TMK m.169, m.182); ihtiyati tedbir (HMK m.389 vd.) mal kaçırma riskinde.
5. **Kanun yolu.** Aile mahkemesi kararlarına karşı istinaf (HMK m.341 vd.) ve kesinlik sınırı üstünde temyiz (m.361 vd.). Boşanma hükmü kesinleşmeden nüfusa işlenmez; fer'iler de bu ana bağlıdır.
6. **Yabancı unsur.** Yurt dışı boşanma kararının tanınması-tenfizi (5718 sK. MÖHUK m.50 vd.) veya nüfusta tescili (idari yol).

## Çıktı modülleri
- Görev-yetki-usul tespit notu ve dayanak maddeler.
- Geçici tedbir talep listesi.
- Kanun yolu ve süre takvimi (istinaf/temyiz) ile tanıma-tenfiz uyarısı.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
