---
name: gorev-yetki-ve-yargi-yolu
description: "Mütalaa konusu uyuşmazlığın hangi yargı koluna, hangi görevli ve yetkili mahkemeye ait olduğunu, varsa zorunlu ön başvuru yolunu belirlemek gerektiğinde kullanılır; dava stratejisinin ilk kapısıdır."
---

# Görev, Yetki ve Yargı Yolu Tespiti

## Görev
Uyuşmazlığın doğru yargı kolu (adli/idari), görevli mahkeme, yetkili yer ve varsa zorunlu ön prosedür (dava şartı arabuluculuk, idari başvuru, hakem heyeti) yönünden çerçevesini çizmek. Yanlış yol veya merci, esasa girilmeden davanın reddine yol açar.

## Soğuk başlangıç (intake)
- Uyuşmazlık özel hukuk mu, idareyle/kamu gücüyle mi ilgili?
- Taraflar tacir mi, uyuşmazlık ticari iş niteliğinde mi?
- Sözleşmede tahkim/yetki şartı var mı?
- Zorunlu bir ön başvuru/arabuluculuk gerekiyor mu?

## Denetim şeması
1. Yargı yolu ayrımı: İdari işlem/eylem ve kamu gücü kullanımı idari yargıda (İYUK m.2 — iptal/tam yargı); özel hukuk ilişkileri adli yargıda; vergi uyuşmazlıkları vergi mahkemesinde. Yargı yolu yanlışsa merci tecavüzü/görevsizlik doğar.
2. Görevli mahkeme: Adli yargıda kural asliye hukuk (HMK m.2); sulh hukukun görevi sınırlıdır (HMK m.4 — kira/tahliye, paylaştırma, vb.). Özel görevli mahkemeler: tüketici mahkemesi (6502), iş mahkemesi (7036), ticaret mahkemesi (TTK m.5 — ticari davalar), aile mahkemesi, fikri-sınai haklar mahkemesi. Görev kamu düzenindendir, re'sen gözetilir (HMK m.114/1-c).
3. Yetki (yer): Genel yetki davalının yerleşim yeri (HMK m.6); özel/kesin yetki halleri (taşınmazda HMK m.12, sözleşmede ifa yeri HMK m.10, haksız fiilde HMK m.16) ayrıca kontrol edilir; kesin yetki re'sen gözetilir.
4. Zorunlu ön prosedür: Ticari ve işçilik alacaklarında dava şartı arabuluculuk (7036 m.3, 6325/TTK m.5/A), tüketici uyuşmazlıklarında parasal sınır altında tüketici hakem heyeti (6502), idari para cezalarında sulh ceza hâkimliği (5326), idari işlemde gerekiyorsa zorunlu idari başvuru.
5. Tahkim/yetki şartı: Geçerli tahkim şartı varsa mahkeme yolu kapalıdır (HMK m.413/tahkim hükümleri); yetki sözleşmesinin geçerlilik şartları (HMK m.17-18) denetlenir.
6. Ara sonuç: Yargı yolu + görevli mahkeme + yetkili yer + zorunlu ön başvuru tek bir tabloda.

## Çıktı modülleri
- Yargı yolu ve görevli mahkeme tespiti (gerekçeli)
- Yetkili yer mahkemesi (genel/özel/kesin ayrımıyla)
- Zorunlu ön prosedür kontrol listesi
- Yanlış yol/merci riski uyarısı

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
