---
name: bddk-denetim-yaptirim
description: "Bankanın kuruluş/faaliyet izni, BDDK denetimi, idari para cezası, faaliyet kısıtlaması veya TMSF'ye devir gibi düzenleyici işlemleri değerlendirmek ve bunlara karşı idari yargı yolunu kurmak gerektiğinde kullanılır."
---

# BDDK Düzenlemesi, Denetimi ve İdari Yaptırımlar

## Görev
BDDK'nın düzenleyici/denetleyici işlemini (izin, tedbir, idari para cezası, faaliyet kısıtlaması, TMSF'ye devir) hukuka uygunluk yönünden değerlendirmek ve idari yargı yolunu kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: faaliyet izni başvurusu/reddi, uyarı/tedbir kararı, idari para cezası (5411 m.146 vd.), faaliyet kısıtlaması, faaliyet izninin kaldırılması (m.71) mı?
- İşlemin tebliğ tarihi ve dava açma süresi (İYUK m.7 — 60 gün) doluyor mu?
- Müvekkil banka mı, banka yöneticisi/ortağı mı, üçüncü kişi mi (ehliyet/menfaat)?
- İşlemin sebebi ve dayanağı (hangi 5411 hükmü) açık mı?

## Denetim şeması
1. **İşlem niteliği**: BDDK işlemi icrai bir idari işlemdir; iptal davasına konu olur. Unsur analizi yetki-şekil-sebep-konu-maksat (idari işlem unsurları) üzerinden yapılır.
2. **Dayanak ve ölçülülük**: İşlemin 5411'deki somut dayanağı (örn. kredi sınırı ihlali m.54, sermaye yeterliliği, sır ihlali) ve seçilen yaptırımın ölçülülüğü (Anayasa m.13) denetlenir. İdari para cezalarında 5411 m.146-153 çerçevesi ve usul güvenceleri (savunma alınması) aranır.
3. **Tedbir ve devir**: Faaliyet izninin kaldırılması (m.71) ve TMSF'ye devir ağır sonuçlu işlemlerdir; şartların gerçekleşip gerçekleşmediği ve usul güvenceleri sıkı denetlenir.
4. **Yargı yolu ve süre**: İptal/tam yargı davası İYUK 2577 uyarınca açılır; dava açma süresi kural olarak 60 gün (m.7), yürütmenin durdurulması (m.27) talep edilebilir. Görevli/yetkili mahkeme (Danıştay/idare mahkemesi) işlemin niteliğine göre belirlenir.
5. **İdari/adli ayrım**: Aynı fiil hem idari yaptırıma hem adli yaptırıma (örn. zimmet 5411 m.160) konu olabilir; her yol ayrı yürütülür. Ara sonuç olarak dava türü, süre, yürütmeyi durdurma gerekçesi ve iptal sebeplerini yaz. İçtihat için karararama.danistay.gov.tr esas alınır [doğrulanacak].

## Çıktı modülleri
- İşlem hukuka uygunluk denetim tablosu (unsur unsur).
- İptal sebepleri ve yürütmeyi durdurma gerekçeleri.
- İdari dava dilekçesi iskeleti ve süre takvimi.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
