---
name: tazminattan-indirim-sebepleri
description: "Karşı taraf zarar görenin kendi kusurunu, zararı ağırlaştıran davranışını veya failin az kusurunu ileri sürerek tazminatın azaltılmasını istediğinde; indirim sebeplerini değerlendirmek için kullanılır."
---

# Tazminattan İndirim Sebepleri

## Görev
TBK m.52'deki indirim sebeplerini (zarar görenin kendi kusuru/müterafik kusur, durumu ağırlaştırması, rıza) ve m.51'in kusur-zarar dengesini denetleyerek tazminat miktarının hakkaniyetle azaltılıp azaltılmayacağını belirlemek. İndirim, sorumluluğu kaldırmaz; miktarı düşürür.

## Soğuk başlangıç (intake)
- Zarar gören kendi davranışıyla zarara katkıda bulundu mu (örn. emniyet kemeri, talimata aykırılık)?
- Zarar görenin zararı azaltma yükümünü ihmal ettiği bir durum var mı?
- Failin kusuru hafif mi; tazminat onu yoksulluğa düşürür mü?
- Zarar görenin rızası ya da riski göze alması söz konusu mu?

## Denetim şeması
1. **Müterafik (birlikte) kusur (m.52/1).** Zarar gören kendi kusuruyla zararın doğmasına/artmasına yol açmışsa hâkim tazminatı indirir; katkı oranı somut olarak belirlenir.
2. **Zararı azaltma yükümü.** Zarar gören, makul önlemlerle zararı azaltabilecekken kaçınmışsa artan kısımdan sorumlu tutulmaz (dürüstlük kuralı TMK m.2 ile birlikte değerlendirilir).
3. **Durumu ağırlaştıran davranış.** Zarar görenin zararı genişleten eylemleri indirim sebebidir; illiyeti tümden kesiyorsa sorumluluk kalkar.
4. **Hafif kusur ve yoksulluk (m.52/2).** Fail hafif kusurluysa ve tazminat onu yoksulluğa düşürecekse, hakkaniyet gerektiriyorsa hâkim tazminatı indirebilir; bu istisnai bir denkleştirmedir.
5. **Rıza ve riski göze alma.** Geçerli rıza aykırılığı kaldırabilir (m.63); kısmî/örtülü rıza ise indirim sebebi olabilir.
6. **Ara sonuç ve ispat.** İndirim sebeplerini ileri süren ve katkı oranını ispatlayan taraf (genelde davalı) yükü taşır (TMK m.6). İndirim oranı gerekçelendirilir; kalan tazminat miktarı netleştirilir.

## Çıktı modülleri
- İndirim sebepleri kontrol listesi (sebep + katkı oranı + dayanak).
- Müterafik kusur değerlendirme notu.
- Net tazminat etkisi hesabı (indirim öncesi/sonrası).

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
