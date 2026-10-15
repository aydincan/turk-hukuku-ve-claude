---
name: bilgi-suistimali-iceriden-ogrenenler
description: "İçsel bilgiye dayalı işlem, içsel bilginin yetkisiz aktarımı veya tavsiye yoluyla kullanılması iddiası ve SPK m.106 kapsamındaki cezai sorumluluk değerlendirileceğinde kullanılır."
---

# Bilgi Suistimali (İçeriden Öğrenenlerin Ticareti)

## Görev
İçsel bilgiye dayalı işlem (insider trading) iddiasını SPK m.106 unsurları üzerinden çözümlemek; failin sıfatı, içsel bilginin niteliği ve işlem-bilgi ilişkisini kurarak ceza ve idari sorumluluk riskini değerlendirmek.

## Soğuk başlangıç (intake)
- İşlemi yapan kim: yönetici, çalışan, danışman, hâkim ortak mı; bilgiye nasıl ulaştı?
- İşleme konu içsel bilgi nedir, ne zaman oluştu ve ne zaman kamuya açıklandı?
- İşlemler bilgi açıklanmadan önce mi yapıldı; kazanç/zarardan kaçınma var mı?
- Müvekkil şüpheli/sanık mı, yoksa savunma/Kurul incelemesine yanıt mı hazırlanıyor?

## Denetim şeması
1. **Fail çevresi:** SPK m.106; içsel bilgiye sıfat veya görev nedeniyle ulaşanlar (yönetici, denetçi, hizmet ilişkisi, hâkim ortak) ile bu bilgiyi bunlardan edinenler kapsamı belirlenir.
2. **İçsel bilgi niteliği:** Bilginin kamuya açıklanmamış, belirli, fiyatı/yatırım kararını önemli ölçüde etkileyebilir nitelikte olduğu saptanır; değilse suç oluşmaz.
3. **Fiil:** Bilgiye dayalı olarak sermaye piyasası aracında işlem yapmak, başkasına yaptırmak, bilgiyi yetkisiz aktarmak veya tavsiyede bulunmak unsurları aranır. Ara sonuç: hangi seçimlik hareketin gerçekleştiği belirlenir.
4. **Manevi unsur ve illiyet:** Kast aranır; işlemin içsel bilgiye dayandığı, emir/işlem kayıtları, zamanlama ve bilgiye erişen listesiyle bağlanır. İspat yükü iddia makamındadır (CMK m.217; şüpheden sanık yararlanır).
5. **Yaptırım ve usul:** Cezai yaptırım m.106; soruşturma/kovuşturma Kurul'un başvurusu/mütalaası şartına bağlıdır (m.115); etkin pişmanlık (m.109) ve aynı fiilin idari yaptırım boyutu ayrıca değerlendirilir. İçtihat için Yargıtay bankası taranır, künye `[doğrulanacak]`.

## Çıktı modülleri
- Unsur unsur suç analizi tablosu (m.106)
- İçsel bilgi-işlem zamanlama kronolojisi
- Savunma/iddia stratejisi ve etkin pişmanlık değerlendirmesi
- Kurul mütalaası/usul yol haritası

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
