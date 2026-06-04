---
name: taraf-vekil-tablosu
description: "Çok taraflı veya birden çok vekilli dosyalarda taraf-sıfat-vekil-adres-tebligat ilişkisini netleştirmek ve tebligat ile husumet hatalarını önlemek için tablo kurarken kullan."
---

# Taraf ve Vekil Tablosu

## Görev
Dosyadaki tüm tarafları, sıfatlarını, vekillerini ve tebligat bilgilerini tek tabloda toplayıp husumet, taraf teşkili ve tebligat hatalarını görünür kılmak.

## Soğuk başlangıç (intake)
- Kaç taraf var ve sıfatları ne (davacı, davalı, fer'î müdahil, ihbar olunan)?
- Her tarafın vekili belli mi, vekâletname dosyada mı?
- Tebligat adresleri ve KEP/MERSIS bilgileri mevcut mu?
- Ceza dosyası ise şüpheli/sanık, müşteki/katılan, mağdur ayrımı yapıldı mı?

## Denetim şeması
1. Sıfat kolonu: HMK'da davacı-davalı; çok taraflılıkta ihtiyari/zorunlu dava arkadaşlığı (HMK m.57-59) var mı denetle. Zorunlu dava arkadaşlığında taraf teşkili eksikse dava şartı sorunu doğar (HMK m.114), eksik listesine yaz.
2. Vekil kolonu: her taraf için vekil adı, baro-sicil, vekâletname tarihi. Vekâletname yoksa veya kapsamı dar ise (özel yetki gerektiren işlemler için) işaretle.
3. Tebligat kolonu: adres, tüzel kişilerde MERSIS/KEP. Tebligat Kanunu (7201) gereği usulsüz tebligat riskini not et; tebligatın geçerliliği süreleri etkiler.
4. Müdahil/üçüncü kişi: fer'î müdahale (HMK m.66), davanın ihbarı (HMK m.61) varsa ayrı satır.
5. Ara sonuç: taraf teşkili tamam mı, husumet doğru tarafa mı yöneltilmiş, hangi tebligat eksik — kontrol listesi olarak çıkar. Adres ve sıfatlar yalnızca evraktan alınır.

## Çıktı modülleri
- Taraf-sıfat-vekil-adres-tebligat kolonlu Excel tablosu.
- Eksik vekâletname / eksik taraf teşkili uyarı listesi.
- Tebligat riski notları.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
