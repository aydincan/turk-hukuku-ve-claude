---
name: muvekkil-ve-idare-iletisimi
description: "İstekli müvekkile süreci sade anlatmak, idareye/KİK'e yazılacak resmi yazıların tonunu ve içeriğini kurmak veya bilgi/belge talep yazıları hazırlamak gerektiğinde kullanılacak iletişim becerisidir."
---

# Müvekkil ve İdare İletişimi

## Görev
İhale sürecinin teknik ve süre-yoğun adımlarını müvekkile anlaşılır biçimde aktarmak; idareye, KİK'e ve ilgili mercilere gönderilecek resmi yazışmaları doğru ton ve içerikle hazırlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim: müvekkil (istekli/idare), karşı idare, KİK?
2. İletişimin amacı: bilgilendirme, bilgi/belge talebi, şikâyet, savunma?
3. Süre baskısı var mı; yazının resmî kayda girmesi mi gerekiyor?
4. Hangi hukuki sonuç hedefleniyor (süre koruma, delil temini, uzlaşma)?

## Denetim şeması
1. **Müvekkil bilgilendirmesi:** Sürecin nerede olduğu, atılacak adım, hak düşürücü süreler ve olası sonuçlar sade dille; teknik terim açıklanarak aktarılır. Gerçekçi beklenti yönetimi yapılır, kesin sonuç vaadinden kaçınılır.
2. **İdareye yazışma (şikâyet/talep):** Saydamlık ilkesi (m.5) çerçevesinde bilgi/belge talebi; şikâyet dilekçesinde işlem, tarih, hukuki aykırılık ve talep açık biçimde, m.55'e uygun olarak yazılır. Resmî kayıt/tebliğ tarihi delil değeri taşır.
3. **KİK'e yazışma:** İtirazen şikâyet dilekçesi m.56'ya uygun; başvuru ehliyeti, süre, iddia ve dayanak somut belgeyle bağlanır, başvuru bedeli dekontu eklenir.
4. **Ton ve üslup:** Resmî, ölçülü, kişiselleştirmeden uzak; iddialar belgeye dayandırılır, suçlayıcı/abartılı dil kullanılmaz.
5. **Ara sonuç:** Her yazışma için muhatap, kanal (EKAP/yazılı), kayıt yöntemi ve süre etkisi belirlenir.

İspat yükü: Yazışmanın gönderim/tebliğ tarihi mutlaka kayda bağlanır.

## Çıktı modülleri
- Müvekkile durum özeti (sade dil) ve adım listesi.
- İdareye/KİK'e resmi yazı taslağı (talep + dayanak + ek).
- Yazışma kayıt ve süre etkisi notu.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
