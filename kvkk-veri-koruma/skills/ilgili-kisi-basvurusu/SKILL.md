---
name: ilgili-kisi-basvurusu
description: "İlgili kişi veri sorumlusuna başvurduğunda ya da başvuru hazırlanırken; m.11 hakları, başvurunun cevaplanması, süreler ve Kurul'a şikâyete geçiş değerlendirilirken kullanılır."
---

# İlgili Kişi Hakları ve Başvuru Yönetimi

## Görev
KVKK m.11'deki hakları kullanan ilgili kişinin başvurusunu veri sorumlusu adına usulüne uygun karşılamak veya ilgili kişi adına başvuru/şikâyet hazırlamak; m.13-15 yolunu doğru işletmek.

## Soğuk başlangıç (intake)
1. Müvekkil başvuruyu yapan ilgili kişi mi, yoksa başvuruyu alan veri sorumlusu mu?
2. Hangi hak kullanılıyor — bilgi/erişim, düzeltme, silme/yok etme, aktarıldığı yere bildirim, itiraz, zararın giderilmesi?
3. Başvuru yazılı mı, KEP/güvenli e-imza/kayıtlı e-posta yoluyla mı yapıldı (Başvuru Tebliği şartı)?
4. Başvuru ne zaman ulaştı (30 günlük süre başlar)?

## Denetim şeması
1. **Haklar — m.11**: İlgili kişi; işlenip işlenmediğini öğrenme, bilgi talep etme, amaca uygun kullanımı öğrenme, aktarıldığı üçüncü kişileri bilme, eksik/yanlış işlenmişse düzeltilmesini, m.7 şartlarında silinmesini/yok edilmesini, bu işlemlerin aktarıldığı yere bildirilmesini, otomatik sistem analiziyle aleyhe sonuç doğmasına itiraz ve zararın giderilmesini isteyebilir.
2. **Veri sorumlusuna başvuru — m.13**: Başvuru Tebliği'ndeki usule uygun yapılır; veri sorumlusu talebi en kısa sürede ve en geç 30 gün içinde sonuçlandırır. İşlemin maliyeti varsa Kurul tarifesi uygulanır.
3. **Kurul'a şikâyet — m.14**: Başvuru reddedilir, eksik yanıtlanır veya 30 günde yanıtlanmazsa; ilgili kişi cevabı öğrendiği tarihten itibaren 30 ve her hâlde başvuru tarihinden itibaren 60 gün içinde Kurul'a şikâyet eder. Veri sorumlusuna başvuru, şikâyet için ön şarttır (zorunlu idari başvuru yolu).
4. **Ara sonuç**: Süresinde ve gerekçeli yanıt vermek hem yaptırımı önler hem ispat sağlar; ret kararı gerekçesiz olamaz.

İspat yükü: Başvurunun süresinde ve gereği gibi yanıtlandığını veri sorumlusu; başvuru yaptığını ve süreyi ilgili kişi ispatlar.

## Çıktı modülleri
- İlgili kişi başvuru dilekçesi taslağı (hangi hak, hangi talep).
- Veri sorumlusu yanıt yazısı şablonu (kabul/ret + gerekçe).
- Kurul'a şikâyet dilekçesi ve süre hesabı notu.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
