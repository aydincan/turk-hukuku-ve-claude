---
name: nitelikli-hal-ceza-belirleme
description: "Bir suçta uygulanacak nitelikli/daha az cezayı gerektiren halleri taramak ve temel cezadan sonuç cezaya giden TCK m.61-62 hesabını yapmak gerektiğinde kullanılır."
---

# Nitelikli Haller ve Cezanın Belirlenmesi

## Görev
Tespit edilen suç tipi üzerinde tüm nitelikli/indirim hallerini taramak ve temel cezadan başlayarak takdiri indirim, teşebbüs, iştirak ve içtima etkilerini sıraya koyarak sonuç cezaya ulaşmak.

## Soğuk başlangıç (intake)
- Hangi suç tipi ve hangi fıkra esas alınıyor?
- Suça etki eden nitelikli unsurlar (silah, gece, kamu görevlisi, örgüt, akrabalık) var mı?
- Failin yaşı, akıl durumu, haksız tahrik veya hata söz konusu mu?
- Suç tamamlandı mı yoksa teşebbüs aşamasında mı kaldı; birden çok suç/mağdur var mı?

## Denetim şeması
1. Temel ceza (TCK m.61): İlgili maddenin alt-üst sınırı içinde; suçun işleniş biçimi, kullanılan araç, zaman-yer, kast/taksir yoğunluğu ve meydana gelen zarar dikkate alınarak temel ceza belirlenir.
2. Nitelikli haller: İlgili özel hükmün nitelikli hal fıkralarını ve daha az cezayı gerektiren halleri uygula. Aynı yönde birden çok nitelikli hal varsa her birini gerekçelendir.
3. Kusurluluğu/haksızlığı etkileyen genel haller: Haksız tahrik (TCK m.29), yaş küçüklüğü (m.31), akıl hastalığı (m.32), sağır-dilsizlik (m.33), hata (m.30), cebir-tehdit (m.28), meşru savunmada sınırın aşılması (m.27).
4. Teşebbüs ve iştirak: Teşebbüste meydana gelen zarar/tehlikeye göre indirim (TCK m.35). İştirakte faillik/azmettirme/yardım ayrımına göre ceza (m.37-39); gönüllü vazgeçme (m.36).
5. İçtima: Zincirleme suç (TCK m.43) tek ceza + artırım; fikrî içtimada en ağır ceza (m.44); bileşik suç (m.42) ayrı ceza verilmez. Aynı neviden veya farklı neviden fikrî içtima ayrımını gözet.
6. Takdiri indirim ve sonuç ceza (TCK m.62): Takdiri indirim nedenleri uygulanır; ardından TCK m.50 (seçenek yaptırımlar), m.51 (erteleme), CMK m.231 (HAGB) imkânları değerlendirilir. Ara sonuç: gerekçeli ceza hesabı zinciri.

## Çıktı modülleri
- Adım adım ceza hesabı tablosu (temel ceza → nitelikli hal → genel haller → teşebbüs/iştirak/içtima → takdiri indirim → sonuç).
- Seçenek yaptırım/erteleme/HAGB uygunluk değerlendirmesi.
- Her adım için madde atıflı gerekçe notu.

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
