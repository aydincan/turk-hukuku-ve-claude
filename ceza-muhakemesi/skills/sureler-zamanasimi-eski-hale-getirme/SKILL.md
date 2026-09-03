---
name: sureler-zamanasimi-eski-hale-getirme
description: "Dava ve ceza zamanaşımı, kanun yolu ve usul süreleri ile süre kaçırıldığında eski hale getirme başvurusu hesaplanırken kullanılır."
---

# Süreler, Zamanaşımı ve Eski Hale Getirme

## Görev
Ceza muhakemesinde işleyen tüm süreleri (zamanaşımı, kanun yolu, usul süreleri) hesaplamak; süre kaçırma riskini ve eski hale getirme imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Suç tarihi ve suçun cezası nedir (zamanaşımı için)?
- Hangi usul/kanun yolu süresi söz konusu, başlangıç tarihi ne?
- Kişi tutuklu mu (denetim süreleri için)?
- Süre kaçırıldıysa kusursuz bir engel var mıydı?
- Şikâyete bağlı suç mu (TCK m.73 altı aylık süre)?

## Denetim şeması
1. **Dava zamanaşımı.** Suçun gerektirdiği cezaya göre TCK m.66'da süreler belirlenir; süre suçun işlendiği günden işler (m.66/6). Kesen ve durduran sebepler m.67'de düzenlenir; kesilmeden sonra süre yeniden işler, ancak en fazla yarısına kadar uzar.
2. **Ceza zamanaşımı.** Kesinleşen cezanın infaz edilememesi halindeki süreler TCK m.68'de gösterilir.
3. **Şikâyet süresi.** Şikâyete bağlı suçlarda fail ve fiilin öğrenilmesinden itibaren 6 ay (TCK m.73); geçerse soruşturma/kovuşturma şartı düşer.
4. **Kanun yolu süreleri.** İtiraz 7 gün (CMK m.268), istinaf 7 gün (m.273), temyiz 15 gün (m.291); başlangıç tefhim, yoklukta tebliğdir. Süreler gün olarak hesaplanır, tatil günü sonaysa ertesi iş gününe uzar (m.39).
5. **Eski hale getirme.** Kusuru olmaksızın süreyi geçiren kişi, engelin kalkmasından itibaren 7 gün içinde eski hale getirme isteyebilir; istem, süreye uyulduğunda yapılması gereken işlemle birlikte sunulur (CMK m.40-42).
6. **Ara sonuç.** Süre hâlâ işliyorsa hemen işlem yapılır; kaçırılmışsa eski hale getirme koşulları (kusursuzluk + 7 gün) denetlenir.

## Çıktı modülleri
- Süre takvimi tablosu (zamanaşımı + kanun yolu + denetim süreleri).
- Zamanaşımı hesabı ve kesen/duran sebep notu.
- Eski hale getirme dilekçesi taslağı (m.40-42 dayanaklı).
- Kritik son tarih uyarısı.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
