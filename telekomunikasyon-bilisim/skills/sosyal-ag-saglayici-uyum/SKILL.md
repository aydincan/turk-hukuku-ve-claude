---
name: sosyal-ag-saglayici-uyum
description: "Belirli erişim eşiğini aşan sosyal ağ sağlayıcılarının temsilci atama, içerik kaldırma başvurularını sonuçlandırma, raporlama, veri yerelleştirme ve bant genişliği daraltma riskine ilişkin uyum ve savunma konularında kullanılır."
---

# Sosyal Ağ Sağlayıcı Yükümlülükleri ve Uyum

## Görev
Bir platformun 5651 anlamında sosyal ağ sağlayıcı sayılıp sayılmadığını ve buna bağlı temsilci, raporlama, başvuru yanıtlama ve veri yükümlülüklerini denetleyerek uyum programı kurmak veya yaptırıma karşı savunma hazırlamak.

## Soğuk başlangıç (intake)
1. Platform Türkiye'den günlük erişim/kullanıcı eşiğini (ilgili düzenlemedeki sayısal eşik) aşıyor mu?
2. Türkiye'de temsilci (gerçek/tüzel kişi) atandı mı, BTK'ya bildirildi mi?
3. İçerik kaldırma/erişim engelleme başvuruları süresinde yanıtlanıyor mu?
4. Şeffaflık/uygulama raporları yayımlanıyor mu; bir BTK bildirimi/yaptırımı var mı?

## Denetim şeması
1. **Kapsam tespiti**: 5651 sosyal ağ sağlayıcı düzenlemesi (7253 s.K. ile getirilen rejim ve ek değişiklikler) — Türkiye'den belirli günlük erişim eşiğini aşan platformlar kapsamdadır. Ara sonuç: platform kapsamda mı (tarih kilidi: eşik ve yükümlülükler değişti).
2. **Temsilci yükümlülüğü**: Türkiye'de yetkili temsilci atama ve BTK'ya bildirme; temsilci atanmaması kademeli yaptırım (idari para cezası, reklam yasağı ve nihayetinde bant genişliği daraltma/erişim kısıtı) doğurur.
3. **Başvuru ve süre**: m.9 ve m.9/A kapsamındaki içerik kaldırma başvurularını yasal süre içinde (kural olarak 48 saat) yanıtlama ve gerekçeli cevap verme; reddedilen başvurularda yargı yolunun açık tutulması.
4. **Raporlama ve veri**: Düzenli şeffaflık/uygulama raporu; Türkiye'deki kullanıcı verilerinin yurt içinde barındırılmasına yönelik düzenleme ve KVKK aktarım kuralları (6698 m.9) birlikte değerlendirilir.
5. **Kademeli yaptırım ve savunma**: Yükümlülük ihlalinde BTK kademeli yaptırım uygular; her aşama ayrı idari işlemdir ve İYUK m.7 süresinde iptal davası ile m.27 yürütmenin durdurulması istemine konu edilir. Ölçülülük ve ifade özgürlüğü dengesi savunmada esastır.

İlkesel içtihat için BTK yaptırımlarında karararama.danistay.gov.tr, temel hak boyutunda kararlarbilgibankasi.anayasa.gov.tr taranır; künye [doğrulanacak] işaretlenir.

## Çıktı modülleri
- Sosyal ağ uyum kontrol listesi (temsilci/raporlama/başvuru/veri).
- Yaptırıma karşı savunma ve iptal davası iskeleti.
- Başvuru yanıtlama akış ve süre takvimi.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
