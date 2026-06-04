---
name: kidem-ihbar-tazminati
description: "Kıdem ve ihbar tazminatına hak kazanma şartları ile tutarın hesaplanması gerektiğinde; hizmet süresi, giydirilmiş ücret, kıdem tavanı, ihbar öneli ve fesih sebebine göre tazminatları kalem kalem belirlemek için kullan."
---

# Kıdem ve İhbar Tazminatı Hesabı

## Görev
Kıdem (mülga 1475 m.14) ve ihbar (İş K. m.17) tazminatına hak kazanma şartlarını denetlemek ve giydirilmiş ücret üzerinden tutarı hesaplamak.

## Soğuk başlangıç (intake)
1. İşe giriş ve çıkış tarihleri; fasılalı çalışma var mı?
2. Fesheden taraf ve fesih sebebi nedir?
3. Son brüt çıplak ücret ve düzenli ekler (yol, yemek, ikramiye, prim) nelerdir?
4. Fesih tarihi hangi yıla ait (kıdem tavanı için)?

## Denetim şeması
1. **Kıdeme hak kazanma (1475 m.14):** En az **1 yıl** kıdem ve hak kazandıran fesih: işveren feshi (m.25/II hariç), işçinin haklı feshi (m.24), erkek için muvazzaf askerlik, kadın için evlilik (1 yıl içinde), emeklilik/yaşlılık aylığı şartlarını sağlama, ölüm. İstifa kural olarak kıdeme hak kazandırmaz.
2. **Kıdem hesabı:** Her tam yıl için **30 günlük** giydirilmiş brüt ücret; artan süreler oranlanır. Giydirilmiş ücrete düzenli ve süreklilik arz eden sosyal yardımlar dahil; arızi ödemeler hariç. **Kıdem tavanı** uygulanır (en yüksek devlet memuruna ödenen bir yıllık emekli ikramiyesi tutarı) — güncel tavan [doğrulanacak]. Kıdem tazminatından yalnızca damga vergisi kesilir, gelir vergisi kesilmez.
3. **İhbar (m.17):** Belirsiz süreli sözleşmede öneller: 0-6 ay → 2 hafta, 6 ay-1,5 yıl → 4 hafta, 1,5-3 yıl → 6 hafta, 3 yıldan fazla → 8 hafta. Önele uymayan taraf, önel süresine ait ücret tutarında ihbar tazminatı öder. İşçinin haklı feshinde (m.24) işçi ihbara hak kazanmaz; işverenin haklı feshinde (m.25) ihbar doğmaz.
4. **Ara sonuç:** Kıdem giydirilmiş ücret + tavan; ihbar giydirilmiş ücret üzerinden, tavansız. İhbar tazminatından gelir ve damga vergisi kesilir.
5. **Faiz:** Kıdeme **fesih tarihinden** en yüksek banka mevduat faizi; ihbara temerrüt/dava tarihinden yasal faiz.

## Çıktı modülleri
- Hak kazanma değerlendirmesi (kıdem ve ihbar ayrı ayrı).
- Giydirilmiş ücret tablosu (kalem kalem).
- Tutar hesabı + tavan kontrolü + faiz başlangıcı.
- Vergi kesintisi notu ve [doğrulanacak] güncel tavan.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
