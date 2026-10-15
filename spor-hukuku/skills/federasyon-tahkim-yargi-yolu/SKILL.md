---
name: federasyon-tahkim-yargi-yolu
description: "Bir spor kararına itiraz veya dava açma yolunu belirlemek, federasyon iç hukuk yolu, tahkim kurulu, CAS ve istisnai yargı/AYM seçeneklerini ve sıralarını çıkarmak gerektiğinde kullanın."
---

# Federasyon, Tahkim Kurulu ve Yargı Yolu Haritası

## Görev
Bir spor kararına (disiplin, transfer, uygunluk, idari) karşı izlenecek itiraz ve dava yolunu sırasıyla belirlemek; iç hukuk yolu, federasyon tahkim kurulu, CAS ve istisnai devlet yargısı/AYM seçeneklerini görev-yetki ve süre ekseninde haritalamaktır.

## Soğuk başlangıç (intake)
1. Karar hangi merciden çıktı (disiplin kurulu, yönetim kurulu, federasyon)?
2. Karar tebliğ tarihi nedir; itiraz/başvuru süresi başladı mı?
3. Futbol mu, başka branş mı?
4. Milletlerarası unsur (FIFA, uluslararası federasyon) var mı?
5. İç başvuru yolları tüketildi mi?

## Denetim şeması
1. **İç hukuk yolu**: Çoğu federasyonda önce disiplin kurulu kararına karşı federasyon içi itiraz/üst kurul yolu tüketilir. Tüketilmeden tahkime gidilemez.
2. **Tahkim Kurulu**: Futbolda **5894 sayılı Kanun m.6** uyarınca TFF Tahkim Kurulu nihai ve kesin mercidir; kararlarına karşı kural olarak yargı yolu kapalıdır. Diğer branşlarda 3289 sayılı Kanun ve federasyon ana statüsündeki tahkim kurulu görevlidir.
3. **Süre**: Tahkim başvuru süreleri talimatlarda kısadır (genelde tebliğden itibaren günlerle); hak düşürücü kabul edilir, kaçırılması başvuruyu reddettirir.
4. **Milletlerarası boyut**: FIFA/uluslararası federasyon organları kararlarına karşı **CAS** (Lozan) yolu; CAS kararının iptali sınırlı olarak İsviçre Federal Mahkemesi önünde gündeme gelir.
5. **İstisnai devlet yargısı/AYM**: Tahkim kararlarının kesinliği nedeniyle devlet yargısı kural olarak kapalıdır; ancak adil yargılanma/mülkiyet gibi temel hak ihlali iddiasıyla **AYM bireysel başvurusu** (6216 sayılı Kanun) gündeme gelebilir; süre ve başvuru yolu tüketme şartları kontrol edilir.
6. **Ara sonuç**: Akış şeması (merci → süre → bir sonraki adım) ve uygulanabilir/uygulanamaz yollar netleştirilir.

## Çıktı modülleri
- Yol haritası şeması (merci → süre → karar türü)
- Süre takvimi (tebliğ tarihinden geriye sayım)
- Başvuru/itiraz dilekçesi iskeleti
- İçtihat notu `[doğrulanacak]`

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
