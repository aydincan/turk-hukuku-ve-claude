---
name: sure-zamanasimi
description: "İbraz, protesto, başvurma ve kambiyo zamanaşımı sürelerini hesaplamak ve takvimlemek; hak kaybı riskini değerlendirirken ve sebep alacağına geçiş gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Kambiyo senedine ilişkin tüm süreleri (ibraz, protesto, başvurma, zamanaşımı) doğru başlangıç anından hesaplamak, hak düşümü ve zamanaşımı risklerini saptamak ve gerektiğinde sebep alacağına geçişi planlamak.

## Soğuk başlangıç (intake)
- Senet tipi nedir (çek/bono/poliçe) ve vade/keşide tarihi nedir?
- İbraz, protesto ve karşılıksız işlem tarihleri nedir?
- Talep kime yöneliyor (asıl borçlu / ciranta / avalist) — süreler buna göre değişir.
- Zamanaşımını kesen/durduran işlem (takip, dava, ikrar) var mı?

## Denetim şeması
1. Çek ibraz süreleri: aynı yerde 10 gün, farklı yerde 1 ay (TTK m.796); sürede ibraz başvurma hakkı ve karşılıksız işlemi için şarttır.
2. Çek zamanaşımı: TTK m.808 — kural olarak 3 yıl (hamilin müracaat borçlularına ve borçluların birbirine karşı süreleri fıkralara göre); başlangıç ibraz süresinin bitiminden işler.
3. Poliçe/bono zamanaşımı: TTK m.749 — kabul edene/asıl borçluya karşı vadeden itibaren 3 yıl; hamilin cirantalar ve düzenleyene karşı protesto/vade tarihinden 1 yıl; cirantanın cirantaya/düzenleyene rücuu, senedi ödediği veya dava edildiği tarihten 6 ay.
4. Protesto/başvurma süreleri: ödememe protestosu ve başvurma süreleri (TTK m.714, m.722) tutulmazsa cirantalara müracaat hakkı düşer (m.730).
5. Kesme/durma: zamanaşımı dava açılması, takip, ödeme emri tebliği, borcun ikrarı gibi sebeplerle kesilir; kesilme yalnızca işlemin yöneldiği borçluya etki eder.
6. Ara sonuç — sebep alacağı: kambiyo zamanaşımı dolsa veya hak düşse bile temel ilişkiden doğan alacak (TBK genel zamanaşımı, kural 10 yıl, TBK m.146; bazı ilişkilerde 5 yıl m.147) ve sebepsiz zenginleşme talebi (TTK m.732) ayrıca değerlendirilir.

## Çıktı modülleri
- Süre/zamanaşımı takvim tablosu (her borçlu için ayrı).
- Hak düşümü/zamanaşımı risk uyarısı.
- Sebep alacağına geçiş notu (dayanak + zamanaşımı).

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
