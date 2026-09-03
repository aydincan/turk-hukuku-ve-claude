---
name: istinaf-temyiz-kanun-yollari
description: "Verilen hükme karşı istinaf (HMK m.341-360) veya temyiz (m.361-373) yoluna başvururken kesinlik sınırını, başvuru süresini, istinaf sebeplerini ve yeni delil/duruşma rejimini değerlendirmek; başvuru dilekçesi hazırlamak için."
---

# İstinaf ve Temyiz Kanun Yolları

## Görev
Aleyhe hükme karşı uygun kanun yolunu (istinaf/temyiz) belirlemek, kesinlik sınırını kontrol etmek, başvuru süresini hesaplamak ve sebepleri gerekçeli olarak kurmak.

## Soğuk başlangıç (intake)
- Gerekçeli karar ne zaman tebliğ edildi?
- Hüküm konusu/değer kesinlik sınırının üstünde mi (yıllık tarifeden teyit)?
- İstinaf mı (ilk derece kararı), temyiz mi (BAM kararı) söz konusu?
- Hangi hata türü var (maddi olay, hukuki niteleme, usul, gerekçe eksikliği)?

## Denetim şeması
1. **İstinaf yolu** (m.341): İlk derece mahkemesi kararlarına karşı; ancak **kesinlik sınırı** altındaki malvarlığı davalarında istinaf kapalıdır (parasal had her yıl yeniden değerleme ile güncellenir, tarihli teyit şart).
2. **İstinaf süresi** (m.345): Kararın **tebliğinden itibaren iki hafta**. Süre içinde başvuru dilekçesi kararı veren mahkemeye verilir.
3. **İstinaf sebepleri ve inceleme** (m.355-357): BAM kural olarak istinaf dilekçesinde belirtilen sebeplerle bağlıdır (kamu düzeni hariç); **yeni vakıa ve delil ileri sürülemez** (m.357), istisnaları dardır. BAM ya esastan inceler, ya kaldırıp gönderir, ya da düzelterek yeniden karar verir.
4. **Temyiz yolu** (m.361): BAM kararlarına karşı; **temyiz edilemeyecek kararlar** (m.362) ve kesinlik sınırı kontrol edilir. Süre **iki hafta** (m.361).
5. **Temyiz incelemesinin niteliği** (m.369 vd.): Yargıtay yalnızca **hukukilik** denetimi yapar; vakıa yeniden değerlendirilmez. Bozma/onama/düzelterek onama sonuçları.
6. **Katılma yolu / karşı başvuru**: Süresi geçtikten sonra dahi karşı tarafın başvurusuna katılma imkânı (m.348) değerlendirilir.

Ara sonuç: "Uygun kanun yolu + açık mı (kesinlik) + son başvuru günü + sebep listesi".

## Çıktı modülleri
- Kesinlik/temyiz edilebilirlik kontrolü (tarihli had teyidi notlu).
- İstinaf/temyiz dilekçesi iskeleti (sebep başlıkları, talep).
- Süre uyarısı ve katılma yolu değerlendirmesi.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
