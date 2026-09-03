---
name: yaptirim-ceza-belirleme
description: "Temel cezanın belirlenmesi, indirim-artırım sırası, seçenek yaptırımlar, erteleme ve güvenlik tedbirleri dahil somut cezanın hesaplanması gerektiğinde kullanılır."
---

# Yaptırım Teorisi ve Ceza Belirleme

## Görev
Suç sabit olduğunda somut cezayı, TCK m.61 sıralamasına ve ilgili yaptırım hükümlerine göre hesaplamak; seçenek yaptırım, erteleme ve güvenlik tedbirlerini değerlendirmek.

## Soğuk başlangıç (intake)
- Sevk maddesinin alt-üst ceza sınırı nedir; nitelikli hâl var mı?
- Teşebbüs, iştirak (yardım), haksız tahrik gibi indirim sebepleri var mı?
- Sanığın geçmişi, tekerrür durumu ve duruşmadaki tutumu nasıl?
- Hükmolunacak ceza erteleme/seçenek yaptırım sınırları içinde mi?

## Denetim şeması
1. **Temel ceza (m.61):** Alt-üst sınır arasında suçun işleniş biçimi, kasıt yoğunluğu, zarar/tehlike, fail-mağdur ilişkisine göre temel ceza belirlenir.
2. **Sıralı uygulama (m.61/4-5):** Artırım ve indirim nedenleri kanunun belirlediği sırayla uygulanır: önce nitelikli hâller, sonra teşebbüs (m.35), iştirak (m.39), haksız tahrik (m.29), yaş küçüklüğü (m.31), takdiri indirim (m.62). Ara sonuç: sıralama doğru mu?
3. **Takdiri indirim (m.62):** Lehe hâllerde altıda bire kadar indirim.
4. **Seçenek yaptırımlar (m.50):** Kısa süreli hapsin adli para cezasına veya seçenek tedbirlere çevrilmesi şartları.
5. **Adli para cezası (m.52):** Gün para cezası sistemi; gün sayısı ve bir gün karşılığı miktar ayrı belirlenir.
6. **Erteleme (m.51) ve tekerrür (m.58):** İki yıl veya altı hapiste erteleme şartları; tekerrür hâlinde mükerrirlere özgü infaz rejimi.
7. **Güvenlik tedbirleri (m.53-60):** Belli hakları kullanmaktan yoksun bırakma, müsadere (m.54-55), akıl hastalarına tedbir (m.57), tüzel kişiler hakkında tedbir (m.60).

## Çıktı modülleri
- Adım adım ceza hesabı tablosu (her aşamada miktar ve madde).
- Seçenek yaptırım/erteleme uygunluk değerlendirmesi.
- Güvenlik tedbiri listesi.
- Lehe kanun (m.7) karşılaştırma notu.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
