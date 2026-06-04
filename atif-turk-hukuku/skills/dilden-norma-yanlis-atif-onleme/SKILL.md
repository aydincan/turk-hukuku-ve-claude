---
name: dilden-norma-yanlis-atif-onleme
description: "Bir metinde mevzuat veya içtihat doğru görünse de yanlış maddeye, mülga hükme, çarpıtılmış ilkeye veya alakasız karara dayanıldığı durumlarda; bu hataları yakalayıp düzeltmek için kullanılır."
---

# Yanlış ve Yanıltıcı Atıf Önleme

## Görev
Görünüşte düzgün ama içerik olarak yanlış atıfları — yanlış madde, mülga hüküm, çarpıtılmış ilke, alakasız emsal — tespit edip düzeltmek; metnin dayanaklarını gerçekten taşır hâle getirmek.

## Soğuk başlangıç (intake)
- Atfedilen madde, ileri sürülen kuralı gerçekten içeriyor mu?
- Hüküm güncel mi, yoksa değişmiş/mülga mı?
- Atfedilen kararın ilkesi, metinde söylendiği gibi mi?
- Emsal kararın vakıası eldeki olaya benziyor mu?

## Denetim şeması
1. **Madde-içerik eşleştirme** — Her mevzuat atfı açılır; maddenin gerçek metni ileri sürülen kuralı içeriyor mu kontrol edilir. Sık hata: doğru kanun, yanlış madde; veya doğru madde, yanlış fıkra/bent.
2. **Yürürlük kontrolü** — Mülga/değişik hükme dayanılmış mı (mevzuat.gov.tr güncel metin)? Eski-yeni kanun karışıklığı (örn. eski BK/yeni TBK madde numaraları) ayıklanır.
3. **İlke çarpıtması** — Kararın kurduğu ilke ile metindeki ifade örtüşüyor mu? İstisna kural gibi, obiter ratio gibi sunulmuş olabilir; düzeltilir.
4. **Emsal uygunsuzluğu** — Atfedilen kararın vakıası farklıysa (farklı sözleşme tipi, farklı taraf sıfatı) emsal değildir; benzerlik kararın amacı bakımından test edilir.
5. **Yollama hatası** — Madde başka hükme yolluyor ama atıf yollanan yere değil, yollayan maddeye yapılmışsa; asıl uygulanacak hükme düzeltilir.
6. **Düzeltme ve gerekçe** — Her hata için doğru atıf + neden yanlış olduğu kısaca yazılır; doğrulanamayan kısım `[doğrulanacak]` bırakılır.

## Çıktı modülleri
- Hatalı atıf → doğru atıf düzeltme tablosu.
- Yürürlük/madde uyumsuzluğu listesi.
- İlke çarpıtması / emsal uygunsuzluğu notları.
- Düzeltilmiş dayanak listesi + işaretler.

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
