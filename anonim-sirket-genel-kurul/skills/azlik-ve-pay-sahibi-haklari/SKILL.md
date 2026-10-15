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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
