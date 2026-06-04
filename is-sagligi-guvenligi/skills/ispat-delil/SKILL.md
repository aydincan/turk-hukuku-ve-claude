---
name: ispat-delil
description: "İSG uyuşmazlıklarında ispat yükünün dağılımını, delil türlerini ve bilirkişi-kusur raporlarının değerlendirilmesini ele almak için kullanılır."
---

# İspat ve Delil Yönetimi

## Görev
İSG dosyasında ispat yükünü doğru dağıtmak, hangi tarafın neyi ispatlayacağını netleştirmek ve delilleri (belge, tanık, bilirkişi/kusur raporu) stratejik biçimde örgütlemek.

## Soğuk başlangıç (intake)
- Hangi vakıa çekişmeli (kaza nitelendirmesi, önlem alınıp alınmadığı, kusur oranı, zarar miktarı)?
- İşverenin uyum belgeleri (risk değerlendirmesi, eğitim, muayene, KKD teslim tutanağı) mevcut mu, imzalı mı?
- Kaza anına ilişkin tutanak, kamera kaydı, tanık, kolluk/iş müfettişi raporu var mı?
- Bilirkişi/kusur raporu düzenlendi mi; itiraz edilecek nokta var mı?

## Denetim şeması
1. **İspat yükü dağılımı:** İşçi/hak sahibi kazayı, zararı ve illiyeti ortaya koyar; işveren ise gerekli İSG önlemlerini aldığını ve gözetme borcunu yerine getirdiğini ispatla yükümlüdür (TBK m.417/2, m.112 mantığı; TMK m.6). Bu dağılım dosyanın iskeletidir.
2. **Belge delilleri:** İmzalı ve tarihli risk değerlendirmesi, İSG eğitim katılım belgeleri, işe giriş/periyodik muayene, KKD zimmet tutanağı, onay/öneri defteri. İmzasız/tarihsiz belge ispat değeri düşüktür.
3. **Diğer deliller:** Tanık (iş arkadaşı, ustabaşı), kamera, makine bakım kayıtları, iş müfettişi ve kolluk tutanağı, ATK/sağlık raporu (maluliyet).
4. **Bilirkişi/kusur raporu:** Kusur dağılımı ve teknik illiyet bu raporla belirlenir. Rapor görevlendirme kapsamına uygun mu, yöntemi ve dayanağı somut mu, hesap ve maddi hata var mı, çelişki taşıyor mu? Gerekçeli itirazla ek rapor/yeni heyet istenebilir.
5. **Karine ve değerlendirme:** Risk değerlendirmesinin/eğitimin yokluğu, kusur aleyhine güçlü emaredir. **Ara sonuç:** Çekişmeli her vakıa için "ispat yükü → mevcut delil → eksik delil" tablosu çıkar.

## Çıktı modülleri
- Çekişmeli vakıa-ispat yükü-delil matrisi.
- Belge delili yeterlilik kontrol listesi.
- Bilirkişi raporuna itiraz gerekçeleri taslağı.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
