---
name: hekim-sorumlulugu-denetim-semasi
description: "Tıbbi müdahaleden doğan tazminat talebinin esasını madde madde denetlemek için kullanılır; kusur, illiyet ve zarar unsurlarını sözleşme ve haksız fiil rejimine göre adım adım çözer."
---

# Hekimin Hukuki Sorumluluğu Denetim Şeması

## Görev
Tıbbi müdahaleden doğan maddi/manevi tazminat talebinin hukuki dayanağını ve başarı şansını sistematik biçimde değerlendirmek.

## Soğuk başlangıç (intake)
1. Hangi tıbbi işlem ve hangi tıbbi sonuç (zarar) söz konusu?
2. İddia edilen kusur teşhiste mi, tedavide mi, takipte mi, onamda mı?
3. Daha önce ATK/bilirkişi/Sağlık Bakanlığı raporu alındı mı?
4. Müdahale öncesi hastanın komorbiditeleri/risk faktörleri var mıydı?

## Denetim şeması
1. **Hukuki sebep seçimi**: Sözleşmesel sorumlulukta kusur karinesi işler; borçlu (hekim) kusursuzluğunu ispatlar (TBK m.112). Haksız fiilde kusuru davacı ispatlar (TBK m.49, m.50). Yarışma halinde davacı lehine olan tercih edilir.
2. **Hukuka aykırılık / özen ihlali**: Tıbbın güncel standardına (endikasyon, doğru teşhis, doğru teknik, takip) aykırılık var mı? Aydınlatma eksikliği başlı başına hukuka aykırılıktır.
3. **Kusur**: Taksir derecesi (basit/ağır). Standart sapması bilirkişi/ATK ile somutlanır.
4. **Zarar**: Maddi zarar (tedavi gideri, iş gücü kaybı, destekten yoksun kalma TBK m.53), manevi zarar (TBK m.56), bedensel bütünlük zararı (TBK m.54).
5. **Uygun illiyet bağı**: Kusur ile zarar arasında uygun nedensellik. Komplikasyon veya hastanın bünyesel durumu illiyeti kesiyor mu? Müterafik kusur indirim sebebidir (TBK m.52).
6. **Ara sonuç**: Unsurlardan biri eksikse sorumluluk doğmaz; tümü varsa tazminat kalemleri hesaplanır.
7. **Hastane işleteninin sorumluluğu**: Özel hastane, ifa yardımcısı olan hekimin fiilinden TBK m.116 uyarınca sorumludur.

## Çıktı modülleri
- Unsur unsur değerlendirme matrisi (var/yok/şüpheli)
- Tazminat kalemleri ve hesap çerçevesi
- Delil ve bilirkişi ihtiyacı listesi
- İlkesel içtihat atfı (Yargıtay 3./15. HD; karararama.yargitay.gov.tr) [doğrulanacak]

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
