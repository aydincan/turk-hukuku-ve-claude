---
name: islem-sonrasi-uyusmazlik-ve-tazminat
description: "Kapanış sonrası beyan-tekeffül ihlali, gizli borç, earn-out anlaşmazlığı veya hile iddialarında talep mimarisini kurmak, görev-yetki ile tahkim/mahkeme tercihini belirlemek için kullanılır."
---

# İşlem Sonrası Uyuşmazlık ve Tazminat Talepleri

## Görev
Kapanış sonrası ortaya çıkan ihlal/zarar iddialarında talebin hukuki temelini, usul yolunu ve ispat stratejisini kurmak.

## Soğuk başlangıç (intake)
- İddia neye dayanıyor (R&W ihlali, gizli borç, earn-out, hile)?
- SPA'da tahkim şartı var mı, tabi hukuk ve dil ne?
- Bildirim süreleri (claim notice) ve sorumluluk sınırları (cap/süre) ne?
- Hile/gizleme iddiası var mı (sınırlamaları aşan)?

## Denetim şeması
1. **Hukuki temel**: Beyan-tekeffül ihlali sözleşmesel tazminat (TBK m.112); ayıp niteliğinde ise satım hükümleri (TBK m.219 vd.) kıyasen; hile varsa sözleşmenin iptali ve tazminat (TBK m.36, m.39).
2. **Bildirim/usul**: SPA'daki claim notice süresine uyum; sürenin kaçırılması hak düşürücü etki yaratabilir.
3. **Usul yolu**: Tahkim şartı varsa HMK m.412 / 4686 (milletlerarası ise) uygulanır; aksi halde ticari dava — asliye ticaret mahkemesi, dava şartı arabuluculuk (TTK m.5/A) gözetilir.
4. **Görev-yetki**: Ticari nitelikte ise asliye ticaret mahkemesi (TTK m.4-5); arabuluculuk dava şartı kontrol edilir.
5. **Sınırlamaların denetimi**: Cap/basket/süre sınırlamaları geçerlidir; ancak hilede sözleşmesel sorumsuzluk kayıtları hükümsüzdür (TBK m.115).
6. **İspat yükü ve delil**: İhlal ve zararı talep eden ispatlar (HMK m.190); DD raporu, disclosure letter, mali kayıtlar delil; bilirkişi ile zarar hesabı.
7. **Ara sonuç**: Talep edilebilir tutar, sınırlamalar düşülerek ve faiz (TBK m.117 vd.) eklenerek hesaplanır.

## Çıktı modülleri
- Talep temeli ve usul yolu değerlendirme notu
- Claim notice taslağı
- Zarar hesabı çerçevesi ve delil dizini
- Dava/tahkim dilekçesi iskeleti ([doldurulacak] yer tutucularla)

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
