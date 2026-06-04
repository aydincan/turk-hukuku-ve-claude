---
name: bono-police-unsurlar
description: "Bono ve poliçenin zorunlu şekil şartlarını, eksiklik sonuçlarını ve poliçeye özgü kabul/keşide ilişkilerini denetlemek; senedin kambiyo vasfını taşıyıp taşımadığını belirlerken kullanılır."
---

# Bono ve Poliçe Unsurları

## Görev
Bono (emre muharrer senet) veya poliçenin zorunlu unsurlarını madde madde denetlemek, eksikliklerin kambiyo vasfına etkisini saptamak ve poliçede kabul ilişkisini çözümlemek.

## Soğuk başlangıç (intake)
- Senet "bono/emre muharrer senet" mi yoksa üç taraflı "poliçe" mi?
- Bedel, vade, lehtar, tanzim yeri-tarihi ve imza tam mı?
- Poliçede muhatap kabul etmiş mi; kabul kaydı var mı?
- Senet matbu form mu, beyaz/açık düzenleme şüphesi var mı?

## Denetim şeması
1. Bono şekil şartları: TTK m.776 — "bono/emre muharrer senet" ibaresi, kayıtsız şartsız belirli bedel ödeme vaadi, vade, ödeme yeri, lehtar, tanzim yeri-tarihi, düzenleyen imzası. Eksiklikte m.777 yorum kuralları (vade yoksa görüldüğünde, ödeme yeri yoksa tanzim yeri, tanzim yeri yoksa düzenleyen ad yanı). İmza ve bedel telafi edilemez; bunların yokluğu vasfı düşürür.
2. Poliçe şekil şartları: TTK m.671 — "poliçe" kelimesi, ödeme emri, muhatap, lehtar, vade, ödeme/keşide yeri-tarihi, keşideci imzası; eksiklik m.672.
3. Bono-poliçe yollaması: bonoya ciro, vade, ödeme, başvurma, protesto, zamanaşımı bakımından poliçe hükümleri uygulanır (TTK m.778).
4. Poliçede kabul: muhatap kabulle (m.691 vd.) asıl borçlu olur; kabul etmezse hamil vadeden önce başvurabilir (m.713). Bonoda düzenleyen, poliçede kabul eden gibi sorumludur (m.778/son).
5. Beyaz senet: açık atılan imzayla verilen senet anlaşmaya aykırı doldurulmuşsa def'i m.680; iyiniyetli hamile karşı ileri sürülemez.
6. Ara sonuç: tüm zorunlu unsurlar tamamsa senet kambiyo vasfını taşır ve kambiyo takibine elverişlidir; değilse adi yazılı delil olarak kalır.

## Çıktı modülleri
- Unsur denetim cetveli (madde-madde var/yok + dayanak).
- Eksikliğin telafi edilebilirliği ve sonuç değerlendirmesi.
- Gerekiyorsa beyaz senet/anlaşmaya aykırı doldurma savunma notu.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
