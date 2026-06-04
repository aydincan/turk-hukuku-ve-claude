---
name: sureler-ve-hak-dusurucu-takvim
description: "İhale sürecindeki tüm başvuru ve dava sürelerini (şikâyet, itirazen şikâyet, iptal davası, doküman itirazı) doğru hesaplamak ve hak kaybını önlemek için kullanılacak süre yönetimi becerisidir."
---

# Süreler ve Hak Düşürücü Takvim

## Görev
İhale sürecindeki başvuru ve dava sürelerini doğru başlangıç anına bağlayarak hesaplamak; hak düşürücü nitelikteki süreleri öne çıkararak kayıp riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Hangi işleme karşı süre işliyor (doküman, kesinleşen karar, KİK kararı, yasaklama)?
2. Başlangıç anı: tebliğ tarihi mi, öğrenme/öğrenilmesi gereken tarih mi?
3. İdareye şikâyet yapıldı mı; idare cevap verdi mi/sustu mu?
4. Sözleşme imzalandı mı (şikâyet süresini etkiler)?

## Denetim şeması
1. **Doküman itirazı:** İhale dokümanına yönelik şikâyet, ihale tarihinden makul süre öncesine kadar (ilgili Yönetmelikteki süre, kural olarak ihale tarihinden 3 iş günü öncesine kadar) yapılır.
2. **Şikâyet (4734 m.55):** Hukuka aykırılığın farkına varıldığı/varılması gereken tarihten itibaren 10 gün. İdare 10 gün içinde karar verir.
3. **İtirazen şikâyet (4734 m.56):** İdare kararının tebliğinden veya 10 günlük sürede karar verilmemesinden itibaren 10 gün içinde KİK'e başvuru. Başvuru bedeli yatırılır.
4. **İptal davası (KİK kararı):** KİK kararının tebliğinden itibaren 30 gün içinde Ankara idare mahkemesinde iptal davası (2577 İYUK m.7).
5. **Yasaklama kararı:** Resmî Gazete'de yayım tarihi esas alınarak idare mahkemesinde 60 gün içinde iptal davası (genel İYUK süresi; özel düzenleme yoksa).
6. **Ara sonuç:** Süreler hak düşürücüdür; geçirilmesi başvurunun/davanın süre yönünden reddine yol açar. Tatil günleri ve tebligat kurallarına dikkat edilir. Tüm güncel gün/tutarlar `[mevzuat tarihi itibarıyla doğrulanacak]` teyit edilir.

İspat yükü: Süreyi koruyan taraf başvuru/tebliğ tarihini belgeyle ortaya koyar.

## Çıktı modülleri
- Olay bazlı geri sayım takvimi (başlangıç anı + süre + son gün).
- Kritik süre uyarı listesi (kırmızı/sarı).
- Tebligat ve tatil günü düzeltme notu.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
