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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
