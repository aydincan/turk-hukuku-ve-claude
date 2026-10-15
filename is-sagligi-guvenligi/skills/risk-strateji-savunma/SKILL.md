---
name: risk-strateji-savunma
description: "İşveren veya çalışan tarafı için iş kazası ve uyum riskini değerlendirmek, savunma stratejisi ve sulh-uzlaşma seçeneklerini tartmak için kullanılır."
---

# Risk Stratejisi ve Savunma Planlaması

## Görev
Tarafın konumuna göre (işveren savunması ya da çalışan/hak sahibi talebi) bütüncül risk değerlendirmesi yapmak; idari, tazminat, rücu ve ceza eksenlerini birlikte tartıp strateji ve sulh seçeneklerini önermek.

## Soğuk başlangıç (intake)
- Müvekkil sıfatı ve hedefi (riski sınırlamak / azami tazminat / cezadan kaçınmak)?
- Dört eksenden hangileri açık (idari ceza, tazminat, SGK rücuu, ceza)?
- Kusur oranı/bilirkişi tahmini ve karşı tarafın delil gücü ne?
- Sulh/uzlaşma için tarafların eğilimi ve ödeme kapasitesi var mı?

## Denetim şeması
1. **Çok eksenli risk haritası:** Aynı kaza dört ayrı sonuç doğurur — idari ceza (6331 m.26), işçi/hak sahibi tazminatı (TBK m.417), SGK rücuu (5510 m.21), ceza (TCK m.85-89). Bir eksendeki kusur tespiti diğerlerini güçlü biçimde etkiler; tek strateji tüm eksenleri gözetmeli.
2. **İşveren tarafı:** Önlem ve uyum belgeleriyle kusuru azaltma (önleme hiyerarşisi, eğitim, yazılı uyarı zinciri), müterafik/üçüncü kişi kusuru argümanı, idari cezada usul itirazı, ceza eksende bilinçli taksir-basit taksir ayrımı.
3. **Çalışan/hak sahibi tarafı:** Risk değerlendirmesi/eğitim eksikliği ve önleme hiyerarşisi ihlaliyle kusuru yükseltme, belirsiz alacakla tam talep, manevi tazminat ve destek kalemleri.
4. **Sulh-uzlaşma ekonomisi:** Ceza ekseninde uzlaşma kapsamı, tazminatta makbuz/ibraname riskleri (gerçek iradeyi yansıtmayan ibra geçersiz olabilir), maluliyetin kesinleşmemesi nedeniyle erken sulhün riski.
5. **Senaryo karşılaştırması:** En iyi/orta/en kötü senaryoda mali ve cezai sonuç. **Ara sonuç:** Önerilen strateji + gerekçe + sonraki adımları sırala.

## Çıktı modülleri
- Dört eksenli risk haritası ve etkileşim notu.
- Taraf bazlı argüman ve savunma listesi.
- Sulh/uzlaşma senaryo karşılaştırma tablosu.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
