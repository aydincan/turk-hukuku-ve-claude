---
name: asiri-dusuk-teklif
description: "Teklifin aşırı düşük olarak değerlendirilmesi, açıklama istenmesi veya açıklamanın yetersiz görülerek reddi tartışıldığında kullanılacak özel değerlendirme becerisidir."
---

# Aşırı Düşük Teklif Sorgulaması

## Görev
Bir teklifin aşırı düşük sayılarak açıklama istenmesi sürecinin ve açıklamanın kabul/reddinin hukuka uygunluğunu denetlemek; istekli adına savunulabilir açıklama stratejisi kurmak.

## Soğuk başlangıç (intake)
1. İhale türü nedir; aşırı düşük sınır değer/sorgulama nasıl hesaplandı?
2. İdare yazılı açıklama istedi mi, talep edilen hangi bileşenler için?
3. Açıklamaya hangi belgeler sunuldu (maliyet, fiyat teklifi, analiz)?
4. Açıklama hangi gerekçeyle reddedildi?

## Denetim şeması
1. **Tespit (m.38):** Diğer tekliflere veya yaklaşık maliyete göre aşırı düşük görünen teklifler reddedilmeden önce yazılı açıklama istenir; idare doğrudan reddedemez, sorgulama zorunludur.
2. **Açıklama konuları:** İmalat sürecinin/hizmetin ekonomikliği, seçilen teknik çözümler, istisnaî elverişli koşullar, teklif edilen işin özgünlüğü gibi unsurlar belgelenir. Yapım/hizmet ihalelerinde önemli maliyet bileşenleri ve sınır değer Kamu İhale Genel Tebliği'ndeki yönteme göre değerlendirilir.
3. **Belgelendirme:** Açıklamanın üçüncü kişilerden alınan proforma/fiyat teklifi, kamu kurumu fiyatları, kendi üretim maliyeti gibi tevsik edici belgelere dayanması gerekir; mevzuata uygun analiz formatı aranır.
4. **Değerlendirme:** Açıklama yeterliyse teklif geçerli kabul edilir; yetersiz/dayanaksızsa reddedilir. İdarenin değerlendirmesi gerekçeli olmalı, soyut ret iptal sebebidir.
5. **Ara sonuç:** Aşırı düşük açıklamasının reddi/kabulü kesinleşen karar bildirimiyle birlikte şikâyet-itirazen şikâyet konusu yapılır. Tebliğdeki güncel hesap yöntemi `[güncel Tebliğ doğrulanacak]` teyit edilir.

İspat yükü: Açıklamayı sunan istekli, fiyatın gerçekçiliğini belgelerle ispatlar; idare reddi somut analizle gerekçelendirir.

## Çıktı modülleri
- Sınır değer/sorgulama hesap kontrolü.
- Maliyet bileşeni bazlı açıklama taslağı iskeleti.
- Ret gerekçesi yeterlilik değerlendirmesi.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
