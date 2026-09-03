---
name: ispat-ve-delil-toplu-is
description: "Toplu is uyusmazliklarinda ispat yukunu ve delil araclarini (uyelik kayitlari, iskolu istatistikleri, tutanaklar, tanik) planlar; sendikal neden, baraj/coklugu veya grev usulunun ispati gerektiginde kullanilir."
---

# İspat ve Delil Stratejisi

## Görev
Toplu iş uyuşmazlığının türüne göre ispat yükünü doğru dağıtmak ve delil mimarisini kurmak. Sendikal neden, baraj/çoğunluk ve grev usulü farklı delil setleri ister.

## Soğuk başlangıç (intake)
- İspatlanacak ana vakıa nedir (sendikal neden / çoğunluk / grev usulü / TİS ihlali)?
- Elde hangi belgeler var (üyelik kaydı, bordro, tutanak, yazışma)?
- Tanık var mı; resmî kayıt erişimi mümkün mü?
- Karşı tarafın elindeki belgeler neler?

## Denetim şeması
1. **Sendikal neden ispatı:** 6356 m.25/7-8 — işçi, sendikal nedeni kuvvetle muhtemel kılan olguları (üyelik/çekilme tarihi, fesihle zaman yakınlığı, eşit durumdaki üye olmayanların korunması) gösterir; ardından geçerli/haklı neden ispatı işverene geçer. Delil: e-Devlet üyelik kaydı, fesih yazısı, karşılaştırmalı işten çıkarma listesi, tanık.
2. **Baraj/çoğunluk ispatı:** Yetki uyuşmazlığında Bakanlık işkolu istatistik tebliğleri, e-Devlet üyelik kayıtları, sendika ve işyeri işçi listeleri esastır (6356 m.41-43). Sayısal tespit belgeye dayanır; tanıkla çoğunluk ispatı kural olarak yetersizdir.
3. **Grev usulü ispatı:** Tutanak tarihleri, çağrı/bildirim yazıları, grev oylaması tutanağı (m.61), erteleme kararı; kanuni/kanun dışı grev ayrımı tarih ve belge ile kurulur.
4. **TİS ihlali ispatı:** Yürürlükteki TİS metni, ödeme/bordro kayıtları, işveren uygulamaları; normatif hükmün ihlali belge üzerinden gösterilir.
5. **Ara sonuç:** Her vakıa için ispat yükü sahibi ve asgari delil seti belirlenir; eksik deliller için celp/müzekkere planı yapılır (Bakanlık, SGK, banka kayıtları).

İspat yükü kuralı her zaman önce iddiacıda, kanunun yer değiştirdiği hallerde (m.25) işverende.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa – yük sahibi – delil).
- Delil toplama ve celp planı.
- Eksik/çelişki listesi.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
