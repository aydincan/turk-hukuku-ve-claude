---
name: ilamli-icra-ve-icranin-geri-birakilmasi
description: "Mahkeme ilamı veya ilam niteliğindeki belgeye dayalı takip yapmak, para dışı edimlerin (teslim, tahliye, çocuk teslimi) cebrî icrasını yürütmek ve icranın geri bırakılması ya da istinaf/temyizde tehir-i icra talep etmek için kullanılır."
---

# İlamlı İcra ve İcranın Geri Bırakılması

## Görev
İlam veya ilam niteliğindeki belgeyle takip kurmak (m.24 vd.); konusu para, teminat, taşınır/taşınmaz teslimi, bir işin yapılması/yapılmaması veya tahliye olan edimleri icra etmek; borçlu lehine icranın geri bırakılması ve tehir-i icra yollarını yönetmek.

## Soğuk başlangıç (intake)
- Elde kesinleşmiş/kesinleşmemiş ilam mı, ilam niteliğinde belge mi (m.38) var?
- İlamın konusu nedir (para, teslim, tahliye, yapma/yapmama)?
- Kanun yolu (istinaf/temyiz) açık mı, tehir-i icra (m.36) gündemde mi?
- Borç icra emrinden sonra ödendi/itfa edildi mi (m.33)?

## Denetim şeması
1. **İcra emri (m.24-32)**: İlamlı takipte borçluya icra emri gönderilir; itiraz takibi durdurmaz. Para alacağında m.32, taşınır teslimi m.24, taşınmaz tahliye/teslimi m.26-28, çocuk teslimi (özel mevzuat/m.25 uygulaması), bir işin yapılması m.30, yapılmaması m.31.
2. **İlam niteliğinde belgeler (m.38)**: Mahkeme huzurunda yapılan sulh/kabul, kayıtsız şartsız para borcu ikrarını içeren düzenleme şeklindeki noter senetleri vb. ilam gibi icra edilir.
3. **İcranın geri bırakılması (m.33)**: Borçlu, icra emrinin tebliğinden sonra borcun itfa/imhal/zamanaşımı gibi sebeple sona erdiğini belgeyle ileri sürerse icra mahkemesinden geri bırakma ister. İlamların zamanaşımı için m.39'a (10 yıl) bakılır.
4. **Tehir-i icra (m.36)**: İstinaf/temyiz yoluna başvuran borçlu, teminat göstererek icranın geçici olarak durdurulmasını isteyebilir; süreler ve teminat oranı denetlenir.
5. **İspat yükü**: Geri bırakma talebinde borçlu, itfa/imhali nitelikli belgeyle ispatlar.
6. **Ara sonuç**: İcra emrinin uygunluğu, kanun yolu etkisi ve teminat planı belirlenir.

## Çıktı modülleri
- İlamlı takip talebi/icra emri taslağı.
- İcranın geri bırakılması veya tehir-i icra dilekçesi.
- Edim türüne göre fiilî icra adımları kontrol listesi.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
