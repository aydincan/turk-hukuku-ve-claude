---
name: sure-zamanasimi-hakduserme
description: "Dava açma, cevap, kanun yolu sürelerini hesaplamak; zamanaşımı ile hak düşürücü süreyi ayırmak ve süre risklerini erken yakalamak gerektiğinde kullanılır."
---

# Süreler, Zamanaşımı ve Hak Düşürücü Süreler

## Görev
Her layihada önce süreyi çözmek: dava açma, cevap, kanun yolu ve maddi hukuk süreleri. Süre kaçırılırsa içerik ne kadar sağlam olursa olsun hak kaybedilir; bu beceri erken uyarı sistemidir.

## Soğuk başlangıç (intake)
- Hangi olay tarihi/tebliğ tarihi süreyi başlatıyor?
- Zamanaşımı mı, hak düşürücü süre mi söz konusu?
- Süreyi durduran/kesen bir işlem var mı (ihtar, dava, başvuru)?
- Süre tatile/adli tatile denk geliyor mu?

## Denetim şeması
1. Zamanaşımı vs. hak düşürücü süre: Zamanaşımı def'i ileri sürülmedikçe hâkim re'sen dikkate almaz (TBK m.161); durur/kesilir (TBK m.153-156). Hak düşürücü süre re'sen gözetilir, durmaz/kesilmez.
2. Maddi hukuk süreleri (örnekler): Genel zamanaşımı TBK m.146 — 10 yıl; haksız fiil TBK m.72 — fiil ve failin öğrenilmesinden 2, her hâlde 10 yıl; ayıpta TBK m.231 / TKHK m.12. Boşanmada affı izleyen hak düşürücü süreler TMK m.161-162.
3. Usul süreleri: HMK cevap iki hafta (m.127); istinaf iki hafta (m.345); İYUK dava açma 60/30 gün (m.7); CMK itiraz yedi gün (m.268), şikâyet TCK m.73 — 6 ay.
4. Sürelerin hesabı (HMK m.92-94): Gün/hafta/ay hesabı; sürenin son günü resmî tatilse ilk iş gününe uzar. Adli tatil (HMK m.102-104) etkisini kontrol edin.
5. Durma/kesilme: Dava açılması, ihtar, icra takibi, kısmi ödeme/ikrar zamanaşımını keser (TBK m.154). Ara sonuç: son gün netleşip risk işaretlenir.

## Çıktı modülleri
- Süre takvimi (başlangıç → son gün)
- Zamanaşımı/hak düşürücü ayrım notu
- Durma-kesilme olayları listesi
- Süre riski uyarısı (kritik/yakın/güvenli)

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
