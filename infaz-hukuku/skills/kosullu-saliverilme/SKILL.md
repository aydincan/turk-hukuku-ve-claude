---
name: kosullu-saliverilme
description: "Koşullu salıverilmenin süre, iyi hâl ve suç tipi şartlarını denetlemek, geri alma sebeplerini değerlendirmek ve koşullu salıverilme kararına itirazı kurgulamak gerektiğinde kullanılır."
---

# Koşullu Salıverilme Şartları ve Denetimi

## Görev
Hükümlünün koşullu salıverilmeden yararlanıp yararlanamayacağını, hangi tarihte yararlanacağını ve geri alma riskini 5275 m.107 ve m.108 çerçevesinde denetlemek.

## Soğuk başlangıç (intake)
- Hükümlü cezasının ne kadarını fiilen çekti?
- İyi hâl değerlendirmesi (5275 m.89) olumlu mu; disiplin cezası var mı?
- Suç mükerrir mi (5275 m.108 ayrı rejim)?
- Suç tipi koşullu salıverilmeyi kısıtlayan kataloğa giriyor mu?

## Denetim şeması
1. Süre şartı: 5275 m.107/2 uyarınca infaz kurumunda geçirilmesi gereken asgari süre; süreli hapiste genel oran ile özel suç tiplerindeki ağırlaştırılmış oranlar ayrılır. Ağırlaştırılmış müebbette ve müebbette farklı asgari fiilî infaz süreleri uygulanır (m.107/2-3). Ara sonuç: aday tarih.
2. İyi hâl şartı: 5275 m.89 uyarınca idare ve gözlem kurulunca yapılan iyi hâl değerlendirmesi şarttır; olumsuz değerlendirme koşullu salıverilmeyi erteler. Disiplin cezalarının kaldırılmış olup olmadığı (m.48) kontrol edilir.
3. Mükerrirlik: ikinci defa mükerrirler için 5275 m.108 daha ağır oran ve denetim süresi getirir; bu rejim ayrıca uygulanır.
4. Geri alma: 5275 m.107/12 vd. — denetim süresi içinde kasıtlı suç işlenmesi veya yükümlülüklere uyulmaması hâlinde koşullu salıverilme geri alınır; bu durumda bakiye ceza aynen infaz edilir. İspat yükü: yükümlülük ihlali iddiasını denetimli serbestlik müdürlüğü/savcılık ortaya koyar.
5. İtiraz: koşullu salıverilme kararına/red kararına karşı infaz hâkimliği ve itiraz mercii yolu (4675 sayılı Kanun, CMK itiraz hükümleri). İlkesel içtihat için karararama.yargitay.gov.tr Yargıtay 1. CD ve CGK kararları taranır; künye `[doğrulanacak]`.
6. Ara sonuç: yararlanma tarihi + geri alma riski değerlendirmesi.

## Çıktı modülleri
- Şart denetim çizelgesi (süre / iyi hâl / suç tipi / mükerrirlik).
- Geri alma risk notu.
- Karara itiraz dilekçesi taslak tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
