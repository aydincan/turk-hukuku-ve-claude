---
name: pay-sahipleri-sozlesmesi-sha
description: "Yatırımcı ve kurucular arasındaki yönetişim ve çıkış dengesini kuran pay sahipleri sözleşmesi (SHA) hazırlanır veya müzakere edilirken; veto, bilgi alma, sürükleme-birlikte satış, önalım gibi hükümlerin Türk hukukundaki geçerliliği ve esas sözleşmeyle ilişkisi denetlenirken kullanılır."
---

# Pay Sahipleri Sözleşmesi (SHA) Kurgusu

## Görev
Kurucu-yatırımcı ilişkisinin yönetişim, kontrol, koruma ve çıkış mekanizmalarını SHA'da TBK serbestisi içinde kurgulamak; hangi hükmün esas sözleşmeye taşınması (ayni etki için) gerektiğini saptamak.

## Soğuk başlangıç (intake)
1. Taraflar ve pay oranları; kim çoğunluk, kim azınlık/yatırımcı?
2. İstenen mekanizmalar: veto/onay konuları, yönetim koltuğu, bilgi alma?
3. Çıkış hükümleri: drag-along, tag-along, önalım, IPO/satış senaryosu?
4. Vesting (kurucu ve çalışan) ve rekabet/devamlılık yükümlülüğü isteniyor mu?
5. İhtilaf çözümü: tahkim mi, mahkeme mi; uygulanacak hukuk?

## Denetim şeması
1. Geçerlilik temeli: SHA hükümleri taraflar arası borç sözleşmesidir (TBK m.26-27 serbestisi). Bunlar şirkete karşı doğrudan etki etmez; ayni etki (devir engeli, imtiyaz) için esas sözleşme/bağlam (TTK m.491-493, m.478-479) gerekir.
2. Yönetişim: Veto/olumlu oy konuları, yönetim kurulu temsili — oy sözleşmesi geçerli; ancak oy hakkının payla bütünlüğü (m.434) ve dürüstlük (TMK m.2) sınırı. Devredilemez YK yetkileri (m.375) sözleşmeyle kurucudan alınamaz.
3. Çıkış mekanizmaları: Drag-along (sürükleme), tag-along (birlikte satış), önalım — taraflar arası borç olarak geçerli; ihlalde cezai şart (TBK m.179) ve aynen ifa/tazminat. Payın üçüncü kişiye geçişini şirkete karşı engellemek için esas sözleşmesel bağlam (m.491-493) eklenmeli.
4. Vesting/ters vesting: Kurucu paylarının hak edilmesi; ayrılma halinde geri alım veya zorunlu satış — TBK serbestisi + esas sözleşmesel devir mekanizması ile kurulur.
5. Çıkmaz (deadlock): Eşit ortaklıkta tıkanma çözümü (shotgun/rus ruleti, üçüncü kişi, fesih); haklı sebeple fesih hakkı saklı (TTK m.531).
6. Uyum/çatışma: SHA-esas sözleşme çelişkisinde şirkete karşı esas sözleşme; taraflar arası SHA. Çatışmayı baştan haritala.
7. İspat/şekil: Yazılı; gerekirse imza onaylı. İhlalde def'i ve cezai şart kanıt zinciri.

## Çıktı modülleri
- SHA hüküm seti taslağı (veto/drag/tag/önalım/vesting + cezai şart).
- Esas sözleşmeye taşınması gereken hükümlerin listesi (ayni etki notu).
- SHA-esas sözleşme uyum/çatışma matrisi.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
