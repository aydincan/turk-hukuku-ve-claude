---
name: temel-kavramlar-ve-sistem
description: "Toplu iş hukukunun çatısını, sendika-TIS-uyusmazlik ucgenini ve 6356 sayili Kanunun yapisini kavramak; bir sorunun toplu mu bireysel mi, hak mi menfaat uyusmazligi mi oldugunu nitelendirmek gerektiginde kullanilir."
---

# Temel Kavramlar ve Sistematik

## Görev
Toplu iş hukukunun üç sütununu (sendika özgürlüğü, toplu iş sözleşmesi, toplu uyuşmazlık) tanıtmak ve önündeki olayı doğru kategoriye yerleştirmek. Yanlış nitelendirme tüm usul yolunu sakatlar; bu beceri ilk süzgeçtir.

## Soğuk başlangıç (intake)
- Taraflar kim: işçi/sendika/işveren/işveren sendikası mı?
- Uyuşmazlık mevcut bir TİS'in yorum-uygulamasından mı (hak), yoksa yeni TİS şartlarından mı (menfaat) doğuyor?
- İşyeri/işletme düzeyi ne; hangi işkolundasınız?
- Yürürlükte TİS var mı, süresi nedir?

## Denetim şeması
1. **Toplu mu bireysel mi?** Talep kişisel işçilik alacağıysa (kıdem, fazla mesai) bireysel iş hukukudur (4857). Örgütlenme, TİS, grev/lokavt söz konusuysa 6356 uygulanır. Sendikal tazminat (6356 m.25) bireysel sonuç doğursa da toplu hukukun güvencesidir.
2. **Hak mı menfaat uyuşmazlığı mı?** TİS m.36 anlamında mevcut sözleşmenin yorumu/ihlali = hak uyuşmazlığı → yargı yolu (İş Mahkemesi). Yeni veya yenilenecek TİS'in içeriği = menfaat uyuşmazlığı → toplu görüşme, arabuluculuk (m.50), grev/lokavt.
3. **Düzey belirleme:** 6356 m.34 — TİS işyeri, işletme (aynı işkolundaki birden çok işyeri) veya grup düzeyinde yapılabilir. Bir işyerinde aynı dönemde yalnızca bir TİS yürürlükte olabilir.
4. **İşkolu:** 6356 m.2 ve İşkolları Yönetmeliği. İşkolu, hem sendika faaliyet alanını hem baraj hesabını belirler; yanlış işkolu yetki tespitini çökertir.
5. **Ara sonuç:** Olay (a) bir TİS'in normatif/borç doğuran hükmünün ihlali mi, (b) örgütlenme/güvence sorunu mu, (c) yeni TİS pazarlığı mı? Cevaba göre ilgili uzmanlık becerisine yönlendirilir.

İspat yükü: sendikal nedenin varlığında işçi iddiayı ortaya koyar, işveren feshin başka geçerli nedene dayandığını ispatlar (6356 m.25/7-8 mantığı).

## Çıktı modülleri
- Nitelendirme notu (toplu/bireysel, hak/menfaat, düzey, işkolu).
- İlgili 6356 madde haritası.
- Sonraki adım ve görevli/yetkili mercii önerisi.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
