---
name: seceneklerin-tartilmasi-ve-gorus
description: "Birden fazla hukuki yorum veya yol mümkün olduğunda her seçeneği lehte-aleyhte tartıp olasılık diliyle gerekçeli bir nihai kanaat oluşturmak gerektiğinde kullanılır; mütalaanın sonuç bölümünü üretir."
---

# Seçeneklerin Tartılması ve Gerekçeli Görüş

## Görev
Olası hukuki yorumları, talep yollarını veya stratejik seçenekleri karşılaştırmalı tartmak ve gerekçeli, olasılık diliyle ifade edilmiş bir nihai kanaat üretmek. Mütalaanın değeri "kesin" demesinde değil, belirsizliği dürüstçe derecelendirmesindedir.

## Soğuk başlangıç (intake)
- Kaç farklı hukuki yorum/yol var?
- Her yolun dayanağı (norm + içtihat) ne kadar güçlü?
- Müvekkilin önceliği ne? (Hız / maliyet / kesinlik / ilişkiyi koruma)
- Karşı tarafın muhtemel argümanı ne?

## Denetim şeması
1. Seçenekleri listele: Her hukuki yorum veya talep yolu (ör. sözleşmeye aykırılık tazminatı vs. haksız fiil; aynen ifa vs. dönme) ayrı başlık altında.
2. Lehte-aleyhte analiz: Her seçenek için dayanak normun gücü, içtihat desteği, ispat zorluğu, süre/zamanaşımı durumu ve karşı argümanlar tartılır.
3. Olasılık dili: Sonuç tek bir derecelendirmeyle ifade edilir — "kuvvetle muhtemel kabul edilir / tartışmalıdır, %50 civarı / zayıf ihtimaldir". Mutlak ifadeden kaçınılır; hâkimin takdir alanı belirtilir.
4. Yarışma ve seçimlik haklar: Birden çok talep yarışıyorsa (TBK'da sözleşme/haksız fiil yarışması, ayıpta seçimlik haklar) hangisinin müvekkil lehine olduğu gerekçelenir.
5. Gerekçeli kanaat: Mütalaa, hangi seçeneği neden önerdiğini açıkça yazar; aleyhe ihtimali gizlemez.
6. Ara sonuç: Önerilen yol + olasılık derecesi + temel gerekçe + alternatif yol notu.

## Çıktı modülleri
- Seçenek karşılaştırma tablosu (yol | dayanak gücü | ispat | risk | süre)
- Olasılık derecelendirmesi gerekçesiyle
- Gerekçeli nihai kanaat paragrafı
- "Şu koşulda tercih değişir" senaryo notu

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
