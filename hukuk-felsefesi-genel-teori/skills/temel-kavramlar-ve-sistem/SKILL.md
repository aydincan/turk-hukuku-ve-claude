---
name: temel-kavramlar-ve-sistem
description: "Hukuk felsefesi ile genel teorinin temel kavramlarını (norm, geçerlilik, meşruiyet, hak, yaptırım, kaynak) ve ekol haritasını netleştirmek; bir teorik soruyu doğru kategoriye yerleştirip pozitif hukuka bağlamak gerektiğinde kullanın."
---

# Temel Kavramlar ve Sistematik

## Görev
Genel hukuk teorisinin temel kavram dağarcığını ve ekollerini bir analiz aracı olarak
sunmak; soruyu geçerlilik, yorum, boşluk veya adalet kategorilerinden hangisine ait olduğunu
belirleyip Türk pozitif hukukuna (TMK m.1, Anayasa m.2/11/138) raptetmek.

## Soğuk başlangıç (intake)
- Soru pozitif bir norm yokken mi soruluyor (boşluk), yoksa var olan normun anlamı/geçerliliği
  mi tartışılıyor?
- Amaç akademik tartışma/sınav mı, yoksa bir uyuşmazlıkta argüman üretmek mi?
- Hangi hukuk dalı bağlamı var (özel/kamu/ceza)? Soyut soru çoğu zaman somut dalda görünür.
- Karşılaştırmalı/yabancı malzeme isteniyor mu, yoksa yalnızca Türk hukuku mu?

## Denetim şeması
1. **Kavramı yerine oturt.** Norm (kural/ilke ayrımı), geçerlilik (yürürlük + bağlayıcılık),
   meşruiyet (içeriksel haklılık), yürürlük (etkililik) ve müeyyide kavramlarını ayır.
   Bunların karıştırılması çoğu teorik hatanın kaynağıdır.
2. **Norm hiyerarşisini kur.** Anayasa m.11 ve m.90/son ışığında Anayasa > milletlerarası
   andlaşma (temel haklarda) > kanun > tüzük/yönetmelik basamağını çıkar; Kelsenci basamak
   teorisinin pozitif karşılığı budur. Üst norma aykırı alt norm tartışmasını burada konumla.
3. **Ekolü araç seç.** Pozitivizm geçerliliği kaynağa bağlar; doğal hukuk içeriğe; realizm
   yargıç davranışına; menfaat/değer içtihadı korunan çıkara. Hangi ekolün soruyu çözdüğünü
   belirt, "tek doğru ekol" iddiasından kaçın.
4. **Pozitif bağı kur.** Her teorik tezi TMK m.1 (hâkimin hukuk yaratması/bilimsel görüş ve
   içtihada başvurma), TMK m.2 (dürüstlük) veya Anayasa m.138 (hâkimin hukuka uygunluğu)
   gibi bir pozitif dayanağa bağla. Ara sonuç: teori → pozitif sonuç köprüsü.
5. **İspat/dayanak yükü.** Teorik iddiayı ulaşılabilir doktrin eserine ve varsa yerleşik
   içtihada dayandır; karar künyesi doğrulanmadıkça [doğrulanacak] işaretle.

## Çıktı modülleri
- Kavram-ayrım tablosu (geçerlilik/meşruiyet/yürürlük).
- Soru tipi etiketi ve ilgili ekol(ler) listesi.
- Pozitif dayanak haritası (madde atıflarıyla).
- İleri çalışma için doktrin okuma listesi (yazar-eser, sayfa [doğrulanacak]).

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
