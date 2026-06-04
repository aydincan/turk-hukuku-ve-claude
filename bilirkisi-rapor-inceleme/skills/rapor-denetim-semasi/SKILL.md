---
name: rapor-denetim-semasi
description: "Eldeki bilirkişi raporunu uçtan uca eleştirel biçimde denetlemek ve hangi usulî hamlenin (ek rapor, yeni heyet, esasa itiraz) seçileceğine karar vermek istendiğinde kullanılır."
---

# Rapor Denetim Şeması ve İtiraz Stratejisi

## Görev
Raporu dört eksende (usul, metodoloji, hesap, çelişki) sistematik denetleyip her bulguyu görevlendirme sorusuna ve dosya deliline çıpalamak; ardından bulguların ağırlığına göre doğru usulî yolu (HMK m.281) seçmek.

## Soğuk başlangıç (intake)
- Görevlendirme kararındaki sorular ile raporun yanıtladığı sorular örtüşüyor mu?
- Hangi husus(lar) sizin aleyhinize ve neden hatalı olduğunu düşünüyorsunuz?
- Dosyada raporla çelişen başka delil/rapor var mı?
- Hedefiniz raporu tümden çürütmek mi, yoksa belirli kalemleri düzeltmek mi?

## Denetim şeması
1. **Usul ekseni:** Bilirkişinin yetkisi, yemini, uzmanlık alanı sınırı (6754 s.K. m.3), görevlendirme kapsamına uygunluk (HMK m.273). Kapsam aşımı veya eksik yanıt belirlenir.
2. **Metodoloji ekseni:** Kullanılan yöntem açıkça belirtilmiş mi; kabuller ve varsayımlar dosya verisiyle örtüşüyor mu; veri kaynağı gösterilmiş mi (HMK m.279 gerekçe zorunluluğu)? Gerekçesiz sonuç denetlenebilir değildir.
3. **Hesap ekseni:** Aritmetik doğruluk, birim/tarih tutarlılığı, faiz başlangıcı ve türü, zamanaşımı/ıslah kesişimi. (Detaylı kontrol için hesap denetimi becerisi.)
4. **Çelişki ekseni:** Rapor içi çelişki, dosyadaki diğer delillerle çelişki, sorulara verilmeyen yanıtlar.
5. **Strateji seçimi (HMK m.281):** Tamamlanabilir eksik → **ek rapor**; yöntem hatası veya tarafsızlık kusuru → **yeni bilirkişi/heyet**; hukuki nitelendirme aşımı veya caizsizlik → **doğrudan esasa itiraz** (rapor hâkimi bağlamaz, HMK m.282). **Ara sonuç:** her bulgu için "hangi yol, hangi gerekçe, hangi dayanak" üçlüsü doldurulur.

## Çıktı modülleri
- Eksen-bulgu-dayanak (görevlendirme sorusu + dosya sayfası) matrisi.
- Bulgu başına önerilen usulî yol ve gerekçesi.
- İki hafta içinde sunulacak itiraz dilekçesinin omurgası.
- Talep sonucu önerisi (ek rapor / yeni heyet / rapora itibar edilmemesi).

## Plugin bağlamı

Bu beceri `bilirkisi-rapor-inceleme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
