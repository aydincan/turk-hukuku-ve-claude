---
name: lehe-kanun-infaz
description: "İnfaz oranlarını değiştiren geçici maddeler, 7242 sayılı Kanun türü değişiklikler, af ve lehe kanun uygulamasının infaza etkisini çözümlemek gerektiğinde kullanılır."
---

# Lehe Kanun, Af ve Geçici Düzenlemelerin İnfaza Etkisi

## Görev
Suç tarihi ile infaz tarihi arasında değişen infaz hükümlerinden hangisinin uygulanacağını, af ve geçici düzenlemelerin etkisini lehe kanun ilkesi (TCK m.7) ışığında çözmek.

## Soğuk başlangıç (intake)
- Suç tarihi ile hüküm/kesinleşme tarihleri nedir?
- Aralıkta infaz oranını değiştiren bir kanun (örn. 7242 sayılı Kanun) yürürlüğe girdi mi?
- Suç tipi geçici düzenlemelerin kapsamına giriyor/dışında mı?
- Bir af, özel af veya seçimlik yaptırım düzenlemesi söz konusu mu?

## Denetim şeması
1. Niteliği belirle: TCK m.7/2 sonradan yürürlüğe giren lehe kanunun uygulanmasını öngörür; ancak infaz rejimine ilişkin hükümlerin maddi ceza hükmü mü yoksa usule ilişkin mi sayılacağı tartışmalıdır. Koşullu salıverilme ve denetimli serbestlik oranları, yerleşik yaklaşım uyarınca suç tarihine göre lehe olan biçimde uygulanır. Ara sonuç: hangi metin uygulanacak?
2. Geçici maddeler: 7242 sayılı Kanun ve TCK geçici m.6 gibi düzenlemeler, belirli suç tipleri dışında oranları değiştirmiştir; kapsam dışı suçlar (terör, kasten öldürme, cinsel suçlar, uyuşturucu ticareti) için istisna rejimi kontrol edilir.
3. Af: genel af mahkûmiyeti tüm sonuçlarıyla, özel af cezanın infazını etkiler (TCK m.65); af kanununun kapsam ve şartları metinden doğrulanır.
4. Karşılaştırmalı uygulama: suç tarihindeki ve hâlihazırdaki düzenlemelere göre iki ayrı infaz hesabı yapılır, hükümlü lehine olan benimsenir. İspat: yürürlük tarihleri ve geçici madde metinleri mevzuat.gov.tr üzerinden.
5. İtiraz/uyarlama: lehe hükmün uygulanması talebi infaz savcılığına/infaz hâkimliğine; uyarlama gereken hâllerde hükmü veren mahkemeye yöneltilir.
6. İlkesel içtihat: lehe kanun ve infaz oranı için karararama.yargitay.gov.tr Yargıtay CGK ve 1. CD; AYM eşitlik/öngörülebilirlik kararları (kararlarbilgibankasi.anayasa.gov.tr). Künye `[doğrulanacak]`.
7. Ara sonuç: uygulanacak metin + lehe hesap + başvuru mercii.

## Çıktı modülleri
- İki senaryolu lehe karşılaştırma tablosu.
- Kapsam/istisna kontrol listesi.
- Lehe hüküm uygulanması veya uyarlama talebi dilekçesi tetiği.

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
