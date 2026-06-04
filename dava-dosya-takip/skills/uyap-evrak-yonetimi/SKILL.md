---
name: uyap-evrak-yonetimi
description: "UYAP üzerinden gelen evrakı, e-tebligatları ve dosya dökümlerini düzenli bir evrak listesine bağlamak, tebliğ tarihlerini ve evrak bütünlüğünü doğrulamak gerektiğinde kullan."
---

# UYAP ve Evrak Yönetimi

## Görev
UYAP'tan gelen evrakı, e-tebligatları ve dosya safahatını numaralı, tarihli ve sayfa referanslı bir evrak listesine dönüştürmek; tebliğ tarihlerini ve evrak bütünlüğünü doğrulayarak süre takvimini beslemek.

## Soğuk başlangıç (intake)
- Elinde UYAP safahat dökümü, e-tebligat kayıtları veya taranmış evrak var mı?
- Hangi evrakın tebliğ tarihi kritik (karar, bilirkişi raporu, dava dilekçesi)?
- Evrak numaralandırılmış/sayfalanmış mı?
- Eksik veya okunaksız belge var mı?

## Denetim şeması
1. Evrak envanteri: her belgeye sıra no, tarih, tür, gönderen/alıcı ve sayfa aralığı ver; safahat dökümüyle eşleştir. Eksik sıra varsa [doldurulacak].
2. Tebliğ doğrulama: e-tebligatta tebliğ tarihi muhatabın elektronik adrese ulaşmasından itibaren beşinci günün sonu sayılır (7201 sayılı Tebligat Kanunu m.7/a); bu tarihi süre takvimine tetikleyici olarak aktar.
3. Bütünlük kontrolü: eki olduğu belirtilen ama dosyada bulunmayan ekler, imzasız/okunaksız sayfalar ayrı not.
4. Süre köprüsü: tebliğ tarihi belirlenen her evrak için tetiklediği süre (cevap, itiraz, kanun yolu) Süre Takvimi becerisine devredilir; çift kayıt önlenir.
5. Ara sonuç: numaralı evrak listesi + doğrulanmış tebliğ tarihleri + eksik/okunaksız liste. Tarihler UYAP kaydından alınır; tahmin edilmez.

## Çıktı modülleri
- Numaralı evrak listesi (no, tarih, tür, taraf, sayfa).
- Tebliğ tarihi doğrulama tablosu.
- Eksik/okunaksız evrak ve eklerin listesi.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
