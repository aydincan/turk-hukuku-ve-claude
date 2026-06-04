---
name: sureler-ve-zamanasimi
description: "Dava açma, idari aşama ve kanun yolu sürelerini ve tarh/tahsil/ceza zamanaşımlarını eksiksiz hesaplayarak süre kaybı riskini ortadan kaldırmak için kullanılır."
---

# Süreler ve Zamanaşımı Takibi

## Görev
Vergi uyuşmazlığındaki tüm süreleri (dava açma, idari başvuru, kanun yolu) ve zamanaşımlarını (tarh, tahsil, ceza kesme) doğru hesaplayıp takvimlemek; durma-kesilme etkilerini birbirine karıştırmadan yönetmek.

## Soğuk başlangıç (intake)
1. İlgili belgenin (ihbarname/ödeme emri/karar) tebliğ tarihi tam olarak nedir?
2. Uzlaşma, düzeltme-şikâyet veya izaha davet süreci işletildi mi; hangi tarihte?
3. Vergiyi doğuran olayın yılı ve dönemi nedir?
4. Hangi aşamadayız: dava açma, istinaf yoksa temyiz mi?

## Denetim şeması
1. **Dava açma süreleri.** İYUK m.7 — vergi mahkemesinde kural 30 gün. AATUHK m.58 — ödeme emrinde 7 gün. Bu iki süre ayrı tutulur.
2. **Durma-kesilme.** Uzlaşma talebi VUK Ek m.7 uyarınca dava süresini durdurur; uzlaşma vaki olmazsa kalan süre (en az 15 gün) içinde dava. Düzeltme-şikâyet başvurusu (VUK m.124) ve cevap süreleri ayrı işler. İYUK m.8 — sürelerin başlangıcı, tatil günleri ve adli tatil (m.61) etkisi.
3. **Tarh zamanaşımı.** VUK m.114 — vergiyi doğuran olayın izleyen yılbaşından itibaren 5 yıl; takdir komisyonuna sevk durmayı (m.114/2) ile sınırlı süre tetikler.
4. **Ceza kesme zamanaşımı.** VUK m.374 — vergi ziyaında 5 yıl, usulsüzlükte 2 yıl; başlangıç tarihleri ayrı.
5. **Tahsil zamanaşımı.** AATUHK m.102 — 5 yıl; m.103 kesilme (ödeme, haciz, teminat vb.), m.104 durma halleri.
6. **Kanun yolu süreleri.** İYUK m.45 — istinaf (BİM) 30 gün; m.46-48 — temyiz (Danıştay) 30 gün; kararın tebliğinden işler. Ara sonuç: her aşama için son gün takvime işlenir, durma sebepleri ayrı sütunda gösterilir.

## Çıktı modülleri
- Süre ve zamanaşımı takvimi (olay / dayanak madde / son gün).
- Durma-kesilme olaylarının kronolojik tablosu.
- Kritik tarih uyarı listesi.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
