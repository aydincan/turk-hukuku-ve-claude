---
name: is-guvencesi-ve-ise-iade
description: "İşçinin iş güvencesi kapsamında olup olmadığını ve işe iade davasının şartları, süresi, arabuluculuk ve sonuçlarını çözmek gerektiğinde; geçersiz feshe karşı işe iade ve boşta geçen süre/işe başlatmama tazminatını hesaplamak için kullan."
---

# İş Güvencesi ve İşe İade Davası

## Görev
İş K. m.18-21 kapsamında iş güvencesi şartlarını denetlemek, işe iade sürecini (arabuluculuk + dava) kurmak ve geçersiz fesih sonuçlarını (işe başlatma ya da tazminat) hesaplamak.

## Soğuk başlangıç (intake)
1. İşyerinde kaç işçi çalışıyor; işverenin aynı işkolundaki diğer işyerleri var mı?
2. İşçinin kıdemi en az 6 ay mı; işveren vekili konumunda mı (m.18/son)?
3. Fesih bildirimi ne zaman tebliğ edildi?
4. Fesih yazılı ve gerekçeli mi?

## Denetim şeması
1. **Kapsam şartları (m.18):** Otuz veya daha fazla işçi, en az 6 ay kıdem, belirsiz süreli iş sözleşmesi. İşveren vekili ve yardımcıları (işletmenin bütününü sevk/yönetenler ile işyerinin tamamını yöneten ve işçi alıp çıkarma yetkisi olanlar) kapsam dışı. İşçi sayısı eşiği işverenin aynı işkolundaki tüm işyerleri birlikte sayılarak belirlenir.
2. **Geçerli sebep yokluğu:** Fesih geçerli sebebe dayanmıyorsa veya sebep ispatlanamıyorsa fesih geçersizdir. İspat yükü işverende (m.20/2).
3. **Süre ve usul:**
   - Arabuluculuğa başvuru: Fesih bildiriminin tebliğinden itibaren **bir ay** içinde arabulucuya başvuru zorunlu (dava şartı — 7036 m.3, m.11 atfı).
   - Anlaşamama tutanağından itibaren **iki hafta** içinde işe iade davası açılır.
4. **Hüküm (m.21):** Mahkeme feshin geçersizliğine karar verirse:
   - Boşta geçen süre ücreti: en çok **4 aya** kadar ücret ve haklar.
   - İşe başlatmama tazminatı: işçinin kıdemine göre **4-8 aylık** ücret (mahkeme takdir eder).
   - İşçi, kesinleşen kararın tebliğinden itibaren **10 işgünü** içinde işe başlamak için işverene başvurmalı; başvurmazsa fesih geçerli sayılır.
   - İşveren bir ay içinde işe başlatmazsa tazminat muaccel olur.

## Çıktı modülleri
- Kapsam şartları kontrol listesi (var/yok).
- Süre takvimi (1 ay arabuluculuk + 2 hafta dava + 10 işgünü başvuru).
- Olası hüküm: boşta geçen + başlatmama tazminatı tahmini aralığı.
- Stratejik not: işe iade mi, alacak davası mı tercih edilmeli.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
