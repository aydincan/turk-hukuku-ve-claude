---
name: ipotek-ve-tasinmaz-rehni
description: "Taşınmaz üzerinde ipotek kurulması, derecesi, kapsamı, paraya çevrilmesi (icra) ve terkini söz konusu olduğunda; alacağın teminat altına alınması, üst sınır/anapara ipoteği ayrımı ve rehnin sona ermesi değerlendirilirken kullanılır."
---

# İpotek ve Taşınmaz Rehni

## Görev
Taşınmaz rehninin kuruluşunu, kapsamını, derece sistemini, paraya çevrilmesini ve terkinini hukuki dayanakla çözümlemek; teminat ile alacak ilişkisini doğru kurmak.

## Soğuk başlangıç (intake)
- Rehin türü: anapara ipoteği mi, üst sınır (azami meblağ) ipoteği mi?
- Teminat altına alınan alacak mevcut mu, doğacak/koşullu mu; tutarı belirli mi?
- Rehin derecesi ve önceki/sonraki takyidatlar (boş derece, sabit/ilerleme sistemi) ne durumda?
- Borç ödendi mi; terkin mi, paraya çevirme (takip) aşaması mı?

## Denetim şeması
1. **Kuruluşu denetle.** İpotek resmi senetle tapu müdürlüğünde kurulur (TMK m.856; TMK m.795 — rehin tescille doğar). Geçerli bir alacağı teminat altına alır; rehin fer'idir, alacağa bağlıdır.
2. **Türü ayır.** Anapara ipoteği: belli, kesin alacak (TMK m.875 kapsamı — asıl alacak, takip giderleri, gecikme faizi). Üst sınır ipoteği: doğmuş/doğacak alacaklar belirli bir azami meblağ ile teminatlandırılır (TMK m.851). Tür, kapsamı ve faizin teminat alanını belirler.
3. **Kapsamı belirle.** Rehin, taşınmazla birlikte bütünleyici parça ve eklentiyi (TMK m.862), kira/ürün gelirlerini koşullu kapsar; kapsam dışı kalanlar ayrıca değerlendirilir.
4. **Derece sistemini uygula.** İpotek tescil edilen derecede yer alır; boşalan dereceden yararlanma (sabit dereceler ilkesi) sözleşme ve sicile göre çözülür. Sonraki rehinli alacaklının durumu sıraya bağlıdır.
5. **Paraya çevirme.** Muaccel alacak için rehnin paraya çevrilmesi yoluyla takip (2004 sayılı İİK m.145 vd.); ipoteğin türüne göre ilamlı/ilamsız ayrımı ve itiraz imkânı. Lex commissoria yasağı: doğrudan mülkiyete geçiş kararlaştırılamaz (TMK m.873/2).
6. **Terkin.** Alacak sona erince malik terkin isteyebilir (TMK m.883); rehin hakkı sona erse de sicilden silinene kadar şeklen durur.
7. **Ara sonuç.** Rehnin geçerliliği, kapsamı ve istenen işlem (tesis/terkin/takip) netleştirilir.

## Çıktı modülleri
- İpotek türü–kapsam–derece analizi.
- Resmi senet / terkin talebi veya rehnin paraya çevrilmesi takip taslağı iskeleti.
- Teminat–alacak uyumu ve faiz kapsamı risk notu.

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
