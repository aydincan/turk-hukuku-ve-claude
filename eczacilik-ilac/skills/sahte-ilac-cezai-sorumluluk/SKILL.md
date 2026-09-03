---
name: sahte-ilac-cezai-sorumluluk
description: "Sahte, taklit, kaçak veya bozulmuş ilaç, ruhsatsız ürün satışı ve sağlık için tehlikeli madde fiillerinde TCK ve 1262 sayılı Kanun kapsamında ceza sorumluluğunu değerlendirmek için kullanılır."
---

# Sahte ve Kaçak İlaç — Cezai Sorumluluk

## Görev
Sahte/taklit/kaçak/bozulmuş ilaç veya ruhsatsız ürün fiilinde uygulanacak ceza normunu belirlemek, unsurları ve isnadı denetlemek.

## Soğuk başlangıç (intake)
- Fiil: sahte/taklit ilaç imali mi, ruhsatsız müstahzar satışı mı, kaçak (gümrük dışı) ilaç mı, bozulmuş ilaç mı?
- Şüpheli sıfatı: üretici, ithalatçı, ecza deposu, eczacı, internet satıcısı?
- Ürün insan sağlığı için tehlike doğurdu mu; analiz/bilirkişi raporu var mı?
- Soruşturma aşaması: arama-el koyma, ifade, iddianame?

## Denetim şeması
1. **Norm seçimi.** Kişilerin hayatını ve sağlığını tehlikeye sokacak biçimde bozulmuş/değiştirilmiş/sahte ilaç → TCK m.187 (bozulmuş veya değiştirilmiş gıda/ilaç); ruhsatsız/taklit müstahzar → 1262 sayılı Kanun m.18-19 cezai hükümleri; kaçak ilaç → 5607 sayılı Kaçakçılıkla Mücadele Kanunu da gündeme gelir.
2. **Unsur denetimi.** Tipiklik (sahtelik/bozulma/ruhsatsızlık), kast (TCK m.21), fail sıfatı; ara sonuç: hangi norm hangi sıfata uyuyor, fikri içtima (TCK m.44) var mı?
3. **İspat ve delil.** Numune analiz raporu, TİTCK/ATK bilirkişi raporu, İTS/karekod kayıtları, ele geçen ürün-fatura zinciri. İspat yükü iddia makamında; lehe delil ve zincirdeki kopukluk savunma argümanı.
4. **İdari-cezai ayrım.** Aynı fiil hem TİTCK idari yaptırımı hem ceza soruşturması doğurabilir; non bis in idem ve idari/cezai sürecin ayrılığı değerlendirilir.
5. **Usul.** CMK çerçevesinde arama-el koymanın hukuka uygunluğu, delil yasakları, sağlık riski varsa bilirkişi zorunluluğu.

## Çıktı modülleri
- Norm-unsur eşleştirme tablosu.
- Savunma stratejisi ve delil itirazları notu.
- İdari-cezai sürecin eşgüdüm haritası.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
