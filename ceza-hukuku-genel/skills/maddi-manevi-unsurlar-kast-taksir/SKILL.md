---
name: maddi-manevi-unsurlar-kast-taksir
description: "Fiilin maddi unsurları (fail, netice, nedensellik) ile manevi unsurun kast mı taksir mi olduğunu, olası kast ile bilinçli taksir sınırını ayırt etmek gerektiğinde kullanılır."
---

# Maddi ve Manevi Unsurlar — Kast ve Taksir

## Görev
Suçun maddi unsurlarını çözümlemek ve failin manevi durumunu (kast/taksir) doğru sınıflandırmak; özellikle olası kast (TCK m.21/2) ile bilinçli taksir (TCK m.22/3) arasındaki ince sınırı netleştirmek.

## Soğuk başlangıç (intake)
- Netice fail tarafından öngörüldü mü; öngördüyse kabullenildi mi yoksa istenmedi mi?
- Fiil ile netice arasındaki nedensellik zinciri kesintisiz mi?
- Suç tipi taksirle işlenebiliyor mu, yoksa yalnızca kasten mi cezalandırılıyor?
- Failin dikkat ve özen yükümlülüğü neydi, hangi kuralı ihlal etti?

## Denetim şeması
1. **Maddi unsur analizi:** Fail-fiil-netice-konu-mağdur tespiti; ihmali suçlarda garantörlük (TCK m.83, m.88 örnekleri) ve hareketle netice arasında nedensellik ile objektif isnadiyet.
2. **Manevi unsurun esası (m.21/1):** Kast, suçun kanuni tanımındaki unsurların bilerek ve istenerek gerçekleştirilmesidir. Doğrudan kast: netice amaçlanmış ya da zorunlu sonuç olarak öngörülmüştür.
3. **Olası kast (m.21/2):** Fail neticeyi öngörmüş ve "olursa olsun" diyerek kabullenmiştir; ceza belirli oranda indirilir. Ara sonuç: kabulleniş var mı?
4. **Taksir (m.22):** Dikkat ve özen yükümlülüğüne aykırılıkla öngörülmeyen netice. Basit taksirde netice öngörülmemiştir.
5. **Bilinçli taksir (m.22/3):** Fail neticeyi öngörmüş fakat istememiş ve gerçekleşmeyeceğine güvenmiştir; ceza artırılır. Sınır ölçütü: olası kastta kabulleniş, bilinçli taksirde gerçekleşmeyeceğine güven.
6. **Netice sebebiyle ağırlaşma (m.23):** Ağır netice yönünden en az taksir aranır; kusursuz sorumluluk yasaktır. Ara sonuç: ağır netice fail açısından öngörülebilir miydi?

## Çıktı modülleri
- Kast/taksir sınıflandırması ve gerekçe (olay-madde eşlemesi).
- Olası kast vs. bilinçli taksir karşılaştırma tablosu.
- Nedensellik/isnadiyet zinciri şeması.
- İspat için gerekli delil ve `[doğrulanacak]` içtihat notu.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
