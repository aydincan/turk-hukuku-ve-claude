---
name: sure-takvimi-ve-zamanasimi
description: "Cevap, itiraz, istinaf, temyiz gibi usul süreleri ile zamanaşımı/hak düşürücü sürelerin son günlerini dayanak maddeyle hesaplayıp takvime bağlamak gerektiğinde kullan."
---

# Süre Takvimi ve Zamanaşımı

## Görev
Dosyadaki tüm usul sürelerini ve maddi zamanaşımı/hak düşürücü süreleri başlangıç olayı, dayanak madde ve son günüyle birlikte takvime dönüştürmek; süre kaçırma riskini sıfırlamak.

## Soğuk başlangıç (intake)
- Hangi yargı kolu: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Süreyi başlatan olay ve tarihi belli mi (tebligat, öğrenme, karar tarihi)?
- Hangi süreler işliyor (cevap, itiraz, kanun yolu, bilirkişiye itiraz)?
- Adli tatil veya resmî tatil araya giriyor mu?

## Denetim şeması
1. Süre kalemini tanımla ve dayanağını yaz: cevap dilekçesi 2 hafta (HMK m.127); bilirkişi raporuna itiraz 2 hafta (HMK m.281); hukukta istinaf 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361). Cezada itiraz 7 gün (CMK m.268), istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291). İcrada itiraz 7 gün (İİK m.62), kambiyoda 5 gün (İİK m.168); itirazın iptali 1 yıl (İİK m.67). İdaride 60 gün (İYUK m.7).
2. Başlangıç olayını sabitle: süre kural olarak tebliğ/öğrenme ile başlar; tarihi evraktan al, yoksa [doldurulacak].
3. Tatil ve son gün: adli tatilin (HMK m.102-104) süreye etkisini ve son günün tatile rastlamasını (uzama) kontrol et. Hesabı dayanak maddeyle göster.
4. Zamanaşımı/hak düşürücü süre: maddi hukuk süresini ilgili alanın kanunundan al (ör. genel zamanaşımı TBK m.146 on yıl; haksız fiil TBK m.72). Bu süreler usul süresinden ayrı izlenir.
5. Ara sonuç: her süre için son gün ve risk seviyesi; hesabın kullanıcıca doğrulanması istenir. Tarih uydurulmaz.

## Çıktı modülleri
- Süre-başlangıç-dayanak madde-son gün-durum kolonlu takvim tablosu.
- Yaklaşan/kritik süreler uyarı listesi.
- Hesap doğrulama notu ([doğrulanacak] son günler).

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
