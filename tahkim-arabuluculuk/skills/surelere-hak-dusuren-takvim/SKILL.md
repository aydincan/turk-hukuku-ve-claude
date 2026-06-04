---
name: surelere-hak-dusuren-takvim
description: "Tahkim ve arabuluculuk süreçlerindeki iptal süresi, dava açma penceresi, tahkim süresi ve zamanaşımı durması gibi sert süreleri hesaplamak ve takvimlemek gerektiğinde kullanılır."
---

# Süreler ve Hak Düşüren Takvim

## Görev
Bu alandaki en sık hak kaybı süre kaçırmadan doğar. Bu beceri iptal süresi, dava açma
penceresi, tahkim süresi ve zamanaşımı durması gibi sert süreleri tek takvimde toplar ve
hatırlatma kurar.

## Soğuk başlangıç (intake)
1. Hangi aşamadasınız (tahkim başlangıcı, hakem kararı sonrası, arabuluculuk son tutanak)?
2. Belirleyici tarih nedir (kararın bildirimi, son tutanak tarihi, başvuru tarihi)?
3. İç tahkim mi MTK mı, dava şartı arabuluculuk mu?
4. Asıl talebin zamanaşımı/hak düşürücü süresi ne durumda?

## Denetim şeması
1. **Hakem kararı iptal süresi**: İç tahkimde kararın bildiriminden itibaren **1 ay**
   (**HMK m.439/4**); MTK'da **30 gün** (**MTK m.15/A-4**). Geçirilirse karar kesinleşir.
2. **Tahkim süresi**: Hakem kararı kural olarak **1 yıl** içinde verilir (**HMK m.427**,
   **MTK m.10/B**); uzatma anlaşma/mahkeme kararıyla. Süre aşımı iptal sebebidir.
3. **Dava şartı arabuluculuk dava açma penceresi**: Anlaşmama son tutanağından itibaren
   **2 hafta** içinde dava açılır (**HUAK m.18/A**); aksi halde yeniden arabuluculuk.
4. **Zamanaşımı/hak düşürücü süre durması**: Arabuluculuk başvurusu **zamanaşımını durdurur,
   hak düşürücü süreyi işlemez kılar** (**HUAK m.18/A-15**); koruma son tutanağa kadar
   sürer. Tahkimde davanın açılmasıyla zamanaşımı kesilir.
5. **Tenfiz/tanıma**: Yabancı kararlarda özel bir hak düşürücü süre öngörülmese de icra
   takibi öncesi tenfiz şarttır; gecikme icra riskini artırır. Ara sonuç: tarih bazlı
   takvim.

## Çıktı modülleri
- Tarih bazlı süre takvimi (her süre için başlangıç, bitiş, dayanak madde).
- Hatırlatma/uyarı kutusu (kesin süreler kırmızı işaretli).
- Zamanaşımı durması-kesilmesi özet notu.

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
