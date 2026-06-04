---
name: lisans-devir-sozlesmeleri
description: "Mali hakların devri veya ruhsat/lisans verilmesine ilişkin sözleşme hazırlanması, incelenmesi veya yorumlanması gerektiğinde; FSEK m.48-52 şekil ve kapsam kurallarına uygunluğu ve hak zincirini denetlemek için kullanılır."
---

# Telif Devir ve Lisans Sözleşmeleri

## Görev
Mali hakların devri (temlik) veya kullanım ruhsatı (lisans) sözleşmesini FSEK m.48-52 çerçevesinde hazırlamak, incelemek ve hak zincirini denetlemek.

## Soğuk başlangıç (intake)
- Hangi eser, hangi mali haklar devre/lisansa konu?
- Devir mi (temlik), münhasır lisans mı, basit lisans mı isteniyor?
- Coğrafi alan, süre, ücret, alt lisans yetkisi belirlendi mi?
- Eser henüz meydana gelmemiş mi (gelecekteki eser)?

## Denetim şeması
1. İşlemin niteliği: Mali hak devri (m.48 — tam temlik) mi, ruhsat/lisans (m.48-49 — münhasır/basit) mı belirlenir. Manevi haklar devredilemez; yalnızca kullanım yetkilendirilebilir (m.16/son).
2. Şekil şartı (m.52): Mali haklara ilişkin sözleşme ve tasarruflar yazılı olmak ve konuları olan hakların ayrı ayrı gösterilmesi zorunludur. Sayılmayan hak devredilmemiş sayılır; sözlü/zımni mali hak devri geçersizdir. Bu emredici şekil dosyada ilk kontroldür.
3. Kapsam ve dar yorum: Devir/lisans, açıkça yazılanla sınırlıdır; tereddütte eser sahibi lehine yorum yapılır. Yer-süre-içerik belirlenir; ileride çıkacak kullanım türleri için açık hüküm aranır.
4. Gelecekteki eser ve haklar: Henüz vücut bulmamış eser üzerindeki tasarruf sınırlıdır (m.48/3); ileride çıkarılacak mevzuatın tanıyacağı haklar baştan devredilemez (m.51).
5. Devralanın yetkileri ve cayma: Devralanın hakkı süresinde kullanmaması hâlinde eser sahibinin cayma hakkı (m.58); aşırı zarar hâlinde m.59 değerlendirilir. Alt devir/alt lisans ancak izinle (m.49).
6. Ara sonuç: Geçerli, kapsamı net, hak zinciri kesintisiz bir sözleşme; eksikse redline ve tamamlama önerisi.

İspat yükü: devir/lisans iddiasını ileri süren yazılı belgeyle ispatlar (m.52, HMK m.200 vd.).

## Çıktı modülleri
- Sözleşme taslağı/redline (hak listesi, yer-süre-ücret, alt lisans, cayma).
- m.52 şekil ve kapsam uygunluk kontrol listesi.
- Hak zinciri (chain of title) şeması.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
