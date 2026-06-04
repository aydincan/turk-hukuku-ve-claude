---
name: redline-ve-alternatif-lafiz
description: "Riskli maddeler için somut düzeltme metni, alternatif lafız ve yedek (fallback) pozisyonlar üretip gerekçelendirmek gerektiğinde kullanılır."
---

# Redline ve Alternatif Lafız Üretimi

## Görev
Tespit edilen her riskli madde için "mevcut lafız → önerilen lafız → gerekçe (madde atfıyla)" üçlüsünü ve yedek pozisyonları üreterek müzakereye hazır redline metni oluşturmak.

## Soğuk başlangıç (intake)
- Hangi maddeler redline'a girecek (risk haritasından gelen öncelikli liste)?
- Müvekkilin ideal ve kabul edilebilir asgari pozisyonu ne (anchor + fallback)?
- Karşı tarafın metni değiştirme esnekliği ve pazarlık gücü ne?
- Üslup: agresif tam redline mi, dengeli "market standard" mı?

## Denetim şeması
1. **Önceliklendirme**: Deal-breaker maddeler tam yeniden yazılır; pazarlık maddelerine alternatif sunulur; kabul edilebilir maddelere yalnız not düşülür.
2. **Lafız tasarımı**: Her öneri için (a) mevcut metin, (b) önerilen metin, (c) gerekçe — emredici dayanak (TBK m.27, m.115, m.182) veya denge/menfaat gerekçesi. Belirsiz ifadeler ölçülebilir/tetikleyicili hale getirilir.
3. **Karşılıklılık enjeksiyonu**: Tek taraflı hak/yükümlülükler karşılıklı hale getirilir (fesih, ceza, gizlilik, tazminat).
4. **Yedek pozisyon (fallback)**: Her kritik talep için 1-2 kademeli geri çekilme lafzı (örn. sınırsız tavan → işlem bedeli tutarında tavan → 2 katı tavan).
5. **Tutarlılık denetimi**: Değiştirilen madde tanımlar, çapraz atıflar ve diğer maddelerle çelişmesin; "severability/bölünebilirlik" ve "tüm sözleşme" kayıtlarıyla uyum.
6. **Yer tutucu disiplini**: Bilinmeyen veriler (tutar, süre, taraf) `[doldurulacak]`; teyit gereken mevzuat/içtihat `[doğrulanacak]` etiketiyle bırakılır, uydurulmaz.

## Çıktı modülleri
- Redline tablosu: madde / mevcut lafız / önerilen lafız / gerekçe / öncelik.
- Yedek pozisyon (fallback) basamakları.
- Markup'lı sözleşme metni veya değişiklik listesi (track-changes mantığı).

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
