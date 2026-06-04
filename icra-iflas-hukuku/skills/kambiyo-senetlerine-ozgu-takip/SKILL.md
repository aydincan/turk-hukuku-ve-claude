---
name: kambiyo-senetlerine-ozgu-takip
description: "Çek, bono veya poliçeye dayalı haciz/iflas yoluyla takip kurmak, ödeme emrine 5 gün içinde itiraz veya şikâyet etmek ve kambiyo vasfı denetimini yapmak gerektiğinde kullanılır."
---

# Kambiyo Senetlerine Özgü Takip

## Görev
Çek/bono/poliçeye dayanarak kambiyo senetlerine özgü haciz yolu (m.167 vd.) ile takip yapmak; senedin kambiyo vasfını ve takip yetkisini denetlemek; borçlu tarafında borca/imzaya itiraz ve şikâyet yollarını kullanmak.

## Soğuk başlangıç (intake)
- Senet çek mi, bono mu, poliçe mi; TTK'daki zorunlu unsurları (TTK m.671, m.776, m.692; çek için 5941 s.K. ve TTK m.780) taşıyor mu?
- Alacaklı meşru hamil mi; ciro silsilesi düzgün mü?
- Ödeme emri tebliğ tarihi nedir (itiraz/şikâyet 5 gün)?
- Çek için ibraz süresi/karşılıksız işlemi yapıldı mı?

## Denetim şeması
1. **Kambiyo vasfı (m.170/a)**: Senedin kambiyo senedi sayılması için zorunlu şekil şartları aranır; eksikse senet kambiyo vasfını taşımaz, takip iptal edilir. Bu husus süresiz şikâyet kapsamında değerlendirilir.
2. **Takip talebi ve ödeme emri (m.168)**: Borçluya 5 gün içinde borca/imzaya itiraz, 10 gün içinde ödeme veya mal beyanı bildirilir; itiraz icra mahkemesine yapılır ve kural olarak **takibi durdurmaz** (m.169, m.169/a — ancak teminatla durdurma mümkündür).
3. **İmzaya itiraz (m.170)**: 5 gün içinde icra mahkemesine; mahkeme inceleme yapar, haksız çıkan taraf aleyhine tazminat ve para cezası gündeme gelir.
4. **Borca itiraz (m.169, m.169/a)**: İtirazın esası icra mahkemesinde incelenir; itiraz yerinde görülürse takip durur.
5. **Yetki ve hamillik**: Senet bedeli, vade, faiz başlangıcı (TTK) ve hamilin müracaat hakkı (protesto/ibraz şartları) denetlenir.
6. **Ara sonuç**: Senedin geçerliliği, takibin durup durmayacağı ve teminat/tazminat riski belirlenir.

## Çıktı modülleri
- Senet vasfı kontrol listesi (zorunlu unsurlar + ciro).
- Kambiyo takip talebi taslağı / itiraz dilekçesi.
- Teminatla durdurma ve tazminat risk notu.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
