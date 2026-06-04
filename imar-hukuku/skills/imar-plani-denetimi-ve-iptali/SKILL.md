---
name: imar-plani-denetimi-ve-iptali
description: "İmar planına veya plan değişikliğine itiraz ve iptal davası gündeme geldiğinde; askı-ilan süreci, üst ölçeğe ve şehircilik ilkelerine aykırılık, kamu yararı denetimi ve dava açma süresinin hesabı sorulduğunda kullanılır."
---

# İmar Planı Denetimi ve Plan İptal Davası

## Görev
Bir imar planı veya plan değişikliğinin hukuka uygunluğunu denetlemek; iptal davasının süre, ehliyet ve esas yönünden kurulmasını sağlamak.

## Soğuk başlangıç (intake)
- Plan hangi ölçekte (1/5000 nazım, 1/1000 uygulama) ve hangi idarece onaylandı?
- Plan/değişiklik askıya çıktı mı, askı tarihleri neler, itiraz ettiniz mi?
- Müvekkilin taşınmazı plan sınırı içinde mi, menfaati nasıl etkileniyor?
- Üst ölçekli plana veya ada/parsel dengesine aykırılık iddiası var mı?

## Denetim şeması
1. **Yetki ve usul (3194 m.8/b)**: Plan, yetkili idare meclisince onaylanıp **bir ay süreyle askıya** çıkarılır. Askı süresinde idareye itiraz edilebilir; idare itirazı 15 günde değerlendirir. Süreç usulü işlemediyse şekil sakatlığı doğar.
2. **Dava açma süresi (İYUK m.7, m.11)**: Askı süresi sonundan itibaren 60 gün; askı içinde yapılan itirazın reddi/zımni reddi yeni 60 günlük süre başlatır. Süre, planın askısının dayandığı ilana göre titizlikle hesaplanır (geç öğrenme/menfaat ihlalinin doğduğu an tartışılır).
3. **Ehliyet ve menfaat (İYUK m.2)**: Davacının planla güncel, kişisel ve meşru menfaat ilişkisi; parsel maliki, komşu parsel maliki, meslek odası/dernek dava ehliyeti ayrı ayrı değerlendirilir.
4. **Esas denetimi**: Üst ölçekli plana uygunluk; **şehircilik ilkeleri, planlama esasları ve kamu yararı** üçlü ölçütü (Danıştay yerleşik denetim ölçütü); donatı alanı dengesi, yoğunluk artışı/kazanılmış hak, kademe atlama yasağı. Plan değişikliğinde "zorunluluk ve kamu yararı" gerekçesi aranır.
5. **İspat ve bilirkişi**: Şehir plancısı bilirkişi, plan paftaları, plan açıklama raporu ve plan notları; keşif. İspat yükü işlemin hukuka uygunluğunu kanıtlama bakımından idarededir, aykırılık iddiasını davacı somutlaştırır.
6. **Ara sonuç + tedbir**: Esaslı sakatlık varsa iptal + **yürütmenin durdurulması (İYUK m.27)**; telafisi güç zarar (inşaat başlaması) vurgulanır. İçtihat atfı yapılacaksa Danıştay 6. Daire künyesi `[doğrulanacak]` ile ve karararama.danistay.gov.tr teyidiyle.

## Çıktı modülleri
- Süre hesap tablosu (askı-itiraz-dava).
- Aykırılık gerekçeleri listesi (yetki/şekil/üst plan/kamu yararı).
- YD talepli iptal dilekçesi iskeleti.
- Bilirkişiye yöneltilecek sorular taslağı.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
