---
name: temyiz-kanun-yolu
description: "Bölge adliye mahkemesi kararına karşı Yargıtaya temyiz başvurusu, temyiz edilebilirlik sınırı, hukuka aykırılık sebepleri ve bozma sonuçları değerlendirilirken kullanılır."
---

# Temyiz Kanun Yolu

## Görev
BAM ceza dairesi kararına karşı temyiz yolunun açık olup olmadığını, süresini ve hukuka aykırılık sebeplerini belirlemek; Yargıtay incelemesini ve bozma sonucunu yönlendirmek.

## Soğuk başlangıç (intake)
- BAM kararı ne zaman tefhim/tebliğ edildi?
- Karar temyiz edilebilir mi (m.286 sınırları, katalog)?
- Mutlak/nispi hangi hukuka aykırılık sebepleri var?
- Sanık lehine mi aleyhe mi temyiz söz konusu?
- Dosyada hukukun yanlış uygulanması mı, eksik inceleme mi öne çıkıyor?

## Denetim şeması
1. **Süre.** Temyiz, BAM kararının tefhiminden, yokluğunda tebliğinden itibaren 15 gün içinde yapılır (CMK m.291).
2. **Temyiz edilebilirlik.** İstinaf üzerine verilen bazı kararlar kesindir; temyiz yalnızca m.286'da gösterilen ağırlıktaki hükümler için açıktır (ör. belirli hapis cezası eşiğinin üzerindeki mahkûmiyetler). Sınır ve istisnalar m.286'dan ve güncel düzenlemeden doğrulanır.
3. **Sebep.** Temyiz ancak hukuka aykırılık nedenine dayanır (m.288); Yargıtay maddi olayı yeniden değerlendirmez, hukukun uygulanmasını denetler.
4. **Mutlak bozma nedenleri.** m.289'da sayılan haller (mahkemenin kanuna aykırı kuruluşu, hâkimin yasaklılığı, aleniyet ihlali, gerekçesizlik, savunma hakkının kısıtlanması, hükmün hukuka aykırı delile dayanması vb.) hukuka aykırılık sayılır.
5. **Karar.** Yargıtay temyiz istemini reddeder, hükmü bozar veya düzelterek onar (m.302-303). Bozmadan sonra direnme/uyma süreci işler (m.307); direnme kararları Ceza Genel Kurulunda incelenir.
6. **Ara sonuç.** Sebepli ve süresinde temyiz hazırlanır; temyiz kapalıysa yalnız itiraz/yargılamanın yenilenmesi yolları kalır.

## Çıktı modülleri
- Temyiz edilebilirlik ve süre denetim notu.
- Temyiz dilekçesi iskeleti (mutlak/nispi sebepler m.289 eşlemesi).
- Bozma sonrası senaryo analizi (uyma/direnme).
- Yargıtay daire içtihadı arama notu (karararama.yargitay.gov.tr).

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
