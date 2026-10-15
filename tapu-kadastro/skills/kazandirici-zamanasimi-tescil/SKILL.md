---
name: kazandirici-zamanasimi-tescil
description: "Tapusuz ya da malik kaydı belirsiz/ölü taşınmazın uzun süreli zilyetlikle kazanılarak adına tescili istendiğinde; olağan (m.712) ve olağanüstü (m.713) kazandırıcı zamanaşımı şartları, süre, zilyetlik niteliği ve istisna araziler değerlendirilirken kullanılır."
---

# Kazandırıcı Zamanaşımı ve Tescil (TMK m.712-713)

## Görev
Zilyetliğe dayalı mülkiyet kazanımının şartlarını denetlemek ve uygun olduğunda tescil davasını kurmak; olağan ve olağanüstü zamanaşımı ile kadastro zilyetliğini (3402 m.14) ayırt etmek.

## Soğuk başlangıç (intake)
- Taşınmaz tapulu mu (kim adına) yoksa tapusuz mu; tapu varsa malik ölü/gaip/belirsiz mi?
- Zilyetlik kaç yıldır, kesintisiz ve davasız mı; malik sıfatıyla mı kullanılıyor?
- Taşınmazın niteliği (tarım, orman, mera, kıyı, kamu) ve yüzölçümü nedir?
- Zilyetlik miras/satış yoluyla devralındıysa önceki zilyetlikle birleştirme mümkün mü?

## Denetim şeması
1. **Olağan zamanaşımı (TMK m.712).** Bir taşınmaza tapuda malik görünen ancak tescili yolsuz olan kişi; davasız, aralıksız ve iyiniyetle 10 yıl zilyet kalırsa kazanımı geçerli sayılır. İyiniyet (TMK m.3) ve geçerli tescil görünüşü şarttır.
2. **Olağanüstü zamanaşımı (TMK m.713).** Tapuda kayıtlı olmayan veya maliki 20 yıl önce ölmüş/gaipliğine karar verilmiş ya da kim olduğu belirlenemeyen taşınmazda; davasız, aralıksız, malik sıfatıyla 20 yıl zilyetlik → mahkemeden tescil istenebilir. İyiniyet aranmaz; ilan ve itiraz prosedürü işletilir.
3. **İstisna arazileri ele.** Orman (kadastro/orman mevzuatı), kıyı (Kıyı Kanunu), mera/yaylak, kamu malları ve özel kanunla tescili yasak yerler zamanaşımıyla kazanılamaz. Nitelik tespiti dava şartı gibidir.
4. **Zilyetliği birleştir.** Zilyetlik, önceki zilyetten devren (miras/satış) geçmişse süreler eklenir (TMK m.996, m.700); ancak nitelik ve davasızlık tüm dönem için aranır.
5. **Husumet ve usul.** Davalı Hazine ve/veya ilgili idare; tapulu ise malik/mirasçıları. Tescil davasında ilan, keşif, yerel bilirkişi-tanık ve fen incelemesi yapılır.
6. **Kadastro paraleli.** Kadastro sırasında aynı zilyetlik 3402 m.14 ile tespit konusu olur; süre ve sınırlar (40 dönüm, vergi kaydı) burada uygulanır.
7. **Ara sonuç.** Hangi madde (712/713/3402-14), süre tamam mı, taşınmaz tescile elverişli mi.

## Çıktı modülleri
- Şart kontrol listesi (süre / davasızlık / malik sıfatı / iyiniyet / nitelik).
- Tescil davası dilekçe iskeleti (husumet, ilan talebi, keşif/bilirkişi talebi).
- Tescile engel nitelik (orman/kıyı/mera) risk notu.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
