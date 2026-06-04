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

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
