---
name: ispat-delil-bilirkisi
description: "Ekonomik suç dosyasında belge, banka kaydı, dijital veri ve kurum raporlarının (VDK, MASAK, SPK, BDDK) delil değeri, delil yasakları ve mali bilirkişi raporunun denetimi söz konusu olduğunda kullanılır."
---

# İspat, Delil ve Bilirkişi Değerlendirmesi

## Görev
Ekonomik suç dosyasının delil mimarisini kurmak; kurum raporları ile bilirkişi raporlarının değerini, hukuka aykırı delil sorununu ve maddi hesabı denetlemek.

## Soğuk başlangıç (intake)
- Hangi deliller var? (fatura/defter, banka hareketleri, e-posta/mesaj, müfettiş raporu)
- Delil nasıl elde edildi? (arama-elkoyma kararı, MASAK bildirimi, açık kaynak)
- Hesaba/zarara ilişkin bilirkişi raporu düzenlendi mi?
- Çelişkili veya eksik delil/rapor var mı?

## Denetim şeması
1. **Delil serbestisi ve yasak (CMK)**: Ceza muhakemesinde her şey delil olabilir (m.217), ancak hukuka aykırı yöntemle elde edilen deliller hükme esas alınamaz (Anayasa m.38/6, CMK m.206/2-a, m.217/2, m.230). Dijital delilde elkoyma usulü ve imaj/hash zinciri (CMK m.134 yöntemi) kontrol edilir.
2. **Kurum raporlarının niteliği**: VDK vergi suçu raporu, MASAK inceleme raporu, SPK denetim raporu ve BDDK raporları delil/uzman görüşü niteliğindedir; bağlayıcı değildir, mahkeme serbestçe değerlendirir. Rapordaki tespit-sonuç bağı ve metodoloji denetlenir.
3. **Bilirkişi raporu**: Mali/muhasebe bilirkişisi, görevlendirme kapsamı, dayanak belgeler, hesap yöntemi ve çelişki bakımından incelenir; eksiklik/çelişki halinde ek rapor veya yeni bilirkişi talep edilir. Hukuki nitelendirme bilirkişiye bırakılamaz (hâkimin işi).
4. **İspat yükü ve şüpheden sanık yararlanır**: Kast ve fiil iddia makamınca ispatlanır; şüphe sanık lehine yorumlanır. Savunma karşıt delil ve karşıt inceleme (sahte fatura zincirinde karşıt mükellef kaydı) ile çalışır.
5. **Belge zinciri**: Fatura-ödeme-mal akışı-stok-banka kaydı bütünlüğü kurularak işlemin gerçekliği veya sahteliği gösterilir.
6. **Ara sonuç**: Delil listesi, hukuka uygunluk durumu, rapor güvenilirliği ve ispat boşlukları netleşir.

## Çıktı modülleri
- Delil envanteri ve elde ediliş hukukîliği tablosu
- Kurum raporu metodoloji eleştirisi
- Bilirkişi raporu denetim/itiraz notu
- Belge-akış zinciri analizi
- Karşıt delil ve ispat stratejisi

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
