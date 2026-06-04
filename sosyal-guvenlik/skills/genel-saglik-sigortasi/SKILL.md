---
name: genel-saglik-sigortasi
description: "GSS kapsamı, tescil, prim borcu, bakmakla yükümlü olunan kişi statüsü ve sağlık yardımlarından yararlanma koşulları söz konusu olduğunda; özellikle GSS borç ve gelir testi uyuşmazlıklarında kullanılır."
---

# Genel Sağlık Sigortası (GSS)

## Görev
Kişinin GSS kapsamını, tescil ve prim yükümlülüğünü, bakmakla yükümlü olunan kişi statüsünü ve sağlık hizmetinden yararlanma hakkını çözümlemek; GSS prim borcuna ilişkin uyuşmazlığı yönetmek.

## Soğuk başlangıç (intake)
- Kişi sigortalı (4/a-b-c) mi, bağımsız GSS'li mi, yoksa bakmakla yükümlü olunan kişi mi?
- GSS prim borcu tebliğ edildi mi; gelir testi yapıldı mı?
- Sağlık hizmetinden yararlanma reddedildi mi (prim borcu/kapsam dışı)?
- Öğrenci, yabancı, vatansız veya uluslararası koruma statüsü var mı?

## Denetim şeması
1. Kapsam — 5510 m.60: GSS'li sayılanlar (sigortalılar, gelir/aylık alanlar, yeşil kart yerine geçen kapsam, ikamet eden yabancılar) belirlenir.
2. Bakmakla yükümlülük — m.3/10 ve m.60: Eş, çocuk ve ana-baba sigortalı üzerinden yararlanma koşulları; bu durumda ayrı GSS tescili gerekmez.
3. Gelir testi — m.60-61: Bağımsız GSS'lide prime esas kazanç, hane içi gelirin asgari ücretin üçte birine göre durumuna göre belirlenir; gelir testi sonucuna SGK'ya itiraz ve dava yolu açıktır.
4. Prim ve borç — m.67 ve m.88: Sağlık yardımından yararlanmada prim borcu olmama koşulu (belirli istisnalar/yapılandırmalar saklı); GSS borçlarında zamanaşımı m.93.
5. Yararlanma — m.67: Müstehaklık koşulları (gün şartı, prim borcu durumu). Ara sonuç: kapsam, borç ve müstehaklık durumu. İspat: SGK tescil/gelir testi kayıtları, hane bilgileri.

## Çıktı modülleri
- GSS kapsam ve statü tespiti.
- Gelir testi sonucuna itiraz/dava değerlendirmesi.
- Prim borcu ve müstehaklık durum notu.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
