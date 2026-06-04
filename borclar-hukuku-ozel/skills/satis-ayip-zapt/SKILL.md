---
name: satis-ayip-zapt
description: "Satılan malın ayıplı çıkması veya üçüncü kişinin hak iddiasıyla zapt edilmesi halinde alıcının haklarını, ihbar sürelerini ve seçimlik hakları belirlemek gerektiğinde; satıcının sorumluluğunun denetimi için kullanılır."
---

# Satış Sözleşmesi — Ayıptan ve Zapttan Sorumluluk

## Görev
Satılanın maddi/hukuki/ekonomik ayıbı veya zaptı halinde alıcının seçimlik haklarını, gözden geçirme-ihbar yüklerini ve zamanaşımını TBK m.207 vd. çerçevesinde denetlemek; ticari satışta TTK m.23 sürelerini ayırmak.

## Soğuk başlangıç (intake)
- Satım konusu ne (taşınır/taşınmaz, ticari mal mı, tüketici işlemi mi)?
- Ayıp mı, zapt mı (üçüncü kişinin üstün hakkı mı)?
- Teslim tarihi ve ayıbın fark edildiği/bildirildiği tarih?
- Açık mı gizli ayıp; satıcı ayıbı biliyor/ağır kusurlu mu?

## Denetim şeması
1. **Ayıbın varlığı (m.219).** Lüzumlu vasıfların yokluğu veya değeri/yararı azaltan eksiklik. Satıcı, ayıbı bilmese de sorumlu (m.219/2).
2. **Gözden geçirme ve ihbar (m.223).** Alıcı, teslimden sonra imkân bulur bulmaz gözden geçirip ayıbı uygun sürede bildirmeli; aksi halde malı kabul etmiş sayılır. Gizli ayıpta ortaya çıkınca derhal ihbar. **Ticari satışta TTK m.23/c:** açık ayıp 2 gün, muayene gerektiren gizli ayıp 8 gün.
3. **Seçimlik haklar (m.227).** Dönme (sözleşmeden), bedel indirimi, ücretsiz onarım, ayıpsız misli ile değişim; ayrıca genel hükümlere göre tazminat (m.229). Dönme aşırı ise hâkim bedel indirimine hükmedebilir (m.227/4).
4. **Zapttan sorumluluk (m.214-218).** Üçüncü kişi üstün hakla malı alırsa tam/kısmi zapt; alıcının davayı satıcıya ihbarı (m.215) ispat ve rücu için kritik. Tam zaptta sözleşme kendiliğinden sona erer (m.217).
5. **İspat yükü.** Ayıbın varlığını ve teslim anında mevcudiyetini alıcı; süresinde ihbar edildiğini de alıcı; ayıbın bilinmesine rağmen susulduğunu ileri sürense buna göre ispatlar.
6. **Zamanaşımı (m.231).** Teslimden itibaren 2 yıl; taşınmaz yapı eserlerinde 5 yıl. Satıcının ağır kusuru/hile varsa süre işlemez (m.231/2). Ara sonuç: hak ve süre haritası çıkar.

## Çıktı modülleri
- Ayıp ihbar mektubu taslağı (tarih/içerik unsurlarıyla).
- Seçimlik hak ve süre tablosu (adi/ticari ayrımı).
- Dava dilekçesi iskeleti (talep sonucu + dayanak madde).

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
