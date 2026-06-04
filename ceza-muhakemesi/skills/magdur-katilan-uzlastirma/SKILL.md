---
name: magdur-katilan-uzlastirma
description: "Mağdur/müşteki ve katılanın haklarını, davaya katılmayı, uzlaştırma ve seri/basit muhakeme yollarını değerlendirmek gerektiğinde kullanılır."
---

# Mağdur, Katılan Hakları ve Uzlaştırma

## Görev
Mağdur/müşteki ve katılanın usuli haklarını kullandırmak; uzlaştırma, seri ve basit muhakeme gibi alternatif/hızlandırılmış yolların uygunluğunu değerlendirmek.

## Soğuk başlangıç (intake)
- Müvekkil mağdur/müşteki mi, davaya katılmak istiyor mu?
- Suç uzlaştırma kapsamında mı (CMK m.253 listesi)?
- Zararın giderilmesi ve tazminat talebi var mı?
- Sanık seri muhakeme/basit yargılamaya uygun mu?
- Katılma talebi için uygun aşama hangisi?

## Denetim şeması
1. **Mağdur hakları.** Mağdur ve şikâyetçi; delil toplanmasını isteme, vekille temsil, soruşturma sonucundan bilgi alma haklarına sahiptir (CMK m.234). Mağdura hakları bildirilir.
2. **Davaya katılma.** Suçtan zarar gören, mağdur veya malen sorumlu, kovuşturma evresinde hüküm verilinceye kadar davaya katılabilir (m.237); katılan kanun yollarına başvurabilir (m.242).
3. **Uzlaştırma.** Soruşturulması/kovuşturulması şikâyete bağlı suçlar ile m.253'te sayılan suçlarda uzlaştırma zorunlu olarak denenir; uzlaşma sağlanırsa KYOK/düşme sonucu doğar (m.253-255). Uzlaştırmacı görevlendirilir.
4. **Seri muhakeme.** Savcı, m.250'deki katalog suçlarda şüphelinin müdafi huzurunda kabulü halinde yarı oranında indirimli yaptırım önerir; mahkeme onaylarsa hüküm kurulur.
5. **Basit yargılama.** Mahkeme, üst sınırı 2 yıl veya altı suçlarda duruşma yapmadan dosya üzerinden basit yargılama uygulayabilir (m.251-252); itiraz halinde duruşmalı yargılamaya dönülür.
6. **Ara sonuç.** Uygun yol (katılma/uzlaştırma/seri/basit) seçilir; zarar giderimi ve tazminat stratejisi buna göre kurulur.

## Çıktı modülleri
- Mağdur/katılan hak ve talep listesi.
- Davaya katılma dilekçesi taslağı (m.237 dayanaklı).
- Uzlaştırma/seri muhakeme uygunluk tablosu (m.253/m.250 kapsamı).
- Zarar giderimi ve tazminat yönlendirme notu.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
