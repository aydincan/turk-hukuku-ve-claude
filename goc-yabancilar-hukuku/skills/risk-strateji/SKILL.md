---
name: risk-strateji
description: "Yabancının dosyasında izlenecek yol seçenekleri tartılacağında; sınır dışı/gözetim riski, başvuru-dava ardışıklığı ve en lehe statünün belirlenmesi gerektiğinde kullanılır."
---

# Risk Değerlendirmesi ve Strateji

## Görev
Yabancının dosyasında mevcut riskleri (uzaklaştırma, gözetim, statü kaybı, yaptırım) haritalamak, seçenekleri olası sonuç ve sürelere göre tartmak, en lehe ve uygulanabilir yol haritasını kurmak.

## Soğuk başlangıç (intake)
1. Müvekkilin önceliği nedir (Türkiye'de kalış, çalışma, koruma, vatandaşlık, sınır dışını önleme)?
2. Aktif/potansiyel idari işlemler ve riskler nelerdir?
3. Zaman baskısı var mı (gözetim, yaklaşan süre, ailenin durumu)?
4. Geçmiş ihlal, giriş yasağı veya ceza kaydı var mı?

## Denetim şeması
1. **Risk envanteri**: Sınır dışı (YUKK m.54), gözetim (m.57), ikamet ret/iptal (m.33/50), izinsiz çalışma yaptırımı (6735 m.23), giriş yasağı (m.9), statü kaybı.
2. **Koruma kalkanları**: Geri gönderme yasağı (m.4/m.55), uluslararası/geçici koruma başvurusunun askıya alıcı etkisi, aile birliği ve çocuğun üstün yararı (AİHS m.8), sağlık durumu.
3. **Seçenek tartımı**: Her yol için (başvuru, idari itiraz, dava+YD, koruma başvurusu) başarı olasılığı, süre, askıya alıcı etki ve geri dönülemezlik karşılaştırılır. Statüler arası geçişte en aktif koruma sağlayan yol önceliklendirilir.
4. **Ardışıklık ve eşzamanlılık**: Örneğin sınır dışıya karşı dava açarken paralel koruma başvurusunun gözetim ve uzaklaştırmaya etkisi planlanır; çelişkili statü taleplerinden kaçınılır.
5. **Kötü senaryo planı**: Süre kaçarsa/dava reddedilirse alternatif (gönüllü dönüş, üçüncü ülke, yeniden başvuru) hazırlanır.
**Ara sonuç**: Önceliklendirilmiş, sürelere bağlanmış tek bir yol haritası ve yedek plan.

## Çıktı modülleri
- Risk haritası (risk, olasılık, etki, dayanak madde).
- Seçenek karşılaştırma tablosu ve tavsiye.
- Aşamalı eylem planı ve tetik tarihleri.

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
