---
name: temel-kavramlar-ve-sistem
description: "Konkordato ile yeniden yapılandırmanın temel kavramlarını, türlerini ve iflas/icra rejimi içindeki yerini netleştirmek; hangi kurumun (adi konkordato, mal varlığının terki, finansal yeniden yapılandırma) somut olaya uyduğunu ayırt etmek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Konkordato Sistematiği

## Görev
Mali güçlük içindeki borçlunun durumunu doğru hukuki kuruma yerleştirmek: adi konkordato (İİK m.285 vd.), iflastan sonra konkordato (m.309/A), mal varlığının terki suretiyle konkordato (m.309/h vd.) ve mahkeme dışı finansal yeniden yapılandırma arasından doğru aracı seçmek; konkordatonun vade/tenzilat/karma türlerini ayırmak.

## Soğuk başlangıç (intake)
- Borçlu kim: gerçek kişi tacir, sermaye şirketi, kooperatif mi? Ölçeği ve işkolu?
- Mali durum: borca batık mı, yoksa borca batık olmadan ödeme güçlüğü mü var?
- Talep eden kim: borçlu mu, alacaklı mı (İİK m.285)?
- Halihazırda iflas talebi/iflas davası veya icra takipleri var mı?
- Amaç: işletmenin sürdürülmesi mi, alacaklıların iflasa göre daha iyi tatmini mi?

## Denetim şeması
1. **Kurum seçimi.** İflasın ertelenmesi 7101 sayılı Kanunla kaldırıldı; mali güçlükte başat araç konkordatodur (İİK m.285). Mahkeme denetimi istenmiyorsa finansal yeniden yapılandırma (5411 s.K. Geçici m.32 / FYY çerçeve anlaşmaları) değerlendirilir.
2. **Tür tayini.** Tenzilat konkordatosu (alacaktan vazgeçme), vade konkordatosu (ödeme süresi tanıma) veya karma. Proje ekonomisi buna göre kurgulanır.
3. **Borca batıklık ayrımı.** Borca batıklık varsa TTK m.376 ve İİK m.179 ile ilişki kurulur; konkordato talebi iflasa alternatif olarak öne çıkar.
4. **Ehliyet.** Borçlu her hâlde; alacaklı ancak iflas talep edebilecek nitelikteyse talep edebilir (m.285/2). İspat yükü: talep edenin mali güçlük/alacak iddiasını belgelemesi gerekir.
5. **Ara sonuç.** Kurum, tür ve görevli mahkeme (Asliye Ticaret Mahkemesi) tespit edilir; sonraki beceriye (denetim şeması ve mühlet) köprü kurulur.

## Çıktı modülleri
- Kurum ve tür tespiti notu (gerekçeli).
- Konkordato vs. finansal yeniden yapılandırma karşılaştırma tablosu.
- Talep ehliyeti ve görev-yetki özeti.
- Sonraki adım için yol haritası.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
