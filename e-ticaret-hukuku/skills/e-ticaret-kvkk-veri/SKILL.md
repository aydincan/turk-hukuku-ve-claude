---
name: e-ticaret-kvkk-veri
description: "E-ticaret sitesi veya platformunun müşteri verisi işleme, açık rıza, aydınlatma, çerez ve veri aktarımı yükümlülüklerinin KVKK uyumunun denetlenmesi gerektiğinde kullanılır."
---

# E-Ticarette Kişisel Veri ve KVKK Uyumu

## Görev
E-ticaret faaliyetinde toplanan kişisel verilerin (üyelik, sipariş, ödeme, davranışsal/çerez verisi) 6698 sayılı KVKK'ya uygun işlenmesini denetlemek; ticari ileti onayı ile KVKK rızasının ayrıştırılmasını sağlamak.

## Soğuk başlangıç (intake)
- Hangi veri kategorileri işleniyor (kimlik, iletişim, ödeme, konum, çerez/davranış)?
- İşlemenin hukuki sebebi ne (sözleşmenin ifası, meşru menfaat, açık rıza)?
- Yurt dışına aktarım var mı (yurt dışı ödeme/bulut/pazarlama araçları)?
- Aydınlatma metni, çerez politikası ve VERBİS kaydı mevcut mu?

## Denetim şeması
1. Hukuki sebep (6698 m.5): sipariş/teslim için işleme çoğu kez sözleşmenin ifası (m.5/2-c) ya da meşru menfaate (m.5/2-f) dayanır; pazarlama/profilleme için kural olarak açık rıza gerekir. Rıza, hizmet şartına bağlanamaz.
2. Aydınlatma (6698 m.10): veri sorumlusu kimliği, işleme amaçları, aktarım, toplama yöntemi ve hakları içeren aydınlatma yapılır; ticari ileti onayından ayrı belgelenir.
3. Ticari ileti–KVKK ayrımı: 6563 ileti onayı ile KVKK açık rızası farklı hukuki kurumlardır; tek kutucukla birlikte alınması sakıncalıdır, ayrı ayrı ve özgür iradeyle alınmalıdır.
4. Aktarım (6698 m.9): yurt dışı aktarımda 2024 değişikliği sonrası yeterlilik kararı, uygun güvenceler (standart sözleşme/bağlayıcı kurallar) ya da istisna zemini aranır; standart sözleşme Kurula bildirilir.
5. Güvenlik ve ihlal (6698 m.12): teknik-idari tedbirler; veri ihlalinde Kurula ve ilgili kişiye makul sürede bildirim.
İspat yükü: rıza, aydınlatma ve tedbirlerin varlığını veri sorumlusu ispatlar.

## Çıktı modülleri
- Veri işleme envanteri ve hukuki sebep tablosu.
- Aydınlatma/açık rıza/çerez metni boşluk raporu.
- Aktarım ve ihlal müdahale notu.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
