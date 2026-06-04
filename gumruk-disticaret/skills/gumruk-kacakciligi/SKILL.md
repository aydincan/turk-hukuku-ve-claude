---
name: gumruk-kacakciligi
description: "Gümrük işlemleriyle bağlantılı kaçakçılık suç ve kabahatleri, 5607 sayılı Kanun kapsamında cezai sorumluluk ve etkin pişmanlık söz konusu olduğunda; idari yük ile cezai riski birlikte yönetmek için kullanılır."
---

# Gümrük Kaçakçılığı ve Cezai Sorumluluk

## Görev
Gümrük işlemleriyle bağlantılı eylemlerin 5607 sayılı Kaçakçılıkla Mücadele Kanunu kapsamında suç mu kabahat mi oluşturduğunu değerlendirmek; cezai sorumluluk, etkin pişmanlık ve idari yükümlülükle ilişkisini birlikte yönetmek.

## Soğuk başlangıç (intake)
- İddia edilen eylem nedir (eşyayı gümrük işlemine tabi tutmadan ithal, sahte belge, gerçeğe aykırı beyan, transit/antrepo eşyasının amacı dışı kullanımı)?
- Soruşturma/kovuşturma aşaması nedir; el koyma var mı?
- Eşyanın kıymeti/vergileri belirlenmiş mi; ödeme veya teminat yapıldı mı?
- Etkin pişmanlık veya idari uzlaşma imkânı kullanılabilir mi?

## Denetim şeması
1. Suç-kabahat ayrımı: Eylemin 5607 m.3'teki ithalat/ihracat kaçakçılığı suçlarından birini mi yoksa idari yaptırımlık kabahati mi oluşturduğu belirlenir. Aynı maddi olayın hem 4458 idari cezası hem 5607 suçu kapsamına girebileceği gözetilir.
2. Tipiklik: Eşyayı gümrük işlemlerine tabi tutmaksızın ithal, aldatıcı işlem/sahte belge ile vergi ödememe, transit/şartlı muafiyet eşyasını amacı dışında tasarruf gibi seçimlik hareketler ayrı ayrı denetlenir.
3. Kast: Kaçakçılık suçları kasten işlenir (TCK m.21); beyan hatası, sınıflandırma görüş ayrılığı gibi durumlarda kastın bulunup bulunmadığı kritiktir.
4. Etkin pişmanlık: 5607'de soruşturma/kovuşturma evresine göre kademeli etkin pişmanlık ve ödemeye bağlı indirim/ceza ilişkisi değerlendirilir; eşyanın gümrüklenmiş değerinin ödenmesi sonuca etki eder.
5. İdari-cezai paralellik: 4458 ek tahakkuk/uzlaşma ile 5607 soruşturması paralel yürüyebilir; non bis in idem ve idari-adli süreçlerin etkileşimi gözetilir.
6. İspat: Suçun maddi ve manevi unsurlarını iddia makamı ispatlar; savunma beyan hatasını, kast yokluğunu ve belge geçerliliğini ortaya koyar. Bu beceri ceza savunması üretmez; risk haritalar ve uzman ceza avukatına yönlendirir.
7. Ara sonuç: Eylemin nitelendirmesi, ceza riski ve etkin pişmanlık/uzlaşma seçenekleri belirlenir. İlkesel içtihat karararama.yargitay.gov.tr üzerinden doğrulanır [doğrulanacak].

## Çıktı modülleri
- Suç-kabahat nitelendirme ve risk haritası
- İdari-cezai süreç paralellik notu
- Etkin pişmanlık/ödeme stratejisi değerlendirmesi

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
