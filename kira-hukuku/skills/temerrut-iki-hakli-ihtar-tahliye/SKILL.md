---
name: temerrut-iki-hakli-ihtar-tahliye
description: "Kiracı kira veya yan gider ödemediğinde, temerrüt nedeniyle tahliye veya iki haklı ihtara dayalı tahliye değerlendirildiğinde ya da ihtarname içeriği ve süreleri tartışıldığında bu beceriyi kullan."
---

# Kira Bedelinin Ödenmemesi, Temerrüt ve İki Haklı İhtar

## Görev
Ödenmeyen kira/yan gider üzerinden temerrüt yoluyla tahliyenin (TBK m.315) ve iki haklı ihtar yoluyla tahliyenin (TBK m.352/2) şartlarını kurmak; ihtar süresini ve içeriğini doğru oluşturmak; ilamsız tahliye takibiyle bağlantısını kurmak.

## Soğuk başlangıç (intake)
- Hangi dönem kiraları/yan giderler ödenmedi, tutar ne?
- Kira ödemesinin yeri ve zamanı sözleşmede nasıl belirlenmiş?
- Daha önce kaç kez yazılı ihtar gönderildi, tarihleri ve içerikleri?
- İhtar noterden mi, taahhütlü mü gönderildi?

## Denetim şeması
1. **Temerrüt — süreli ihtar (TBK m.315)**: Kiracı muaccel kira/yan gideri ödemezse, kiraya veren yazılı olarak **en az otuz gün** süre verir (konut ve çatılı işyerinde bu süre otuz günden az olamaz) ve bu süre içinde ödenmezse sözleşmeyi feshedeceğini bildirir. Süre, ihtarın kiracıya ulaşmasıyla başlar.
2. **İhtar içeriği**: Hangi dönem borcu, tutar, ödeme yeri, süre ve ödenmezse fesih/tahliye uyarısı açıkça yer almalı. Eksik/belirsiz ihtar sonuç doğurmaz.
3. **Sonuç**: Süre sonunda ödenmezse fesih ile tahliye davası veya İİK m.272 vd. ilamsız tahliye takibi başlatılabilir.
4. **İki haklı ihtar (TBK m.352/2)**: Bir kira yılı (veya bir yıldan kısa süreli sözleşmede tüm kira süresi) içinde kira bedelini ödememesi nedeniyle kiracıya yazılı olarak **iki haklı ihtar** yapılmışsa, kiraya veren kira süresinin/dönemin bitiminden başlayarak **bir ay** içinde dava ile tahliye isteyebilir. İhtarların ayrı dönemlere ait ve haklı olması gerekir; aynı dönem için tek ihtar sayılır.
5. **İspat yükü**: Kiraya veren ihtarları ve tebliği; kiracı ödemeyi (makbuz/banka kaydı — HMK m.200) ispatlar.
6. **Ara sonuç**: Hangi yolun (temerrüt feshi mi, iki haklı ihtar mı) somut olayda elverişli olduğu ve süre durumu.

## Çıktı modülleri
- Otuz günlük temerrüt ihtarnamesi taslağı.
- İki haklı ihtar dosyası kontrol listesi.
- İlamsız tahliye takip talebine köprü notu.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
