---
name: sureler-ve-zamanasimi
description: "Sosyal güvenlik dosyasındaki tüm hak düşürücü süre, zamanaşımı ve idari başvuru sürelerinin tek tabloda çıkarılması ve hak kaybı riskinin önlenmesi gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Dosyadaki bütün süreleri (hak düşürücü, zamanaşımı, idari başvuru, dava açma) doğru madde dayanağıyla çıkarmak ve hak kaybı riskini önceden işaretlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık türü nedir (hizmet tespiti, prim, rücu, gelir testi, aylık)?
- Hangi tarihte işlem/olay gerçekleşti, hangi tarihte tebliğ edildi?
- Daha önce idari başvuru/itiraz yapıldı mı; tarihleri nedir?
- Süreyi durduran/kesen bir işlem (başvuru, kısmi ödeme) var mı?

## Denetim şeması
1. Hizmet tespitinde hak düşürücü süre: 5510 m.86/9 — hizmetin geçtiği yılın sonundan 5 yıl; işverence kuruma belge verilmişse süre işlemez (istisna mutlaka denetlenir).
2. Kurum alacaklarında zamanaşımı — m.93: Prim ve diğer Kurum alacaklarında 10 yıllık zamanaşımı; başlangıç ve kesilme/durma halleri kontrol edilir.
3. İdari başvuru süreleri — 5510 m.101 / 7036 m.4: Kurum işlemine itiraz ve sonrasında dava açma süresi; zımni red anı esas alınır.
4. Rücu ve tazminatta zamanaşımı: Haksız fiile dayalı rücuda TBK m.72 (haksız fiil zamanaşımı) ve özel hükümler birlikte; başlangıç anı içtihatla belirlenir [doğrulanacak].
5. Aylık/gelir taleplerinde geçmişe yönelik istemler: Ödenmemiş aylıkların geriye doğru istenebileceği süreler m.97 çerçevesinde değerlendirilir. Ara sonuç: süre takvimi ve risk işareti. İspat: tebliğ, başvuru ve ödeme tarih belgeleri.

## Çıktı modülleri
- Süre takvimi tablosu (olay / dayanak madde / başlangıç / bitiş / durum).
- Acil/yaklaşan süre uyarı listesi.
- Süreyi koruyucu işlem önerileri (başvuru, ihtarname, dava).

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
