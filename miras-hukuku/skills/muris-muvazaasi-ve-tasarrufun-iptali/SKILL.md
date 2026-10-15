---
name: muris-muvazaasi-ve-tasarrufun-iptali
description: "Mirasbırakanın mirasçıdan mal kaçırmak için yaptığı görünüşte satış/devir işlemlerine ya da geçersiz vasiyetnameye karşı iptal/butlan davası kurarken; muvazaa, ehliyetsizlik, şekil sakatlığı ve irade fesadı iddialarında kullanılır."
---

# Muris Muvazaası ve Ölüme Bağlı Tasarrufun İptali

## Görev
Mirastan mal kaçırma amaçlı muvazaalı sağlararası işlemleri ve geçersiz ölüme bağlı tasarrufları geçersiz kılmak; muris muvazaası (TBK m.19) ile vasiyet iptali (TMK m.557-559) yollarını ayırmak.

## Soğuk başlangıç (intake)
- İhtilaflı işlem sağlararası devir mi (tapuda satış/bağış), ölüme bağlı tasarruf mu?
- Devir bedeli gerçekten ödendi mi? Alıcının ödeme gücü ve akrabalık?
- Davacı saklı paylı mı, yoksa tüm mirasçı mı? (muvazaada herkes, tenkiste yalnız saklı paylı)
- Vasiyette şekil sakatlığı, ehliyetsizlik veya irade fesadı iddiası var mı?
- İşlemin/ölümün tarihi ve öğrenme tarihi?

## Denetim şeması
1. **Muris muvazaası (TBK m.19; 1.4.1974 t. 1/2 İBK çerçevesi):** Mirasbırakan, mirasçıdan mal kaçırmak için taşınmazı görünüşte satar ama gerçekte bağışlar. Görünüşteki sözleşme muvazaadan, gizli bağış şekil eksikliğinden geçersizdir; tapu iptali ve tescil istenir. Süreye/saklı pay şartına tabi değildir; tüm mirasçılar açabilir.
2. **Muvazaa ölçütleri:** Mirasbırakanın kaçırma saiki, bedel-değer dengesizliği, satış için makul ihtiyaç yokluğu, taraflar arası ilişki, ödeme delili yokluğu. Yargıtay yerleşik içtihadına bakılır — künyeler doğrulanmadan zikredilmemeli, karararama.yargitay.gov.tr'den `[doğrulanacak]`.
3. **Tenkisten ayır:** Gerçek (gizleme amacı olmayan) bağışta muvazaa değil tenkis yolu işler. Sıralamada: önce muvazaa, başarısızsa terditli tenkis.
4. **Vasiyet iptali (m.557):** Ehliyetsizlik, irade sakatlığı (yanılma-aldatma-korkutma), hukuka/ahlaka aykırı içerik, şekle aykırılık. Hak düşürücü süre (m.559): iptal sebebi ve ölümün öğrenilmesinden 1 yıl, her hâlde iyiniyetlilere karşı 10, kötüniyetlilere 20 yıl.
5. **Ara sonuç:** doğru dava türü (iptal-tescil / vasiyet iptali / terditli tenkis), görev (asliye hukuk), yetki (taşınmaz — HMK m.12).

## Çıktı modülleri
- Tapu iptali ve tescil (muris muvazaası) dava dilekçesi taslağı
- Terditli tenkis talebi entegrasyonu
- Muvazaa karine ve delil listesi (tanık, ödeme, banka)
- Vasiyetnamenin iptali dava taslağı (süre uyarılı)

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
