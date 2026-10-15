---
name: kloz-tasarimi-strateji
description: "Bir sözleşmeye tahkim veya arabuluculuk klozu yerleştirirken forum, dil, yer, kurum ve çok kademeli uyuşmazlık çözüm zinciri kurmak; uyuşmazlık öncesi strateji belirlemek gerektiğinde kullanılır."
---

# Kloz Tasarımı ve Forum Stratejisi

## Görev
Sözleşme müzakeresinde uyuşmazlık çözüm mimarisini kurmak: tahkim mi devlet yargısı mı,
çok kademeli (müzakere-arabuluculuk-tahkim) zincir mi; yer, dil, kurum ve uygulanacak
hukuk seçimini stratejik olarak belirlemek.

## Soğuk başlangıç (intake)
1. Sözleşme yerli mi sınır ötesi mi, taraflar ve ifa yeri nerede?
2. Uyuşmazlık değeri ve niteliği (gizlilik, teknik bilirkişi, hız ihtiyacı) nedir?
3. İcra/tenfiz nerede aranacak (karşı tarafın malvarlığı nerede)?
4. Çok kademeli çözüm (önce arabuluculuk, sonra tahkim) isteniyor mu?

## Denetim şeması
1. **Forum seçimi**: Yabancılık unsuru ve tenfiz ihtiyacı varsa tahkim (**New York
   Sözleşmesi** sayesinde tenfiz kolaylığı) tercih edilir; tamamen yerli ve düşük değerli
   uyuşmazlıkta devlet yargısı daha ekonomik olabilir. Elverişlilik **HMK m.408** süzgeci.
2. **Kloz unsurları**: Tahkim klozunda **tahkim yeri, dil, hakem sayısı, kurum kuralları**
   (ör. ISTAC, ICC, ITOTAM) ve esasa uygulanacak hukuk açıkça belirlenir; yazılılık
   (**HMK m.412**, **MTK m.4**) sağlanır. Eksik/çelişkili kloz patolojiktir.
3. **Çok kademeli (multi-tier) zincir**: Önce zorunlu müzakere/arabuluculuk, sonra tahkim
   öngörülebilir; her kademenin **süresi ve geçiş şartı** somut yazılmalı, aksi halde
   tahkime erişim tartışmaya açılır. Dava şartı arabuluculuk kapsamındaki uyuşmazlıklarda
   yasal zorunluluk ayrıca gözetilir.
4. **Tenfiz odaklı tasarım**: Hakem kararının icra edileceği ülkenin rejimi (kamu düzeni,
   elverişlilik) baştan değerlendirilir; karşı tarafın malvarlığının bulunduğu yer
   belirleyicidir.
5. **Ara sonuç**: Önerilen forum, kloz iskeleti ve strateji gerekçesi.

## Çıktı modülleri
- Forum karşılaştırma tablosu (tahkim/arabuluculuk/devlet yargısı; maliyet-hız-tenfiz).
- Tahkim ve/veya çok kademeli kloz taslağı ([doldurulacak] yer, dil, kurum, hukuk).
- Tenfiz/strateji risk notu.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
