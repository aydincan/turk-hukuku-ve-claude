---
name: sinir-disi-idari-gozetim
description: "Yabancı hakkında sınır dışı etme (deport) kararı veya idari gözetim kararı verildiğinde; kararın hukuka uygunluğunu, geri gönderme yasağını ve dava/itiraz sürelerini denetlemek için kullanılır."
---

# Sınır Dışı Etme ve İdari Gözetim

## Görev
Sınır dışı etme ve idari gözetim kararlarını YUKK çerçevesinde denetlemek, sınır dışı edilemeyecekler ve geri gönderme yasağı korumalarını tespit etmek, kısa dava/itiraz sürelerini kaçırmadan yürütmeyi durdurmak.

## Soğuk başlangıç (intake)
1. Sınır dışı kararının tebliğ tarihi ve gerekçesi (hangi YUKK m.54 fıkrası) nedir?
2. İdari gözetim kararı var mı; gözetim başlangıç tarihi ve geri gönderme merkezi neresi?
3. Yabancı koruma başvurusu yaptı mı, ailesi/çocuğu Türkiye'de mi, sağlık durumu nedir?
4. Geri dönüşte yaşam/işkence riski var mı (m.55 / AİHS m.3)?

## Denetim şeması
1. **Sınır dışı sebebi**: YUKK m.54 — hangi fıkraya dayanıldığı (kamu düzeni/güvenliği, vize-ikamet ihlali, çalışma izni olmadan çalışma, terör/örgüt irtibatı vb.) ve maddi dayanağı denetlenir.
2. **Sınır dışı edilemeyecekler**: m.55 — geri gönderildiğinde ölüm cezası/işkence/insanlık dışı muamele riski, ciddi sağlık/yaş/gebelik, insan ticareti veya şiddet mağduru durumu. Bu haller mutlak engel oluşturabilir.
3. **Karara karşı dava**: Sınır dışı kararına karşı idare mahkemesine dava — kısa hak düşürücü süre (m.53); dava açılması halinde kural olarak işlem yürütülmez (geri gönderme yasağının usulî güvencesi). Süre titizlikle hesaplanır.
4. **İdari gözetim**: m.57 — valilik kararıyla, geri gönderme merkezinde; süre sınırı ve uzatma rejimi, aylık değerlendirme. Gözetime karşı sulh ceza hâkimliğine itiraz (m.57/6); hâkim kararı kesindir, ancak şartlar değişirse yeniden başvuru mümkündür.
5. **Alternatif yükümlülükler**: m.57/A — gözetim yerine ikamet zorunluluğu, bildirim, teminat gibi tedbirler.
**İspat yükü**: Sınır dışı sebebinin varlığını idare ispatlar; m.55 koruması ve riski yabancı somut delil/anlatıyla ortaya koyar. Tereddütte geri gönderme yasağı lehe işler.

## Çıktı modülleri
- Süre hesap tablosu (tebliğ → dava/itiraz son günü).
- Sınır dışına karşı iptal davası ve YD/yürütülmeme talebi dilekçesi.
- İdari gözetime karşı sulh ceza hâkimliği itiraz dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
