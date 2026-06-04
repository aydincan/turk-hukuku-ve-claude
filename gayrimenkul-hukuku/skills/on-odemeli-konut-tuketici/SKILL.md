---
name: on-odemeli-konut-tuketici
description: "Maketten/projeden konut satışı, taksitli ödeme, cayma, teslim gecikmesi veya teminat sorunları söz konusu olduğunda; 6502 sayılı TKHK çerçevesinde tüketicinin haklarını ve satıcının yükümlülüklerini değerlendirmek için kullanılır."
---

# Ön Ödemeli Konut Satışı ve Tüketici Koruması

## Görev
Henüz inşa edilmemiş ya da inşa hâlindeki konutun bedelinin önceden/taksitle ödendiği satışları, tüketici lehine emredici kurallar süzgecinden geçirmek: şekil, cayma, teslim süresi, devir ve teminat (yapı denetimi/bina tamamlama sigortası) yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
- Alıcı tüketici mi (ticari/mesleki amaç dışı); satıcı/yapı sahibi kim?
- Sözleşme noterde resmî şekilde mi yapıldı; satış vaadi/sözleşme tarihi ne?
- Bedel peşin mi taksitli mi ödendi; cayma süresi içinde mi?
- Teslim tarihi geçti mi; teminat (bina tamamlama sigortası/banka teminatı) sağlandı mı?

## Denetim şeması
1. **Kapsam ve şekil**: Ön ödemeli konut satışı, tüketicinin bedeli önceden/taksitle ödediği, konutun gelecekte teslim edileceği satıştır (6502 m.40). Sözleşme yazılı/noterde resmî şekilde kurulur ve teminat şartına bağlanır; şekle ve zorunlu içeriğe aykırılık tüketici aleyhine ileri sürülemez (m.41, ilgili yönetmelik).
2. **Cayma hakkı**: Tüketici, sebep göstermeden ve cezasız olarak 14 gün içinde cayabilir (m.43); satıcı caymadan sonra makul sürede ödenenleri iade eder.
3. **Teslim süresi**: Konut en geç sözleşme tarihinden itibaren 48 ayı geçmeyecek şekilde teslim edilmelidir (m.44); gecikme tüketiciye sözleşmeden dönme/tazminat imkânı verir.
4. **Devir ve dönme**: Tüketici, yükümlülüklerini ifa ederek sözleşmeyi devredebilir; sözleşmeden dönmede satıcı, ödenen bedeli (sınırlı kesintiyle) iade eder (m.42-45).
5. **Teminat zorunluluğu**: Satıcı, projedeki konutların belli oranını aşan satışlarda bina tamamlama sigortası veya muadili teminatı sağlamakla yükümlüdür (m.40/son ve yönetmelik); teminat yoksa tüketici lehine sonuç doğar.
6. **Yargı yolu**: Uyuşmazlık tüketici hakem heyeti parasal sınırını aşıyorsa tüketici mahkemesinde görülür (m.68, m.73); değer sınırına dikkat edilir.
7. **Ara sonuç**: Emredici kurallara aykırılık tüketici lehine; cayma/dönme/teslim gecikmesi taleplerinin uygun yargı yoluna yönlendirilmesi.

## Çıktı modülleri
- Cayma/dönme bildirimi taslağı (süre, iade talebi).
- Teslim gecikmesi nedeniyle dönme/tazminat dilekçesi iskeleti.
- Tüketici hakem heyeti/tüketici mahkemesi yönlendirme ve parasal sınır notu.

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
