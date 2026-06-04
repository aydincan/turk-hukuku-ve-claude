---
name: idari-dava-yargi-yolu
description: "Göç İdaresi veya Bakanlık işlemine (ikamet ret, sınır dışı, çalışma izni ret, vatandaşlık ret) karşı dava açılacağında; görevli-yetkili mahkemeyi, süreyi ve yürütmenin durdurulmasını saptamak için kullanılır."
---

# İdari Dava ve Yargı Yolu

## Görev
Göç ve yabancılar alanındaki idari işlemlere karşı doğru yargı yolunu, görevli-yetkili mahkemeyi ve süreyi belirlemek; iptal davası ve yürütmenin durdurulması stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem türü nedir (ikamet, sınır dışı, gözetim, çalışma izni, vatandaşlık)?
2. İşlemin tebliğ/öğrenme tarihi nedir?
3. İdari itiraz/komisyon yolu öngörülmüş mü, tüketildi mi?
4. Yabancı gözetim altında mı, yürütmenin acilen durdurulması gerekiyor mu?

## Denetim şeması
1. **Yargı yolu ayrımı**: Çoğu işlem idari yargı (İYUK m.2 iptal davası). İstisna: idari gözetim kararına karşı **sulh ceza hâkimliği** (YUKK m.57/6); ceza irtibatlı (göçmen kaçakçılığı TCK m.79, insan ticareti m.80) konular adli yargı.
2. **Görev ve yetki**: İdare mahkemesi görevli; sınır dışı kararına karşı dava tek hâkimli idare mahkemesinde görülür (YUKK m.53). Yetki, işlemi tesis eden idarenin/yabancının bulunduğu yer üzerinden İYUK m.32-33 ile belirlenir.
3. **Süreler**: Genel iptal davası süresi İYUK m.7 — 60 gün; sınır dışı kararına karşı YUKK m.53'teki özel kısa süre; idari gözetime karşı m.57'deki süre. Süreler işlemden işleme değişir, her dosyada ayrı hesaplanır.
4. **Dava şartları**: İYUK m.2 — ehliyet ve menfaat (yabancı ya da vekili), kesin/yürütülebilir işlem, süre. İdari merci tecavüzü (m.15) ve idari başvuru yolları kontrol edilir.
5. **Yürütmenin durdurulması**: İYUK m.27 — açıkça hukuka aykırılık + telafisi güç/imkânsız zarar; sınır dışıda zaten dava işlemi durdurabilir, çalışma/ikamette YD ayrıca talep edilir.
**Ara sonuç**: Tek bir görevli-yetkili mahkeme, kesin bir son gün ve YD gerekçesi netleştirilir.

## Çıktı modülleri
- Yargı yolu/görev-yetki/süre karar tablosu.
- İptal davası dilekçesi iskeleti (işlem-vakıa-hukuki sebep-YD-talep).
- Süre takvimi ve kanun yolları (istinaf/temyiz) notu.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
