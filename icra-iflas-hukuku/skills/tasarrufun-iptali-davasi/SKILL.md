---
name: tasarrufun-iptali-davasi
description: "Borçlunun alacaklılardan mal kaçırmak için yaptığı (bağış, eşler arası devir, düşük bedelli satış gibi) tasarrufları iptal ettirmek gerektiğinde; aciz vesikası şartı, iptale tabi tasarruf türleri ve üçüncü kişinin durumu için kullanılır."
---

# Tasarrufun İptali (İptal Davaları)

## Görev
Borçlunun alacaklıyı zarara uğratan tasarruflarını (m.277-284) iptal ettirerek haczi/satışı o mal üzerinde mümkün kılmak; iptal sebeplerini ve üçüncü kişinin iyiniyet durumunu denetlemek.

## Soğuk başlangıç (intake)
- Alacak için kesin/geçici aciz vesikası var mı (m.277, m.105)?
- İptali istenen tasarruf ne (bağış, satış, ipotek, ödeme)?
- Tasarruf borcun doğumundan sonra/şüphe döneminde mi yapıldı?
- Üçüncü kişi borçlunun yakını mı; iyiniyetli sayılabilir mi?

## Denetim şeması
1. **Dava şartı — aciz hali (m.277)**: İptal davası açabilmek için alacaklının elinde (geçici/kesin) aciz vesikası veya iflas bulunmalıdır. Bu, davanın ön şartıdır.
2. **İvazsız tasarruflar (m.278)**: Bağışlamalar ve bağışlama benzeri tasarruflar (ör. mutat dışı hediyeler, eşe/yakına düşük bedelli devirler) iflas/haciz tarihinden geriye doğru belirli süre içinde iptale tabidir.
3. **Acizden doğan iptal (m.279)**: Borçlunun mevcut borçları için olağandışı ödeme, teminat verme veya muaccel olmayan borcu ödeme gibi tasarrufları, alacaklıların durumunu bilen lehtara karşı iptal edilebilir.
4. **Zarar verme kastı (m.280)**: Borçlunun mallarını kaçırma kastıyla yaptığı, üçüncü kişinin bu kastı bildiği/bilmesi gerektiği tasarruflar iptale tabidir; yakınlar bakımından bilme karinesi vardır.
5. **İspat yükü ve sonuç (m.283)**: Alacaklı iptal sebebini ispatlar; dava kabul edilirse alacaklı o mal üzerinde haciz/satış isteyebilir, mülkiyet üçüncü kişide kalmaya devam eder. Zamanaşımı m.284 (5 yıl) denetlenir.
6. **Ara sonuç**: İptale en uygun sebep, davalı çevresi ve tahsil etkisi belirlenir.

## Çıktı modülleri
- Aciz vesikası ve şüphe dönemi kontrolü.
- İptal sebebi seçim notu (m.278/279/280).
- Dava dilekçesi iskeleti ve zamanaşımı takvimi.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
