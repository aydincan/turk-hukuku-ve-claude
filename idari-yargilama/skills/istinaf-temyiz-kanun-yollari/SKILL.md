---
name: istinaf-temyiz-kanun-yollari
description: "İlk derece kararına karşı bölge idare mahkemesine istinaf veya Danıştay'a temyiz başvurusunun, parasal sınırların ve kesinlik kurallarının değerlendirilmesinde kullanılır; hangi karara hangi kanun yolunun açık olduğu ve sürelerin belirlenmesinde başvurulur."
---

# İstinaf ve Temyiz Kanun Yolları

## Görev
İlk derece idari/vergi mahkemesi kararına karşı doğru kanun yolunu (istinaf/temyiz), süreyi ve kesinlik durumunu belirleyip başvuruyu kurgulamak.

## Soğuk başlangıç (intake)
- Karar idare/vergi mahkemesinin mi, BİM'in mi; ilk derece Danıştay mı?
- Uyuşmazlığın parasal değeri kesinlik/temyiz sınırının neresinde?
- Karar lehe mi aleyhe mi; hangi kısmı temyiz/istinaf edilecek?
- Kararın tebliğ tarihi nedir?

## Denetim şeması
1. **İstinaf** (İYUK m.45): İdare ve vergi mahkemelerinin nihai kararlarına karşı, kararın tebliğini izleyen günden itibaren **30 gün** içinde bölge idare mahkemesine (BİM) istinaf yolu açıktır. Konusu belirli bir parasal sınırın (yıllık yeniden değerleme ile güncellenen tutar — **[doğrulanacak]**) altında kalan davalardaki kararlar kesindir, istinafa kapalıdır.
2. **İstinaf incelemesi**: BİM hem maddi olay hem hukuk yönünden inceleme yapar; gerekirse tahkikat yenileyip işin esası hakkında karar verir. BİM kararlarının bir kısmı kesindir.
3. **Temyiz** (İYUK m.46): BİM'in m.46'da sayılan kararlarına ve ilk derece olarak Danıştay'ca verilen kararlara karşı, tebliği izleyen günden itibaren **30 gün** içinde Danıştay'a temyiz yolu açıktır. Temyiz parasal sınırı yıllık güncellenir (**[doğrulanacak]**).
4. **Temyiz sebepleri** (İYUK m.49): Görev-yetki dışında bir işe bakılması, hukuka aykırı karar verilmesi, usul hükümlerine uyulmaması gibi sebepler. Temyiz yalnızca hukukilik denetimidir; Danıştay maddi vakıa tahkikatı yapmaz, bozar veya onar.
5. **Kanun yararına temyiz**: Kesinleşmiş kararlar için Danıştay Başsavcısı tarafından (İYUK ilgili hükmü) sınırlı denetim; hüküm sonucu etkilenmez.
6. **Ara sonuç — yürütme**: İstinaf/temyiz başvurusu kural olarak kararın yürütmesini kendiliğinden durdurmaz; gerektiğinde YD talep edilir (İYUK m.52). Kararın düzeltilmesi yolu kaldırılmıştır.

## Çıktı modülleri
- Açık kanun yolu, süre ve mahkeme tespiti
- Parasal sınır/kesinlik değerlendirmesi ([doğrulanacak] güncel tutar uyarısı)
- İstinaf/temyiz dilekçesi sebep iskeleti

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
