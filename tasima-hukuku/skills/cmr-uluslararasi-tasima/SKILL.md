---
name: cmr-uluslararasi-tasima
description: "Çıkış veya varış ülkesi yurt dışında olan karayolu eşya taşımalarında CMR Konvansiyonu'nun uygulanması, CMR belgesi, rezervler ve CMR'ye özgü sorumluluk-zamanaşımı kurallarının değerlendirilmesi gerektiğinde kullanılır."
---

# CMR ve Uluslararası Karayolu Taşıması

## Görev
Sınır aşan karayolu eşya taşımasında CMR'nin uygulanabilirliğini saptamak ve CMR'ye özgü sorumluluk, ihbar/rezerv ve zamanaşımı rejimini işletmek.

## Soğuk başlangıç (intake)
1. Çıkış ve varış ülkeleri hangileri; en az biri CMR tarafı mı?
2. Taşıma karayoluyla ve ücret karşılığı bir araçla mı yapıldı (CMR m.1 kapsamı)?
3. CMR belgesi (sevk mektubu/CMR waybill) düzenlendi mi; sürücü teslimde rezerv/şerh koydu mu?
4. Zararın ve ihbarın tarihleri nedir; teslimden bu yana ne kadar süre geçti?

## Denetim şeması
1. **Kapsam:** CMR m.1 — iki farklı ülke arasında karayoluyla ücret karşılığı eşya taşıması ve en az birinin taraf olması halinde CMR emredici uygulanır. CMR m.41 — aksine anlaşmalar hükümsüz.
2. **CMR belgesinin işlevi:** m.4-9 — belge sözleşmenin ve eşyanın teslim alındığının karinesidir; eksikliği sözleşmeyi geçersiz kılmaz ama ispat zorlaştırır. Rezervsiz teslim alma, iyi durumda teslim karinesi doğurur (m.9).
3. **Sorumluluk:** m.17/1 — ziya, hasar ve gecikmeden sorumluluk. Kurtuluş m.17/2 (genel) ve m.17/4 (özel risk sebepleri); ispat m.18.
4. **İhbar/rezerv süreleri:** m.30 — açık hasarda teslimde, gizli hasarda 7 gün içinde yazılı rezerv; gecikmede 21 gün içinde ihbar. Süresinde rezerv yoksa eşyanın iyi teslim edildiği varsayılır.
5. **Tazminat sınırı:** m.23 — kg başına 8,33 SDR; ayrıca taşıma ücreti, gümrük ve masraflar iade edilir (m.23/4). Gecikmede taşıma ücreti ile sınırlı (m.23/5).
6. **Sınırın kalkması:** m.29 — taşıyıcının kastı veya buna eş kusuru (lex fori'ye göre değerlendirilen ağır kusur) halinde sınırlar uygulanmaz.
7. **Zamanaşımı:** m.32 — kural 1 yıl; kasıt/ağır kusurda 3 yıl. Süre teslim, ziyada teslim için kararlaştırılan günden başlar; yazılı talep süreyi durdurur (m.32/2).

## Çıktı modülleri
- CMR uygulanabilirlik testi ve TTK ile yarışma notu.
- Rezerv/ihbar süre takvimi (m.30) ve durum tespiti.
- CMR tazminat hesabı (m.23) ve zamanaşımı (m.32) değerlendirmesi.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
