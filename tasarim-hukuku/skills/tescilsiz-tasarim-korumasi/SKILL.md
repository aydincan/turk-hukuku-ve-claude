---
name: tescilsiz-tasarim-korumasi
description: "Kamuya sunmadan doğan 3 yıllık tescilsiz koruma kapsamının, taklit/kopyalama unsurunun ve ispat sorununun değerlendirilmesi; tescil yokken hızlı tüketilen ürünler veya fuarda ilk kez sergilenen tasarımlar için koruma arandığında kullanılır."
---

# Tescilsiz Tasarım Koruması

## Görev
Tescil olmadan, yalnızca kamuya sunma ile doğan korumayı işletmek: koruma süresini, kapsamını (taklit/kopyalamaya karşı) ve kamuya sunmanın ispatını yönetmek. Moda, mobilya, ambalaj gibi hızlı yenilenen sektörlerde kritiktir.

## Soğuk başlangıç (intake)
1. Tasarım kamuya ilk kez ne zaman, nerede, hangi belgeyle sunuldu (fuar fotoğrafı, katalog, web arşivi, fatura)?
2. Bu sunma Türkiye'de ilgili sektör çevrelerince makul şekilde bilinebilir nitelikte miydi (SMK m.57/3 anlamında)?
3. Karşı tarafın ürünü, korunan tasarımı bilerek/kopyalayarak mı üretti, yoksa bağımsız tasarım mı?
4. 3 yıllık süre dolmuş mu?

## Denetim şeması
1. Korumanın doğumu (SMK m.55/4): Tescilsiz tasarım, Türkiye'de kamuya ilk sunulduğu tarihte korunmaya başlar. "Kamuya sunma" SMK m.57/3'e göre tanımlanır (yayım, sergileme, ticarette kullanım vb.).
2. Süre (SMK m.69/2): Kamuya ilk sunma tarihinden itibaren 3 yıl. Bu süre uzatılamaz; süre dolmuşsa koruma talebi reddedilir.
3. Koruma kapsamı (SMK m.57/2, m.59): Tescilsiz tasarım sadece, korunan tasarımın aynısının veya genel izlenim itibarıyla ondan ayırt edilemeyen bir tasarımın "kopyalanması/taklidi" sonucu kullanımına karşı koruma sağlar. Bağımsız yaratım tecavüz değildir.
4. Kopyalama unsuru: Tescilliden farklı olarak, davalının önceki tasarımı bilerek kullandığı (kopyaladığı) ortaya konmalıdır. Benzerliğin yüksekliği ve davalının tasarıma erişim imkânı kopyalama karinesini güçlendirir.
5. Yenilik/ayırt edicilik: Tescilsiz korumanın da geçerli olması için tasarım yine SMK m.56-57 şartlarını taşımalıdır; karşı taraf bunların yokluğunu def'i olarak ileri sürebilir.
6. Ara sonuç: Süre içinde miyiz, kamuya sunma ispatlanabilir mi, kopyalama unsuru var mı — üçü birlikte karşılanmıyorsa koruma işlemez.

## Çıktı modülleri
- Kamuya sunma delil dosyası (tarih damgalı görsel, fuar/katalog kaydı, web arşivi).
- 3 yıllık süre takvimi ve kalan süre.
- Kopyalama/bağımsız yaratım değerlendirme notu ve strateji.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
