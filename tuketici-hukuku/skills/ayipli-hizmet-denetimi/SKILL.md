---
name: ayipli-hizmet-denetimi
description: "Bir hizmetin (tamir, kurs, sağlık dışı bakım, taşıma, dijital hizmet vb.) gereği gibi ifa edilmemesi halinde tüketicinin seçimlik haklarını ve sürelerini değerlendirmek gerektiğinde kullanılır."
---

# Ayıplı Hizmet Denetimi

## Görev
Sunulan hizmetin ayıplı olup olmadığını belirlemek, tüketicinin seçimlik haklarını (yeniden görme, indirim, dönme, onarım) altlamak ve hizmet ayıbına özgü ispat ve süre kurallarını uygulayarak çözüm yolunu belirlemek.

## Soğuk başlangıç (intake)
- Hizmet ne ve ne zaman ifa edildi; sözleşmede taahhüt edilen nitelik neydi?
- Eksiklik/kusur nedir; tüketici nasıl bir sonuç bekliyordu?
- Tüketici ne istiyor: hizmetin yeniden görülmesi, indirim, dönme, ek masrafların karşılanması?
- Zarar doğdu mu; hizmetin sonucu telafi edilebilir nitelikte mi?

## Denetim şeması
1. **Ayıplı hizmet (TKHK m.13):** Sözleşmede kararlaştırılan veya objektif olarak sahip olması gereken nitelikleri taşımayan, sağlayıcı tarafından reklam/vaat yoluyla bildirilen özellikleri içermeyen ya da eksik/kötü ifa edilen hizmet ayıplıdır.
2. **İspat (m.15 yollamasıyla m.10 kıyası):** Hizmetin ayıplı ifa edildiğine ilişkin ispatta, ifadan sonra makul sürede ortaya çıkan ayıplar bakımından sağlayıcının özen yükümü ve dosya delilleri (sözleşme, rapor, bilirkişi) tartılır.
3. **Seçimlik haklar (m.15):** Tüketici (a) hizmetin yeniden görülmesi, (b) ayıp oranında bedel indirimi, (c) ücretsiz onarım/eksikliğin giderilmesi, (d) sözleşmeden dönme haklarından birini seçebilir. Sağlayıcı bu talebi makul sürede ve tüketici için ciddi sorun çıkarmadan yerine getirmelidir. Ücretsiz onarım/yeniden görme orantısızsa diğer haklar gündeme gelir.
4. **Tazminat:** Seçimlik hakların yanında ayıbın sebep olduğu diğer zararlar genel hükümlere (TBK) göre talep edilebilir.
5. **Zamanaşımı (m.16):** Kural iki yıl; sağlayıcının ağır kusuru veya hilesi varsa süreyle sınırlı sorumluluktan yararlanamaz.
6. **Ara sonuç:** Talep süre içinde mi, hizmet ayıbı sabit mi, hangi seçimlik hak en uygun?

## Çıktı modülleri
- Hizmet ayıbı nitelendirmesi ve seçimlik hak önerisi.
- İspat ve delil ihtiyaç listesi (rapor, yazışma, ödeme belgesi).
- Sağlayıcıya talep yazısı taslağı.
- Yol haritası (hakem heyeti/mahkeme).

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
