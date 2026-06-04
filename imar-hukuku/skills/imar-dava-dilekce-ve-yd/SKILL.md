---
name: imar-dava-dilekce-ve-yd
description: "İmar uyuşmazlığında iptal veya tam yargı dilekçesi, yürütmenin durdurulması talebi ya da idari başvuru/itiraz dilekçesi hazırlanacağında; vakıa-hukuki sebep-talep mimarisi ve YD koşulları sorulduğunda kullanılır."
---

# İmar Davası Dilekçesi ve Yürütmenin Durdurulması

## Görev
İmar uyuşmazlığına uygun, İYUK formatında dava/başvuru dilekçesi üretmek; yürütmenin durdurulması talebini gerekçeli kurmak.

## Soğuk başlangıç (intake)
- Dava türü iptal mi, tam yargı mı, ikisi birlikte mi?
- Dava konusu işlem ve tarafları (davalı idare) net mi?
- Süre durumu uygun mu, YD talebi gerekiyor mu?
- Eldeki belgeler ve talep edilen sonuç (iptal/tazminat tutarı) ne?

## Denetim şeması
1. **Dava türü ve taraf (İYUK m.2)**: İptal davası (yetki-şekil-sebep-konu-maksat sakatlığı) mı, tam yargı (tazminat/el atma) mı belirlenir; davalı idare doğru gösterilir (işlemi tesis eden makam). Husumet hatası ret riskidir.
2. **Dilekçe mimarisi (İYUK m.3)**: Taraflar, konu, **tebliğ/öğrenme tarihi**, vakıalar (olay kronolojisi), hukuki sebepler (3194 ilgili maddeleri + İYUK + Anayasa m.35), deliller ve net **talep sonucu** (iptal / tazminat miktarı / YD). Her vakıa bir delile bağlanır.
3. **Yürütmenin durdurulması (İYUK m.27)**: İki koşul birlikte: **(a) işlemin açıkça hukuka aykırılığı ve (b) telafisi güç/imkânsız zarar.** Yıkım, inşaatın başlaması, parselin elden çıkması gibi geri dönülemez sonuçlar zarar koşulunu, üst plana/yönetmeliğe aykırılık hukuka aykırılık koşulunu somutlaştırır. Gerekçe iki koşulu da ayrı ayrı işlemelidir.
4. **İspat yükü kurgusu**: İşlemin hukuka uygunluğunu idare savunur; davacı sakatlığı ve menfaat ihlalini somut delille gösterir. Bilirkişi/keşif talebi dilekçede istenir.
5. **Yer tutucu disiplini**: Bilinmeyen veriler `[doldurulacak]` ile bırakılır; uydurma tarih/sayı/karar yazılmaz. İçtihat gerekiyorsa ilkesel atıf + `[doğrulanacak]` ve karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynak notu.
6. **Ara sonuç**: Süre, husumet ve talep sonucu son kez kontrol edilir; harç/gider ve ekler listesi tamamlanır.

## Çıktı modülleri
- İYUK formatlı dava dilekçesi iskeleti (vakıa-sebep-talep).
- YD talebi gerekçe bloğu (iki koşul ayrı).
- Delil listesi ve bilirkişi/keşif talep paragrafı.
- Üst makama başvuru/itiraz dilekçesi alternatifi.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
