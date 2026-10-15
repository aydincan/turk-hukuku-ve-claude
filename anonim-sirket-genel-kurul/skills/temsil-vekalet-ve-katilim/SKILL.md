---
name: temsil-vekalet-ve-katilim
description: "Pay sahibinin genel kurulda vekille temsili, organ temsilcisi, tevdi eden ve bagimsiz temsilci, hazir bulunanlar listesi ve katilma hakki konularinda taslak veya denetim gerektiginde kullanilir."
---

# Temsil, Vekâlet ve Katılım

## Görev
Pay sahibinin genel kurula bizzat veya temsilci aracılığıyla katılımını düzenlemek; temsil belgelerini hazırlamak ve hazır bulunanlar listesinin doğruluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Pay sahibi gerçek kişi mi, tüzel kişi mi; temsilci pay sahibi olmak zorunda mı (esas sözleşme şartı)?
2. Halka açık şirket mi (kurumsal temsilci/organın temsilcisi düzenlemeleri farklılaşır)?
3. Paylar bir bankaya/aracı kuruma mı tevdi edilmiş (tevdi eden temsilcisi)?
4. Temsil belgesi yazılı ve usulüne uygun mu; çıkar çatışması var mı?

## Denetim şeması
1. **Temsil ilkesi:** Pay sahibi paylarını GK'de temsilci aracılığıyla da kullandırabilir; temsilcinin pay sahibi olması şart değildir; esas sözleşmedeki aksine hüküm temsilci yönünden geçersizdir (m.425). Temsil için yazılı yetki belgesi gerekir.
2. **Özel temsilci türleri:** Organın temsilcisi, bağımsız temsilci ve kurumsal temsilci için çağrıda öneri yapılır ve şirketin internet sitesinde duyurulur (m.428); tevdi eden temsilcisi, payları tevdi eden adına oyu talimata uygun kullanır (m.429-430). Bu temsilciler talimat ve açıklama yükümlülüğüne tabidir.
3. **Hazır bulunanlar listesi:** Toplantıya katılanların ad, pay miktarı, oy sayısı ve temsil bilgileri listede gösterilir; liste YK ve toplantı başkanlığınca imzalanır (m.415, m.417). Liste, nisap ve oy hesabının temel ispat aracıdır.
4. **Çıkar çatışması:** Temsilcinin m.436 kapsamına giren işlerde oy kullanması yasaktır; vekâletin bu sınırı aşması iptal sebebi yaratır.
5. **İspat yükü/ara sonuç:** Temsil yetkisinin varlığını temsilci/pay sahibi belgeyle ispatlar. Geçersiz temsille kullanılan oylar nisap dışı bırakılır; sonuç değişiyorsa karar iptale açıktır.

## Çıktı modülleri
- Vekâletname/temsil belgesi taslağı (yetki kapsamı ve talimatlı).
- Hazır bulunanlar listesi şablonu.
- Temsil geçerlilik kontrol listesi ve çıkar çatışması uyarısı.

## Plugin bağlamı

Bu beceri `anonim-sirket-genel-kurul` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
