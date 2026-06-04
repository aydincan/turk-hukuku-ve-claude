---
name: sureler-zamanasimi
description: "Fikri-sınai uyuşmazlıkta TÜRKPATENT itiraz süreleri, hükümsüzlük/iptal, tazminat zamanaşımı, ihtiyati tedbir sonrası dava süresi ve sessiz kalma yoluyla hak kaybını hesaplamak gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Davaya etki eden tüm süreleri (idari itiraz, dava, tedbir, zamanaşımı, hak düşürücü) doğru hesaplayıp takvime bağlamak; hak kaybını önlemek.

## Soğuk başlangıç (intake)
- Bir TÜRKPATENT/YİDK kararı var mı ve tebliğ tarihi nedir?
- Tecavüz ne zaman öğrenildi, ne zaman gerçekleşti, devam ediyor mu?
- İhtiyati tedbir dava açılmadan mı alındı?
- Marka kaç yıldır biliniyor/kullanılıyor (sessiz kalma riski)?

## Denetim şeması
1. İdari süreçler: Marka yayımına itiraz ve karara itiraz süreleri SMK m.18-20 çerçevesinde (yayımdan itibaren itiraz; YİDK kararına karşı dava süresi tebliğden 2 ay — SMK m.21 ilgili hükmü). Süre kaçırılırsa idari karar kesinleşir.
2. Tazminat zamanaşımı: Tecavüz haksız fiildir; TBK m.72 — zararı ve faili öğrenmeden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanabilir (TBK m.72/1 son cümle).
3. Süregelen tecavüz: İhlal devam ediyorsa zamanaşımı her gün yeniden işlemeye başlar; geçmişe dönük talepte 2 yıllık kesit korunur.
4. Tedbir sonrası dava: Dava açılmadan alınan ihtiyati tedbirde 2 hafta içinde esas dava açılmazsa tedbir kendiliğinden kalkar (HMK m.397/1). Delil tespitinde benzer disiplin.
5. Sessiz kalma: Marka hükümsüzlüğünde 5 yıl boyunca sonraki markaya sessiz kalma hak kaybı doğurur; kötüniyet istisnadır (SMK m.25/6).
6. Hak düşürücü-zamanaşımı ayrımı: Hükümsüzlük davaları kural olarak süreye tabi değildir (kullanmama/sessiz kalma istisnaları hariç). Ara sonuç: her süre kaynağı (idari, adli, tedbir) ayrı izlenir.

## Çıktı modülleri
- Süre takvimi tablosu (kaynak / başlangıç / bitiş / dayanak madde).
- Zamanaşımı risk notu (süregelen ihlal vurgusuyla).
- Tedbir/delil tespiti dava açma süresi uyarısı.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
