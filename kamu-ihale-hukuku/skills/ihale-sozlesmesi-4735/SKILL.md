---
name: ihale-sozlesmesi-4735
description: "Sözleşme imzası, kesin teminat, iş artışı/eksilişi, fiyat farkı, süre uzatımı, gecikme cezası ve sözleşmenin feshi gibi sözleşme aşaması sorunlarında 4735 sayılı Kanun çerçevesinde kullanılır."
---

# İhale Sözleşmesinin Kuruluşu ve Uygulanması (4735)

## Görev
İhale üzerinde kalan istekliyle imzalanan idari hukuk sözleşmesinin (4735 sayılı KİSK) kuruluş, ifa, değişiklik ve fesih boyutlarını denetlemek; tarafların yükümlülük ve risklerini saptamak.

## Soğuk başlangıç (intake)
1. Sözleşme imzalandı mı; kesin teminat (%6) alındı mı (4735 m.5, 4734 m.43)?
2. Sözleşmenin türü: birim fiyat, anahtar teslimi götürü bedel, karma?
3. İhtilaf konusu: iş artışı/eksilişi, fiyat farkı, süre uzatımı, gecikme cezası mı?
4. Fesih iradesi var mı; kim kaynaklı (idare/yüklenici)?

## Denetim şeması
1. **Sözleşmenin imzası (4734 m.42-44):** Kesinleşen ihale kararı bildiriminden sonra, yasal sürelerde davet ve imza; kesin teminat alınır. İmzadan kaçınan istekli/idarenin sonuçları (teminat irat, yasaklama) değerlendirilir.
2. **Sözleşme türü ve değişmezlik (4735 m.4-5):** Tip sözleşmeler esastır; sözleşmede taraflarca aleyhe esaslı değişiklik yapılamaz. Sözleşme hükümleri ihale dokümanına uygun olmak zorundadır.
3. **İş artışı/eksilişi (4735 m.24):** Öngörülemeyen durumlarda, yapım işlerinde sözleşme bedelinin belirli oranına kadar (mevzuattaki güncel oran) iş artışı yapılabilir; sınır aşılırsa ayrı ihale gerekir.
4. **Fiyat farkı ve süre uzatımı:** Fiyat farkı ancak dokümanda öngörülmüşse ve esaslara göre ödenir; mücbir sebep (4735 m.10) hallerinde süre uzatımı verilir, gecikme cezası işletilmez.
5. **Gecikme ve fesih (4735 m.20-22):** Yüklenici taahhüdünü ihlal ederse protesto/ceza ve sözleşmenin feshi gündeme gelir; fesihte kesin teminat irat, hesabın tasfiyesi ve yasaklama (m.26) sonuçları doğar.
6. **Ara sonuç:** Sözleşme uyuşmazlıklarında yargı yolu ve yetkili mahkeme (idari sözleşme niteliği, tahkim şartı varsa tahkim) ayrıca belirlenir.

İspat yükü: İfa/mücbir sebep iddiasını ileri süren taraf belgeyle ispatlar.

## Çıktı modülleri
- Sözleşme yükümlülük-risk matrisi.
- İş artışı/fiyat farkı/süre uzatımı hesap kontrolü.
- Fesih senaryosu ve sonuç analizi (teminat, tasfiye, yasaklama).

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
