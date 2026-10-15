---
name: vakia-kronolojisi
description: "Olayların ve usul işlemlerinin tarih sırasıyla dizilmesi, her vakıanın dayandığı evraka bağlanması ve zaman içindeki boşlukların görülmesi gerektiğinde kullan."
---

# Vakıa Kronolojisi

## Görev
Maddi olayları ve usul işlemlerini tarih sırasıyla dizip her birini dayandığı belgeye bağlayarak dosyanın zaman çizgisini ve boşluklarını görünür kılmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın başlangıç olayı (sözleşme, kaza, fesih, suç tarihi) hangi tarih?
- Hangi evrak hangi olayı belgeliyor (sözleşme, fatura, tutanak, tebligat)?
- Maddi olay kronolojisi mi, usul işlemleri kronolojisi mi, yoksa ikisi birden mi?
- Tarih çelişkisi yaratan belgeler var mı?

## Denetim şeması
1. Olay satırı: tarih, olay/işlem, dayanak evrak (ad + sayfa), tarafı. Tarih belirsizse [doldurulacak] yaz; yaklaşık tarih uydurma.
2. Maddi olay - usul ayrımı: maddi vakıalar (zamanaşımı ve hak düşürücü süre başlangıcı için kritik) ile usul işlemleri (tebligat, duruşma, ara karar) ayrı renk/kolon.
3. Süre tetikleyici tespiti: her olayın bir süreyi başlatıp başlatmadığını işaretle (tebligat → cevap süresi HMK m.127; karar tebliği → istinaf süresi HMK m.345). Bu satırlar süre takvimine devredilir.
4. Boşluk ve çelişki: kronolojideki açıklanamayan aralıklar ve çelişen tarihler ayrı not. İspat yükü (HMK m.190) açısından hangi vakıayı kimin ispatlaması gerektiğini belirt.
5. Ara sonuç: zaman çizgisi + süre tetikleyici işaretleri + boşluk listesi. Her satır kaynağa bağlı; belgesiz vakıa eklenmez.

## Çıktı modülleri
- Tarih-olay-dayanak-taraf kolonlu kronoloji tablosu.
- Süre tetikleyici olaylar alt listesi.
- Tarih boşlukları ve çelişkileri notu.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
