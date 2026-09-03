---
name: vatandaslik-hukuku
description: "Türk vatandaşlığının kazanılması, kaybı, evlilik veya istisnai yolla edinimi ya da başvuru reddi söz konusu olduğunda; 5901 sayılı Kanun kapsamında şart ve usulü saptamak için kullanılır."
---

# Türk Vatandaşlığı

## Görev
Yabancının vatandaşlık kazanma yolunu 5901 sayılı Türk Vatandaşlığı Kanunu çerçevesinde belirlemek, şartları madde bazında denetlemek, başvuru dosyasını kurmak ve ret/kaybettirme işlemine karşı yargı yolunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Kazanım yolu nedir: doğumla, genel başvuru, evlilik, istisnai (yatırım) ya da yeniden kazanma?
2. Türkiye'de yasal ikamet süresi ve mevcut izin türü nedir?
3. Evlilik yolu için evlilik süresi ve aile birliği fiilen sürüyor mu?
4. Başvuru reddedildi mi ya da kaybettirme/iptal kararı var mı, tarihi?

## Denetim şeması
1. **Doğumla kazanma**: 5901 m.5-8 — soybağı (m.7) veya doğum yeri (m.8, vatansızlık önleyici).
2. **Genel yetkili makam kararıyla (sonradan)**: m.11 — kesintisiz 5 yıl Türkiye'de ikamet, Türkiye'de yerleşmeye karar verdiğini davranışlarıyla teyit, genel sağlık, iyi ahlak, yeterli Türkçe, geçim, kamu düzeni-güvenliği engeli bulunmaması.
3. **Evlenme yoluyla**: m.16 — Türk vatandaşıyla en az 3 yıldır evli olma ve evliliğin fiilen sürmesi, aile birliği içinde yaşama, evlilik birliğiyle bağdaşmayan faaliyette bulunmama, kamu düzeni-güvenliği engeli olmaması. Evlilik kendiliğinden vatandaşlık vermez; başvuru ve değerlendirme şarttır.
4. **İstisnai (m.12)**: Yatırım/nitelikli kişi gibi hallerde Cumhurbaşkanı kararıyla; ikincil mevzuattaki yatırım eşikleri kontrol edilir.
5. **Ret ve kaybettirme**: Başvuru reddi idari işlem olup İYUK m.2 ile dava edilebilir (genel 60 gün); çıkma, kaybettirme ve iptal halleri (m.29 vd.) ayrı denetlenir. Maddi gerçeğe aykırı/sahte belge ile kazanım iptal sebebidir.
**İspat yükü**: İkamet, evlilik birliği ve geçim gibi şartların varlığını başvuran belgeyle; ret/iptalin maddi dayanağını idare ortaya koyar.

## Çıktı modülleri
- Kazanım yolu-şart eşleştirme tablosu ve belge listesi.
- Başvuru dosyası kontrol listesi.
- Ret/iptal işlemine karşı idari dava iskeleti.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
