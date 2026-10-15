---
name: ozel-uzman-mutalaasi
description: "Bilirkişi raporunu mahkemenin atadığı bilirkişi dışında bir özel uzmandan alınacak mütalaayla teknik olarak çürütmek; bu mütalaanın delil değerini ve itirazla nasıl bağlanacağını planlamak istendiğinde kullanılır."
---

# Karşı Uzman Mütalaası ile Çürütme

## Görev
Resmî bilirkişi raporunun teknik yanını, tarafın kendi seçtiği bir uzmandan aldığı mütalaayla karşılamak; bu mütalaayı usulî olarak doğru konumlandırıp itiraza güç katacak biçimde dosyaya kazandırmak.

## Soğuk başlangıç (intake)
- Raporun çürütülmek istenen teknik noktası tam olarak nedir?
- Bu alanda mütalaa verebilecek bağımsız bir uzmana erişim var mı?
- Mütalaa, rapordaki yöntem hatasını mı yoksa hesap/veri hatasını mı hedefliyor?
- Mütalaa itiraz süresine yetiştirilebilecek mi?

## Denetim şeması
1. **Delil niteliği:** Tarafın aldığı uzman mütalaası, mahkemece atanan bilirkişi raporu gibi bağlayıcı bir delil olmayıp tarafın iddiasını destekleyen, hâkimin serbest takdirine (HMK m.282) sunulan bir görüştür. Bu sınır mütalaada açıkça belirtilmelidir.
2. **Hedef seçimi:** Mütalaa, raporun en zayıf ve teknik olarak çürütülebilir noktasına odaklanır (yöntem, kabul, veri veya hesap). Hukuki nitelendirmeye girmez; aksi hâlde bilirkişi raporuyla aynı görev sınırı sorununa düşer (HMK m.266).
3. **Çıpalama:** Mütalaadaki her itiraz, resmî rapordaki sayfa/paragrafa ve dosya verisine bağlanır; böylece mahkeme iki teknik görüşü karşılaştırabilir.
4. **Usule bağlama:** Mütalaa, HMK m.281 itiraz dilekçesine ek olarak ve süresinde sunulur; gerekirse mütalaa doğrultusunda yeni/üçüncü heyet veya ek rapor talep edilir.
5. **Ara sonuç:** Mütalaa, soyut itirazı bilimsel temele oturtarak yeni heyet talebinin gerekçesini güçlendirir.

## Çıktı modülleri
- Çürütülecek teknik noktanın ve karşı tezin tek cümlelik özeti.
- Uzmandan istenecek soruların listesi (rapordaki paragraflara çıpalı).
- Mütalaanın itiraz dilekçesine bağlanma planı.
- Mütalaanın delil değerine ilişkin sınırlayıcı not (bağlayıcı değil, takdiri).

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
