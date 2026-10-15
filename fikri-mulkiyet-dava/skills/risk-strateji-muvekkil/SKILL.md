---
name: risk-strateji-muvekkil
description: "Dava açmadan önce ihtarname/cease and desist, tedbir-esas-ceza yol seçimi, kazanma şansı ve maliyet değerlendirmesi ile müvekkile sade dilde risk haritası ve strateji önerisi sunmak gerektiğinde kullanılır."
---

# Risk, Strateji ve Müvekkil İletişimi

## Görev
Uyuşmazlığa girmeden önce hak sahibinin (veya tecavüzle suçlanan tarafın) stratejik konumunu değerlendirmek; ihtar, müzakere, tedbir, dava ve ceza seçenekleri arasında gerekçeli yol önermek ve müvekkile sade dilde aktarmak.

## Soğuk başlangıç (intake)
- Müvekkil hak sahibi mi, tecavüzle suçlanan taraf mı?
- Öncelik hızlı durdurma mı, tazminat mı, ticari ilişkiyi korumak mı?
- Karşı tarafın hükümsüzlük/kullanmama gibi karşı kozları var mı?
- Bütçe, zaman ve kamuoyu/itibar hassasiyeti nedir?

## Denetim şeması
1. Konum tespiti: Hakkın geçerliliği (sicil, kullanım kanıtı), tecavüzün gücü ve karşı tarafın olası savunmaları (kullanmama m.19, hükümsüzlük, önceki hak) birlikte tartılır; zayıf hak üzerine agresif dava tedbir tazminatı riski doğurur.
2. İhtar adımı: Çoğu olayda ihtarname/cease and desist ile durdurma ve müzakere denenir; ihtar, sonraki tedbir talebinde kötüniyeti ve devam eden tecavüzü belgeler. Ancak ihtar, karşı tarafa delil karartma fırsatı verebilir — gizli delil tespiti/tedbir önceliği değerlendirilir.
3. Yol seçimi: (a) sadece hukuk (tedbir+tecavüz+tazminat), (b) ceza eklemek (caydırıcılık, arama), (c) idari yol (hükümsüzlük/iptal için TÜRKPATENT/Ankara FSHM). Maliyet, süre ve kanıt gücü matrisi kurulur.
4. Karşı taraf temsili: Tecavüzle suçlanan müvekkilde önce hakkın geçerliliği ve kullanım kapsamı sorgulanır; hükümsüzlük/kullanmama def'i ile savunma kurgulanır, sulh seçeneği tartılır.
5. Müvekkil iletişimi: Olasılıklar yüzde kesinlik vaadi olmadan; en iyi/orta/kötü senaryo ve tahmini süre-maliyet sade dille sunulur. Karar müvekkilindir; yazılı bilgilendirme alınır.

## Çıktı modülleri
- Risk haritası (hak gücü / tecavüz gücü / karşı koz / senaryo).
- Yol seçimi karşılaştırma tablosu.
- Müvekkile sade dilde strateji notu ve ihtarname taslağı.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
