---
name: kanun-yollari-istinaf-temyiz
description: "Vergi mahkemesi kararına karşı bölge idare mahkemesine istinaf ve Danıştaya temyiz başvurularının kesinlik sınırlarını, sürelerini ve başvuru sebeplerini belirlemek için kullanılır."
---

# Kanun Yolları (İstinaf ve Temyiz)

## Görev
Vergi mahkemesi kararına karşı hangi kanun yolunun açık olduğunu (istinaf/temyiz/kesinlik) belirlemek; başvuru süresini, parasal sınırları ve bozma-kaldırma sebeplerini doğru kurgulamak.

## Soğuk başlangıç (intake)
1. Vergi mahkemesi kararı lehe mi aleyhe mi; karar ne zaman tebliğ edildi?
2. Uyuşmazlığın parasal değeri (vergi aslı + ceza) ne kadar?
3. Karar tek hâkimle mi kurul halinde mi verildi?
4. İtiraz edilecek husus maddi vakıa mı yoksa hukuki yorum/usul mü?

## Denetim şeması
1. **İstinaf yolu.** İYUK m.45 — vergi mahkemesi kararlarına karşı kararın tebliğinden itibaren 30 gün içinde bölge idare mahkemesine istinaf; belirli parasal sınırın altındaki davalarda karar kesin (sınır her yıl yeniden değerleme oranıyla güncellenir, **güncel tutar teyit edilmeli**).
2. **İstinaf incelemesi.** BİM hem maddi olay hem hukuki denetim yapar; gerektiğinde yeniden karar verir (m.45/4-5). İstinaf sebepleri (eksik inceleme, delil değerlendirme hatası, hukuka aykırılık) ayrı başlıklanır.
3. **Temyiz yolu.** İYUK m.46 — BİM kararlarına karşı, kanunda sayılan ve belirli parasal sınırı aşan davalarda kararın tebliğinden itibaren 30 gün içinde Danıştaya temyiz; çoğu uyuşmazlıkta istinaf kararı kesindir, yalnızca sınır üstü ve sayılı hallerde temyiz açıktır (**sınır ve liste teyit edilmeli**).
4. **Temyiz sebepleri.** İYUK m.49 — görev-yetki, hukuka aykırılık, usul hükümlerine aykırılık. Danıştay bozma kararı verirse dosya BİM'e gönderilir.
5. **Yürürlük ve teminat.** Kanun yolu başvurusunun yürütmeye etkisi ve YD talebi ayrı değerlendirilir (İYUK m.27, m.52). Ara sonuç: kararın kesin olup olmadığı, açıksa hangi merciye hangi sürede başvurulacağı netleştirilir.

## Çıktı modülleri
- Kanun yolu haritası (kesinlik / istinaf / temyiz, parasal sınır uyarısı).
- İstinaf veya temyiz dilekçesi iskeleti (sebep başlıklarıyla).
- Süre ve YD talep notu.

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
