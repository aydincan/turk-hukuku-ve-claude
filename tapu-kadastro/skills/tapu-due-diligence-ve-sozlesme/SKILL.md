---
name: tapu-due-diligence-ve-sozlesme
description: "Bir taşınmazın satın alınması, finansmanı veya devri öncesinde tapu kaydı, takyidat, imar ve nitelik yönünden risk taraması yapılırken; satış vaadi/satış işlemi, kapora ve devir güvenliği kurgulanırken kullanılır."
---

# Tapu İncelemesi (Due Diligence) ve Devir Sözleşmesi

## Görev
Taşınmaz devri öncesinde hak, yük ve sınır risklerini sistematik taramak; güvenli devir ve sözleşme yapısını kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: doğrudan satış mı, taşınmaz satış vaadi mi, ipotekli/krediyle alım mı?
- Tapu kaydı, akit tablosu, takyidat listesi ve imar durumu temin edildi mi?
- Satıcı malik mi, vekil mi (vekâletnamenin kapsamı/güncelliği), tüzel kişi mi?
- Taşınmazın niteliği (arsa/tarla/bina), kat irtifakı/mülkiyeti, yapı kayıt/ruhsat durumu nedir?

## Denetim şeması
1. **Hak sahipliğini doğrula.** Güncel tapu kaydı ve akit tablosuyla malikin yetkisini, devir zincirini ve önceki yolsuzluk emarelerini kontrol et (TMK m.1020 aleniyet). Vekâletle işlemde 2644 sayılı Tapu Kanunu m.26 ve vekâletin kapsamı/iptal durumu.
2. **Takyidatları tara.** İpotek, haciz, ihtiyati tedbir, şerhler (satış vaadi, kira, önalım), beyanlar (aile konutu, kamulaştırma) — her takyidatın alıcıya etkisini (TMK m.1009-1010, m.1023) değerlendir.
3. **Nitelik ve imar süzgeci.** Orman/mera/kıyı niteliği, imar planı durumu, kaçak yapı/yapı kayıt belgesi (imar mevzuatı) devri ve kullanımı etkiler; bu skorlar ayrı imar/kat mülkiyeti incelemesine bağlanır.
4. **Şekil ve devir güvenliği.** Mülkiyet devri yalnız tapuda resmi senetle geçer (TMK m.706, m.705). Taşınmaz satış vaadi geçerlilik için resmi (noter) şekle tabidir (TBK m.237, Noterlik Kanunu m.60); vaadi güçlendirmek için tapuya şerh (TMK m.1009).
5. **Bedel ve risk dağıtımı.** Kapora/cayma parası (TBK m.177), ifa zamanı, takyidat temizleme yükümlülüğü, zapttan/ayıptan sorumluluk (TBK m.214 vd.) sözleşmede netleştirilir; emanet (escrow)/şartlı ödeme önerilir.
6. **Ara sonuç.** Devir güvenli mi, hangi takyidat temizlenmeli, hangi koşul kapanış şartı olmalı.

## Çıktı modülleri
- Tapu/takyidat risk skor tablosu (kırmızı/sarı/yeşil).
- Taşınmaz satış vaadi veya satış öncesi protokol iskeleti, kapanış şartları listesi.
- Kapanış öncesi giderilmesi gereken eksikler ve [doldurulacak] alanlar.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
