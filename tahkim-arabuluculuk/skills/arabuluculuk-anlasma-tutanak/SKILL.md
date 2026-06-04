---
name: arabuluculuk-anlasma-tutanak
description: "Arabuluculuk sonunda düzenlenen anlaşma belgesi veya son tutanağı kaleme almak, denetlemek ve icra edilebilirliğini sağlamak gerektiğinde kullanılır."
---

# Arabuluculuk Anlaşma Belgesi ve Tutanak

## Görev
Arabuluculuk sürecinin yazılı çıktısını (anlaşma belgesi veya son tutanak) hukuken sağlam,
icra edilebilir ve ileride uyuşmazlık doğurmayacak şekilde hazırlamak veya denetlemek.

## Soğuk başlangıç (intake)
1. Süreç anlaşma ile mi anlaşmama ile mi sonuçlandı, kısmi anlaşma var mı?
2. Anlaşma konuları neler, edimler somut ve infazı kabil mi?
3. Taraflar avukatla mı temsil edildi (icra edilebilirlik şerhi etkisi)?
4. Belge dava şartı arabuluculuk sonucu mu, sonraki dava açma süresine etkisi ne?

## Denetim şeması
1. **Belge türü**: Anlaşma sağlandıysa **anlaşma belgesi**; sağlanamadıysa **son tutanak**
   (**HUAK m.17, m.18**). Son tutanağa anlaşılan/anlaşılamayan hususlar açıkça yazılır.
2. **İçerik sağlamlığı**: Taraflar, uyuşmazlık konusu, üzerinde anlaşılan edimler, ödeme
   takvimi, ferağ/feragat kapsamı açık ve infaza elverişli olmalı. Belirsiz edim icra
   sorunudur.
3. **İcra edilebilirlik**: Taraflar **ve avukatları ile arabulucunun** birlikte imzaladığı
   anlaşma belgesi **icra edilebilirlik şerhi niteliğinde** olup ilam hükmündedir
   (**HUAK m.18/4**). Avukatla imzalanmadıysa **sulh hukuk mahkemesinden** şerh alınır.
4. **Anlaşılan konunun davaya kapanması**: Anlaşılan hususlar yönünden taraflar dava
   açamaz; bu, belgenin kesin etkisidir. Anlaşılamayan kısım için dava şartı sürer.
5. **Ara sonuç**: Belgenin icra edilebilirliği, açık riskler ve düzeltme önerileri.

## Çıktı modülleri
- Anlaşma belgesi / son tutanak taslağı (taraf, edim, takvim, imza bölümleriyle).
- İcra edilebilirlik kontrol listesi (avukat imzası vs. mahkeme şerhi ayrımı).
- Edim infaz riski notu (belirsiz/asimetrik ifadelerin işaretlenmesi).

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
