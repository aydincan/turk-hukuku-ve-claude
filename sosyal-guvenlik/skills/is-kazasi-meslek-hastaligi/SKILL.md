---
name: is-kazasi-meslek-hastaligi
description: "İş kazası veya meslek hastalığı bildirimi, sürekli iş göremezlik gelirinin bağlanması, işverenin/üçüncü kişinin kusuru ve SGK rücu boyutu söz konusu olduğunda; hem sigortalı hem işveren cephesinden kullanılır."
---

# İş Kazası ve Meslek Hastalığı

## Görev
Olayın iş kazası/meslek hastalığı niteliğini saptamak, sigortalıya sağlanacak edimleri ve işveren/üçüncü kişi sorumluluğu ile Kurumun rücu hakkını çözümlemek.

## Soğuk başlangıç (intake)
- Olay nerede, ne zaman, hangi koşulda gerçekleşti; sigortalı görevde miydi?
- SGK'ya iş kazası bildirimi yapıldı mı, ne zaman?
- Sürekli iş göremezlik derecesi (maluliyet oranı) tespit edildi mi?
- İşverenin İSG yükümlülüğü ihlali veya üçüncü kişi kusuru var mı?

## Denetim şeması
1. İş kazası tanımı — 5510 m.13: Sigortalının işyerinde, işveren talimatıyla başka yere giderken, görevle ilgili olarak vb. uğradığı olay. Tanıma giren bağlantı (illiyet) kurulur.
2. Meslek hastalığı — m.14: İşin niteliğinden kaynaklanan, yükümlülük süresi ve hastalık listesi ölçütleriyle tespit. SGK Yüksek Sağlık Kurulu/ATK raporu belirleyici.
3. Bildirim: İşveren iş kazasını m.13 ve İş Sağlığı ve Güvenliği Kanunu (6331 m.14) uyarınca süresinde bildirmekle yükümlüdür; bildirmeme rücu ve ceza doğurur.
4. Edimler: Geçici iş göremezlik ödeneği (m.18), sürekli iş göremezlik geliri (m.19), ölüm halinde hak sahiplerine gelir (m.20).
5. Sorumluluk ve rücu — m.21: Kaza işverenin kastı/kusuru veya İSG ihlali sonucu ise SGK, yaptığı masraf ve bağladığı geliri işverene rücu eder. Kusur oranı bilirkişiyle saptanır; ispat yükü kusurda Kuruma/davacıya aittir. Ara sonuç: maluliyet, edim ve rücu tutarı.

## Çıktı modülleri
- Olay nitelendirme notu (iş kazası/meslek hastalığı unsurları).
- Edim ve maluliyet özeti.
- İşverene karşı rücu/maddi-manevi tazminat değerlendirmesi (TBK m.49-55 ile bağlantı).

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
