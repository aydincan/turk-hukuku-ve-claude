---
name: sorumluluk-tazminat-ve-sorumsuzluk
description: "Sorumluluk sınırlaması, tazminat tavanı, sorumsuzluk anlaşması ve dolaylı zarar dışlama gibi maddelerin geçerliliğini ve dengesini incelemek gerektiğinde kullanılır."
---

# Sorumluluk, Tazminat ve Sorumsuzluk Kaydı Denetimi

## Görev
Sorumluluk sınırlaması, tazminat tavanı, sorumsuzluk anlaşması, dolaylı zarar dışlama ve tazminat (indemnity) kayıtlarını geçerlilik ve denge yönünden denetlemek; geçersiz olanları ve müvekkili koruyacak lafzı belirlemek.

## Soğuk başlangıç (intake)
- Sözleşmede sorumluluğu sınırlayan/kaldıran kayıt var mı; kimin lehine?
- Edim uzmanlık/ruhsat gerektiren bir hizmet mi (TBK m.115/f.3)?
- Tazminat tavanı, dolaylı/netice zararı dışlama, kâr kaybı dışlama kayıtları var mı?
- Yardımcı kişi/alt yüklenici kullanılıyor mu (TBK m.116)?

## Denetim şeması
1. **Sorumsuzluk yasağı**: TBK m.115/f.1-2 — borçlunun ağır kusurundan (kast/ağır ihmal) sorumlu olmayacağına ilişkin anlaşma **kesin geçersiz**. m.115/f.3 — uzmanlık gerektiren, kanun/yetkili makam izniyle yürütülen faaliyette hafif kusur sorumsuzluğu da geçersiz.
2. **Yardımcı kişi**: TBK m.116/f.2 — yardımcı kişinin fiilinden doğan sorumluluğun önceden kaldırılması anlaşması geçerli olabilir; ancak izne tabi/uzmanlık faaliyetinde sınırlanamaz.
3. **Tazminat tavanı (cap)**: Cap kural olarak geçerli ama ağır kusuru kapsayamaz; "tüm hâller dahil" tavan kasıt/ağır kusura karşı işlemez. Sigorta limitiyle uyumu kontrol edilir.
4. **Dolaylı zarar/kâr kaybı dışlama**: TBK'da menfi/müspet zarar ayrımı (m.112 vd.); "kâr kaybı talep edilemez" kaydı müvekkil lehineyse korunur, aleyhineyse istisna (ağır kusur) eklenir.
5. **İndemnity (zarar tazmin taahhüdü)**: Kapsam, tetikleyici, tavan, süre ve "third-party claim" prosedürü netleştirilir; tek taraflı/sınırsız indemnity pazarlığa çekilir.
6. **İspat yükü**: Kusursuzluğunu borçlu ispatlar (TBK m.112). Sorumsuzluk kaydının geçersizliği hâkimce resen dikkate alınır.

## Çıktı modülleri
- Geçerli/geçersiz sorumsuzluk kayıtları tablosu (madde atfıyla).
- Dengeli tavan ve istisna lafzı önerisi (ağır kusur/kasıt hariç).
- İndemnity prosedürü ve sigorta uyumu notu.

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
