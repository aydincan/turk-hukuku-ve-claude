---
name: uyusmazlik-yargi-yol-gorev
description: "Bir telekom veya internet uyuşmazlığında idari yargı mı, sulh ceza hâkimliği mi, adli/tüketici yargısı mı yoksa BTK başvurusu mu gerektiği, görevli merci ve süre belirsiz olduğunda kullanılır."
---

# Telekom-Bilişim Uyuşmazlıklarında Yargı Yolu ve Görev-Yetki

## Görev
Uyuşmazlığı doğru yola (idari yargı, sulh ceza hâkimliği, adli/tüketici yargısı, BTK idari başvuru) yönlendirmek; görevli/yetkili mercii, başvuru/dava süresini ve acil koruma ihtiyacını net biçimde tespit etmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı: BTK işlemi mi, 5651 içerik tedbiri mi, abonelik/sözleşme mi, veri/gizlilik mi?
2. Müvekkilin sıfatı ve karşı taraf kim (işletmeci, BTK, içerik sahibi, abone)?
3. Tebliğ/öğrenme tarihi nedir; süre işliyor mu?
4. Acil koruma (yürütmenin durdurulması/ihtiyati tedbir/erişim kararı) ihtiyacı var mı?

## Denetim şeması
1. **Yol ayrımı**: BTK düzenleyici/yaptırım işlemi → idari yargı (İYUK). 5651 m.8/8A/9/9A erişim engelleme-içerik çıkarma → sulh ceza hâkimliği (CMK m.267 itiraz). Abonelik/hizmet özel hukuk → adli yargı; gerçek kişi tüketici ise 6502 tüketici hakem heyeti/mahkemesi. Veri ihlali → KVKK Kurulu ve sonrasında idari yargı. Ara sonuç: hangi yol.
2. **İdari yargı**: İYUK m.2 iptal/tam yargı; m.7 süre (kural 60 gün, özel kanun süresi varsa o); m.27 yürütmenin durdurulması (telafisi güç zarar + açık hukuka aykırılık). Görevli yer kural olarak idare mahkemesi.
3. **Sulh ceza hâkimliği**: 5651 erişim engelleme/içerik çıkarma kararı ve itirazı; karar ve itiraz süreleri kısa olduğundan süre disiplini kritiktir.
4. **Adli/tüketici yargı**: Tüketici işleminde parasal sınıra göre hakem heyeti/tüketici mahkemesi; ticari nitelikte asliye ticaret/asliye hukuk; ihtiyati tedbir HMK m.389 vd.
5. **Süre disiplini**: İdari, ceza usulü ve özel hukuk sürelerinin ayrı işlediği; hak düşürücü süre/zamanaşımı karışıklığı en sık hatadır. Süre takvimi sabitlenmeden dilekçe yazılmaz.

## Çıktı modülleri
- Yol ve görevli/yetkili merci tespiti.
- Süre takvimi ve YD/itiraz/ihtiyati tedbir ihtiyaç notu.
- Yanlış mercie başvuru riski uyarısı.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
