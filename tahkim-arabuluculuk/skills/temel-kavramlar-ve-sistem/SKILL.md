---
name: temel-kavramlar-ve-sistem
description: "Tahkim ile arabuluculuk arasındaki temel ayrımı, iç/milletlerarası tahkim ve ihtiyari/dava şartı arabuluculuk rejimlerini ve uygulanacak normu belirlemek gerektiğinde kullanılır; bir uyuşmazlığın hangi alternatif çözüm yoluna oturduğunu tasnif eder."
---

# Temel Kavramlar ve Sistematik

## Görev
Önüne gelen uyuşmazlığı doğru rejime oturtmak: tahkim mi arabuluculuk mu; tahkim ise iç
(HMK) mi milletlerarası (MTK) mi; arabuluculuk ise ihtiyari mi dava şartı mı. Yanlış
nitelendirme süre kaçırma ve usulden ret doğurur; bu beceri rejim haritasını çıkarır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık konusu nedir, tarafların üzerinde serbestçe tasarruf edebileceği bir hak mı?
2. Taraflar arasında tahkim/arabuluculuk anlaşması var mı, varsa lafzı nedir?
3. Yabancılık unsuru var mı (taraf yerleşim yeri, tahkim yeri, edimin yapılacağı yer)?
4. Uyuşmazlık iş, ticari, tüketici, kira gibi dava şartı arabuluculuğa tabi bir alan mı?

## Denetim şeması
1. **Elverişlilik**: Tahkim için **HMK m.408** — taşınmaz üzerindeki ayni haklara veya
   iki tarafın iradesine tabi olmayan işlere ilişkin uyuşmazlıklar tahkime elverişsizdir.
   Arabuluculuk için **HUAK m.1/2** — tarafların serbestçe tasarruf edebileceği işler;
   aile içi şiddet iddiası içeren uyuşmazlıklar elverişsiz. Elverişsizse devlet yargısı.
2. **Tahkim/arabuluculuk ayrımı**: Bağlayıcı bir karar mı (tahkim, **HMK m.407 vd.** /
   **MTK**) yoksa tarafların ürettiği anlaşma mı (arabuluculuk, **HUAK**) isteniyor?
3. **Tahkim alt-rejimi**: Yabancılık unsuru (**MTK m.2**) varsa ve tahkim yeri Türkiye
   ise **4686 MTK**; yoksa **HMK m.407-444**. Tahkim yeri yurt dışıysa kararın tenfizi
   **MÖHUK m.60-63** ve **New York Sözleşmesi**.
4. **Arabuluculuk alt-rejimi**: İş (**7036 m.3**), ticari (**TTK m.5/A**), tüketici
   (**TKHK m.73/A**), kira/komşu/kat mülkiyeti (**HUAK m.18/B**) ise **dava şartı**;
   değilse **ihtiyari** (**HUAK m.13**). Dava şartı ise dava açmadan önce başvuru zorunlu.
5. **Ara sonuç**: Rejim + dayanak madde + yetkili merci + temel süre tek tabloda.

## Çıktı modülleri
- Rejim nitelendirme tablosu (tahkim/arabuluculuk, iç/MTK, ihtiyari/dava şartı).
- Uygulanacak norm listesi (madde atıflı).
- Bir sonraki adım ve süre uyarısı (iptal/dava açma süreleri).

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
