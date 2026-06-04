---
name: ispat-delil-ve-piyasa-verisi
description: "Sermaye piyasası uyuşmazlıklarında emir/işlem kayıtları, KAP-MKK-Takasbank verileri, ses/talimat kayıtları ve bilirkişi incelemesi gibi delillerin toplanması ve değerlendirilmesi gerektiğinde kullanılır."
---

# İspat, Delil ve Piyasa Verisi

## Görev
Sermaye piyasası uyuşmazlığında ispat planını kurmak; içsel bilgi, fiyat etkisi, işlem zamanlaması ve kusur unsurlarını doğru delil türleriyle bağlamak.

## Soğuk başlangıç (intake)
- İspatlanması gereken çekirdek vakıa nedir (içsel bilgi, yapaylık, yerindelik ihlali, zarar)?
- Hangi kayıtlara erişilebilir: emir/işlem, KAP, MKK, Takasbank, ses/talimat kayıtları?
- Karşı tarafın elindeki ve üçüncü kişideki belgeler için talep gerekiyor mu?
- İspat yükü kimde; karine veya yer değiştirme söz konusu mu?

## Denetim şeması
1. **İspat yükü dağılımı:** Kural olarak iddia eden ispatla yükümlüdür (HMK m.190; cezada CMK m.217 ve şüpheden sanık yararlanır). İzahname/kamuyu aydınlatma sorumluluğunda özen ispatı sorumlu tarafa geçer.
2. **Delil türü-eşleştirme:** İçsel bilgi ve zamanlama için emir/işlem kayıtları, içsel bilgiye erişen listesi, KAP açıklama saatleri; fiyat etkisi için fiyat-hacim analizi ve bilirkişi raporu; varlık/sahiplik için MKK ve Takasbank kayıtları; talimat uyuşmazlığında ses/talimat kayıtları kullanılır.
3. **Delil toplama usulü:** Üçüncü kişi/karşı taraftaki belgeler için belge ibrazı (HMK m.219-220), gerekirse delil tespiti (HMK m.400); Kurul incelemesinde idarenin re'sen araştırma yetkisi not edilir. Ara sonuç: hangi delilin nasıl ve kimden temin edileceği netleşir.
4. **Bilirkişi:** Piyasa analizinin uzmanlık gerektirdiği hallerde bilirkişi incelemesi (HMK m.266); raporun görev kapsamı, metodoloji ve dayanak yönünden denetimi yapılır, çelişki ek rapor/itirazla giderilir.
5. **Hukuka uygunluk:** Ses kaydı, içsel belge gibi delillerin hukuka uygun yolla elde edilmesi (HMK m.189/2) değerlendirilir; hukuka aykırı delil dışlanır.

## Çıktı modülleri
- Vakıa-delil eşleştirme matrisi
- Delil toplama/talep listesi (HMK dayanaklarıyla)
- Bilirkişi sorularına yönelik nokta atışı çerçeve
- İspat yükü ve risk notu

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
