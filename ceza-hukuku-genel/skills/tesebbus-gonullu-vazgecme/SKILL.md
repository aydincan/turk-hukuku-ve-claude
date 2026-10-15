---
name: tesebbus-gonullu-vazgecme
description: "Suçun tamamlanmadığı, icra hareketlerine başlanıp netice gerçekleşmediği durumlarda teşebbüs ile gönüllü vazgeçme ayrımını ve ceza sonuçlarını belirlemek gerektiğinde kullanılır."
---

# Teşebbüs ve Gönüllü Vazgeçme

## Görev
İcra hareketlerine başlanmış fakat netice gerçekleşmemiş suçlarda teşebbüs (TCK m.35), gönüllü vazgeçme (m.36) ve elverişsiz teşebbüs ayrımlarını yapıp ceza sonucunu belirlemek.

## Soğuk başlangıç (intake)
- Hazırlık hareketleri mi yapıldı, yoksa icraya başlandı mı?
- Suç neden tamamlanmadı; failin elinde olmayan bir engel mi araya girdi?
- Fail kendi iradesiyle mi durdu, yoksa dış etkenle mi engellendi?
- Kullanılan araç/yöntem neticeyi gerçekleştirmeye elverişli miydi?

## Denetim şeması
1. **İcraya başlama eşiği (m.35/1):** Failin elverişli araçlarla doğrudan doğruya icraya başlaması gerekir; hazırlık hareketleri kural olarak cezalandırılmaz. Ara sonuç: eşik aşıldı mı?
2. **Tamamlanamama nedeni:** Suç, failin elinde olmayan nedenlerle tamamlanamadıysa teşebbüs gündeme gelir.
3. **Teşebbüste ceza (m.35/2):** Meydana gelen zarar/tehlikenin ağırlığına göre cezada indirim; ağırlaştırılmış müebbet/müebbet hapsi gerektiren suçlarda kademeli indirim öngörülür.
4. **Gönüllü vazgeçme (m.36):** Fail icra hareketlerinden gönüllü vazgeçer ya da neticeyi kendi çabasıyla önlerse, teşebbüsten cezalandırılmaz; yalnız o ana kadarki hareketler bağımsız bir suç oluşturuyorsa o suçtan sorumlu olur. Ara sonuç: durma gönüllü mü, dış engel mi?
5. **Elverişsiz teşebbüs / işlenemez suç:** Araç ya da konu neticeyi doğurmaya mutlak elverişsizse cezalandırılabilirlik tartışılır; somut tehlike ölçütü değerlendirilir.
6. **İçtima ile ilişki:** Tamamlanan başka bir suç varsa ayrıca değerlendirilir.

## Çıktı modülleri
- Hazırlık/icra/teşebbüs/gönüllü vazgeçme aşama haritası.
- İndirim oranı ve hesap notu.
- Gönüllü vazgeçme savunması taslağı (somut argümanlarla).
- Eksik vakıa ve `[doğrulanacak]` içtihat listesi.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
