---
name: ispat-ve-delil
description: "Sosyal güvenlik uyuşmazlığında hangi delilin neyi ispatladığı, SGK kayıtları, bordro, tanık ve bilirkişi raporunun değeri ile re'sen araştırma ilkesinin uygulanması gerektiğinde kullanılır."
---

# İspat ve Delil Yönetimi

## Görev
Uyuşmazlık türüne göre ispat yükünü dağıtmak, mevcut ve getirtilebilecek delilleri değerlendirmek ve delil stratejisini kurmak.

## Soğuk başlangıç (intake)
- İspatlanması gereken vakıa ne (çalışma olgusu, kazanç miktarı, kusur, maluliyet)?
- Elde hangi belgeler var (hizmet dökümü, bordro, işe giriş bildirgesi, sağlık raporu)?
- Tanık var mı; bordro tanığı mı komşu işyeri tanığı mı?
- Bilirkişi/sağlık kurulu raporu gerekiyor mu?

## Denetim şeması
1. İspat yükü — TMK m.6 ve özel kurallar: Kural olarak iddia eden ispatla yükümlü; ancak hizmet tespiti gibi kamu düzenine ilişkin davalarda hâkim re'sen araştırma yapar (HMK genel ilkeleriyle birlikte).
2. Resmi/yazılı delil önceliği: SGK hizmet dökümü, işyeri sicil dosyası, dönem bordroları, işe giriş bildirgesi, müfettiş raporu; bunlar aksi ispatlanana dek güçlü karinedir.
3. Tanık delili: Çalışma olgusunun ispatında bordro tanıkları (aynı dönem aynı işyerinde bildirilmiş kişiler) önceliklidir; salt komşu işyeri tanığıyla sonuç güçlü destekleyici delil gerektirir.
4. Bilirkişi/sağlık kurulu: Kusur oranı, maluliyet derecesi, prim/PEK hesabı bilirkişi ve Kurum sağlık kurulu/ATK raporlarıyla saptanır; rapora itiraz ve ek rapor talebi disiplinli yürütülür.
5. Çelişki yönetimi: Belge ile tanık, raporlar arası çelişkiler işaretlenir; gerekirse yeniden inceleme istenir. Ara sonuç: her vakıa için delil eşleşmesi ve eksik delil listesi.

## Çıktı modülleri
- Vakıa-delil eşleştirme matrisi.
- Getirtilecek belge ve tanık listesi.
- Bilirkişi/sağlık kurulu raporuna itiraz noktaları.

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
