---
name: mutalaa-temel-yapi-ve-tur
description: "Bir hukuki görüş veya mütalaa hazırlanması istendiğinde işin türünü (dava içi uzman görüşü, danışmanlık görüşü, kurumsal risk mütalaası) belirleyip iskeletini kurmak için kullanılır; mütalaanın dava dilekçesi ve bilirkişi raporundan farkını netleştirir."
---

# Mütalaa Temel Yapısı ve Türü

## Görev
Talep edilen metnin gerçekten hukuki mütalaa mı, dava dilekçesi mi, yoksa bir bilgilendirme notu mu olduğunu ayırt etmek; doğru türü seçip standart mütalaa iskeletini kurmak. Mütalaa analitik ve dengeli yazılır; dava dilekçesi taraf-savunucudur (bkz. Dava Dilekçesi Atölyesi), bilirkişi raporu maddi vakıayı inceler, mütalaa ise hukuki nitelendirme yapar.

## Soğuk başlangıç (intake)
- Bu görüş ne için kullanılacak? (Mahkemeye HMK m.293 uyarınca uzman görüşü olarak mı, dava öncesi karar vermek için mi, sözleşme/işlem yapısı için mi?)
- Talep eden kim ve hangi sıfatla? (Müvekkil / karşı taraf / nötr danışan)
- Yanıtlanması istenen somut hukuki soru(lar) nedir?
- Hangi belge ve vakıalar veriliyor; eksik olan ne?

## Denetim şeması
1. Tür tayini: Dava içi uzman görüşü HMK m.293 kapsamına girer ve karşı tarafça incelenir; tarafsız-bilimsel üslup gerektirir. Danışmanlık mütalaası iç kullanım içindir, aleyhe senaryoyu açıkça tartabilir. Bu ayrım dil ve kapsamı belirler.
2. Kapsam ve sınır: Mütalaa yalnızca sunulan vakıa çerçevesiyle bağlıdır; bu sınır metnin başına yazılır ("İşbu görüş tarafıma iletilen ... belgelerine dayanmaktadır"). Eksik bilgi varsayımları işaretlenir.
3. İskelet kurulumu — standart altı bölüm: (a) Sorunun konusu ve kapsam, (b) Maddi olay özeti, (c) Hukuki çerçeve (mevzuat), (d) Hukuki değerlendirme (altlama), (e) İçtihat-doktrin desteği, (f) Sonuç ve öneriler.
4. Tarafsızlık testi: Metin, hasım bir hukukçunun eline geçtiğinde çürütülemeyecek kadar dengeli mi? Aleyhe argümanlar tartılmış mı? (Mütalaanın ikna gücü dürüstlüğünden gelir.)
5. Ara sonuç: Tür + iskelet + kapsam sınırı netleştiğinde içerik üretimine geçilir.

## Çıktı modülleri
- Mütalaa türü ve gerekçesi (tek paragraf)
- Doldurulmuş altı bölümlü iskelet (başlıklar + her başlık altında 1-2 cümlelik yönerge)
- Kapsam/sınır beyanı taslağı
- Eksik bilgi ve varsayım listesi

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
