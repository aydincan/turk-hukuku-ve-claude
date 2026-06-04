---
name: temel-kavramlar-ve-kapsam
description: "Bir uyuşmazlığın TKHK kapsamına girip girmediğini, tarafların tüketici-satıcı-sağlayıcı niteliğini ve hangi alt rejimin uygulanacağını belirlemek gerektiğinde; tüm tüketici dosyalarının ilk filtresi olarak kullanılır."
---

# Temel Kavramlar ve Kapsam Süzgeci

## Görev
Eldeki olayın tüketici hukuku alanına girip girmediğini netleştirmek, taraf sıfatlarını (tüketici, satıcı, sağlayıcı, kredi veren) doğru nitelendirmek ve hangi alt rejimin (ayıp, haksız şart, mesafeli satış, kredi, abonelik) uygulanacağını belirleyerek dosyayı doğru ele yönlendirmek.

## Soğuk başlangıç (intake)
- Sözleşmenin tarafları kim; alan gerçek/tüzel kişi mal veya hizmeti ticari ya da mesleki amaçla mı edindi?
- İşlem nedir (mal satışı, hizmet, kredi, abonelik) ve nerede/nasıl kuruldu (mağaza, internet, kapıda, telefonla)?
- Sorunun çekirdeği ne: ayıp mı, sözleşme şartı mı, cayma mı, ücret/faiz mi?
- Tutar nedir ve uyuşmazlık tarihi ne (parasal sınır ve süre için kritik)?

## Denetim şeması
1. **Tüketici sıfatı (TKHK m.3/1-k):** Ticari veya mesleki amaçlarla hareket etmeyen gerçek ya da tüzel kişi mi? Ticari amaç varsa kişi tüketici değildir; çift amaçlı (karma) işlemlerde baskın amaca bakılır. İspat: amaç ve kullanım, dosyadaki olgulardan çıkarılır.
2. **Karşı taraf (m.3/1-i, j):** Satıcı, mal sunan; sağlayıcı, hizmet sunan kişidir. Kamu tüzel kişileri de dahil olabilir.
3. **Tüketici işlemi (m.3/1-l):** Mal/hizmet piyasalarında tüketici ile satıcı/sağlayıcı arasında kurulan her türlü sözleşme ve hukuki işlem; eser, taşıma, simsarlık, sigorta, vekâlet, bankacılık dahil. Bir tarafın tüketici olması yeterlidir (m.83/2).
4. **Kapsam dışı kontrolü:** İki tacir/esnaf arası işlem, salt kamusal ilişki ya da TKHK'da düzenlenmemiş ve genel hükme tabi alan ise tüketici rejimi uygulanmaz; ara sonuç olarak dosya TBK/TTK alanına aktarılır.
5. **Alt rejim seçimi:** Çekirdek soruna göre doğru madde grubuna yönlendir — ayıp (m.8-16), haksız şart (m.5), mesafeli/kapıdan (m.47-49), kredi (m.22-39), abonelik (m.52).
6. **Tamamlayıcı norm (m.83/1):** TKHK'da boşluk varsa genel hükümler uygulanır; ancak emredici tüketici lehine hükümler saklıdır.

## Çıktı modülleri
- Kapsam değerlendirme notu (tüketici işlemi var/yok, gerekçe).
- Taraf sıfatları tablosu.
- Uygulanacak alt rejim ve sevk edilecek beceri önerisi.
- Parasal sınır/süre açısından erken uyarı.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
