---
name: sureler-zamanasimi-bildirim
description: "Bilişim/siber uyuşmazlıkta ceza zamanaşımı, dava açma süreleri, KVKK ihlal bildirim süresi ve başvuru sürelerini hesaplamak ve hak kaybını önleyecek takvim kurmak gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Bildirim Takvimi

## Görev
Olaya bağlı tüm süreleri (bildirim, şikâyet, dava, zamanaşımı) tespit edip hak düşürücü kayıpları önleyecek bir takvim kurmak.

## Soğuk başlangıç (intake)
1. Olay/öğrenme tarihi ve fark edilme anı ne?
2. Hangi süreçler söz konusu? (ceza, KVKK bildirim, tazminat, idari dava?)
3. Şikâyete bağlı suç var mı, fail/zarar biliniyor mu?
4. Bir tebligat/karar var mı, tarihi ne?

## Denetim şeması
1. **KVKK ihlal bildirimi.** Veri ihlalinde Kurula bildirim, öğrenmeden itibaren Kurul uygulaması gereği **72 saat** içinde yapılır; ilgili kişilere de makul en kısa sürede bildirilir. Gecikme ayrı bir yaptırım riskidir.
2. **Ceza zamanaşımı (TCK m.66-72).** Dava zamanaşımı suçun cezasının üst sınırına göre belirlenir (TCK m.66); bilişim suçlarının çoğunda 8 yıllık dilim devreye girer. Şikâyete bağlı suçlarda **6 aylık** şikâyet süresi (TCK m.73) failin ve fiilin öğrenilmesinden itibaren işler. Banka/kart suçları ve nitelikli haller resen takip edilir.
3. **Tazminat zamanaşımı.** Haksız fiilde zarar ve failin öğrenilmesinden itibaren **2 yıl** ve her halde fiilden itibaren **10 yıl** (TBK m.72); fiil aynı zamanda suçsa daha uzun ceza zamanaşımı uygulanır. Sözleşmesel taleplerde genel **10 yıl** (TBK m.146), özel hallerde **5 yıl** (TBK m.147).
4. **İdari/içerik süreleri.** KVKK Kurul kararına/idari yaptırıma karşı dava açma süresi (2577 İYUK m.7, kural 60 gün; idari para cezası niteliğine göre değerlendirilir). 5651 sulh ceza/BTK kararlarına itiraz CMK itiraz süresine (kural 7 gün) tabidir.
5. **Ara sonuç.** Her süre için başlangıç anı, uzunluk, son gün ve durma/kesilme halleri belirlenip tek takvimde toplanır. İspat açısından öğrenme tarihinin belgelenmesi önemlidir.

## Çıktı modülleri
- Süre takvimi tablosu (süreç, başlangıç, uzunluk, son gün, dayanak).
- Hak düşürücü riskler ve öncelikli aksiyonlar.
- Şikâyet/dava/itiraz için son tarih uyarı notu.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
