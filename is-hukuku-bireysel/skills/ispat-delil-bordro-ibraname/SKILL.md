---
name: ispat-delil-bordro-ibraname
description: "İş davasında ispat yükünün dağılımı, bordro-puantaj değeri, tanık-yazılı delil dengesi ve ibranamenin geçerliliği tartışıldığında; hangi tarafın neyi ispatlayacağını ve belgelerin delil değerini saptamak için kullan."
---

# İspat, Delil, Bordro ve İbraname Denetimi

## Görev
İş uyuşmazlığında ispat yükünü doğru dağıtmak, bordro/puantaj/özlük dosyasının delil değerini belirlemek ve ibranamenin TBK m.420 geçerliliğini denetlemek.

## Soğuk başlangıç (intake)
1. İhtilaflı vakıalar neler (ücret miktarı, fazla çalışma, fesih sebebi, izin)?
2. İmzalı bordro, banka kaydı, puantaj/PDKS, özlük dosyası mevcut mu?
3. Tanık var mı; tanıklar dönem ve mesai düzenini biliyor mu?
4. İbraname imzalanmış mı; tarihi ve içeriği nedir?

## Denetim şeması
1. **İspat yükü temeli (HMK m.190; TMK m.6):** İddia eden ispatla yükümlüdür. İş hukukunda kayıt tutma işverende olduğundan kayıt ibraz edilmemesi işveren aleyhine değerlendirilebilir.
2. **Fesih sebebinin ispatı:** Geçerli/haklı feshi işveren ispatlar (m.20/2). İşçi savunmasının alınmaması ve yazılı-gerekçeli fesih yapılmaması işveren aleyhinedir.
3. **Bordro değeri:** İmzalı ve ihtirazi kayıtsız bordroda tahakkuk eden kalemler (fazla çalışma, tatil) kural olarak ödenmiş sayılır; aksini işçi ancak **yazılı delille** çürütebilir. Tahakkuk yoksa veya bordro imzasızsa o dönem işçi lehine tanıkla ispata açıktır.
4. **Fazla çalışma/tatil:** Kural olarak işçi ispatlar; yazılı delil yoksa tanıkla ispat mümkün. Uzun dönemli ve fiziken kesintisiz çalışma iddialarında hakkaniyet/takdiri indirim uygulanır.
5. **Ücret miktarı:** Çekişmeliyse meslek kuruluşu/sendika emsal ücret araştırması delil olur.
6. **İbraname (TBK m.420):** Geçerlilik için ibra (a) yazılı, (b) sözleşme sona erdikten en az **1 ay** sonra düzenlenmiş, (c) alacak türü ve miktarı açıkça belirtilmiş, (d) ödeme banka/eksiksiz yapılmış olmalı. Eksikse ibra geçersiz; miktar içeren ama tam ödeme içermeyen belge **makbuz** hükmündedir ve kısmi ödeme olarak değerlendirilir.

## Çıktı modülleri
- Vakıa bazında ispat yükü tablosu.
- Belge delil değeri değerlendirmesi (bordro/puantaj/özlük).
- İbraname geçerlilik denetimi sonucu.
- Delil tamamlama ve celp/keşif/bilirkişi talep listesi.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
