---
name: is-kazasi-meslek-hastaligi-tespit
description: "Bir olayın iş kazası veya meslek hastalığı sayılıp sayılmadığını belirlemek, bildirim yükümlülüklerini ve sürelerini denetlemek için kullanılır."
---

# İş Kazası ve Meslek Hastalığı Tespiti ve Bildirim

## Görev
Bir olayı iş kazası (5510 m.13) veya meslek hastalığı (5510 m.14) olarak nitelendirmek, bildirim yükümlülüklerini (6331 m.14, 5510 m.13/2) ve sürelerini denetlemek; eksik/geç bildirimin sonuçlarını çıkarmak.

## Soğuk başlangıç (intake)
- Olay nerede, ne zaman, hangi koşulda gerçekleşti; çalışan o sırada işveren otoritesi altında mıydı?
- Yaralanma/ölüm var mı; sağlık raporu/epikriz mevcut mu?
- SGK'ya ve kolluğa bildirim yapıldı mı, tarihleri ne?
- Meslek hastalığı iddiası varsa maruziyet ve yükümlülük süresi nedir?

## Denetim şeması
1. **İş kazası unsurları (5510 m.13):** Sigortalının (a) işyerinde, (b) işveren tarafından yürütülen iş nedeniyle, (c) işveren tarafından görevle başka yere gönderilmesi sırasında, (d) emziren kadının çocuğuna süt verme zamanlarında, (e) işverence sağlanan taşıtla gidiş-gelişte bedence/ruhça zarara uğraması. Bu hallerden biri varsa iş kazasıdır; illiyet geniş yorumlanır.
2. **Meslek hastalığı (5510 m.14):** İşin niteliğine bağlı maruziyet sonucu hastalık; yükümlülük süresi ve maruziyet süresi listeye göre değerlendirilir, gerekirse Meslek Hastalıkları/SGK Sağlık Kurulu raporu.
3. **Bildirim (6331 m.14, 5510 m.13/2):** İşveren kazayı kazadan sonraki üç iş günü içinde SGK'ya bildirir; ölümlü/ağır kazalarda kolluğa derhal haber verme. İSG kayıt yükümlülüğü ve ramak kala olaylarının kaydı (m.14/2) ayrıca denetlenir.
4. **İspat:** Olayın iş kazası olduğunu kural olarak iddia eden (çalışan/hak sahibi) ortaya koyar; SGK tespiti yoksa iş mahkemesinde tespit davası açılabilir. **Ara sonuç:** Nitelendirme + bildirim durumu netleştir; geç bildirim idari cezaya ve SGK'ya doğan masrafların işverene rücuuna zemin olur.

## Çıktı modülleri
- İş kazası/meslek hastalığı nitelendirme notu (madde altlamalı).
- Bildirim takvimi ve eksiklik raporu.
- Gerekirse tespit davası yol haritası.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
