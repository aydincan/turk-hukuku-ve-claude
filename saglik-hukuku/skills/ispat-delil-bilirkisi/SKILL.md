---
name: ispat-delil-bilirkisi
description: "Tıbbi uyuşmazlıkta ispat yükünün dağılımını, hangi delillerin toplanacağını ve ATK/bilirkişi raporlarının nasıl denetleneceğini belirlemek için kullanılır."
---

# İspat, Delil ve Bilirkişi/ATK Raporu

## Görev
İspat yükünün taraflar arasında dağılımını saptamak, dosyaya kazandırılacak delilleri planlamak ve bilirkişi/ATK raporunu metodolojik olarak denetlemek.

## Soğuk başlangıç (intake)
1. Tartışmalı vakıa kusur mu, illiyet mi, aydınlatma mı, zarar miktarı mı?
2. Tıbbi kayıtlar (epikriz, ameliyat notu, onam formu, tetkikler) tam mı?
3. Dosyada hangi raporlar var (ATK, üniversite, özel bilirkişi)?
4. Tanık (ekip, refakatçi) ve uzmanlık dalı belli mi?

## Denetim şeması
1. **İspat yükü dağılımı**: Genel kural TMK m.6 — iddia eden ispatla yükümlüdür. Davacı kusur, illiyet ve zararı; hekim/hastane ise aydınlatma ve onamın varlığını ispatlar. Sözleşmesel sorumlulukta kusursuzluk ispatı borçludadır (TBK m.112).
2. **Delil toplama**: Tıbbi kayıtların eksiksiz celbi (HMK m.219-220 belge ibrazı), tedavi gören kurum dosyası, onam belgeleri, görüntüleme/laboratuvar verileri, tanık.
3. **Bilirkişi/ATK**: HMK m.266 vd. uyarınca özel/teknik bilgi gerektiren konularda bilirkişiye başvuru; sağlık uyuşmazlıklarında ATK İhtisas Kurulları sık başvurulur. Hâkim raporla bağlı değildir.
4. **Rapor denetimi**: Görevlendirme kapsamına uygunluk, dayanak vakıaların doğruluğu, metodolojinin açıklığı, sonuç-gerekçe tutarlılığı, çelişki ve maddi hata kontrolü.
5. **İtiraz / ek rapor**: Çelişki veya eksiklik varsa gerekçeli itiraz, ek rapor, üniversiteden veya farklı kuruldan yeni rapor talebi (HMK m.281).
6. **Ara sonuç**: Belirleyici teknik sorun raporla çözülür; rapor yetersizse hüküm bozma sebebidir.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa bazlı)
- Delil toplama ve celp listesi
- Bilirkişi/ATK rapor denetim kontrol listesi
- Gerekçeli rapor itiraz taslağı (yer tutuculu)

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
