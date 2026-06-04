---
name: somut-olaya-uygulama-altlama
description: "Eldeki maddi olayın bir norma uyup uymadığını adım adım göstermek gerektiğinde; vakıaları norm unsurlarına yerleştirip gerekçeli bir hukuki sonuca varmak için kullanılır."
---

# Somut Olaya Uygulama (Altlama / Subsumption)

## Görev
Maddi olayı (küçük önerme) norm unsurlarına (büyük önerme) yerleştirerek, her unsuru ayrı ayrı denetleyip gerekçeli ve izlenebilir bir hukuki sonuç üretmek.

## Soğuk başlangıç (intake)
- Hukuken önemli vakıalar nelerdir; çekişmeli olan hangileri?
- Talep/iddianın dayandığı norm ve onun unsurları neler?
- Hangi unsur tartışmalı, hangisi açıkça sağlanmış?
- Karşı tarafın def'i/itirazı hangi unsuru hedefliyor?

## Denetim şeması
1. **Talep temelini bul** — "Kim kimden, neye dayanarak, ne istiyor?" Norm seçilir (örn. tazminat için TBK m.49; ifa için sözleşme + TBK m.112).
2. **Normu unsurlara ayır** — Hükmün her bir unsuru (örn. TBK m.49: fiil, hukuka aykırılık, kusur, zarar, illiyet bağı) liste hâline getirilir.
3. **Unsur-unsur altlama** — Her unsur için: ilgili vakıa + o unsurun sağlanıp sağlanmadığı + kısa gerekçe. Çekişmeli unsurda yorum/içtihat devreye sokulur; çekişmesiz unsur kısa geçilir.
4. **İspat yükü** — TMK m.6 / HMK m.190: her unsuru, lehine sonuç çıkaran taraf ispatlar. Karşı taraf, karşı vakıaları (def'i, itiraz) ispatla yükümlüdür. Unsur ispatlanamazsa o unsur "gerçekleşmemiş" sayılır.
5. **Karşı normlar** — Hak düşürücü/engelleyici/bozucu itirazlar (örn. zamanaşımı def'i, ifa, ibra) ayrı altlanır.
6. **Ara sonuç ve nihai sonuç** — Her unsur grubunda ara sonuç verilir; tüm unsurlar sağlanıyorsa talep haklı, biri eksikse reddedilir. Sonuç, TMK m.2 dürüstlük süzgecinden geçirilir.

## Çıktı modülleri
- Vakıa listesi (çekişmeli/çekişmesiz ayrımı).
- Norm + unsur tablosu.
- Unsur-unsur altlama (vakıa → değerlendirme → ara sonuç).
- İspat yükü dağılımı ve nihai sonuç.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
