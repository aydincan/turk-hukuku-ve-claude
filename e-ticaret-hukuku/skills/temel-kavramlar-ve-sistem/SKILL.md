---
name: temel-kavramlar-ve-sistem
description: "E-ticaret uyuşmazlığının hangi kanun kümelerine değdiğini ve tarafların sıfatını (hizmet sağlayıcı, aracı hizmet sağlayıcı, tüketici, tacir) belirlemek gerektiğinde; alanın norm haritasını çıkarmak için kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
E-ticaretle ilgili bir olayda hangi kanunların ve yönetmeliklerin uygulanacağını, tarafların hukuki sıfatını ve hangi yükümlülük katmanının tetiklendiğini belirlemek; sonraki becerilere doğru giriş kapısını açmak.

## Soğuk başlangıç (intake)
- Müvekkil hangi rolde: kendi ürün/hizmetini satan mı (hizmet sağlayıcı), yoksa başkalarının satışına aracılık eden platform mu (aracı hizmet sağlayıcı)?
- Karşı taraf tüketici mi (gerçek kişi, ticari amaç dışı) yoksa tacir/işletme mi?
- Yıllık net işlem hacmi ve işlem sayısı yaklaşık ne? (ETAHS eşikleri için)
- Olayın çekirdeği ne: sözleşme/iade mi, ticari ileti mi, veri mi, içerik kaldırma mı, yaptırım mı?

## Denetim şeması
1. Sıfat tespiti: 6563 m.2 tanımlarına göre "hizmet sağlayıcı" ve "aracı hizmet sağlayıcı" ayrımı yapılır. 7416 sayılı Kanun sonrası "elektronik ticaret hizmet sağlayıcı (ETHS)" ve "elektronik ticaret aracı hizmet sağlayıcı (ETAHS)" kavramları ile net işlem hacmine bağlı kademeli yükümlülükler devreye girer.
2. İlişki tipi: Karşı taraf 6502 m.3 anlamında tüketici ise hem 6563 hem 6502 (mesafeli sözleşme, m.48) uygulanır; B2B ise 6502 dışında kalır, 6563 + TBK/TTK yürür.
3. Norm kümesi haritası: ticari iletişim → 6563 m.6-7 + Ticari Elektronik İleti Yönetmeliği + İYS; veri → 6698 KVKK; içerik/barındırma → 5651; haksız rekabet → TTK m.54-55.
4. Yükümlülük katmanı: bilgi verme (6563 m.3), sözleşme öncesi bilgilendirme ve sipariş (m.4-5), ETBİS kaydı (m.11), aracı sorumluluğu (m.9).
5. Ara sonuç: olaya değen 2-4 norm kümesi listelenir, her biri için sorumlu beceri işaretlenir.
İspat yükü: yükümlülüğün yerine getirildiğini ispat külfeti kural olarak sağlayıcıdadır (bilgilendirme/onay kayıtları).

## Çıktı modülleri
- Taraf sıfatı ve ölçek tablosu.
- Uygulanacak normlar matrisi (kanun-madde-yönetmelik).
- İlgili alt-beceriye yönlendirme notu.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
