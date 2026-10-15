---
name: genel-kurul-tutanagi-ve-tescil
description: "Toplanti tutanaginin icerigi, baskanlik divani, Bakanlik temsilcisi imzasi, kararlarin ticaret siciline tescil ve ilani ile internet sitesi yukumlulukleri konusunda taslak veya denetim gerektiginde kullanilir."
---

# Genel Kurul Tutanağı ve Tescil

## Görev
Genel kurul tutanağını mevzuata uygun düzenlemek; tescile tabi kararların ticaret siciline tescil ve ilanı ile internet sitesi yükümlülüklerini denetlemek.

## Soğuk başlangıç (intake)
1. Toplantı başkanlığı (divan) usulüne uygun oluştu mu; Bakanlık temsilcisi imzası gerekli mi?
2. Hangi kararlar tescile tabi (esas sözleşme değişikliği, sermaye, organ seçimi)?
3. Toplantı fiziki mi, elektronik genel kurul (EGK) mı?
4. Tutanak ve ekleri (hazır bulunanlar listesi, vekâletnameler) tam mı?

## Denetim şeması
1. **Tutanak içeriği:** Tutanak; toplantı yeri-tarihi, hazır pay/oy miktarı, gündem, kararlar, her karara ilişkin oy sonuçları, muhalefet şerhleri ve sorulan soruların cevaplarını içerir; toplantı başkanlığı ve Bakanlık temsilcisi (varsa) tarafından imzalanır (m.422). Eksik/çelişkili tutanak ispatı zayıflatır ve iptal riskine zemin hazırlar.
2. **Muhalefet şerhi:** İptal davası açacak pay sahibinin (toplantıda hazır olup) karara karşı **muhalefetini tutanağa geçirtmiş** olması gerekir (m.446/1-b); bu kayıt davacı sıfatının ön şartıdır. Şerhin açık ve karara özgülenmiş olması önemlidir.
3. **Tescil ve ilan:** Tescile tabi kararlar, toplantıyı izleyen süre içinde ticaret siciline tescil ve TTSG'de ilan ettirilir; YK tescil ödevini yerine getirir. İptal davasında üç aylık süre, kararın alınmasından (kural) işler; tescil tarihi ayrıca ilan ve sicil kaydı için önemlidir.
4. **İnternet sitesi/EGK:** m.1524 kapsamındaki şirketlerde internet sitesine konulması zorunlu içerikler ile pay senetleri borsada işlem gören şirketlerde elektronik genel kurul (EGK) zorunluluğu denetlenir; EGK'de m.1527 ve ilgili yönetmelik uygulanır.
5. **İspat yükü/ara sonuç:** Tutanağın usule uygunluğunu şirket gösterir. Tutanağın imzasız/eksik olması veya zorunlu tescilin yapılmaması, üçüncü kişilere karşı hüküm ve sorumluluk sonuçları doğurur; karar geçerliliğini doğrudan değil, ispat ve aleniyet yönünden etkiler.

## Çıktı modülleri
- Genel kurul tutanağı taslağı (divan + temsilci imza blokları).
- Muhalefet şerhi örnek metni.
- Tescil/ilan ve internet sitesi yükümlülük kontrol listesi.

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
