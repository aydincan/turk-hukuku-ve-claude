---
name: enerji-uyusmazlik-yargi-yol
description: "Bir enerji uyuşmazlığında idari yargı mı adli yargı mı tahkim mi gerektiği, görevli mahkeme, dava açma süresi ve yürütmenin durdurulması belirsiz olduğunda kullanılır."
---

# Enerji Uyuşmazlıklarında Yargı Yolu ve Görev-Yetki

## Görev
Enerji uyuşmazlığını doğru yargı koluna, görevli/yetkili mahkemeye veya tahkime yönlendirmek; dava açma süresini ve yürütmeyi durdurma ihtiyacını net biçimde tespit etmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı EPDK işlemi mi, sözleşme mi, haksız fiil/alacak mı?
2. İlgili sözleşmede tahkim/yetki şartı var mı?
3. Tebliğ/öğrenme tarihi nedir; süre işliyor mu?
4. Acil koruma (yürütmenin durdurulması/ihtiyati tedbir) ihtiyacı var mı?

## Denetim şeması
1. **Yargı kolu ayrımı**: EPDK/idare işlemi → idari yargı (İYUK). Tarafların özel hukuk ilişkisinden doğan alacak/sözleşme → adli yargı; tahkim şartı varsa tahkim. Ara sonuç: hangi yargı kolu.
2. **İdari yargı**: İYUK m.2 iptal/tam yargı; m.7 dava açma süresi (kural 60 gün, özel kanun süresi varsa o); m.27 yürütmenin durdurulması (telafisi güç zarar + açık hukuka aykırılık). Görevli yer kural olarak idare mahkemesi; konuya göre Danıştay ilk derece.
3. **Adli yargı**: Ticari nitelikli enerji sözleşmelerinde asliye ticaret mahkemesi (TTK m.4-5); HMK m.6 yetki ve sözleşmedeki yetki şartı. İhtiyati tedbir HMK m.389 vd.
4. **Tahkim**: Geçerli tahkim şartında (HMK m.412 / 4686) hakem yargılaması; hakem kararının iptali (HMK m.439) ve milletlerarası unsurlu işlemde tenfiz.
5. **Süre disiplini**: İdari ve adli sürelerin ayrı işlediği, hak düşürücü süre/zamanaşımı karışıklığı en sık hata; süre takvimi sabitlenmeden dilekçe yazılmaz.

## Çıktı modülleri
- Yargı yolu ve görevli/yetkili merci tespiti.
- Süre takvimi ve YD/ihtiyati tedbir ihtiyaç notu.
- Yanlış mercie başvuru riski uyarısı.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
