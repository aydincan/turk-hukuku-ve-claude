---
name: infaz-hakimligi-basvuru
description: "Ceza infaz kurumu işlem ve kararlarına karşı infaz hâkimliğine şikâyet, süre, görev-yetki ve itiraz mercii yolunu kurgulamak gerektiğinde kullanılır."
---

# İnfaz Hâkimliğine Başvuru ve İtiraz

## Görev
İnfaz kurumu idaresinin işlem ve kararlarına ya da infaz savcılığı uygulamalarına karşı 4675 sayılı İnfaz Hâkimliği Kanunu yolunu doğru biçimde işletmek.

## Soğuk başlangıç (intake)
- Hangi işlem/karar şikâyet konusu (disiplin, nakil, infaz hesabı, hak kısıtlaması)?
- İşlem hükümlüye ne zaman tebliğ/uygulanıp öğrenildi (süre için)?
- Hangi infaz kurumu/savcılık yetki alanındasınız (yetki için)?
- Daha önce idareye başvuru yapıldı mı?

## Denetim şeması
1. Görev: 4675 sayılı Kanun m.4 uyarınca infaz kurumu idaresinin işlem ve eylemlerine ilişkin şikâyetleri infaz hâkimliği inceler; ceza yargılamasıyla ilgili olmayan, infaza özgü uyuşmazlıklar bu yola tabidir. Ara sonuç: konu infaz hâkimliği görevinde mi?
2. Süre: şikâyet, işlemin öğrenildiği tarihten itibaren kanunda öngörülen süre içinde (4675 m.5) yapılmalıdır; sürenin kaçırılması başvuruyu usulden reddettirir. İspat yükü: süreye uygunluğu başvurucu, aksini idare ortaya koyar.
3. Yetki: hükümlünün bulunduğu infaz kurumunun yargı çevresindeki infaz hâkimliği yetkilidir.
4. İnceleme ve karar: infaz hâkimi dosya üzerinden inceler, gerekirse bilgi/belge ister; kabul, ret veya işlemin iptaline karar verir (4675 m.6).
5. İtiraz: infaz hâkimliği kararına karşı ağır ceza mahkemesine (CMK itiraz hükümleri çerçevesinde) itiraz yolu açıktır (4675 m.6). Ara sonuç: itiraz mercii ve süresi.
6. İlkesel içtihat: görev sınırı ve süre başlangıcı için karararama.yargitay.gov.tr; tutulma koşulları ihlalinde AYM bireysel başvuru (kararlarbilgibankasi.anayasa.gov.tr). Künye `[doğrulanacak]`.
7. Ara sonuç: görev/yetki/süre üçlüsü + başvuru stratejisi.

## Çıktı modülleri
- Görev-yetki-süre kontrol çizelgesi.
- Şikâyet dayanak listesi.
- İnfaz hâkimliği şikâyet ve itiraz dilekçesi tetiği.

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
