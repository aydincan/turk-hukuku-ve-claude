---
name: musteri-iletisimi-ve-ihtarname
description: "Karşı tarafa ihtarname gönderilecek, müvekkile risk anlatılacak veya tecavüz iddiasına cevap verilecekse; iletişimi yönetmek ve dengeli, geri tepmeyen ihtarname kurmak için kullanılır."
---

# Müvekkil İletişimi ve İhtarname Yönetimi

## Görev
Marka uyuşmazlığında taraflar arası iletişimi yönetmek: tecavüz edene ihtarname (cease and desist) hazırlamak, müvekkile riski sade dille anlatmak ve gelen ihtarnameye/iddiaya stratejik cevap kurmak. İhtarname hem caydırıcı hem de aşırıya kaçıp haksız tehdit/geri tepme yaratmayacak biçimde dengeli olmalıdır.

## Soğuk başlangıç (intake)
- İhtarname gönderen taraf mı, cevap veren taraf mı?
- Markanın tescil/hak durumu sağlam mı (ihtardan önce teyit edildi mi)?
- Amaç durdurma mı, tazminat mı, sulh/lisans mı?
- Karşı tarafla ticari ilişki sürdürülecek mi?

## Denetim şeması
1. **Hak teyidi (ön kontrol).** İhtar göndermeden önce kendi markanın geçerliliği, kullanım durumu ve kapsamı doğrulanır; zayıf hakka dayalı ihtar karşı dava (menfi tespit) riski doğurur.
2. **İhtarname içeriği.** Hak sahipliği ve tescil bilgisi, tecavüz fiilinin somut tarifi, dayanak maddeler (m.7, m.29), talep (durdurma, ürün toplama, taahhüt), makul süre ve sonuç ihtarı (dava/tazminat). Abartılı/asılsız tehditten kaçınılır.
3. **Müvekkile bilgilendirme.** Riskin gerçekçi anlatımı (kazanma ihtimali, maliyet, süre); en iyi/en kötü senaryo; karar müvekkilindir.
4. **Gelen ihtara cevap.** İddianın dayanağı denetlenir (gerçek tescil mi, kullanmama def'i mümkün mü, dürüst kullanım/önceye dayalı hak savunması var mı); ölçülü cevap veya sulh önerisi.
5. **Delil ve kayıt.** Tüm yazışmalar tarih/teslim kanıtıyla saklanır; ihtar, ileride zamanaşımı/temerrüt ve kusur tartışmasında dayanak olur.
6. **Sulh kapısı.** Koexistence sözleşmesi, lisans veya sınırlı kullanım gibi çözümler erken masaya konur.

## Çıktı modülleri
- İhtarname taslağı ([doldurulacak] yer tutucularla, dayanak madde listeli).
- Müvekkile sade dilli risk-özet notu (senaryolu).
- Gelen ihtara cevap iskeleti ve savunma kontrol listesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
