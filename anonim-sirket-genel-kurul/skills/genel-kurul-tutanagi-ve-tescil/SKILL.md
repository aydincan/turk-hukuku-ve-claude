---
name: genel-kurul-tutanagi-ve-tescil
description: "Toplanti tutanaginin icerigi, baskanlik divani, Bakanlik temsilcisi imzasi, kararlarin ticaret siciline tescil ve ilani ile internet sitesi yukumlulukleri konusunda taslak veya denetim gerektiginde kullanilir."
---

# Genel Kurul Tutanağı ve Tescil

## Görev
Genel kurul tutanağını mevzuata uygun düzenlemek; tescile tabi kararların ticaret siciline tescil ve ilanı ile internet sitesi yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
1. Toplantı başkanlığı (divan) usulüne uygun oluştu mu; Bakanlık temsilcisi imzası gerekli mi?
2. Hangi kararlar tescile tabi (esas sözleşme değişikliği, sermaye, organ seçimi)?
3. Toplantı fiziki mi, elektronik genel kurul (EGK) mı?
4. Tutanak ve ekleri (hazır bulunanlar listesi, vekâletnameler) tam mı?

## Denetim şeması
1. **Tutanak içeriği:** Tutanak; toplantı yeri-tarihi, hazır pay/oy miktarı, gündem, kararlar, her karara ilişkin oy sonuçları, muhalefet şerhleri ve sorulan soruların cevaplarını içerir; toplantı başkanlığı ve Bakanlık temsilcisi (varsa) tarafından imzalanır (m.422). Eksik/çelişkili tutanak ispatı zayıflatır ve iptal riskine zemin hazırlar.
2. **Muhalefet şerhi:** İptal davası açacak pay sahibinin (toplantıda hazır olup) karara karşı **muhalefetini tutanağa geçirtmiş** olması gerekir (m.446/1-b); bu kayıt davacı sıfatının ön şartıdır. Şerhin açık ve karara özgülenmiş olması önemlidir.
3. **Tescil ve ilan:** Tescile tabi kararlar, toplantıyı izleyen süre içinde ticaret siciline tescil ve TTSG'de ilan ettirilir; YK tescil ödevini yerine getirir. İptal davasında üç aylık süre, kararın alınmasından (kural) işler; tescil tarihi ayrıca ilan ve sicil kaydı için önemlidir.
4. **İnternet sitesi/EGK:** m.1524 kapsamındaki şirketlerde internet sitesine konulması zorunlu içerikler ile pay senetleri borsada işlem gören şirketlerde elektronik genel kurul (EGK) zorunluluğu denetlenir; EGK'de m.1527 ve ilgili yönetmelik uygulanır.
5. **İspat yükü/ara sonuç:** Tutanağın usule uygunluğunu şirket gösterir. Tutanağın imzasız/eksik olması veya zorunlu tescilin yapılmaması, üçüncü kişilere karşı hüküm ve sorumluluk sonuçları doğurur; karar geçerliliğini doğrudan değil, ispat ve aleniyet yönünden etkiler.

## Çıktı modülleri
- Genel kurul tutanağı taslağı (divan + temsilci imza blokları).
- Muhalefet şerhi örnek metni.
- Tescil/ilan ve internet sitesi yükümlülük kontrol listesi.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
