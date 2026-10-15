---
name: zaman-bakimindan-uygulama
description: "Olay eski yürürlükteyken doğmuş ama yeni bir kanun çıkmışsa ya da kanun değişikliği devam eden ilişkileri etkiliyorsa; hangi kanunun uygulanacağını ve geçmişe etki sorununu çözmek için kullanılır."
---

# Normların Zaman Bakımından Uygulanması

## Görev
Bir olaya eski mi yeni mi kanunun uygulanacağını, geçmişe yürüme yasağı, geçiş hükümleri ve derhal uygulama ilkeleri çerçevesinde belirlemek.

## Soğuk başlangıç (intake)
- Olay/işlem hangi tarihte gerçekleşti; kanun değişikliği ne zaman yürürlüğe girdi?
- İlişki tamamlanmış mı, yoksa hâlâ devam eden bir durum mu (sürekli borç, kira, velayet)?
- Değişen kanunda geçici/geçiş maddesi var mı?
- Alan ceza mı (lehe kanun ilkesi farklı işler) yoksa özel hukuk mu?

## Denetim şeması
1. **Yürürlük tarihini sabitle** — Kanunun ve ilgili maddenin yürürlük tarihi (Resmî Gazete) ve geçici maddeleri tespit edilir; mevzuat.gov.tr karşılaştırmalı metni esas alınır.
2. **Kural: geçmişe etkisizlik** — Hukuki güvenlik gereği yeni kanun, tamamlanmış olaylara ve kazanılmış haklara kural olarak uygulanmaz; eski olay eski kanuna tabidir.
3. **Derhal uygulama** — Yeni kanun, yürürlükten sonraki olgulara ve devam eden hukuki durumların ileriye dönük sonuçlarına derhal uygulanır (özellikle kamu düzeni ve genel ahlakı ilgilendiren hükümler — TMK Yürürlük Kanunu mantığı).
4. **Geçiş hükmü önceliği** — Kanunda açık geçiş/geçici hüküm varsa o esas alınır; genel ilkeler ancak geçiş hükmü yoksa devreye girer.
5. **Ceza istisnası** — Suç ve cezada kanunilik ve **lehe kanunun geçmişe yürümesi** (TCK m.7) ilkesi ayrıdır; özel hukuk mantığıyla karıştırılmaz.
6. **Zamanaşımı/süre değişimi** — Süreye ilişkin yeni hükümlerin başlamış sürelere etkisi, çoğunlukla özel geçiş hükmüyle düzenlenir; yoksa lehe/derhal uygulama tartışılır.

## Çıktı modülleri
- Olay-kanun zaman çizgisi.
- Uygulanacak kanun + dayanak ilke (geçmişe etkisizlik/derhal uygulama/geçiş hükmü).
- Kazanılmış hak değerlendirmesi.
- Ceza ise lehe kanun notu + `[doğrulanacak]` içtihat.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
