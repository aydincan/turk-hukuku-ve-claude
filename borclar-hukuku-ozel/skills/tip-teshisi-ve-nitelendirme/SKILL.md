---
name: tip-teshisi-ve-nitelendirme
description: "Eldeki sözleşmenin hangi isimli sözleşme tipine girdiğini, karma/atipik olup olmadığını ve hangi hükmün uygulanacağını belirlemek gerektiğinde; uyuşmazlığa doğru kanun çerçevesini oturtmak için ilk adımda kullanılır."
---

# Sözleşme Tipinin Teşhisi ve Nitelendirme

## Görev
Tarafların verdiği ada bakmaksızın, edimlerin gerçek niteliğine göre sözleşmeyi TBK Özel Hükümler'deki bir tipe oturtmak; karma/atipik ise uygulanacak hüküm rejimini belirlemek. Yanlış nitelendirme, süreleri ve seçimlik hakları kökünden değiştirir.

## Soğuk başlangıç (intake)
- Edimler neler: bir şeyin mülkiyeti mi devrediliyor, kullanımı mı bırakılıyor, bir iş/sonuç mu taahhüt ediliyor, bir işin görülmesi mi üstleniliyor?
- Bedel var mı, varsa karşılığı ne (satış mı bağışlama mı)?
- Sonuç mu yoksa özenli çaba mı borçlanılıyor (eser ↔ vekâlet ayrımı)?
- Sözleşmenin adı ne; metindeki ad ile edimler örtüşüyor mu?

## Denetim şeması
1. **Baskın edimi belirle.** Mülkiyet devri + bedel → satış (TBK m.207). Kullanımın bedel karşılığı bırakılması → kira (m.299). Bir sonuç/eser taahhüdü → eser (m.470). Bir işin görülmesi/sonuç garantisi olmadan → vekâlet (m.502). Karşılıksız kazandırma → bağışlama (m.285).
2. **Eser/vekâlet sınırını çiz.** Sonuç taahhüdü ve eserin ayıpsız teslimi riski yüklenicideyse eser; sadece özenli edim borçlanılıyorsa vekâlet (m.506 özen). İnşaat, yazılım geliştirme, tadilat tipik eserdir.
3. **Satış/eser sınırı.** Hazır malın devri satış; sipariş üzerine imal + teslim genelde eser (m.470). Misli şey imalinde baskın görüşe göre eser hükümleri.
4. **Karma/atipik tespit et.** Birden çok tipin edimleri birleşiyorsa (ör. kapı karşılığı bakım + kullanım) baskın edime göre temel rejim, yan edimlere kıyasen ilgili hükümler; TBK m.646 ve Genel Hükümler tamamlayıcı.
5. **Emredici taban kontrolü.** Tüketici tarafı varsa 6502 TKHK, konut/çatılı işyeri kirası ise TBK m.339 vd. emredici hükümleri tipe ekle.
6. **Ara sonuç:** Uygulanacak madde bloğu, görevli mahkeme ve süre rejimi netleşir; ispat yükü genel kural TMK m.6 ile tipe özgü ihbar yüklerine göre dağıtılır.

## Çıktı modülleri
- Nitelendirme notu (tip + dayanak madde + gerekçe).
- Karma sözleşmede edim-rejim eşleme tablosu.
- Yanlış nitelendirme riski ve alternatif senaryo uyarısı.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
