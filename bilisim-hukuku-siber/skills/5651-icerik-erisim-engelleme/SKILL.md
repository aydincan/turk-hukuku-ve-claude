---
name: 5651-icerik-erisim-engelleme
description: "İnternette yer alan hukuka aykırı içeriğe karşı içeriğin çıkarılması, erişimin engellenmesi ve özel hayatın korunması başvurularını; içerik/yer/erişim sağlayıcı sorumluluğunu çözmek gerektiğinde kullanılır."
---

# 5651 İçerik Kaldırma ve Erişim Engelleme

## Görev
İnternet ortamındaki hukuka aykırı içeriğe karşı 5651 sayılı Kanun yollarını seçmek; doğru başvuru merciini, usulü ve süreyi belirlemek; sağlayıcı sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
1. İçerik ne ve nerede? (URL, platform, yayın tarihi?)
2. İhlal türü ne? (kişilik hakkı, özel hayat, hakaret, telif, katalog suç?)
3. Önce sağlayıcıya başvuruldu mu, yanıt geldi mi?
4. Acil mi (özel hayat, gecikmesinde sakınca) yoksa olağan mı?

## Denetim şeması
1. **Sağlayıcı sıfatı.** 5651'de içerik, yer, erişim ve toplu kullanım sağlayıcı tanımları (m.2) sorumluluk ve muhatabı belirler. Yer sağlayıcı kural olarak içeriği denetlemekle yükümlü değildir ancak uyar-kaldır yükümlülüğü doğabilir.
2. **İçeriğin çıkarılması / erişimin engellenmesi (m.9).** Kişilik hakkı ihlal edilen kişi önce içerik/yer sağlayıcıya başvurabilir; sonuç alınamazsa sulh ceza hâkimliğine başvurarak içeriğin çıkarılması ve/veya erişimin engellenmesini isteyebilir. Hâkim kararını talepten itibaren kanunda öngörülen kısa sürede (24 saat) verir; karara karşı itiraz yolu açıktır.
3. **Özel hayatın gizliliği (m.9/A).** Özel hayatın gizliliğinin ihlali halinde doğrudan BTK'ya başvurarak erişimin engellenmesi istenebilir; gecikmesinde sakınca bulunan hallerde BTK Başkanı resen tedbir uygulayıp 24 saat içinde hâkim onayına sunar.
4. **Katalog suçlar ve resen engelleme (m.8).** Kanunda sayılan katalog suçlara ilişkin içerikte hâkim/savcı veya BTK kararıyla erişim engellenir. Ölçülülük gereği URL bazlı engelleme tercih edilir; aşırı geniş engelleme hukuka aykırı olabilir.
5. **İspat ve ara sonuç.** İhlal ve içeriğin varlığı başvurucu tarafından belgelenir (ekran görüntüsü + URL + tarih, mümkünse noter/teknik tespit). Doğru yol (m.9 / m.9/A / m.8), mercі ve süre belirlenir.

## Çıktı modülleri
- Yol seçim tablosu (sağlayıcı başvurusu / sulh ceza / BTK).
- İçerik çıkarma-erişim engelleme başvuru/dilekçe taslağı.
- İtiraz dilekçesi iskeleti ve ölçülülük argümanı.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
