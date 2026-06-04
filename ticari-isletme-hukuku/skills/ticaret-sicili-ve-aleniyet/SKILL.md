---
name: ticaret-sicili-ve-aleniyet
description: "Tescil, ilan ve sicil kaydinin ucuncu kisilere etkisi, gorunuse guven ve tescile davet/itiraz gerektiginde; sicildeki yanlis veya eksik kayitlarin sorumluluk dogurup dogurmadigini degerlendirmek icin kullanilir."
---

# Ticaret Sicili ve Aleniyetin Etkisi

## Görev
Tescil ve ilanın hukuki etkilerini belirlemek: kayıt üçüncü kişilere karşı ne zaman ileri sürülebilir, görünüşe güven hangi hallerde korunur, yanlış/eksik kayıt kimi bağlar? Sicil aleniyeti ticari güvenliğin temelidir.

## Soğuk başlangıç (intake)
1. Hangi olgu tescile tabi (temsil yetkisi, unvan, şube, fesih)?
2. Tescil ve ilan yapılmış mı; tarihleri ne?
3. Üçüncü kişi kayda mı, gerçek duruma mı güveniyor?
4. Kayıt gerçeğe aykırı veya eksik mi?

## Denetim şeması
1. **Tescil zorunluluğu ve usulü:** TTK m.26-33 — tescile tabi olgular ilgili sicil müdürlüğünde tescil ve gerektiğinde ilan edilir. Tescil istemi süresinde yapılmazsa sicil müdürünün re'sen/davetle müdahalesi (m.32-33).
2. **Olumlu aleniyet:** TTK m.36/1 — tescil ve ilanı gereken bir husus tescil ve ilan edilmişse, üçüncü kişiler bunu bilmediklerini ileri süremezler (ilan tarihinden itibaren; m.36/1'deki on beş günlük korunma istisnası saklı). İlanı gereken bir husus ilan edilmemişse, ancak bunu bilen üçüncü kişilere karşı ileri sürülebilir.
3. **Görünüşe güven (olumsuz aleniyet):** TTK m.37 — sicildeki bir kaydın üçüncü kişilerce bilinmemesi gereken hallerde, kayda dayanan görünüşe iyiniyetle güvenen korunur. Gerçek durumla kayıt çeliştiğinde iyiniyetli üçüncü kişi sicile güvenebilir.
4. **Yanlış/eksik tescilden sorumluluk:** TTK m.38 — tescil ve ilanın gerçeğe aykırı olmasından doğan zarardan kusuru olanlar sorumludur. İspat yükü: kayda güvendiğini ve iyiniyetli olduğunu üçüncü kişi; aksini (kötüniyet) ileri süren karşı taraf ispatlar.
5. **Ara sonuç:** İlan edilmiş olgu herkese karşı ileri sürülebilir; ilan edilmemişse yalnızca bilen üçüncü kişiye karşı. Görünüşe iyiniyetle güvenen üçüncü kişi kural olarak korunur.

## Çıktı modülleri
- Tescil/ilan kronolojisi ve etki tarihleri tablosu.
- Üçüncü kişinin durumu (kayda mı, gerçeğe mi güveniyor) değerlendirmesi.
- Tescile davet veya sicil kaydının düzeltilmesi başvuru taslağı.

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
