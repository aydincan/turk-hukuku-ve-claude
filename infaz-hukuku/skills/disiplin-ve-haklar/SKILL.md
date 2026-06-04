---
name: disiplin-ve-haklar
description: "Ceza infaz kurumunda verilen disiplin cezalarını, savunma hakkını, disiplin cezasının kaldırılmasını ve hükümlü haklarına yönelik ihlalleri denetlemek gerektiğinde kullanılır."
---

# İnfaz Disiplin Cezaları ve Hükümlü Hakları

## Görev
Kurum içi disiplin cezalarının hukuka uygunluğunu, savunma hakkına riayeti ve hükümlü haklarına müdahaleleri 5275 disiplin hükümleri çerçevesinde denetlemek.

## Soğuk başlangıç (intake)
- Hangi disiplin cezası verildi (kınama, ziyaret/haberleşme kısıtlama, hücre vb.)?
- Savunma alındı mı; disiplin kurulu kararı gerekçeli mi?
- Eylem hangi disiplin fiiline karşılık geliyor?
- Cezanın koşullu salıverilmeye/iyi hâle etkisi var mı?

## Denetim şeması
1. Disiplin cezası kataloğu: 5275 m.38-44 kınamadan hücreye kadar dereceli cezaları, m.37 ölçülülük ilkesini düzenler; kıyas yasağına benzer biçimde fiil-ceza eşleşmesi denetlenir. Ara sonuç: ceza türü mevzuata uygun mu?
2. Usul güvenceleri: disiplin soruşturmasında savunma hakkı tanınması, disiplin kurulu kararının gerekçeli olması zorunludur (5275 m.47). İspat yükü: eylemin sübutunu idare ortaya koymalıdır.
3. Çocuk ve özel durumlar: çocuk hükümlülerde farklı disiplin rejimi (5275 m.46) ve özel koruma.
4. Cezanın kaldırılması/ortadan kalkması: iyi hâl ve süre şartıyla disiplin cezalarının kaldırılması (5275 m.48); bu, koşullu salıverilme değerlendirmesini etkiler.
5. Hak ihlali boyutu: ziyaret, haberleşme, sağlık ve insan onuruna uygun tutulma haklarına orantısız müdahale, AYM bireysel başvuru konusu olabilir (kararlarbilgibankasi.anayasa.gov.tr).
6. İtiraz: disiplin cezasına karşı infaz hâkimliği ve itiraz mercii yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
7. Ara sonuç: cezanın hukuka uygunluğu + itiraz dayanakları.

## Çıktı modülleri
- Disiplin cezası hukuka uygunluk çizelgesi.
- Savunma/usul eksiği listesi.
- İnfaz hâkimliğine şikâyet dilekçesi tetiği.

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
