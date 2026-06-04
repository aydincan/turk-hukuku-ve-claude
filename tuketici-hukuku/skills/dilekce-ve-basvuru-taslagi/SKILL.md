---
name: dilekce-ve-basvuru-taslagi
description: "Tüketici uyuşmazlığında ihtarname, hakem heyeti başvurusu, dava/itiraz dilekçesi veya cayma/fesih bildirimi taslağı üretmek gerektiğinde; layiha mimarisi ve yer tutucu disipliniyle kullanılır."
---

# Dilekçe, Başvuru ve Sözleşme Taslakları

## Görev
Tüketici uyuşmazlığının gerektirdiği yazılı metni (ihtarname, hakem heyeti başvurusu, dava dilekçesi, hakem heyeti kararına itiraz, cayma/fesih bildirimi) usul kurallarına uygun, vakıa-hukuki sebep-talep mimarisiyle ve eksik bilgilerde yer tutucu disipliniyle üretmek.

## Soğuk başlangıç (intake)
- Hangi metin gerekiyor (ihtar, başvuru, dava, itiraz, bildirim)?
- Taraflar, talep konusu ve değeri nedir?
- Hangi maddi vakıalar ve deliller var; eksik bilgi hangileri?
- Hedeflenen sonuç (iade, onarım, fesih, tazminat) ne?

## Denetim şeması
1. **Metin türü seçimi:** Çözüm yoluna göre doğru belgeyi belirle — hakem heyeti başvurusu (m.66 usulü), tüketici mahkemesi dava dilekçesi (HMK m.119 zorunlu unsurları), hakem heyeti kararına itiraz dilekçesi (m.70, 15 gün), ihtarname (TBK m.117 temerrüt için) veya cayma/fesih bildirimi.
2. **Zorunlu unsurlar (HMK m.119):** Mahkeme, taraflar ve TC/adres, dava konusu, değer, açık vakıalar, dayanılan deliller, hukuki sebepler, açık talep sonucu ve imza. Eksik unsur ön incelemede tamamlattırılır; baştan eksiksiz yaz.
3. **Hukuki sebep altlaması:** Talebe göre TKHK madde grubunu doğru göster (ayıp m.11/15, haksız şart m.5, cayma m.48/24, abonelik m.52); tamamlayıcı olarak TBK/HMK maddelerini ekle.
4. **Talep sonucu netliği:** Eda talebini para/edim olarak somut yaz; faiz başlangıcı ve türünü (avans/yasal/ticari) belirt; fazlaya ilişkin haklar saklı tut.
5. **Yer tutucu disiplini:** Bilinmeyen tarih, tutar, ad için [doldurulacak: ...] biçiminde açık yer tutucu kullan; uydurma veri girme.
6. **Delil bağlama:** Her vakıayı ilgili delile bağla; delil listesini ayrı blokta ver.
7. **Ara sonuç:** Metin usulen eksiksiz mi, talep ve sebep tutarlı mı, yer tutucular işaretli mi?

## Çıktı modülleri
- Seçilen türde hazır taslak metin.
- Zorunlu unsur kontrol listesi.
- Delil dizini.
- Doldurulacak alanlar özeti.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
