---
name: safe-donusturulebilir-enstruman
description: "Erken aşama finansmanda SAFE, dönüştürülebilir tahvil/borç gibi pay dönüşümü taahhüt eden enstrümanlar kullanılırken; bunların Türk hukukundaki niteliği, dönüşüm mekaniği, indirim/tavan ve sermaye artırımına bağlanması netleştirilirken kullanılır."
---

# SAFE ve Dönüştürülebilir Enstrümanlar

## Görev
Pay dönüşümü taahhüt eden enstrümanı (SAFE, dönüştürülebilir borç) Türk hukukuna geçerli biçimde uyarlamak; dönüşüm mekaniğini, indirim/değerleme tavanını ve gelecekteki sermaye artırımına bağlanmasını kurmak.

## Soğuk başlangıç (intake)
1. Enstrüman SAFE mi, dönüştürülebilir borç/tahvil mi (geri ödeme/faiz var mı)?
2. Dönüşüm tetikleyicisi ne: nitelikli yatırım turu, çıkış, vade sonu?
3. İndirim oranı (discount) ve/veya değerleme tavanı (valuation cap) var mı?
4. Yatırımcı para girişini ne zaman yaptı; şirkete fiilen ödendi mi?
5. Şirket AŞ mi; kayıtlı sermaye sistemi mevcut mu?

## Denetim şeması
1. Hukuki nitelik: Türk hukukunda SAFE isimsiz/karma sözleşmedir (TBK m.26 sözleşme serbestisi). Borç (geri ödenebilir) niteliği taşıyorsa karz/tüketim ödüncü hükümleri (TBK m.386 vd.); salt pay taahhüdü ise gelecekteki sermaye artırımına katılma taahhüdü olarak kurgulanır.
2. Dönüşüm = sermaye artırımı: Dönüşüm anında yatırımcıya pay, bir bedelli sermaye artırımıyla (TTK m.456 vd.) verilir; rüçhan hakkının (m.461) bu yatırımcı lehine kullandırılması/sınırlanması GK kararıyla kurgulanmalı.
3. Sermayenin korunması: Para girişi sermaye taahhüdüne mahsup edilecekse, nakdî sermaye ödeme kuralları (m.344) ve takas/mahsup geçerliliği denetlenmeli; ayni nitelik doğarsa değerleme (m.343) gündeme gelir.
4. İndirim ve tavan: Discount ve cap yalnızca dönüşüm fiyatını/pay adedini belirleyen sözleşmesel parametrelerdir; cap table'a etkisi en olumsuz senaryoyla modellenir.
5. Tahvil yolu: Dönüştürülebilir tahvil resmi yolla ihraç edilecekse TTK m.504-507 (borçlanma senetleri) ve SPK mevzuatı; halka kapalı kurguda genellikle sözleşmesel dönüştürülebilir borç tercih edilir.
6. İspat/şekil: Yazılı sözleşme; para girişi banka kaydıyla; dönüşüm için GK/YK kararı ve tescil. Eşik/oran değerlerini [doldurulacak] bırak.

## Çıktı modülleri
- SAFE/dönüştürülebilir borç sözleşmesi taslağı (tetikleyici, indirim, tavan).
- Dönüşüm mekaniği ve sermaye artırımı adım planı.
- En olumsuz senaryo cap table dönüşüm tablosu.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
