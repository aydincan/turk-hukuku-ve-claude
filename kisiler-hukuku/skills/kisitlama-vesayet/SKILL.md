---
name: kisitlama-vesayet
description: "Bir yetişkinin akıl hastalığı, savurganlık, alkol-uyuşturucu bağımlılığı, kötü yaşam tarzı ya da özgürlüğü bağlayıcı ceza nedeniyle kısıtlanması veya korunması gerektiğinde kullanılır."
---

# Kısıtlama (Hacir) ve Vesayet Başvurusu

## Görev
Bir kişinin TMK m.405-408'deki kısıtlama sebeplerinden birine girip girmediğini değerlendirmek, kısıtlama (hacir) ve vesayet altına alma talebini doğru sebep ve usulle kurmak; gerektiğinde daha hafif koruma araçlarını (yasal danışman, vasi) tartmak.

## Soğuk başlangıç (intake)
- Korunacak kişinin durumu: akıl hastalığı/zayıflığı, savurganlık, bağımlılık, kötü yaşam tarzı, kötü yönetim mi?
- Kişi işlerini kendi göremiyor mu, yakınlarını tehlikeye/yoksulluğa mı düşürüyor, sürekli yardım mı gerekiyor?
- Özgürlüğü bağlayıcı bir ceza (bir yıl veya daha fazla) infaz ediliyor mu?
- Kişinin kendisi mi talep ediyor (m.408), yoksa yakını/makam mı?

## Denetim şeması
1. **Kısıtlama sebepleri** — TMK m.405: akıl hastalığı veya akıl zayıflığı sebebiyle işlerini göremeyen, korunması/sürekli yardım gerektiren veya başkalarının güvenliğini tehdit eden ergin kısıtlanır (sağlık kurulu raporu zorunlu). TMK m.406: savurganlık, alkol/uyuşturucu bağımlılığı, kötü yaşam tarzı veya malvarlığını kötü yönetme; kişi kendini/ailesini yoksulluğa düşürme tehlikesi yaratıyor veya sürekli korunma/bakım gerekiyorsa kısıtlanır.
2. **Ceza nedeniyle** — TMK m.407: bir yıl veya daha uzun süreli özgürlüğü bağlayıcı cezaya mahkûm olan her ergin kısıtlanır; infaz kurumu yönetimi bildirimde bulunur.
3. **İstek üzerine** — TMK m.408: yaşlılığı, sakatlığı, deneyimsizliği veya ağır hastalığı sebebiyle işlerini gerektiği gibi yönetemediğini ispat eden ergin, kendi isteğiyle kısıtlanabilir.
4. **Usul ve güvenceler** — Görevli mahkeme sulh hukuk mahkemesidir; çekişmesiz yargı (HMK m.382/2-b). m.405/406'da kişinin dinlenmesi; m.409: dinlenme ve bilirkişi (sağlık kurulu raporu) zorunluluğu. Karar ilan edilir; vasi atanır (TMK m.413 vd.).
5. **Ölçülülük / hafif araç** — Kısıtlama yerine yeterliyse yasal danışman atanması (TMK m.429) tercih edilir; ölçülülük (Anayasa m.13) gözetilir.

## Çıktı modülleri
- Kısıtlama sebebi teşhisi + dayanak madde.
- Zorunlu güvenceler kontrol listesi (rapor, dinleme).
- Başvuru dilekçesi iskeleti (sulh hukuk, talep sonucu, vasi önerisi).
- Sağlık kurulu raporu için `[doldurulacak]` ek notu.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
