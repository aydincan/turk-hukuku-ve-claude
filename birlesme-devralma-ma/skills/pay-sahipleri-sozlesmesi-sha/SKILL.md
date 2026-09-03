---
name: pay-sahipleri-sozlesmesi-sha
description: "Devralma sonrası ortaklık ilişkisini, yönetim ve oy haklarını, çıkış mekanizmalarını (tag/drag, ön alım) ve azınlık korumalarını düzenleyen pay sahipleri sözleşmesini tasarlamak için kullanılır."
---

# Pay Sahipleri Sözleşmesi (SHA) ve Yönetişim

## Görev
İşlem sonrası ortaklık yapısını, yönetişimi ve çıkış mekanizmalarını TTK'nın emredici sınırları içinde sözleşmeyle düzenlemek.

## Soğuk başlangıç (intake)
- İşlem sonrası ortaklık yapısı nedir (çoğunluk/azınlık)?
- Yönetim kurulu kompozisyonu ve veto hakları nasıl olacak?
- Çıkış senaryoları (IPO, satış) ve süre öngörülüyor mu?
- SHA hükümleri esas sözleşmeye taşınacak mı?

## Denetim şeması
1. **Sözleşme-esas sözleşme ilişkisi**: SHA taraflar arası borçsal etki doğurur; üçüncü kişilere ve şirkete karşı etki için esas sözleşmeye (TTK m.340 tipiklik sınırı) yansıtılması gerekir.
2. **Yönetişim**: Yönetim kurulu üyeliği için aday gösterme, imtiyazlı pay (TTK m.478-479), veto/önemli işlem onay listesi.
3. **Oy sözleşmeleri**: Oy hakkının kullanımına ilişkin sözleşmeler geçerlidir; ancak TTK'nın emredici nisap ve eşit işlem ilkesi (TTK m.357) sınır oluşturur.
4. **Çıkış mekanizmaları**: Birlikte satma hakkı (tag-along), birlikte satışa zorlama (drag-along), ön alım (pre-emption), alım/satım opsiyonları (call/put); TTK m.493 bağlam sınırları gözetilir.
5. **Kilitlenme çözümü**: Deadlock için Texas shootout / Russian roulette gibi mekanizmalar; emredici hükümlere aykırılık denetimi.
6. **Yaptırım**: İhlalde cezai şart (TBK m.179) ve aynen ifa talebi sınırları.
7. **İspat yükü**: SHA ihlalini ileri süren taraf ispatlar.

## Çıktı modülleri
- SHA madde başlıkları iskeleti
- Yönetişim ve veto matrisi
- Tag/drag/ön alım klozları
- Esas sözleşmeye taşınacak hükümler listesi

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
