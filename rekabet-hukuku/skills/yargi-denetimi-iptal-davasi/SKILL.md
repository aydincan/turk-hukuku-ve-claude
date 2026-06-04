---
name: yargi-denetimi-iptal-davasi
description: "Rekabet Kurulu kararlarına karşı idari yargıda iptal davası açma, dava açma süresi ve yetkili mahkeme, yürütmenin durdurulması ve istinaf/temyiz yolunu yönetmek istendiğinde kullanılır."
---

# Kurul Kararına Karşı Yargı Denetimi

## Görev
Rekabet Kurulu'nun nihai kararına (ihlal/ceza, izin ret, muafiyet ret) karşı 2577 sayılı İYUK çerçevesinde iptal davası stratejisini kurmak; süre, yetki, yürütmenin durdurulması ve kanun yollarını yönetmek.

## Soğuk başlangıç (intake)
- Dava konusu karar: ihlal+ceza mı, birleşme reddi mi, muafiyet/menfi tespit reddi mi, şikâyetin reddi mi?
- Gerekçeli karar tebliğ edildi mi; tebliğ tarihi nedir?
- Cezanın tahsil/ödeme durumu ve nakit etkisi nedir (yürütmeyi durdurma ihtiyacı)?
- İddia edilen sakatlık: usul (savunma hakkı) mı, esas (pazar tanımı, etki analizi) mı?

## Denetim şeması
1. **Yargı yolu ve yetki** — Kurul kararları idari işlemdir; iptal davası idari yargıda, Ankara İdare Mahkemeleri/idari yargı düzeninde görülür; temyiz Danıştay'dadır.
2. **Dava açma süresi (İYUK m.7)** — kural olarak yazılı bildirim (gerekçeli kararın tebliği) tarihinden itibaren 60 gün. Sürenin başlangıcı için tebligatın usulüne uygunluğu kontrol edilir; süre hak düşürücüdür.
3. **Yürütmenin durdurulması (İYUK m.27)** — telafisi güç/imkânsız zarar ve açık hukuka aykırılık şartları birlikte gösterilirse para cezasının tahsili durdurulabilir; teminat gündeme gelebilir.
4. **İptal sebepleri** — idari işlemin yetki, şekil, sebep, konu, maksat unsurları üzerinden: savunma hakkı ihlali ve eksik soruşturma (şekil/usul), hatalı pazar tanımı veya etki analizi (sebep), ölçüsüz ceza (konu), takdir yetkisinin amaç dışı kullanımı (maksat).
5. **İspat ve bilirkişi** — iktisadi analiz, pazar payı/HHI ve etki konularında teknik itiraz; gerektiğinde bilirkişi.
6. **Kanun yolu** — ilk derece kararına karşı istinaf/temyiz; süreler ve kesinleşme takip edilir.

## Çıktı modülleri
- Süre hesabı ve dava açma takvimi (tebliğ tarihinden 60 gün).
- İptal sebepleri matrisi (yetki-şekil-sebep-konu-maksat).
- Yürütmeyi durdurma talep gerekçesi taslağı.
- Doğrulanacak Danıştay içtihadı atıfları `[doğrulanacak]` (karararama.danistay.gov.tr).

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
