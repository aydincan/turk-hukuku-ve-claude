---
name: mulkiyet-hakki-ihlali
description: "Kamulaştırma, kamulaştırmasız el atma, vergi/idari yaptırım, alacağa erişememe, tapu iptali gibi nedenlerle mülkiyet hakkına müdahale edildiği iddia edildiğinde kullanılır."
---

# Mülkiyet Hakkı İhlali

## Görev
Anayasa m.35 ve AİHS Ek 1 No'lu Protokol m.1 çerçevesinde mülkiyete müdahalenin var olup olmadığını, türünü ve ölçülülüğünü değerlendirmek.

## Soğuk başlangıç (intake)
- Söz konusu "mülk" nedir (taşınmaz, alacak, meşru beklenti, ekonomik değer)?
- Müdahale türü: yoksun bırakma (kamulaştırma), kullanımın kontrolü (yaptırım/imar), genel kural mı?
- Müdahalenin yasal dayanağı ve güttüğü kamu yararı nedir?
- Tazminat/denkleştirme sağlandı mı, sağlandıysa yeterli mi?

## Denetim şeması
1. Mülk kavramı — m.35: mevcut mallar yanında, icra edilebilir alacaklar ve yeterince somut "meşru beklenti" de mülk sayılır; salt umut yetmez.
2. Müdahale türü — üç kural: (a) mülkten yoksun bırakma, (b) kullanımın kontrolü, (c) genel müdahale. Her biri kendi ağırlığında incelenir.
3. Kanunilik — m.13/m.35: müdahale erişilebilir, öngörülebilir ve belirli bir kanuna dayanmalıdır. Kanuni dayanak yoksa diğer ölçütlere geçmeden ihlal doğar.
4. Meşru amaç — kamu yararı veya genel yarar güdülmelidir.
5. Ölçülülük (adil denge) — başvurucunun katlandığı külfet ile güdülen kamu yararı arasında makul denge aranır. Kamulaştırmada gerçek değer üzerinden ve makul sürede ödenen tazminat; kamulaştırmasız el atmada bedelin tam karşılanması; aşırı bireysel külfet ihlal doğurur.
6. Usuli güvenceler — başvurucuya itiraz ve görüşlerini sunma imkânı tanınmış olmalıdır.

İspat yükü: mülkün ve aşırı külfetin varlığını başvurucu; müdahalenin haklılığını idare/Devlet ortaya koyar.

Ara sonuç: müdahale türü ve hangi ölçütte (kanunilik/amaç/denge) ihlal bulunduğu.

## Çıktı modülleri
- Mülk niteliği ve müdahale türü tespiti.
- Kanunilik–amaç–ölçülülük altlaması.
- Tazminat/denkleştirme yeterlilik notu.
- İlke kararlarına atıf [doğrulanacak].

## Plugin bağlamı

Bu beceri `anayasa-mahkemesi-bireysel-basvuru` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
