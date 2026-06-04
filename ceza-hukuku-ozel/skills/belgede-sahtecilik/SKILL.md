---
name: belgede-sahtecilik
description: "Resmî/özel belgede sahtecilik, resmî belgenin düzenlenmesinde yalan beyan ve bunların dolandırıcılık gibi suçlarla içtimaı gündeme geldiğinde kullanılır."
---

# Kamu Güvenine Karşı Suçlar (Belgede Sahtecilik)

## Görev
Sahtecilik suçlarında belgenin niteliğini (resmî/özel), sahteciliğin türünü (maddi/fikrî) ve diğer suçlarla içtima ilişkisini madde metniyle belirlemek.

## Soğuk başlangıç (intake)
- Belge resmî belge mi (kamu görevlisinin görevi gereği düzenlediği) yoksa özel belge mi?
- Sahtecilik belgenin tümüyle uydurulması mı, üzerinde değişiklik mi, yoksa gerçeğe aykırı beyanın belgeye geçirilmesi mi?
- Sahte belge kullanıldı mı; kullanılarak ayrıca bir yarar sağlandı mı?
- Belge aldatma kabiliyetine (iğfal kabiliyeti) sahip mi?

## Denetim şeması
1. Resmî belgede sahtecilik (TCK m.204): Resmî belgeyi sahte düzenleme, değiştirme veya sahte belgeyi kullanma + kast. Belgenin kanunen kesin delil oluşturması nitelikli hal (m.204/3). Kamu görevlisi tarafından işlenmesi ağırlaştırıcı (m.204/2).
2. Özel belgede sahtecilik (TCK m.207): Özel belgeyi sahte düzenleme/değiştirme ve kullanma; tamamlanması için belgenin kullanılması da unsurdur.
3. Maddi/fikrî sahtecilik ayrımı: Belgenin fiziksel olarak tahrif edilmesi maddi sahtecilik; içeriğin gerçeğe aykırı olması fikrî sahteciliktir. Resmî belgenin düzenlenmesinde yalan beyan (TCK m.206) ile resmî belgede fikrî sahteciliği ayır.
4. Iğfal (aldatma) kabiliyeti: Sahteciliğin suç oluşturması için belgenin nesnel olarak aldatıcı olması gerekir; bilirkişi/kriminal inceleme bu unsuru belirler. Aldatma kabiliyeti yoksa tipiklik gerçekleşmez.
5. İçtima: Sahte belge bir dolandırıcılığın aracı olarak kullanıldıysa, sahtecilik ve dolandırıcılık (TCK m.157-158) gerçek içtima kurallarına göre ayrı ayrı değerlendirilir; tek fiille birden çok suç söz konusuysa fikrî içtima (m.44) tartışılır.
6. Ara sonuç: Belge türü + sahtecilik türü + uygulanacak madde + iğfal kabiliyeti tespiti + diğer suçlarla içtima sonucu.

## Çıktı modülleri
- Belge/sahtecilik nitelendirme tablosu (madde atıflı).
- İğfal kabiliyeti için bilirkişi sorusu önerisi.
- İçtima değerlendirme notu (sahtecilik + dolandırıcılık vb.).

## Plugin bağlamı

Bu beceri `ceza-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
