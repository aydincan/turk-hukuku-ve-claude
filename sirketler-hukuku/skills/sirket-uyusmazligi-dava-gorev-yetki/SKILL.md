---
name: sirket-uyusmazligi-dava-gorev-yetki
description: "Bir şirket uyuşmazlığında görevli mahkeme (asliye ticaret), yetki, ticari dava niteliği, arabuluculuk dava şartı, ihtiyati tedbir ve süreler belirlenirken; doğru usul rotasını ve süreleri kaçırmamak için kullanılır."
---

# Şirket Uyuşmazlıklarında Dava, Görev ve Yetki

## Görev
Şirket kaynaklı uyuşmazlığı doğru usul rotasına oturtmak: ticari dava niteliği, görevli/yetkili mahkeme, dava şartı arabuluculuk, ihtiyati tedbir ve hak düşürücü süreler.

## Soğuk başlangıç (intake)
1. Uyuşmazlık türü ne (genel kurul iptali, sorumluluk, pay devri, fesih, alacak)?
2. Taraflar tacir mi; uyuşmazlık mutlak ticari dava mı (TTK m.4)?
3. Konusu para alacağı mı (dava şartı arabuluculuk gerekir mi)?
4. Hak düşürücü/zamanaşımı süresi işliyor mu (ör. iptal 3 ay)?
5. Acil koruma (ihtiyati tedbir, kararın icrasının ertelenmesi) gerekiyor mu?

## Denetim şeması
1. Ticari dava niteliği: TTK m.4 (mutlak ticari davalar — TTK'dan doğanlar dâhil) ve m.5 (görev). Şirketler hukuku uyuşmazlıkları kural olarak ticari davadır.
2. Görev: Asliye ticaret mahkemesi (TTK m.5; 6102/6335 düzenlemeleri). Tek hâkim/heyet ayrımı parasal sınıra göre.
3. Yetki: Genel kurul iptali ve birçok şirket davası için şirket merkezi mahkemesi (ör. m.445/2). Genel yetki HMK m.6; sözleşmeden doğan alacakta HMK m.10.
4. Dava şartı arabuluculuk: Ticari davalarda konusu bir miktar para olan alacak/tazminat talepleri için dava açmadan önce arabuluculuk zorunlu (TTK m.5/A; 6325 sayılı HUAK ve ilgili düzenlemeler). İptal/tespit davaları kural olarak kapsam dışı — talebin niteliğini denetle.
5. Süreler: Genel kurul iptali 3 ay (m.445); sorumlulukta m.560 zamanaşımı; pay devrine bağlı talepler ilgili özel sürelere tabi. Süreyi en başta takvimle.
6. İhtiyati tedbir/koruma: HMK m.389 vd. tedbir; genel kurul kararının icrasının ertelenmesi m.449 (teminat).
7. İspat ve dava şartları: HMK m.114-115 dava şartları (görev, yetki kesin değilse ilk itiraz, arabuluculuk dava şartı); HMK m.190 ispat yükü.

## Çıktı modülleri
- Usul rotası kararı (görev-yetki-arabuluculuk-süre tablosu).
- Süre takvimi ve hak düşürücü süre uyarıları.
- İhtiyati tedbir/erteleme talebi taslağı.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
