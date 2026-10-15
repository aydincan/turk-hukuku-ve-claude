---
name: spor-siddet-6222-ceza
description: "Saha olayları, seyirden yasaklanma, şike, teşvik primi veya müsabaka güvenliği suçlarını 6222 sayılı Kanun çerçevesinde değerlendirmek ve ceza savunması ya da müşteki stratejisi kurmak gerektiğinde kullanın."
---

# Sporda Şiddet ve Spor Suçları (6222)

## Görev
Spor müsabakaları ile bağlantılı suç ve idari yaptırımları 6222 sayılı Kanun çerçevesinde değerlendirmek; seyirden yasaklanma, şike/teşvik primi ve saha güvenliği suçlarında unsur analizi yaparak savunma ya da şikâyet stratejisi kurmaktır.

## Soğuk başlangıç (intake)
1. Olay ne: saha içi/dışı şiddet, hakaret/çirkin tezahürat, sahaya girme, şike iddiası?
2. Müvekkilin sıfatı: sporcu, taraftar, yönetici, görevli?
3. Adli süreç hangi aşamada (soruşturma, kovuşturma) ve idari (seyirden yasaklanma) tedbir var mı?
4. Görüntü kaydı, tutanak ve tanık var mı?
5. Tedbir/yasak kararının tebliğ tarihi nedir?

## Denetim şeması
1. **Norm tespiti**: 6222 sayılı Kanunun ilgili maddesi belirlenir — örn. şike ve teşvik primi (m.11), seyirden yasaklanma (m.18), müsabaka alanına usulsüz girme, hakaret içeren tezahürat gibi fiiller.
2. **Suç unsurları**: Maddi unsur (fiil, netice), manevi unsur (kast), faillik ve iştirak; şikede edim-karşı edim ilişkisi ve teşebbüs tartışılır.
3. **İdari tedbir-ceza ayrımı**: Seyirden yasaklanma idari tedbir niteliğindedir; adli ceza süreciyle paralel yürür. Tedbire karşı **sulh ceza hâkimliği** itiraz yolu ve süresi kontrol edilir.
4. **Görev ve usul**: Suçlar adli yargıda (CMK 5271) görülür; soruşturma, koruma tedbirleri, iddianame ve istinaf/temyiz aşamaları izlenir. Disiplin süreci federasyonda ayrıca yürür (non bis in idem tartışması).
5. **Delil**: Güvenlik kamerası kayıtları, hakem/gözlemci ve emniyet tutanakları, elektronik bilet/PASSOLIG kayıtları değerlendirilir.
6. **Ara sonuç**: İsnadın sübut ihtimali, lehe deliller ve hem adli hem idari ayakta savunma çizgisi belirlenir.

## Çıktı modülleri
- Unsur analizi tablosu (madde → unsur → eldeki delil)
- Savunma ya da şikâyet dilekçesi taslağı
- Seyirden yasaklanmaya itiraz dilekçesi
- Adli/idari/disiplin paralel süreç haritası

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
