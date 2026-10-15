---
name: maddi-tazminat-hesabi
description: "Sorumluluk kurulduktan sonra maddi zararın kalemlerini ayrıştırmak, fiili zarar ve yoksun kalınan kârı hesaplatmak ve hâkimin takdir yetkisini değerlendirmek gerektiğinde kullanılır."
---

# Maddi Tazminatın Belirlenmesi ve Hesabı

## Görev
Maddi zararı kalem kalem belirlemek (fiili zarar + yoksun kalınan kâr), tazminatın kapsamını TBK m.50-51 çerçevesinde tespit etmek ve hâkimin zararı tam ispatlanamayan hallerde takdir yetkisini (m.50/2) doğru konumlandırmak. Hesaplar daima dayanağıyla gösterilir.

## Soğuk başlangıç (intake)
- Zarar kalemleri neler (onarım/yenileme bedeli, gelir kaybı, masraflar)?
- Belge/fatura/ekspertiz var mı; zarar tam belgelenebiliyor mu?
- Zarar görenin kusuru veya zararı artıran davranışı var mı?
- Sigorta/üçüncü kişi ödemesi yapıldı mı (denkleştirme)?

## Denetim şeması
1. **Zarar kavramı.** Malvarlığında istem dışı azalma; farazi (zarar olmasaydı) malvarlığı ile gerçek malvarlığı arasındaki fark. Fiili zarar (doğrudan kayıp) ve yoksun kalınan kâr (mahrum kalınan kazanç) ayrılır.
2. **Tazminatın kapsamı (m.51).** Hâkim, tazminatın kapsamını ve ödenme biçimini zararın ağırlığı ile kusurun derecesini göz önünde tutarak belirler. Kural tam tazmin; zararı aşan zenginleşme verilmez.
3. **İspat ve takdir (m.50).** Zarar görenin zararını ispatı asıldır; zararın gerçek miktarı kesin ispat edilemiyorsa hâkim olayların olağan akışını ve zarar görenin aldığı önlemleri göz önünde tutarak hakkaniyetle belirler (m.50/2).
4. **Denkleştirme (yararların mahsubu).** Aynı olaydan doğan ve zararı azaltan yararlar (kurtarılan değer, bazı ödemeler) belirli ölçüde mahsup edilebilir; sosyal güvenlik/sigorta ödemelerinin etkisi ve rücu ilişkisi ayrıca incelenir.
5. **Faiz ve dönem.** Haksız fiilde temerrüt kural olarak fiil/zarar tarihinde başlar; talep edilen faiz türü ve başlangıcı belirtilir.
6. **Ara sonuç.** Kalem-tutar-dayanak tablosu kurulur; belgesiz kalemler için bilirkişi/ekspertiz ihtiyacı ve m.50/2 takdiri işaretlenir. Karmaşık hesaplarda aktüer/bilirkişi yönlendirmesi yapılır.

## Çıktı modülleri
- Zarar kalemleri ve tutar-dayanak tablosu.
- Bilirkişi/ekspertiz soru listesi (belirsiz kalemler için).
- Faiz türü-başlangıç notu ve talep sonucu rakamı taslağı.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
