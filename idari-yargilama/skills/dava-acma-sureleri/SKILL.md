---
name: dava-acma-sureleri
description: "İdari davada 30/60 günlük genel süreler, m.11 başvurusunun durdurucu etkisi, m.13 ön başvurusu ve özel kanun süreleri hesaplanırken kullanılır; sürenin başlangıcı, durması ve kaçırılıp kaçırılmadığı tartışmalı olduğunda başvurulur."
---

# Dava Açma Süreleri ve Sürenin Hesabı

## Görev
İdari davanın süresinde açılıp açılmadığını; başlangıç anını, durma/uzama hâllerini ve özel kanun sürelerini dikkate alarak kesin biçimde hesaplamak. Süreler kamu düzenindendir ve resen incelenir.

## Soğuk başlangıç (intake)
- İşlem ilgilisine tebliğ mi edildi, ilan mı edildi, yoksa başka yolla mı öğrenildi; tarih nedir?
- İşleme karşı m.11 kapsamında üst makama başvuruldu mu; başvuru tarihi ve cevabı?
- Uyuşmazlık vergiyle mi ilgili (30 gün), genel idari mi (60 gün)?
- Özel bir kanun (kamulaştırma, ihale, YUKK vb.) farklı bir süre öngörüyor mu?

## Denetim şeması
1. **Genel süre** (İYUK m.7): Danıştay ve idare mahkemelerinde **60 gün**, vergi mahkemelerinde **30 gün**. Süre, yazılı bildirimin (tebliğ) yapıldığı tarihi izleyen günden başlar. İlanı gereken işlemlerde ilan süresinin bitimini izleyen günden işler.
2. **İdari başvuru ile durma** (İYUK m.11): İlgililer, dava açma süresi içinde işlemi yapan makama veya üst makama başvurarak işlemin kaldırılmasını/değiştirilmesini isteyebilir. Bu başvuru **işlemeye başlamış süreyi durdurur**. İdarenin cevabı veya 30 günlük zımni ret süresinin dolmasıyla kalan süre yeniden işlemeye başlar (durmuş olan süre kaldığı yerden devam eder).
3. **Tam yargı ön başvurusu** (İYUK m.13): İdari eylem zararlarında 1 yıl / 5 yıl sınırı (bkz. tam yargı becerisi).
4. **İptal sonrası tam yargı** (İYUK m.12): İptal davasıyla birlikte veya iptal kararının/temyizde onanmasının tebliğinden itibaren 60 gün içinde tam yargı açılabilir.
5. **Özel kanun süreleri**: 2942 sayılı Kamulaştırma K., 4734/4735 sayılı ihale mevzuatı, 6458 sayılı YUKK, 6183 sayılı AATUHK ödeme emri (7 gün/15 gün gibi) süreleri saklıdır ve genel süreye önceliklidir.
6. **Ara sonuç — son gün**: Sürenin son günü çalışmaya ara verme (adli tatil — İYUK m.61) veya resmî tatile rastlarsa, süre tatili izleyen ilk iş gününün mesai bitiminde sona erer (İYUK m.8). Adli tatilde biten süreler tatilin bitiminden itibaren 7 gün uzar.

## Çıktı modülleri
- Süre hesap tablosu (başlangıç, durma, son gün)
- m.11 başvurusu yapılmışsa durma/devam analizi
- Süre aşımı riski ve önerilen ivedi adımlar

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
