---
name: basvuru-formu-ve-dilekce
description: "Bireysel başvuru formunun doldurulması, ihlal iddialarının altlanması, ek belgeler, harç, vekâlet ve maddi/manevi tazminat talebi yazılırken; başvuruyu fiilen kaleme almak için kullanılır."
---

# Başvuru Formu ve Dilekçe Hazırlığı

## Görev
6216 m.47 ve İçtüzük m.59-63'e uygun, eksiksiz ve ikna edici bir bireysel başvuru formu ile eklerini hazırlamak.

## Soğuk başlangıç (intake)
- Başvurucu ve varsa vekilin kimlik/iletişim bilgileri ve vekâletname hazır mı?
- Nihai karar ve tüm derece mahkemesi kararları, tebliğ belgeleri elde mi?
- İhlal edilen hak(lar) ve dayanak vakıalar net mi?
- Tazminat talebi var mı; miktar ve gerekçesi belirlendi mi?

## Denetim şeması
1. Zorunlu unsurlar — m.47/2 ve İçtüzük m.59: başvurucu/temsilci bilgileri, işlem/karar tarihleri, başvuru yollarının tüketildiği tarih, ihlal edildiği ileri sürülen hak ve gerekçeleri, talep. Eksik form için giderme süresi verilir; giderilmezse ret.
2. Form üzerinden başvuru — başvuru, AYM'nin resmî başvuru formuyla yapılır; doğrudan AYM'ye veya mahkemeler/yurt dışı temsilcilikler aracılığıyla sunulabilir. Güncel form ve usul resmî siteden teyit edilir.
3. İhlal altlaması — her hak için: ilgili Anayasa maddesi → müdahale/olay → m.13 ölçütleri (kanunilik, amaç, ölçülülük) → AYM/AİHM ilkesi [doğrulanacak] → sonuç. Kanun yolu şikâyeti izlenimi vermekten kaçınılır; anayasal boyut öne çıkarılır.
4. Mağdur sıfatı ve esasa etki — başvurucunun güncel-kişisel-doğrudan etkilenmesi ve usuli kusurun sonuca etkisi açıkça gösterilir.
5. Talep ve giderim — m.50: ihlal tespiti, yeniden yargılama veya tazminat (maddi/manevi) açıkça talep edilir; tazminat istenmiyorsa belirtilir.
6. Ekler ve harç — dayanak kararlar, tebliğ belgeleri, deliller eklenir; başvuru harcının yatırıldığı belgelenir (güncel tutar teyit edilir).

İspat yükü: tüm iddiaların belgeyle desteklenmesi başvurucuya aittir.

Ara sonuç: forma aktarılmaya ve avukat incelemesine hazır, eksiksiz başvuru taslağı.

## Çıktı modülleri
- Başvuru formu taslağı (alan alan, [doldurulacak] yer tutucularıyla).
- İhlal gerekçeleri bölümü (hak bazlı altlama).
- Talep ve tazminat bölümü.
- Ek belge ve harç kontrol listesi.

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
