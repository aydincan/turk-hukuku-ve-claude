---
name: eser-sozlesmesi-ayip-temerrut
description: "İnşaat, imalat, tadilat veya yazılım gibi bir eserin ayıplı, geç veya eksik teslim edilmesi halinde iş sahibinin haklarını ve yüklenicinin sorumluluğunu denetlemek gerektiğinde kullanılır."
---

# Eser Sözleşmesi — Ayıp, Teslim ve Temerrüt

## Görev
Eserin (inşaat, imalat, tadilat, yazılım) ayıbı, gecikmesi veya bedel uyuşmazlığında tarafların haklarını TBK m.470-486 çerçevesinde denetlemek; ayıba karşı tekeffül ile temerrüt rejimini ayırmak.

## Soğuk başlangıç (intake)
- Eserin konusu ve teslim durumu (teslim edildi/edilmedi, kabul var mı)?
- Ayıp türü (gizli/açık, ağır/önemli); gözden geçirme yapıldı mı?
- Ücret götürü mü, yaklaşık mı; ek iş/imalat var mı?
- Gecikme varsa kesin vade/ihtar durumu?

## Denetim şeması
1. **Yüklenicinin özen ve sadakat borcu (m.471).** Malzeme yüklenicininse ayıba karşı satıcı gibi sorumlu; iş sahibininse uygun olmayan malzeme/talimatı bildirme yükü (m.472).
2. **Eseri gözden geçirme ve bildirim (m.477).** İş sahibi teslimden sonra imkân bulunca gözden geçirip ayıpları uygun sürede bildirir; aksi halde kabul edilmiş sayılır. Açıkça/örtülü kabul yüklenicinin sorumluluğunu (kasten gizlenen ayıp hariç) kaldırır.
3. **İş sahibinin seçimlik hakları (m.475).** Eser ayıplı ve kullanılamaz/kabul beklenemezse dönme; ayıbın giderilmesini isteme (aşırı masraf gerektirmiyorsa); bedelden indirim. Ayrıca yüklenicinin kusuru varsa tazminat.
4. **Ayıp sorumluluğu zamanaşımı (m.478).** Teslimden itibaren 2 yıl; taşınmaz yapılarda 5 yıl; yüklenicinin ağır kusuru varsa 20 yıl. Süreler kabul tarihiyle bağlantılı işletilir.
5. **Ücret ve ek iş (m.480-481).** Götürü bedelde kural olarak artırılamaz; olağanüstü hâl/aşırı ifa güçlüğünde hâkim uyarlayabilir (m.480/2; TBK m.138 ile birlikte). Yaklaşık bedel aşımında iş sahibinin dönme hakkı (m.481).
6. **Temerrüt/erken dönme (m.473).** İşe zamanında başlamama veya gecikme açıkça öngörülüyorsa iş sahibi süre vermeden dönebilir. İş sahibinin tazminatla fesih hakkı m.484. İspat: ayıbı iş sahibi, ayıbın iş sahibi malzeme/talimatından kaynaklandığını yüklenici ispatlar. Ara sonuç: hak-süre matrisi.

## Çıktı modülleri
- Ayıp bildirim ve onarım talebi yazısı.
- Bedelden indirim/dönme dava iskeleti.
- Götürü-yaklaşık bedel uyarlama notu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
