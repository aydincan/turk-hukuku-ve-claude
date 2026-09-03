---
name: risk-haritasi-ve-skorlama
description: "Sözleşmenin tamamını tarayıp her riskli maddeyi olasılık-etki ve deal-breaker/pazarlık/kabul edilebilir olarak etiketleyen yapılandırılmış bir risk tablosu üretmek gerektiğinde kullanılır."
---

# Madde Madde Risk Haritası ve Skorlama

## Görev
Sözleşmeyi baştan sona tarayarak müvekkil aleyhine her kaydı tespit etmek, olasılık ve etki üzerinden skorlamak ve önceliklendirilmiş bir risk tablosu çıkarmak.

## Soğuk başlangıç (intake)
- Müvekkilin işlemden beklediği temel menfaat ve kabul edemeyeceği "kırmızı çizgiler" neler?
- İşlem hacmi/tutarı ve sürekliliği nedir (etki ağırlığı için)?
- Karşı tarafın pazarlık gücü ve metni değiştirme esnekliği var mı?
- Acil/zaman baskısı veya sektörel zorunluluk var mı?

## Denetim şeması
1. **Tarama eksenleri**: (a) Edim-bedel dengesi, (b) sorumluluk/tazminat dağılımı (TBK m.112, m.115), (c) fesih/dönme hakları (m.125), (d) cezai şart (m.179), (e) süre/yenileme, (f) gizlilik/rekabet yasağı, (g) uyuşmazlık/yetki (HMK m.17), (h) mücbir sebep ve uyarlama (m.138).
2. **Asimetri testi**: Her hak/yükümlülük için "karşı tarafta da var mı?" sorulur; tek taraflı fesih, tek taraflı cezai şart, tek taraflı değişiklik yetkisi (m.24) işaretlenir.
3. **Skorlama**: Olasılık (riskin gerçekleşme ihtimali) × Etki (parasal + operasyonel + itibari) = risk düzeyi. Etiket: **Deal-breaker** (imzalanamaz), **Pazarlık** (redline şart), **Kabul edilebilir** (not düşülür).
4. **Emredici filtre**: Geçersiz kayıtlar (TBK m.27, m.115) ayrı "lehe risk" olarak işaretlenir — karşı tarafın dayanağı çökebilir.
5. **İspat/uygulanabilirlik**: Madde teoride lehe ama ispatı/icrası zor mu (belirsiz tetikleyici, ölçülemez ceza)?
6. **Ara sonuç**: Önceliklendirilmiş risk tablosu ve redline'a taşınacak maddeler.

## Çıktı modülleri
- Madde / risk / olasılık-etki / etiket / öneri sütunlu risk tablosu (Excel'lenebilir).
- Deal-breaker özeti ve karar notu.
- Müvekkile tek sayfalık risk skoru özeti.

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
