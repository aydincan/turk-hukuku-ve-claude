---
name: saklama-imha-politikasi
description: "Kişisel veri saklama sürelerinin belirlenmesi, silme-yok etme-anonim hale getirme yöntemlerinin tasarlanması veya kişisel veri saklama ve imha politikasının hazırlanması gerektiğinde kullanılır."
---

# Saklama ve İmha Politikası

## Görev
KVKK m.4 (süreyle sınırlılık), m.7 (silme/yok etme/anonim hale getirme) ve Kişisel Verilerin Silinmesi, Yok Edilmesi veya Anonim Hale Getirilmesi Hakkında Yönetmelik çerçevesinde saklama-imha politikası ve süre matrisi kurmak.

## Soğuk başlangıç (intake)
1. Hangi veri kategorileri için ne kadar süre saklama gerekiyor; bu süreyi hangi kanun belirliyor?
2. Veri sorumlusu Veri Saklama ve İmha Politikası hazırlamakla yükümlü mü (VERBİS'e kayıtlılar için zorunlu)?
3. İmha hangi ortamlarda yapılacak (fiziksel, elektronik, bulut)?
4. Periyodik imha süresi belirlendi mi (Yönetmelik azami 6 ay)?

## Denetim şeması
1. **Süre belirleme — m.4/2-d**: Veri, ilgili mevzuatta öngörülen veya işlendiği amaç için gerekli olan süre kadar saklanır. Süre; kanuni saklama yükümlülüğü (örn. TTK m.82 ticari defterler, VUK saklama süreleri, iş hukuku zamanaşımları) ve amaç gereği ihtiyaç birlikte değerlendirilerek her kategori için ayrı saptanır.
2. **İmha yükümlülüğünün doğması — m.7**: İşleme sebepleri ortadan kalktığında veri re'sen veya ilgili kişi talebiyle silinir, yok edilir ya da anonim hale getirilir. Üç yöntem ortam ve amaca göre seçilir.
3. **Periyodik imha**: Yönetmelik uyarınca saklama-imha politikası olan sorumlu, imha işlemini periyodik (en fazla 6 ayda bir) yapar; işlemler kayıt altına alınır ve bu kayıtlar en az 3 yıl saklanır.
4. **Anonimleştirme ölçütü**: Anonim hale getirilen veri geri döndürülemez olmalı; aksi halde hâlâ kişisel veridir ve KVKK kapsamındadır.
5. **Ara sonuç**: Amaç sona erdiği halde saklamaya devam, m.4 ihlali ve yaptırım sebebidir; politika, fiili imha kayıtlarıyla tutarlı olmalıdır.

İspat yükü: İmhanın usulüne uygun yapıldığını veri sorumlusu imha tutanak ve loglarıyla ispatlar.

## Çıktı modülleri
- Veri kategorisi bazlı saklama süresi matrisi (mevzuat dayanağıyla).
- Saklama ve İmha Politikası taslağı.
- Periyodik imha tutanağı ve log şablonu.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
