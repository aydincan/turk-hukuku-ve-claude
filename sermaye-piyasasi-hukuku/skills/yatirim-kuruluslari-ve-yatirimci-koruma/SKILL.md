---
name: yatirim-kuruluslari-ve-yatirimci-koruma
description: "Aracı kurum/banka ile yatırımcı arasındaki çerçeve sözleşme, uygunluk-yerindelik, emir gerçekleştirme, müşteri varlıklarının korunması ve yatırımcı tazmini sorunları gündeme geldiğinde kullanılır."
---

# Yatırım Kuruluşları ve Yatırımcının Korunması

## Görev
Yatırım kuruluşu (aracı kurum/banka) ile yatırımcı arasındaki ilişkiyi SPK m.34 vd. ve yatırım hizmetleri tebliğleri çerçevesinde denetlemek; uygunluk/yerindelik testi, emir gerçekleştirme, müşteri varlıkları ve tazmin yollarını değerlendirmek.

## Soğuk başlangıç (intake)
- Hangi yatırım hizmeti söz konusu: alım-satım aracılığı, portföy yönetimi, danışmanlık mı?
- Çerçeve sözleşme ve uygunluk/yerindelik testi yapıldı mı; risk bildirimi imzalandı mı?
- Şikâyet konusu: yetkisiz işlem, yerindelik ihlali, emir gerçekleştirmeme, varlık kaybı mı?
- Müvekkil yatırımcı mı, yatırım kuruluşu mu; kuruluş faaliyet iznini koruyor mu?

## Denetim şeması
1. **Hizmet nitelendirmesi:** Sunulan hizmetin türü (SPK m.37 yatırım hizmet ve faaliyetleri) belirlenir; her hizmet farklı yükümlülük setine tabidir.
2. **Uygunluk/yerindelik:** Müşteri sınıflandırması ve yerindelik/uygunluk testinin yapılıp yapılmadığı, ürünün müşteri profiline uygunluğu denetlenir; eksiklik kuruluşun sorumluluğunu ağırlaştırır.
3. **Emir ve özen:** Emir gerçekleştirme ilkeleri, en iyi şekilde gerçekleştirme ve özen yükümlülüğü; yetkisiz/talimat dışı işlem iddiası talimat kayıtları ve ses kayıtlarıyla incelenir. Ara sonuç: kusurun kimde olduğu netleşir.
4. **Müşteri varlıkları:** Müşteri varlıklarının kuruluş malvarlığından ayrı tutulması, MKK/Takasbank nezdindeki kayıtlar üzerinden doğrulanır; kayıp halinde Yatırımcı Tazmin Merkezi (SPK m.83) devreye girer.
5. **Sorumluluk ve yol:** Sözleşmeye aykırılık/haksız fiil (TBK m.112, m.49) ile SPK yükümlülükleri birlikte değerlendirilir; uyuşmazlıkta sözleşmesel tahkim, Kurul şikâyeti ve adli yargı yolları ayrıştırılır. İspatta talimat/işlem kayıtları esastır.

## Çıktı modülleri
- Hizmet ve yükümlülük haritası
- Uygunluk/yerindelik ve emir denetim notu
- Tazmin yolu (YTM/dava/tahkim) değerlendirmesi
- Yatırımcı talep iskeleti veya kuruluş savunma çerçevesi

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
