---
name: butlan-ve-yokluk
description: "Genel kurul kararinin iptal degil butlan veya yokluk yaptirimina tabi oldugu degerlendirilecekse; vazgecilemez haklara, sermayenin korunmasina aykirilik ve cagri yoklugu gibi hallerde suresiz tespit davasi gerektiginde kullanilir."
---

# Butlan ve Yokluk Tespiti

## Görev
İptal edilebilirlik eşiğini aşan ağır sakatlıkları — butlan (m.447) ve yokluk — teşhis etmek; süresiz ileri sürülebilen tespit davası stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Sakatlık, pay sahibinin vazgeçilemez/müktesep haklarına mı, sermayenin korunmasına mı, AŞ'nin temel yapısına mı ilişkin?
2. Çağrı hiç yapılmadı mı veya toplantı/karar iradesi hiç oluşmadı mı (yokluk göstergeleri)?
3. Karar üzerine işlemler yapıldı, tescil edildi mi (iyiniyetli üçüncü kişi sorunu)?
4. Aynı sakatlık için üç aylık iptal süresi kaçırıldı mı?

## Denetim şeması
1. **Butlan sebepleri (m.447):** GK kararı özellikle; (a) pay sahibinin GK'ye katılma, asgari oy, dava ve kanundan kaynaklanan **vazgeçilmez haklarını sınırlandıran** veya ortadan kaldıran, (b) pay sahibinin **bilgi alma, inceleme ve denetleme** haklarını kanunen izin verilen ölçü dışında kısıtlayan, (c) AŞ'nin **temel yapısını bozan** veya **sermayenin korunması** hükümlerine aykırı kararlardır. Bu hâllerde karar batıldır; herkes, süresiz olarak tespit davası açabilir.
2. **Yokluk:** Kararın hukuken var sayılabilmesi için gereken kurucu unsurların hiç bulunmaması hâli yokluktur (örn. hiç çağrı yapılmadan ve çağrısız toplantı şartları da olmadan "karar" alınması, gerçek bir toplantı/oylama iradesinin hiç oluşmaması). Yokluk da süresiz ileri sürülür.
3. **İptalle sınır:** Salt usul aykırılıkları (süre, gündem, nisap hatası) kural olarak iptal sebebidir; bunları butlana çevirmemeye dikkat et. Butlan/yokluk dar yorumlanır, aksi hukuki güvenliği zedeler.
4. **Yargı yolu:** Tespit/butlan davası asliye ticaret mahkemesinde, şirket merkezinde, şirkete karşı açılır; m.448-450 hükümleri kıyasen uygulanır. Hukuki yarar dava şartıdır.
5. **İspat yükü/ara sonuç:** Butlan/yokluk sebebini ileri süren ispatlar; mahkeme re'sen de gözetebilir. Karar baştan itibaren hüküm doğurmaz; ancak iyiniyetli üçüncü kişilerin tescile dayanan kazanımları ayrıca değerlendirilir.

## Çıktı modülleri
- Butlan/yokluk sebebi nitelendirme notu (m.447 alt-bent eşleştirmesi).
- Tespit davası dilekçe iskeleti (hukuki yarar vurgusuyla).
- İptal/butlan/yokluk ayrım tablosu ve süre uyarısı.

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
