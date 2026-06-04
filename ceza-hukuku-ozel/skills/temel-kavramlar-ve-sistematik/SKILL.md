---
name: temel-kavramlar-ve-sistematik
description: "Somut bir olayda hangi suç tipinin (veya tiplerinin) gündeme geldiğini belirlemek, TCK İkinci Kitap sistematiğine yerleştirmek ve genel hükümlerle bağ kurmak gerektiğinde kullanılır."
---

# Özel Hükümler Sistematiği ve Suç Tipi Belirleme

## Görev
Bir olay anlatımından hareketle gündeme gelebilecek tüm suç tiplerini TCK 5237 İkinci Kitap sistematiği içinde tespit etmek, bunları korunan hukuki değere göre tasnif etmek ve hangi maddelere odaklanılacağını belirlemek.

## Soğuk başlangıç (intake)
- Olayda kim kime, ne yaptı; somut fiil(ler) nelerdir?
- Bir zarar/netice doğdu mu (ölüm, yaralanma, malvarlığı kaybı, itibar zedelenmesi)?
- Fail kamu görevlisi mi; mağdurla aralarında özel bir ilişki (akrabalık, vesayet, hizmet) var mı?
- Birden fazla fiil/mağdur veya tek fiille birden çok ihlal söz konusu mu?

## Denetim şeması
1. Fiil ayrıştırması: Anlatımı tek tek hareketlere böl. Her hareket için ayrı tipiklik araması yap; tek fiille birden çok suç olabileceğini (fikrî içtima TCK m.44) unutma.
2. Korunan hukuki değere göre tasnif: hayat (m.81 vd.), vücut dokunulmazlığı (m.86 vd.), hürriyet (m.106, m.109), şeref (m.125 vd.), cinsel dokunulmazlık (m.102-105), malvarlığı (m.141 vd., m.155, m.157), kamu güveni (m.204, m.207), kamu idaresi (m.247, m.252, m.257).
3. Tip seçimi ve sınır çizme: Benzer tipleri ayır. Örneğin malın rızayla teslim alınıp sonra mal edinilmesi güveni kötüye kullanma (m.155); hileyle teslim alınması dolandırıcılık (m.157); rıza olmaksızın alınması hırsızlık (m.141); cebir/tehditle alınması yağma (m.148).
4. Genel hükümlerle bağ: Seçilen her tip için kast/taksir (m.21-22), teşebbüs (m.35), iştirak (m.37-41) ve içtima kurallarının uygulanıp uygulanmadığını işaretle; ileri analiz için ilgili uzman beceriye yönlendir.
5. Ara sonuç: Olası suç tiplerinin listesi, her biri için dayanak madde ve "kuvvetli/zayıf ihtimal" notu; eksik bilgi varsa hangi olgunun açıklığa kavuşturulması gerektiği.

## Çıktı modülleri
- Suç tipi haritası (madde atıflı tablo: tip, korunan değer, dayanak madde, ihtimal derecesi).
- Sınır tipler arası ayrım notu (neden bu tip, neden öteki değil).
- Genel hükümler kontrol bayrakları (teşebbüs/iştirak/içtima/şikâyet) ve hangi uzman beceriye gidileceği.

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
