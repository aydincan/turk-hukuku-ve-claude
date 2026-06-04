---
name: cek-hukuku
description: "Çekin unsurlarını, ibraz ve karşılıksız işlemlerini, çek düzenleme yasağı ve adli para cezasını ele almak; çekle ilgili takip, savunma veya 5941 sayılı Kanun kapsamında ceza riski değerlendirmesinde kullanılır."
---

# Çek Hukuku ve Karşılıksız Çek

## Görev
Çekin geçerliliğini, ibraz ve ödeme sürecini, karşılıksız çıkması halinde hukuki ve cezai sonuçlarını değerlendirmek; alacaklı için tahsil/takip, keşideci için savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
- Çek üzerinde keşide tarihi, bedel, banka (muhatap) ve imza tam mı; çek "ileri tarihli" mi?
- Çek bankaya ibraz edildi mi; karşılıksızdır işlemi yapıldı mı, kısmi ödeme var mı?
- Müvekkil keşideci mi, lehtar/hamil mi, ciranta mı?
- Çek hesabı kime ait, tüzel kişi ise imza yetkilisi kim?

## Denetim şeması
1. Şekil şartları: TTK m.780 unsurları (çek kelimesi, kayıtsız şartsız ödeme emri, muhatap banka, ödeme yeri, keşide yeri-tarihi, imza). Eksiklik m.781 ile değerlendirilir; bazı eksiklikler yorum kurallarıyla tamamlanır.
2. İbraz süreleri: TTK m.796 — aynı yerde 10 gün, farklı yerde 1 ay; sürede ibraz başvurma hakkının korunması için şarttır. Çekte vade yoktur; gösterildiğinde ödenir (m.795).
3. Karşılıksız işlemi: banka kısmen/tamamen karşılıksızlığı çek arkasına/sisteme işler (5941 s. K. m.3). Hamil sürede ibraz ve karşılıksız işlemi şartını yerine getirmelidir.
4. Cezai sonuç: karşılıksız çekte, hamilin şikâyeti üzerine keşideci hakkında adli para cezası ve çek düzenleme/çek hesabı açma yasağı uygulanır (5941 s. K. m.5). Şikâyet süresi ve çek bedelinin ödenmesi halinde davanın/cezanın akıbeti m.5/10-11 çerçevesinde değerlendirilir. İspat yükü ve fail: hesap sahibi gerçek/tüzel kişi ayrımına dikkat.
5. Takip yolu: çek kambiyo senedi olduğundan kambiyo senetlerine özgü takip yapılır (İİK m.167 vd.); menfi tespit/istirdat için İİK m.72.
6. Ara sonuç: ibraz süresi kaçırılmışsa cezai süreç ve cirantalara başvuru zayıflar; çek yine TTK m.808 (3 yıl) zamanaşımına dek kambiyo takibine konu olabilir, sebep alacağı saklıdır.

## Çıktı modülleri
- Çek geçerlilik ve ibraz takvimi tablosu.
- Karşılıksız çek şikâyet dilekçesi taslağı (5941 m.5) — bedel/tarih [doldurulacak].
- Keşideci için savunma notu (yetki, ileri tarih, ödeme defi, şikâyet süresi).

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
