---
name: tedbir-ve-ivedi-koruma
description: "Sınır dışı, infaz, sağlık veya yaşamsal tehlike gibi telafisi imkânsız zarar riski bulunan hallerde geçici tedbir (ivedi koruma) talep edilirken kullanılır."
---

# Tedbir ve İvedi Koruma Talebi

## Görev
İçtüzük m.73 kapsamında, başvurucunun yaşamına veya maddi-manevi bütünlüğüne yönelik ciddi ve telafisi imkânsız zarar tehlikesinde AYM'den geçici tedbir kararı talep etmek.

## Soğuk başlangıç (intake)
- Hangi icra/işlem yakın ve telafisi imkânsız zarar doğuruyor (sınır dışı, infaz, tıbbi durum)?
- Zarar gerçekleşirse esas hakkındaki kararın anlamı kalır mı?
- Tehlikenin yakınlığını ve ciddiyetini gösteren belgeler var mı?
- Asıl başvuru yapıldı mı, eşzamanlı mı yapılacak?

## Denetim şeması
1. Dayanak — İçtüzük m.73: başvurucunun yaşamına ya da maddi veya manevi bütünlüğüne yönelik ciddi tehlike bulunması hâlinde Bölüm, esas inceleme sonuçlanıncaya kadar gerekli tedbirlere resen veya talep üzerine karar verebilir.
2. Eşik — tehlikenin (a) ciddi, (b) yakın/gerçek ve (c) telafisi imkânsız olması aranır. Soyut/uzak risk yetmez; somut belgeyle ortaya konmalıdır.
3. Tipik haller — sınır dışı/iade kararında işkence-kötü muamele riski (m.17), ağır hastada infazın ertelenmemesi, hayati tıbbi müdahaleye erişimin engellenmesi.
4. Usul — tedbir talebi, başvuru formuyla birlikte veya başvuru derdestken ayrıca ve gecikmeksizin yapılır; aciliyet gerekçesi öne çıkarılır. AYM tedbiri reddedebilir, kabul edebilir veya koşula bağlayabilir; tedbire uyulmaması ayrı sonuç doğurabilir.
5. Süreklilik — tedbir, esas karara kadar veya AYM aksini belirtene dek sürer; koşullar değişirse kaldırılması istenebilir.

İspat yükü: yakın ve ağır tehlikeyi somut belgeyle başvurucu ortaya koyar.

Ara sonuç: "tedbir koşulları var / zayıf / yok" değerlendirmesi.

## Çıktı modülleri
- Tedbir talebi dilekçesi taslağı (aciliyet + telafisizlik gerekçesi).
- Tehlikeyi belgeleyen ek listesi.
- Asıl başvuruyla ilişkilendirme.
- Tedbir reddi halinde alternatif yol notu.

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
