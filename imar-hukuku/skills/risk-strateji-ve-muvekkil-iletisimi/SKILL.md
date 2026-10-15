---
name: risk-strateji-ve-muvekkil-iletisimi
description: "İmar dosyasında dava açmadan önce kazanım şansı, idari çözüm, maliyet ve geri dönülemez risklerin tartılması; müvekkile sade dilde durum, seçenek ve beklenti yönetimi sunulması gerektiğinde kullanılır."
---

# Risk Haritası, Strateji ve Müvekkil İletişimi

## Görev
İmar uyuşmazlığında hukuki yolların kazanım olasılığını, maliyetini ve riskini tartmak; müvekkile anlaşılır bir strateji ve beklenti çerçevesi sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin asıl amacı ne (yapıyı korumak, tazminat, inşaata devam, süre kazanmak)?
- Geri dönülemez bir adım var mı (yıkım yakın mı, inşaat ilerliyor mu)?
- İdari çözüm/uzlaşma (ruhsata bağlama, aykırılığı giderme, YKB) mümkün mü?
- Maliyet, süre ve itibar açısından kısıtlar neler?

## Denetim şeması
1. **Hedef ve seçenek ayrımı**: Müvekkilin gerçek menfaati ile hukuki araç eşleştirilir: iptal davası, tam yargı (tazminat), idari başvuru/uzlaşma, aykırılığı giderme, Yapı Kayıt Belgesi değerlendirmesi. Her seçeneğin sonucu ayrı yazılır.
2. **Kazanım olasılığı**: İşlemin unsur sakatlığı (yetki-şekil-sebep-konu-maksat), üst plana/yönetmeliğe aykırılık ve içtihat eğilimi tartılarak güçlü/zayıf/belirsiz olarak derecelendirilir; belirsizlik açıkça belirtilir, garanti verilmez.
3. **Geri dönülemez risk**: Yıkım, satış, inşaatın ilerlemesi gibi telafisi imkânsız sonuçlar varsa, **yürütmenin durdurulması (İYUK m.27)** ve ivedi başvuru önceliklendirilir; zamanlama riski en kritik kalemdir.
4. **Maliyet-fayda**: Harç, bilirkişi-keşif gideri, vekâlet ücreti, süre (idari yargıda istinaf/temyiz dahil yıllar) ile beklenen kazanım karşılaştırılır; uzlaşma/idari çözüm maliyet avantajıyla sunulur.
5. **Müvekkil iletişimi (sade dil)**: Teknik kavramlar (emsal, DOP, mühürleme, YD) yalın anlatılır; "kesin kazanırız" yerine olasılık, süre ve maliyet dürüstçe aktarılır; kararı müvekkilin vermesi sağlanır.
6. **Ara sonuç**: Önerilen yol, gerekçesi, alternatifleri, ilk 30 günde atılacak adımlar ve süre uyarıları tek sayfalık karar notuna bağlanır.

## Çıktı modülleri
- Risk haritası (seçenek × olasılık × maliyet × süre).
- Geri dönülemez risk ve ivedilik uyarısı.
- Müvekkile sade dilde durum/strateji notu.
- İlk adımlar ve süre takvimi (eylem planı).

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
