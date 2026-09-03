---
name: vergi-cezalari-denetimi
description: "Vergi ziyaı, usulsüzlük ve özel usulsüzlük cezalarının tipikliğini, kusur unsurunu, kat oranını ve indirim imkânlarını ayrı ayrı denetlerken kullanılır."
---

# Vergi Cezalarının Denetimi

## Görev
İhbarname ile kesilen idari nitelikteki vergi cezalarını (vergi ziyaı, usulsüzlük, özel usulsüzlük) unsurları, oranı ve uygulanabilir indirimler bakımından denetlemek; ceza ile vergi aslını birbirinden ayırarak savunma kurmak.

## Soğuk başlangıç (intake)
1. Hangi ceza kesildi: vergi ziyaı mı (VUK m.341/344), usulsüzlük mü (m.351-352), özel usulsüzlük mü (m.353, mük.355)?
2. Cezanın oranı/katı ne; üç kat (m.344/2, m.359 fiilleri) uygulandı mı?
3. Fiil tek mi yoksa birden çok dönem/belge mi; tekerrür (VUK m.339) var mı?
4. Daha önce uzlaşma veya ceza indirimi (VUK m.376) talep edildi mi?

## Denetim şeması
1. **Tipiklik.** Her ceza türü için fiilin kanuni tarife uyup uymadığı denetlenir: vergi ziyaı için ziyaın gerçekleşmesi (m.341); usulsüzlük için şekli ödevin ihlali; özel usulsüzlük için belge düzenine aykırılık (fatura/belge alıp vermeme, m.353).
2. **Kusur ve kat.** Vergi ziyaı cezası kural olarak bir kat; VUK m.359'daki kaçakçılık fiilleriyle işlenmişse üç kat (m.344/2). Üç kat uygulamasının dayanağı (sahte belge kullanma/düzenleme tespiti) somut delille aranır.
3. **İndirim ve af mekanizmaları.** VUK m.376 — ihbarnamenin tebliğinden itibaren 30 gün içinde başvuru ile cezada indirim. Uzlaşma (Ek m.1) ile karşılaştır; her iki yol birlikte kullanılamaz, dava hakkıyla ilişkisi tartılır.
4. **Zamanaşımı.** VUK m.374 — ceza kesmede zamanaşımı süreleri (vergi ziyaında 5 yıl, usulsüzlükte 2 yıl) ve başlangıç tarihi denetlenir.
5. **Tek fiil-içtima.** VUK m.336 — aynı fiille hem vergi ziyaı hem usulsüzlük doğmuşsa ağır olanın uygulanması. Ara sonuç: kesilen cezaların ayrı ayrı mı, içtima ile mi değerlendirilmesi gerektiği belirlenir.

## Çıktı modülleri
- Ceza türü / unsur / oran / indirim karşılaştırma tablosu.
- VUK m.376 indirim başvuru taslağı (alternatif: uzlaşma).
- Cezaya özgü iptal gerekçeleri (dilekçeye eklenecek).

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
