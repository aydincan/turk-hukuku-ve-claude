---
name: tuketici-hakem-heyeti-basvuru
description: "Tüketici sıfatıyla mal veya hizmet uyuşmazlığı yaşayan kişi ayıplı ürün, iade, abonelik, haksız şart veya cayma gibi konularda parasal sınır altı uyuşmazlık için hakem heyetine başvuracağında kullanılır."
---

# Tüketici Hakem Heyeti Başvurusu

## Görev
Tüketici işleminden doğan, parasal sınır altındaki uyuşmazlık için tüketici hakem heyetine eksiksiz ve kabul edilebilir bir başvuru hazırlamak.

## Soğuk başlangıç (intake)
- Mal/hizmeti ticari amaç dışında, kişisel ihtiyaç için mi aldınız (tüketici sıfatı)?
- Satıcı/sağlayıcı kim, işlem tarihi ve tutarı nedir?
- Sorun ne (ayıp, iade reddi, haksız şart, abonelik, fazla tahsilat)?
- Satıcıya yazılı başvuru/şikâyet yaptınız mı, yanıt geldi mi?
- Elinizde fatura, sözleşme, mesaj/e-posta var mı?

## Denetim şeması
1. **Tüketici işlemi mi (6502 sayılı TKHK m.3):** Bir tarafın tüketici, diğerinin satıcı/sağlayıcı olduğu işlem olmalı. Ticari amaçlı alımlar tüketici korumasının dışındadır.
2. **Parasal sınır ve görev:** Sınır altı uyuşmazlıkta tüketici hakem heyetine başvuru **zorunludur**; sınır üstünde tüketici mahkemesi görevlidir. Güncel parasal sınır her yıl Ticaret Bakanlığı tebliğiyle güncellenir — **[doğrulanacak]**, ezbere yazılmaz.
3. **Yetkili heyet:** Tüketicinin veya satıcının yerleşim yerindeki il/ilçe tüketici hakem heyeti. Tüketici kendi yerleşim yeri heyetine başvurabilir.
4. **Esas hak — örnek:** Ayıplı malda tüketicinin seçimlik hakları (6502 sayılı Kanun m.11): değişim, ücretsiz onarım, bedel indirimi, sözleşmeden dönme. Ayıp ihbarı ve zamanaşımı süreleri (kural olarak iki yıl, m.12) kontrol edilir.
5. **İspat:** Fatura, sözleşme, ayıbı gösteren fotoğraf/rapor, yazışmalar başvuruya eklenir. İspat yükü kural olarak iddia edende; ayıbın teslim anında varlığı karinesi tüketici lehinedir.
6. **Ara sonuç:** Sıfat + sınır altı + yetkili heyet + delil tamamsa başvuru yapılır. Heyet kararına karşı tüketici mahkemesinde itiraz süresi işler (karar tebliğinden itibaren 15 gün — **[doğrulanacak]**).

## Çıktı modülleri
- Hakem heyeti başvuru dilekçesi taslağı ([doldurulacak] yer tutucularıyla).
- Delil/ek belge listesi.
- Karara itiraz yolu ve süre uyarısı.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
