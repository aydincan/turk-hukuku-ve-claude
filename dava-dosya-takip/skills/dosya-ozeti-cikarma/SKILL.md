---
name: dosya-ozeti-cikarma
description: "Dağınık bir dava dosyasından künye, talep, taraflar ve aşamayı tek sayfalık yapılandırılmış özete dönüştürmek gerektiğinde; yeni gelen veya devralınan dosyaya hızlı hâkim olmak için kullan."
---

# Dosya Özeti Çıkarma

## Görev
Bir dava dosyasının dağınık evrakını; künye, taraflar, talep, aşama ve sıradaki iş kalemlerini içeren tek sayfalık, Excel'lenebilir bir özete indirgemek. Amaç dosyaya 5 dakikada hâkim olmayı sağlamaktır.

## Soğuk başlangıç (intake)
- Dosya hangi yargı koluna ait: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Elinde hangi evrak var (dava/iddianame, cevap, bilirkişi raporu, tensip, ara karar, UYAP dökümü)?
- Mahkeme ve esas numarası ile tarafların adları belli mi?
- Özet kimin için: hâkim olmak için mi, müvekkile rapor için mi, devir için mi?

## Denetim şeması
1. Künye kalemi: mahkeme adı, esas no, dava türü, dava tarihi, talep sonucu. HMK m.119 zorunlu unsurları (taraflar, talep, vakıalar, hukuki sebep, deliller) dosyada mevcut mu, eksik unsur var mı denetle. Eksikse [doldurulacak].
2. Taraf kalemi: davacı/davalı (ceza dosyasında şüpheli-sanık-müşteki-katılan), vekilleri, tebligat adresleri. Vekâletname dosyada mı; yoksa eksik listesine yaz.
3. Talep ve dayanak: dava dilekçesindeki talep sonucu ile hukuki sebepleri evraktan birebir aktar; yorum ekleme.
4. Aşama tespiti: dilekçeler aşaması mı, ön inceleme (HMK m.137) mi, tahkikat mı, istinaf mı? Son işlem tarihinden çıkar.
5. Ara sonuç: bir sonraki kritik adım (duruşma, cevap süresi, rapora itiraz) ve son günü ile birlikte not et; her veri kaynağına (evrak + tarih + sayfa) bağlanır. Belgede olmayan bilgi uydurulmaz.

## Çıktı modülleri
- Tek sayfalık künye tablosu (mahkeme, esas no, taraflar, talep, aşama).
- Sıradaki iş kalemleri listesi (ne, ne zaman, dayanak madde).
- Eksik evrak ve [doldurulacak] alanları listesi.

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
