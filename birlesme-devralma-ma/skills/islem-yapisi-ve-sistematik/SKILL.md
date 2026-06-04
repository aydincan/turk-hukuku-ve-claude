---
name: islem-yapisi-ve-sistematik
description: "Bir M&A işleminin temel iskeletini kurmak, pay devri ile varlık devri ile teknik birleşme arasında seçim yapmak, taraf-hedef-bedel-onay haritasını çıkarmak ve hangi norm kümelerinin devreye gireceğini belirlemek için kullanılır."
---

# İşlem Yapısı ve M&A Sistematiği

## Görev
İşlemin hukuki gerçekleştirme biçimini (pay devri / varlık devri / TTK m.134 teknik birleşme / TTK m.159 bölünme) ve buna bağlı norm setini belirlemek; taraf-hedef-bedel-onay haritasını çıkarmak.

## Soğuk başlangıç (intake)
- Hedef hangi tür şirket (AŞ mı, limited mi)? Halka açık mı?
- Müvekkil alıcı mı, satıcı mı; payların tamamı mı azınlık mı devrediliyor?
- Bedel yapısı nedir (peşin / vadeli / earn-out / escrow)?
- Düzenlenmiş sektör (banka, enerji, sigorta, telekom) ve rekabet eşiği söz konusu mu?

## Denetim şeması
1. **Yapı tercihi**: Pay devri sözleşmesel ve hızlıdır, hedefin tüm pasifi (gizli borçlar dahil) devralanla birlikte kalır → beyan-tekeffül ve indemnity kritiktir. Varlık devrinde TBK m.202 uyarınca devralan, devraldığı malvarlığının borçlarından devredenle **müteselsilen** sorumlu olur (iki yıl); bu nedenle borç süzgeci gerekir.
2. **Teknik birleşme** (TTK m.136): Devralma veya yeni kuruluş yoluyla; külli halefiyet, birleşme sözleşmesi (TTK m.145), birleşme raporu (TTK m.147), genel kurul onayı (TTK m.151) ve alacaklıların korunması (TTK m.157) zorunludur.
3. **Şekil**: AŞ nama yazılı pay devri ciro + zilyetlik devri ve pay defteri kaydı (TTK m.490, m.499); limited pay devri **yazılı + noter onaylı** sözleşme ve genel kurul onayı (TTK m.595).
4. **Devir engelleri**: Esas sözleşmede bağlam (TTK m.491-492), ön alım hakkı, sözleşmelerde change-of-control klozları taranır.
5. **Ara sonuç**: Hangi izinlerin (rekabet, sektörel, ortaklık onayı) kapanış şartı olacağı ve hangi belgelerin (SPA, SHA, disclosure) hazırlanacağı belirlenir.

## Çıktı modülleri
- İşlem yapısı karar notu (pay/varlık/birleşme gerekçeli karşılaştırma)
- Taraf-hedef-bedel-onay haritası tablosu
- Gerekli onay ve şekil şartları kontrol listesi
- Yol haritası (signing → CP → closing → post-closing) takvimi

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
