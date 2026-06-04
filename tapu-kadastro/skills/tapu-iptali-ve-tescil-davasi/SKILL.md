---
name: tapu-iptali-ve-tescil-davasi
description: "Yolsuz veya geçersiz bir tescilin iptali ile gerçek hak durumuna uygun tescilin sağlanması gerektiğinde; muris muvazaası, sahte vekâletname, ehliyetsizlik, hile, irade fesadı, harici satış gibi sebeplerle tapu kaydına itiraz edileceğinde kullanılır."
---

# Tapu İptali ve Tescil Davası

## Görev
Gerçek hak durumuna aykırı (yolsuz) tescilin iptalini ve doğru malik adına tescili sağlayacak davayı sebep, taraf, görev/yetki ve ispat yönünden kurmak.

## Soğuk başlangıç (intake)
- İptal sebebi ne: muris muvazaası, sahte/iptal edilmiş vekâletname, ehliyetsizlik, irade fesadı (hata-hile-korkutma), harici/geçersiz satış, çifte tapu?
- Dava konusu pay mı, tüm parsel mi; ara malikler / iyiniyetli üçüncü kişi devri var mı?
- Davacının üstün hakkı hangi belgeye dayanıyor (miras, önceki tescil, sözleşme)?
- Tapudaki son işlem tarihi ve elden ele devir zinciri nedir?

## Denetim şeması
1. **Sebebi hukuken adlandır.** Muvazaa/muris muvazaası → TMK m.706, TBK m.19 ve TBK m.237; saklı pay değil, mülkiyetin hiç geçmemesi tartışılır. İrade fesadı → TBK m.30-39. Ehliyetsizlik → TMK m.15. Sahte vekâlet → temsil yetkisinin yokluğu.
2. **Yolsuz tescil zeminini kur.** Geçerli hukuki sebep yoksa tescil yolsuzdur (TMK m.1024); gerçek hak sahibi düzeltmeyi/iptali isteyebilir (TMK m.1025).
3. **İyiniyetli üçüncü kişi süzgecinden geçir.** Yolsuz tescile dayanarak iyiniyetle ayni hak kazanan üçüncü kişi korunur (TMK m.1023); bu durumda iptal yerine TMK m.1007 tazminatı (Hazineye karşı) gündeme gelir. İyiniyet TMK m.3'e göre değerlendirilir, kötüniyet ispatı davacıdadır.
4. **Taraf ve husumeti belirle.** Davalı kayıt maliki ve varsa ara malikler; muris muvazaasında davacı saklı pay sahibi olmayan mirasçı da olabilir, husumet diğer mirasçı/lehtara yöneltilir.
5. **Görev ve yetki.** Görevli mahkeme asliye hukuk; yetki taşınmazın bulunduğu yer kesin yetkisi (HMK m.12). Dava değeri taşınmazın/payın değeridir (harç).
6. **İspat yükü.** İddianın türüne göre davacıda (TMK m.6); muvazaada yazılı delil/yakınlık karinesi, ehliyetsizlikte sağlık kurulu raporu, vekâlette sahtelik incelemesi. Tapu kaydı, akit tablosu, keşif esastır.
7. **Ara sonuç.** İptal mümkün mü yoksa tazminata mı dönülmeli; talep sonucu (iptal + tescil) net yazılır.

## Çıktı modülleri
- Sebep–delil–talep matrisi (her iptal sebebine bağlanan delil ve madde).
- Dava dilekçesi iskeleti (taraflar, vakıa, hukuki sebep, talep sonucu, [doldurulacak] alanlar).
- İyiniyetli üçüncü kişi riski ve alternatif tazminat yolu notu.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
