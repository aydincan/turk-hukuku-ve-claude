---
name: yapay-zeka-sorumluluk
description: "Bir yapay zekâ sistemi (otonom karar, üretken çıktı, gömülü ürün) bir kişiye zarar verdiğinde geliştirici, kullanan ve veri sağlayıcı arasında sorumluluğun haksız fiil, kusursuz sorumluluk ve sözleşme temelinde dağıtılması gerektiğinde kullanılır."
---

# Yapay Zekâ Kaynaklı Zarar ve Sorumluluk

## Görev
Yapay zekâ kaynaklı bir zararda sorumluluğun hukuki temelini (haksız fiil, kusursuz sorumluluk, sözleşmeye aykırılık) belirleyip geliştirici, sistemi kullanan ve veri sağlayıcı arasındaki dağılımı ve ispat yükünü çözümlemek.

## Soğuk başlangıç (intake)
1. Zarar nasıl doğdu: hatalı/önyargılı karar, yanlış üretken çıktı (uydurma bilgi), otonom cihaz/araç davranışı, veri sızıntısı?
2. Taraflar arasında sözleşme var mı (kullanım koşulları, hizmet sözleşmesi)?
3. Sistemi işleten kim; çıktı insan denetiminden geçti mi?
4. Zarar bedensel/mali/manevi mi; mağdur tüketici mi, işletme mi?

## Denetim şeması
1. **Sözleşme/haksız fiil ayrımı**: Taraflar arasında sözleşme varsa öncelik TBK m.112 vd. (gereği gibi ifa etmeme) ve sorumluluk sınırlaması/genel işlem koşulu denetimi (m.20-25). Sözleşme yoksa haksız fiil (m.49 vd.): fiil, hukuka aykırılık, kusur, zarar, illiyet. Ara sonuç: hangi rejim.
2. **Kusursuz sorumluluk**: Yapay zekâyı bir yardımcı kişi gibi kullanan işletme için **adam çalıştıranın sorumluluğu (TBK m.66)** ve riski yüksek otonom sistemlerde **tehlike sorumluluğu / tehlikeli işletme (TBK m.71)** tartışılır; bu hallerde kusur ispatı gerekmez, illiyet ve zarar yeter.
3. **İlliyet ve ispat**: YZ kararının "kara kutu" niteliği illiyetin ispatını zorlaştırır; bilirkişi, log ve model dokümanı kritik. İspat yükü kural olarak zarar görende; kusursuz sorumlulukta kusur dışındaki unsurlar yeterli.
4. **Üretken model çıktısı**: Yanlış/iftira niteliğinde çıktıda kişilik hakkı ihlali (TMK m.24-25, TBK m.58 manevi tazminat) ve sağlayıcının özen yükümlülüğü.
5. **Rücu ve dağıtım**: Müteselsil sorumlulukta (TBK m.61) iç ilişkide kusur/sözleşme uyarınca rücu; geliştirici-kullanan arası sözleşmedeki tazmin ve sorumluluk maddeleri belirleyici.

AB'de Ürün Sorumluluğu Direktifi reformu karşılaştırmalı kaynaktır, Türkiye'de doğrudan uygulanmaz. Künyeyi [doğrulanacak] işaretle.

## Çıktı modülleri
- Sorumluluk temeli ve taraf matrisi.
- İspat ve delil (log/bilirkişi) gereksinim listesi.
- Tazminat talebi veya savunma stratejisi taslağı.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
