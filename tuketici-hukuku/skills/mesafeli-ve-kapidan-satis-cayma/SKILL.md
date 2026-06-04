---
name: mesafeli-ve-kapidan-satis-cayma
description: "İnternetten, telefonla veya iş yeri dışında kurulan sözleşmelerde tüketicinin cayma hakkını, 14 günlük süreyi, istisnaları ve iade/geri ödeme yükümlülüklerini değerlendirmek gerektiğinde kullanılır."
---

# Mesafeli ve Kapıdan Satış — Cayma Hakkı

## Görev
İnternet, telefon, posta gibi uzaktan iletişim araçlarıyla (mesafeli) ya da iş yeri dışında (kapıdan) kurulan sözleşmelerde tüketicinin cayma hakkını altlamak; ön bilgilendirme yükümlülüğünü, sürenin başlangıcını, istisnaları ve karşılıklı iade borçlarını belirlemek.

## Soğuk başlangıç (intake)
- Sözleşme nasıl kuruldu (internet sitesi, telefon, kapıda, fuar)?
- Mal mı hizmet mi; teslim/ifa ne zaman gerçekleşti?
- Tüketiciye ön bilgilendirme ve cayma formu verildi mi?
- Tüketici ne zaman cayma iradesini bildirdi ya da bildirmek istiyor?

## Denetim şeması
1. **Nitelendirme:** Mesafeli sözleşme (TKHK m.48) tarafların fiziksel karşı karşıya gelmeksizin uzaktan iletişim araçlarıyla kurduğu sözleşmedir; iş yeri dışında sözleşme (m.47) satıcının olağan iş yeri dışında kurulur. Her ikisinde de cayma rejimi uygulanır.
2. **Ön bilgilendirme:** Satıcı/sağlayıcı, cayma hakkı ve şartları dahil zorunlu bilgileri Yönetmeliğe uygun vermek zorundadır. Bilgilendirme eksikse cayma süresi uzar (kural olarak bir yıl uzayabilir; eksik gideren bildirimden itibaren 14 gün işler).
3. **Cayma süresi:** Kural 14 gün. Mallarda süre teslim günü, hizmetlerde sözleşme günü esas alınarak başlar; tüketici gerekçe göstermeden ve cezai şart ödemeden cayabilir (m.48/4).
4. **İstisnalar (Yönetmelik):** Tüketicinin istekleri doğrultusunda kişiselleştirilen mallar, çabuk bozulan/son kullanma tarihi geçebilecek ürünler, açılınca iadesi sağlık/hijyen açısından uygun olmayan ürünler, dijital içerik (ifaya başlanmışsa) ve benzeri hallerde cayma hakkı yoktur; bu istisna somut olaya uygulanmalıdır.
5. **İade ve geri ödeme:** Cayma bildiriminin ulaşmasından itibaren satıcı 14 gün içinde tüm ödemeleri iade eder; tüketici malı 10 gün içinde geri gönderir. İade masrafına ilişkin bilgilendirme yoksa masraf satıcıya aittir.
6. **Ara sonuç:** Cayma süresi içinde mi, istisna kapsamında mı, geri ödeme yükümlülüğü doğdu mu?

## Çıktı modülleri
- Cayma hakkı değerlendirme notu (süre, istisna).
- Cayma bildirimi taslağı.
- Geri ödeme/iade takvimi.
- Bilgilendirme eksikliğine dayalı argüman seti.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
