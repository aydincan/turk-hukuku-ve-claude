---
name: sure-ve-zamanasimi-imar
description: "İmar işlemlerine karşı dava açma süresi, askı-ilan ve itiraz sürelerinin hesabı ya da bir sürenin kaçırılıp kaçırılmadığı sorulduğunda; İYUK süreleri, üst makama başvuru ve sürenin başlangıcı tartışıldığında kullanılır."
---

# İmar Uyuşmazlıklarında Süre ve Hak Düşürücü Süreler

## Görev
İmar işlemine karşı dava ve başvuru sürelerini doğru hesaplamak; sürenin başlangıcını, durmasını ve kaçırma riskini ortaya koymak.

## Soğuk başlangıç (intake)
- İşlem türü ne (plan, ruhsat, yıkım, para cezası, parselasyon)?
- İşlem ne zaman tebliğ edildi/ilan edildi/öğrenildi?
- Askı ilanı veya üst makama başvuru yapıldı mı?
- Bugünün tarihi itibarıyla kalan süre nedir?

## Denetim şeması
1. **Genel dava süresi (İYUK m.7)**: İdari işlemlere karşı, yazılı bildirim/tebliğ tarihinden itibaren **60 gün** (Danıştay ve idare/vergi mahkemeleri için genel süre). Sürenin başlangıcı tebliğ, ilan veya muttali olma anına göre tespit edilir.
2. **Planlarda askı-itiraz**: Plan **1 ay askıda** kalır; askı süresi sonunda dava süresi başlar. Askı içinde idareye itiraz edilirse, itirazın reddi (açık/zımni) yeni 60 günlük süre açar (İYUK m.11 ile bağlantılı değerlendirme).
3. **Üst makama başvuru (İYUK m.11)**: Dava süresi içinde işlemin kaldırılması/değiştirilmesi için üst makama başvurulabilir; başvuru işlemekte olan süreyi durdurur, cevap (veya 30/60 günlük zımni ret) ile kalan süre işler. İmar para cezası ve bazı işlemlerde bu yol kullanılır.
4. **İşlem türüne özgü farklar**: Yıkım ve mühürlemede sürenin tebliğden işlemesi; parselasyonda ilan; kamulaştırma/acele kamulaştırmada 2942'deki özel süreler; el atma bedelinde zamanaşımı ayrı kurulur. Her işlem için doğru başlangıç saptanır.
5. **İspat**: Tebligat parçası, askı tutanağı, ilan metni, başvuru ve cevap yazıları süreyi ispatlayan belgelerdir; sürenin başlangıcı çekişmeliyse "öğrenme" anı tartışılır (ispat yükü iddia edene).
6. **Ara sonuç**: Net bir süre takvimi (başlangıç-durma-bitiş) çıkarılır; süre dolmuşsa istisnai yollar (zımni ret, yeni işlem, mücbir sebep) değerlendirilir. Süre kritikse ivedi dava + YD önerilir.

## Çıktı modülleri
- İşlem türüne göre süre tablosu (başlangıç-bitiş-kalan gün).
- Askı/itiraz/üst makam başvuru akış şeması.
- Süre durması/yenilenmesi notu.
- Kaçırılan süre için istisna değerlendirmesi.

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
