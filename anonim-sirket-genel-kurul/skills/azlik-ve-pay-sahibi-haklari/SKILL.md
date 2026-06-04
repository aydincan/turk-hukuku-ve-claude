---
name: azlik-ve-pay-sahibi-haklari
description: "Azligin cagri ve gundeme madde ekletme, finansal tablolarin ertelenmesi, ozel denetci atanmasi ve haklı sebeple fesih gibi haklari ile pay sahibinin bilgi alma-inceleme hakki kullanilacaksa kullanilir."
---

# Azlık ve Pay Sahibi Hakları

## Görev
Sermayenin onda birini (halka açıkta yirmide birini) oluşturan azlığın ve tek tek pay sahiplerinin genel kurul çevresindeki haklarını harekete geçirmek veya bunlara karşı şirketi savunmak.

## Soğuk başlangıç (intake)
1. Müvekkilin/grubun pay oranı azlık eşiğini (1/10; halka açıkta 1/20) karşılıyor mu?
2. Talep çağrı/gündem mi, finansal tablo ertelemesi mi, özel denetim mi, fesih mi?
3. Bilgi alma-inceleme talebi GK'de gündeme getirildi ve reddedildi mi?
4. YK çağrı/gündem talebini reddetti mi; mahkeme yoluna gidilecek mi?

## Denetim şeması
1. **Çağrı ve gündem:** Azlık, gerektirici sebepleri ve gündemi belirterek YK'den GK'yi toplantıya çağırmasını veya gündeme madde eklenmesini noter aracılığıyla isteyebilir (m.411). YK reddeder veya yedi iş günü içinde olumlu cevap vermezse, azlık şirket merkezinin bulunduğu yer asliye ticaret mahkemesinden çağrı/gündem iznini ister (m.412).
2. **Finansal tabloların ertelenmesi:** Finansal tabloların müzakeresi ve buna bağlı konular, azlığın istemi üzerine bir ay sonraya **bir kez** ertelenir; ikinci erteleme için yeni/ciddi sebep gerekir (m.420). Bu hak gündeme bağlılıktan bağımsızdır.
3. **Özel denetçi:** Pay sahibi, kullanılması bilgi alma/inceleme hakkına bağlı belirli olayların açıklığa kavuşması için özel denetim isteyebilir; GK kabul ederse mahkemeden, reddederse azlık (sermayenin onda biri/halka açıkta yirmide biri) mahkemeden özel denetçi atanmasını talep eder (m.438-439).
4. **Bilgi alma ve inceleme:** Her pay sahibi GK'de YK'den şirket işleri, denetçiden denetim hakkında bilgi isteyebilir; bilgi verilmesi dürüstlük kuralına uygun olmalı, şirket sırrı sınırı gözetilmelidir (m.437). Haksız ret, bu konudaki kararı iptale ve özel denetim talebine zemin hazırlar.
5. **Haklı sebeple fesih:** Sermayenin onda birini (halka açıkta yirmide birini) temsil eden pay sahipleri, haklı sebeplerin varlığında şirketin feshini mahkemeden isteyebilir; mahkeme fesih yerine duruma uygun başka çözüme de (örn. paylarının gerçek değerle alınması) hükmedebilir (m.531).
6. **İspat yükü/ara sonuç:** Azlık eşiği ve haklı sebebi talep eden ispatlar. Usulüne uygun talep reddedilmişse mahkeme yolu açılır; aksi hâlde talep dava şartı yokluğundan reddedilir.

## Çıktı modülleri
- Noter ihtarnamesi/çağrı-gündem talep taslağı.
- Mahkemeye özel denetçi/çağrı izni başvuru iskeleti.
- Azlık hakları eşik ve süre kontrol listesi.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
