---
name: kanun-yolu-dilekceleri
description: "İlk derece kararına karşı istinaf veya temyiz dilekçesi hazırlamak; istinaf sebeplerini somutlaştırmak, süre ve kesinlik sınırlarını denetlemek gerektiğinde kullanılır."
---

# İstinaf ve Temyiz Dilekçeleri

## Görev
İlk derece veya istinaf kararına karşı kanun yolu dilekçesini kurmak; istinaf sebeplerini somut, gerekçeli ve süresinde ileri sürmek. Yanlış sebep ya da geçmiş süre, kanun yolunun reddini doğurur.

## Soğuk başlangıç (intake)
- Karar hangi mahkemeden, hangi tarihte tebliğ edildi?
- Karar miktar/değer olarak kesinlik sınırının üstünde mi?
- Hangi hukuka aykırılıklar var (maddi/hukuki/usuli)?
- İstinaf mı temyiz mi söz konusu (derece sırası)?

## Denetim şeması
1. Süre ve kesinlik (HMK m.341, m.345): İstinaf süresi kural olarak iki hafta, kararın tebliğinden işler. İstinaf parasal sınırı (m.341) ve temyiz sınırı (m.362) yıllık olarak güncellenir — yürürlükteki tutarı doğrulayın. İYUK'ta istinaf m.45, temyiz m.46.
2. İstinaf sebepleri (HMK m.342, m.355): Dilekçe istinaf sebeplerini içermeli; BAM kural olarak sebeplerle bağlı, kamu düzeni hariç. Sebepleri somutlaştırın: yanlış vakıa tespiti, delil değerlendirme hatası, hukukun yanlış uygulanması, usul hatası (gerekçe yokluğu HMK m.297).
3. Temyiz sebepleri (HMK m.371): Yargıtay yalnızca hukuka aykırılığı denetler; maddi vakıa yeniden incelenmez. Sebepleri hukuk normuna aykırılık ekseninde yazın.
4. Talep: Kararın kaldırılması/bozulması ve (istinafta) yeniden esas hakkında karar veya gönderme.
5. Harç ve ek: Kanun yolu harcı yatırılmalı; dilekçe karar örneğiyle sunulur. Ara sonuç: süre/sınır/sebep uygunsa dilekçe taslağı avukat incelemesine hazır; kesinse müvekkil bilgilendirilir.

## Çıktı modülleri
- İstinaf/temyiz dilekçesi taslağı (sebepler numaralı)
- Süre ve kesinlik sınırı denetim notu
- Sebep-gerekçe eşleşme tablosu
- Harç ve ek evrak kontrol listesi

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
