---
name: cari-hesap
description: "Taraflar arasinda karsilikli alacaklarin bir hesaba kaydedilip donem sonunda bakiyenin tespit edildigi cari hesap iliskisinin kurulmasi, bakiyenin tahakkuku, faiz, sozlesmenin sona ermesi ve bakiyenin talebi gerektiginde kullanilir."
---

# Cari Hesap İlişkisi

## Görev
Cari hesap sözleşmesinin varlığını, işleyişini ve sona ermesini değerlendirmek; dönem sonu bakiyesinin nasıl kesinleştiğini ve talep edilebileceğini belirlemek. Cari hesap, ticari ilişkilerde alacakların netleştirilmesinin özel rejimidir.

## Soğuk başlangıç (intake)
1. Taraflar arasında yazılı cari hesap sözleşmesi var mı (TTK m.89 şekil)?
2. Hesap dönemleri ve bakiye tespit usulü ne?
3. Bakiyeye itiraz edildi mi; tanınma (kabul) gerçekleşti mi?
4. İlişki sona erdi mi; faiz ve zamanaşımı durumu ne?

## Denetim şeması
1. **Tanım ve şekil:** TTK m.89 — iki kişinin (en az biri tacir olması şart değil, ama uygulamada ticari) para, mal, hizmet ve diğer hususlardan doğan alacaklarını ayrı ayrı istemekten karşılıklı olarak vazgeçip bunları kalem kalem alacak-borç şekline çevirerek hesabın kesilmesinden sonra çıkacak bakiyeyi isteyebilecekleri sözleşmedir. Sözleşme yazılı şekle tabidir (m.89/2).
2. **İşleyiş ve hesap dışı kalanlar:** TTK m.90 — belirli alacaklar (örn. takas edilemeyen, özel amaca tahsisli) cari hesaba geçirilemez. Kalemlerin hesaba kaydı, alacağı yenilemez kural olarak (m.91 — aksi kararlaştırılmadıkça).
3. **Faiz:** TTK m.92-93 — aksi kararlaştırılmadıkça her kalem için kaydı tarihinden faiz işler; bileşik faiz ancak TTK m.8/2 şartlarıyla.
4. **Bakiyenin tespiti ve tanınması:** TTK m.94 — dönem sonunda bakiye tespit edilip karşı tarafa bildirilir; bildirimi alan, süresi içinde itiraz etmezse bakiyeyi kabul (tanıma) etmiş sayılır. Tanınan bakiye yeni hesap döneminin ilk kalemi olur.
5. **Sona erme ve zamanaşımı:** TTK m.99 sona erme halleri; TTK m.101 — cari hesabın tasfiyesine, bakiyeye ve faizlere ilişkin davalar 5 yıllık zamanaşımına tabidir. Ara sonuç: yazılı sözleşme + dönem sonu bakiye + tanıma → bakiye muaccel ve dava edilebilir.

## Çıktı modülleri
- Cari hesap geçerlilik ve işleyiş notu (yazılı şekil, kalemler).
- Bakiye tespiti ve tanınma değerlendirmesi.
- Bakiyenin tahsili dava/icra talebi ve zamanaşımı uyarısı.

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
