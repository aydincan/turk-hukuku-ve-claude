---
name: kanun-yollari-istinaf-temyiz
description: "Vergi mahkemesi kararına karşı bölge idare mahkemesine istinaf ve Danıştaya temyiz başvurularının kesinlik sınırlarını, sürelerini ve başvuru sebeplerini belirlemek için kullanılır."
---

# Kanun Yolları (İstinaf ve Temyiz)

## Görev
Vergi mahkemesi kararına karşı hangi kanun yolunun açık olduğunu (istinaf/temyiz/kesinlik) belirlemek; başvuru süresini, parasal sınırları ve bozma-kaldırma sebeplerini doğru kurgulamak.

## Soğuk başlangıç (intake)
1. Vergi mahkemesi kararı lehe mi aleyhe mi; karar size ne zaman tebliğ edildi?
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
