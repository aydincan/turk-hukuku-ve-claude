---
name: sureler-ve-zamanasimi
description: "Taşıma alacak ve tazminat taleplerinde ihbar/rezerv süreleri ile zamanaşımının (TTK 1/3 yıl, CMR 1/3 yıl) hesaplanması, başlangıç anının ve durma-kesilme hallerinin belirlenmesi gerektiğinde kullanılır."
---

# Süreler ve Zamanaşımı

## Görev
Taşımaya özgü kısa zamanaşımı ve hak düşürücü/ihbar sürelerini doğru hesaplamak; başlangıç anı, durma ve kesilme hallerini saptayarak hak kaybını önlemek.

## Soğuk başlangıç (intake)
1. Talep neyden doğuyor: ziya, hasar, gecikme, taşıma ücreti mi?
2. Taşıma TTK'ya mı CMR'ye mi tabi?
3. Teslim/teslim için kararlaştırılan tarih nedir; olaydan bu yana ne kadar geçti?
4. Taşıyıcının kastı veya ağır kusuru iddia ediliyor mu?

## Denetim şeması
1. **TTK zamanaşımı:** TTK m.855/1 — taşıma sözleşmesinden doğan bütün istemler bir yılda zamanaşımına uğrar. m.855/2 — taşıyıcının kastı veya kasta eş kusuru (m.886 anlamında) varsa süre üç yıldır.
2. **Başlangıç anı (TTK):** Genel kural teslim tarihi; ziyada eşyanın teslim edilmesi gereken tarih; gecikmede teslim tarihi (m.855/3 atfıyla belirlenir).
3. **CMR zamanaşımı:** CMR m.32 — kural 1 yıl; kasıt veya lex fori'ye göre kasta eş kusurda 3 yıl. Başlangıç: kısmi ziya/hasar/gecikmede teslim günü; tam ziyada teslim için kararlaştırılan sürenin bitiminden 30 gün (veya kararlaştırılmamışsa 60 gün) sonra (m.32/1).
4. **Durma/kesilme (CMR):** m.32/2 — yazılı talep zamanaşımını durdurur; taşıyıcının yazılı reddi ve belgelerin iadesiyle yeniden işler. Sonraki aynı konulu taleplerin durdurucu etkisi yoktur.
5. **İhbar/rezerv süreleri:** Ayrıca TTK m.889 / CMR m.30 süreleri (teslimde, 7 gün, 21 gün) hak/karine kaybına yol açar — zamanaşımından ayrı izlenir.
6. **Defi niteliği:** Zamanaşımı def'i taraflarca ileri sürülmedikçe hâkim re'sen dikkate almaz (TBK m.161).
7. **Ara sonuç:** Talebin canlı/zamanaşımına uğramış olduğu ve durdurma imkânları.

## Çıktı modülleri
- Zamanaşımı hesap tablosu (başlangıç, süre, bitiş; TTK/CMR ayrı).
- İhbar/rezerv süresi takvimi.
- Süreyi durdurma/kesme stratejisi notu (yazılı talep, dava, takip).

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
