---
name: enerji-ispat-delil
description: "Tarife/uzlaştırma alacağı, lisans yükümlülüğü ihlali, üretim/tüketim verisi, EPC ayıp ve gecikme gibi konularda hangi delilin nasıl elde edileceği ve değerlendirileceği belirlenirken kullanılır."
---

# Enerji Uyuşmazlıklarında İspat ve Delil

## Görev
Enerji dosyasında ispat yükünü doğru dağıtmak; teknik/sayısal delili (ölçüm, uzlaştırma, EPDK kaydı) hukuken kullanılabilir biçimde toplamak ve bilirkişi incelemesine hazırlamak.

## Soğuk başlangıç (intake)
1. İspatı gereken vakıa nedir (bedel, ihlal, üretim miktarı, ayıp, gecikme)?
2. Mevcut belgeler hangileri (lisans, sözleşme, fatura, ölçüm verisi)?
3. Veri EPİAŞ/EPDK/dağıtım şirketinde mi; erişim yetkisi var mı?
4. Teknik konu bilirkişi gerektiriyor mu?

## Denetim şeması
1. **İspat yükü**: TMK m.6 — iddia eden ispatla yükümlü. İdari yaptırımda ihlali idare ispatlar; ancak müvekkil lehine vakıalar (uyum, mücbir sebep) müvekkilce belgelenir.
2. **Belge delili**: Lisans/önlisans, bağlantı ve sistem kullanım anlaşmaları, PPA/EPC, EPDK Kurul kararları ve yazışmaları öncelikli yazılı delildir (HMK m.199 vd.); ticari defterler TTK m.64 ve HMK kapsamında değerlendirilir.
3. **Teknik/sayısal veri**: Sayaç ve ölçüm verisi, EPİAŞ uzlaştırma ve PTF/SMF verileri, üretim raporları; bunların resmî kayıttan temini ve dönem bütünlüğü doğrulanır. Eksik dönem hesabı çürütür.
4. **Bilirkişi**: Tarife/uzlaştırma hesabı, üretim kaybı, EPC performans/ayıp gibi konularda HMK m.266 vd. bilirkişi; rapor metodolojisi ve dayanak verisi denetlenir, çelişki için ek rapor istenir.
5. **Delil tespiti ve sunum**: Acil hallerde HMK m.400 vd. delil tespiti; idari yargıda re'sen araştırma ilkesi gözetilerek eksik belgenin mahkemece getirtilmesi talep edilir.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu (vakıa/delil/kaynak).
- Veri temin ve müzekkere talep listesi.
- Bilirkişiye sorulacak teknik sorular taslağı.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
