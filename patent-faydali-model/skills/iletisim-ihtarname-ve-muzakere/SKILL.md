---
name: iletisim-ihtarname-ve-muzakere
description: "Patent uyuşmazlığında ihtarname gönderilirken/yanıtlanırken, lisans veya sulh müzakeresi yürütülürken ve müvekkile risk anlatılırken kullanılır; dava öncesi iletişim ve uzlaşma yönetimi için temel beceridir."
---

# İhtarname, Müzakere ve Taraf İletişimi

## Görev
Patent/faydalı model uyuşmazlığında ihtarname üretmek/yanıtlamak, lisans veya sulh müzakeresini kurgulamak ve müvekkili risk ile seçenekler konusunda doğru bilgilendirmek.

## Soğuk başlangıç (intake)
1. İletişimin amacı ne: tecavüzü durdurma talebi, lisans teklifi, sulh, ihtarnameye cevap?
2. Hakkın geçerliliği ve kapsamı ne kadar sağlam; karşı taraf hükümsüzlük ileri sürebilir mi?
3. Karşı tarafın ticari konumu, iyiniyeti ve müzakereye yatkınlığı ne?
4. Süre/zamanaşımı baskısı ve delil tespiti ihtiyacı var mı?

## Denetim şeması
1. **İhtarnamenin amacı ve içeriği.** Tecavüz iddiasını dayandığı patenti, istem(leri) ve fiili somut belirten, durdurma/giderme ve tazminat talebini içeren; makul süre tanıyan ihtarname kur. Aşırı/dayanaksız tehdit, karşı tarafın menfi tespit davası açma veya haksız rekabet iddiası riskini doğurabilir — bu yüzden iddiayı kapsam analizine yasla.
2. **İspat ve delil hazırlığı.** İhtardan önce/sonra delil tespiti (HMK m.400 vd.) ve numune temini ile fiili durumu sabitle; ihtarname ileride kötüniyet/tazminat başlangıcı bakımından önem taşır.
3. **İhtarnameye cevap.** Muhatap isen: hakkın geçerliliği, kapsam dışılık, önceki kullanım (SMK m.87), tüketilme (SMK m.152) gibi savunmaları değerlendir; süreyi yönet, gerekirse menfi tespit davasını planla.
4. **Müzakere çerçevesi.** Lisans (kapsam, bedel, alan), sulh (geçmiş kullanım + ileriye dönük lisans), stok eritme, design-around taahhüdü seçeneklerini masaya koy; BATNA olarak dava ve ihtiyati tedbir senaryosunu hesapla.
5. **Müvekkil bilgilendirmesi.** Hakkın gücü, hükümsüzlük riski, maliyet ve süre konusunda gerçekçi tablo sun; karar müvekkilindir, hukuki seçenekleri ve olası sonuçlarını yalın anlat.

## Çıktı modülleri
- İhtarname taslağı iskeleti (dayanak istem + fiil + talep + süre) [doldurulacak yer tutucularıyla].
- İhtarnameye cevap savunma envanteri.
- Müzakere seçenek matrisi (lisans/sulh/design-around) ve BATNA.
- Müvekkil bilgilendirme notu (risk-maliyet-seçenek).

## Plugin bağlamı

Bu beceri `patent-faydali-model` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
