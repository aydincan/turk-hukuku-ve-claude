---
name: ispat-yuku-tmk-6
description: "Bir davada hangi tarafın hangi vakıayı ispatla yükümlü olduğu, karinelerin ve aksini ispat yükünün nasıl dağılacağı tartışıldığında TMK m.6 ve HMK m.190 ile ispat yükü haritasını çıkarmak için kullanılır."
---

# İspat Yükünün Dağılımı (TMK m.6)

## Görev
Uyuşmazlıktaki her çekişmeli vakıa için ispat yükünün hangi tarafta olduğunu TMK m.6 ve HMK m.190 temel kuralı ile karineler çerçevesinde belirlemek; ispatsız kalan vakıanın sonucunu göstermek.

## Soğuk başlangıç (intake)
- Çekişmeli (ispat gerektiren) vakıalar nelerdir; çekişmesiz/ikrar edilen hangileri?
- Talep eden hangi hak doğurucu vakıaları ileri sürüyor; davalı hangi hak engelleyici/düşürücü/bozucu itirazları?
- Olayda yasal bir karine var mı (ör. iyiniyet TMK m.3/1, tapu/sicil TMK m.7, m.1023)?
- Kanunda ispat yükünü tersine çeviren özel bir hüküm var mı?

## Denetim şeması
1. **Temel kural** — TMK m.6 / HMK m.190/1: kanunda aksine hüküm bulunmadıkça, taraflardan her biri *hakkını dayandırdığı olguların* varlığını ispatla yükümlüdür. Hak doğurucu vakıaları talep eden, karşı (engelleyici/bozucu/düşürücü) vakıaları ileri süren ispatlar.
2. **Vakıa türüne göre dağılım** — Davacı: hakkın doğumunun şartları. Davalı: ödeme, ibra, zamanaşımı, irade sakatlığı, sözleşmenin geçersizliği gibi savunma vakıaları.
3. **Karinelerin etkisi** — Yasal karine (ör. iyiniyet TMK m.3/1, resmî sicil/senedin doğruluğu TMK m.7) lehine olan taraf ispat yükünden kurtulur; aksini iddia eden *aksini ispat* yükü altına girer. Fiilî karineler (hayatın olağan akışı) yükü tersine çevirmez, sadece takdiri etkiler.
4. **Aksine hüküm** — Kanun bazı hâllerde yükü çevirir (ör. kusursuzluğu ispat, ayıptan sorumlulukta bazı varsayımlar). Bu özel hükümler m.6'nın temel kuralının önüne geçer.
5. **İspat ölçüsü ve sonuç** — Çekişmeli vakıa tam ispat (HMK) ölçüsünde kanıtlanamazsa, o vakıa *gerçekleşmemiş* sayılır ve ispat yükü kimde ise aleyhine sonuç doğar (ispat yükünün "son sözü").
6. **Senetle ispat sınırı** — HMK m.200-201: belirli tutarın üzerindeki hukuki işlemler kural olarak senetle ispatlanır; tanıkla ispat sınırı ve istisnaları gözetilir.

## Çıktı modülleri
- Çekişmeli vakıa listesi (davacı/davalı yükü ayrımı).
- Karine tablosu ve aksini ispat yükü.
- "Aksine hüküm" kontrolü (yük çevrildi mi).
- İspatsız vakıanın sonucu + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
