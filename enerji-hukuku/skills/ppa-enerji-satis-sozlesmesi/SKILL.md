---
name: ppa-enerji-satis-sozlesmesi
description: "Elektrik/enerji alım satım anlaşmaları, ikili anlaşmalar, kurumsal PPA ve YEKA tipi satış sözleşmelerinin müzakeresi, hazırlanması veya risk incelemesi gerektiğinde kullanılır."
---

# Enerji Satış Sözleşmeleri (PPA) İncelemesi

## Görev
Enerji alım satım (PPA/ikili anlaşma/kurumsal PPA) sözleşmesini fiyat, miktar, risk dağılımı ve düzenleyici uyum açısından incelemek; eksik/asimetrik hükümleri tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Taraflar ve sıfatları (üretici/tedarikçi/tüketici) ile lisans durumu?
2. Fiyat yapısı: sabit, endeksli, PTF bağlantılı, tavan/taban var mı?
3. Süre, miktar (take-or-pay var mı) ve teslim/ölçüm noktası?
4. Teminat, dengesizlik maliyeti ve mevzuat değişikliği riski kime ait?

## Denetim şeması
1. **Geçerlilik ve ehliyet**: TBK 6098 genel hükümler; tarafların lisans/yetki kapsamında bu satışı yapma ehliyeti (lisanssız tüketiciye doğrudan satış sınırları). Ara sonuç: sözleşme konusu mevzuata uygun mu.
2. **Fiyat ve endeks**: Fiyat formülünün belirli/belirlenebilir olması (TBK m.27 kesin hükümsüzlük riski); PTF/endeks bağlantısında veri kaynağı ve hesap günü netliği.
3. **Miktar ve take-or-pay**: Asgari alım taahhüdü, eksik çekiş bedeli ve mücbir sebep istisnası; cezai şart varsa TBK m.182 ve aşırı cezada m.182/3 indirimi.
4. **Risk dağılımı**: Dengesizlik/uzlaştırma maliyeti, YEKDEM tercihi, mevzuat değişikliği (change in law) ve vergi/harç değişiklikleri kime ait; teminat (teminat mektubu/avans) ve temerrüt faizi (ticari işte TBK m.120 + 3095 s.K.).
5. **Uyuşmazlık ve fesih**: Fesih sebepleri, askıya alma, tahkim/yetki şartı (4686/HMK 6100) ve uygulanacak hukuk. Emredici hükümlere ve EPDK piyasa kurallarına aykırı kayıtlar işaretlenir.

## Çıktı modülleri
- Madde madde risk/redline tablosu.
- Eksik veya kesin hükümsüzlük riski taşıyan kayıt listesi.
- Müzakere notu ve alternatif lafız önerileri.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
