---
name: sektorel-yz-uygulama
description: "Sağlıkta klinik karar destek, bankacılıkta kredi skorlama, istihdamda işe alım eleme, sigortada fiyatlama veya kamuda otomatik işlem gibi yüksek etkili yapay zekâ kullanımlarında sektörel mevzuat ile KVKK birlikte değerlendirildiğinde kullanılır."
---

# Sektörel Yüksek Riskli Yapay Zekâ Uygulamaları

## Görev
Bireyin haklarını doğrudan etkileyen sektörel YZ kullanımlarında uygulanacak özel mevzuatı KVKK ile birlikte değerlendirip uyum ve sorumluluk şemasını çıkarmak.

## Soğuk başlangıç (intake)
1. Hangi sektör: sağlık, bankacılık/kredi, istihdam, sigorta, kamu idaresi, sermaye piyasası?
2. YZ kararı bireyi nasıl etkiliyor (kredi reddi, işe alım eleme, tanı önerisi, prim)?
3. Sektörel düzenleyici (BDDK, SGK, TİTCK, SPK, ilgili idare) onay/kayıt gerektiriyor mu?
4. Nihai kararı insan mı veriyor, sistem mi?

## Denetim şeması
1. **Sektör normu tespiti**: Sağlıkta hekimin özen ve aydınlatılmış onam yükümlülüğü (1219/3359, TBK vekâlet), klinik karar destek hekimin sorumluluğunu kaldırmaz; bankacılık/kredide 5411 ve düzenlemeleri; istihdamda 4857 ve eşit davranma; sigortada 5684/TTK; kamuda 2577 İYUK ve gerekçeli işlem. Ara sonuç: baskın sektörel norm.
2. **KVKK katmanı**: Her halde m.4-6 işleme şartı, m.10 aydınlatma ve m.11/1-g otomatik karar itirazı uygulanır; sağlık/biyometrik veride m.6 özel nitelikli rejim.
3. **İnsan denetimi**: Tanı, kredi reddi ve işe alım eleme gibi kararlarda anlamlı insan gözetimi hem sorumluluk hem KVKK açısından kritiktir; biçimsel onay yetmez.
4. **Ayrımcılık riski**: Modelin korunan özellikler üzerinden dolaylı ayrımcılık üretmesi eşitlik ilkesi ve m.4 doğruluk/hukuka uygunluk ihlali doğurabilir; istihdamda 4857 ayrımcılık tazminatı.
5. **Sorumluluk**: Hatalı sektörel kararda sektörel sorumluluk (ör. hekim/banka) ile YZ sağlayıcı sorumluluğu (bkz. sorumluluk becerisi) birlikte değerlendirilir.

İçtihat için karararama.yargitay.gov.tr ve karararama.danistay.gov.tr; künye [doğrulanacak].

## Çıktı modülleri
- Sektör + KVKK çifte uyum tablosu.
- İnsan gözetimi ve ayrımcılık riski değerlendirmesi.
- Sektörel onay/kayıt yol haritası.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
