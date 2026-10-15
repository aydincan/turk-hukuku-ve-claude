---
name: adli-para-cezasi-infazi
description: "Adli para cezasının ödenmesi, taksitlendirme, kamuya yararlı işe çevirme ve ödenmemesi hâlinde hapse çevrilmesini değerlendirmek gerektiğinde kullanılır."
---

# Adli Para Cezasının İnfazı ve Hapse Çevirme

## Görev
Adli para cezasının infaz seçeneklerini ve ödenmemesi hâlinde hapse çevrilme riskini 5275 m.106 ekseninde yönetmek.

## Soğuk başlangıç (intake)
- Adli para cezasının toplam tutarı nedir; ödeme emri tebliğ edildi mi?
- Hükümlünün ödeme gücü ve taksit talebi var mı?
- Daha önce kısmi ödeme yapıldı mı?
- Ceza, hapisten çevrilmiş adli para cezası mı yoksa doğrudan mı (hapse iade kuralı farkı)?

## Denetim şeması
1. Ödeme süreci: kesinleşen adli para cezası tebliğ edilen ödeme emriyle istenir; süresinde ödenmezse Cumhuriyet savcılığınca tahsil/çevirme işlemleri başlar (5275 m.106).
2. Taksitlendirme: hükümlünün talebiyle, kanunda öngörülen koşullarda taksitlendirme mümkündür; bir taksitin ödenmemesi kalanın muacceliyetine yol açabilir. Ara sonuç: ödeme planı uygunluğu.
3. Kamuya yararlı işe çevirme: ödenmeyen para cezası, hükümlünün rızası ve uygunluk hâlinde kamuya yararlı bir işte çalıştırmaya çevrilebilir (5275 m.106). İspat: çalışma uygunluğu ve denetimli serbestlik müdürlüğü değerlendirmesi.
4. Hapse çevirme: ödenmeyen ve çevrilemeyen para cezası, kanunda öngörülen hesaba göre hapse çevrilir; ancak doğrudan hükmedilen adli para cezasında ödendiğinde hükümlü serbest bırakılır. Çevrilen hapis için üst sınır ve hesap kuralları kontrol edilir.
5. İtiraz: çevirme/infaz işlemine karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
6. Ara sonuç: ödeme/taksit/çevirme seçeneği + hapse çevrilme riski.

## Çıktı modülleri
- Ödeme seçenekleri tablosu.
- Hapse çevirme hesabı taslağı.
- Taksit veya kamuya yararlı işe çevirme talep dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
