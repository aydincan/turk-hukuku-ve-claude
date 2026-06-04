---
name: dogrulama-kontrol-listesi-teslim-oncesi
description: "Bir layiha, mütalaa veya sözleşme teslim edilmeden hemen önce; tüm mevzuat, içtihat ve doktrin atıflarının doğruluğunu, güncelliğini ve işaretlenmemiş uydurma kalmadığını topluca denetlemek için kullanılır."
---

# Teslim Öncesi Atıf Doğrulama Kontrol Listesi

## Görev
Bir hukuki metin teslim edilmeden önce, içindeki tüm atıfları sistematik bir kontrol listesinden geçirerek hatalı, güncelliğini yitirmiş veya doğrulanmamış hiçbir dayanağın kalmadığından emin olmak.

## Soğuk başlangıç (intake)
- Belge türü ve muhatabı kim (mahkeme, müvekkil, karşı taraf)?
- Metinde kaç mevzuat, kaç içtihat, kaç doktrin atfı var?
- Hangileri teyit edildi, hangileri hâlâ `[doğrulanacak]`?
- Son değişiklikten sonra yeni eklenen atıf var mı?

## Denetim şeması
1. **Envanter** — Metindeki tüm atıflar listelenir: mevzuat (madde/fıkra/bent), içtihat (künye), doktrin (yazar-sayfa). Her biri için "teyit kaynağı" sütunu açılır.
2. **Mevzuat denetimi** — Her madde mevzuat.gov.tr'den açılır; numara, fıkra, bent ve yürürlük durumu (güncel/değişik/mülga) doğrulanır; zaman bakımından uygulama sorunu yoksa işaretlenir.
3. **İçtihat denetimi** — Her künye resmî bankadan teyit edilir; teyit edilemeyen künye `[doğrulanacak]` ile bırakılır veya çıkarılır — **asla tahmin numarasıyla tamamlanmaz.** İBK/AYM bağlayıcılığı doğru sunulmuş mu kontrol edilir.
4. **Doktrin denetimi** — Yazar-eser-sayfa doğrulanır; doğrulanamayan atıf "kaynak teyit edilecek" notuyla bırakılır.
5. **Tutarlılık ve dürüstlük** — Aleyhe yerleşik içtihat gizlenmemiş; tek karar "yerleşik" diye sunulmamış; doktrin kural gibi gösterilmemiş; kesinlik derecesi dürüstçe yansıtılmış mı?
6. **İşaret taraması** — Metinde kalan tüm `[doğrulanacak]` / `[doldurulacak]` işaretleri raporlanır; bilerek bırakılanlar dışında işaretsiz uydurma kalmadığı teyit edilir.

## Çıktı modülleri
- Atıf envanter tablosu (tür / dayanak / teyit durumu).
- Mevzuat ve içtihat doğrulama sonucu (geçti/düzeltildi/`[doğrulanacak]`).
- Dürüstlük/tutarlılık denetimi notu.
- Kalan işaret listesi ve teslim hazırlık özeti.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
