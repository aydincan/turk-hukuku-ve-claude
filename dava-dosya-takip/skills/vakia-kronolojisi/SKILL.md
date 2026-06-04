---
name: vakia-kronolojisi
description: "Olayların ve usul işlemlerinin tarih sırasıyla dizilmesi, her vakıanın dayandığı evraka bağlanması ve zaman içindeki boşlukların görülmesi gerektiğinde kullan."
---

# Vakıa Kronolojisi

## Görev
Maddi olayları ve usul işlemlerini tarih sırasıyla dizip her birini dayandığı belgeye bağlayarak dosyanın zaman çizgisini ve boşluklarını görünür kılmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın başlangıç olayı (sözleşme, kaza, fesih, suç tarihi) hangi tarih?
- Hangi evrak hangi olayı belgeliyor (sözleşme, fatura, tutanak, tebligat)?
- Maddi olay kronolojisi mi, usul işlemleri kronolojisi mi, yoksa ikisi birden mi?
- Tarih çelişkisi yaratan belgeler var mı?

## Denetim şeması
1. Olay satırı: tarih, olay/işlem, dayanak evrak (ad + sayfa), tarafı. Tarih belirsizse [doldurulacak] yaz; yaklaşık tarih uydurma.
2. Maddi olay - usul ayrımı: maddi vakıalar (zamanaşımı ve hak düşürücü süre başlangıcı için kritik) ile usul işlemleri (tebligat, duruşma, ara karar) ayrı renk/kolon.
3. Süre tetikleyici tespiti: her olayın bir süreyi başlatıp başlatmadığını işaretle (tebligat → cevap süresi HMK m.127; karar tebliği → istinaf süresi HMK m.345). Bu satırlar süre takvimine devredilir.
4. Boşluk ve çelişki: kronolojideki açıklanamayan aralıklar ve çelişen tarihler ayrı not. İspat yükü (HMK m.190) açısından hangi vakıayı kimin ispatlaması gerektiğini belirt.
5. Ara sonuç: zaman çizgisi + süre tetikleyici işaretleri + boşluk listesi. Her satır kaynağa bağlı; belgesiz vakıa eklenmez.

## Çıktı modülleri
- Tarih-olay-dayanak-taraf kolonlu kronoloji tablosu.
- Süre tetikleyici olaylar alt listesi.
- Tarih boşlukları ve çelişkileri notu.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
