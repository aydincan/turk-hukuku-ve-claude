---
name: risk-ve-strateji-toplu-is
description: "Sendika veya isveren tarafi icin toplu sureclerde hukuki ve operasyonel riskleri (yetki dususu, kanun disi grev, sendikal tazminat, idari para cezasi) tartip strateji onerir; bir pazarlik veya catismaya girmeden once konumlandirma gerektiginde kullanilir."
---

# Risk Değerlendirmesi ve Strateji

## Görev
Müvekkilin (sendika veya işveren) toplu süreçteki konumunu risk-fırsat ekseninde tartmak ve uygulanabilir bir strateji önermek. Hukuki doğruluğu ticari/operasyonel gerçeklerle buluşturur.

## Soğuk başlangıç (intake)
- Müvekkil hangi taraf; hedefi nedir (TİS imzası, grevi önleme, maliyet kontrolü)?
- Süreç hangi aşamada (yetki, görüşme, arabuluculuk, grev eşiği)?
- En kötü senaryo (grev, yetki düşmesi, ceza) müvekkil için ne anlama gelir?
- Müzakerede esneklik var mı; kırmızı çizgiler neler?

## Denetim şeması
1. **Yetki riski:** Baraj/çoğunluk tartışmalıysa yetki düşmesi (6356 m.41-44) ile süreç sıfırlanabilir; sendika için kayıt sağlamlaştırma, işveren için itiraz hakkı (m.43) değerlendirilir.
2. **Grev/lokavt riski:** Kanun dışı grev işveren için fesih ve tazminat fırsatı (m.64-67), sendika için ağır risktir; usul kusuru olasılığı baştan ölçülür. İşveren için grev yasağı/erteleme (m.62-63) argümanları haritalanır.
3. **Sendikal tazminat/idari ceza riski:** İşveren için sendikal ayrımcılık (m.25, en az bir yıllık ücret) ve 6356 m.78 idari para cezaları; süreç tasarımı bu riskleri minimize edecek şekilde kurgulanır.
4. **Müzakere kaldıracı:** Sendika açısından grev tehdidi/üye gücü; işveren açısından lokavt, faaliyet sürekliliği planı ve yüksek hakem yolu. Her kaldıracın hukuki sınırı belirtilir.
5. **Ara sonuç:** Senaryolar (anlaşma / arabuluculuk / grev / YHK) olasılık ve maliyetle tartılır; önerilen birincil ve yedek strateji yazılır.

İçtihat eğilimleri için Yargıtay kararları künye `[doğrulanacak]` olarak anılır; uydurma numara verilmez.

## Çıktı modülleri
- Risk matrisi (olasılık × etki).
- Senaryo analizi ve önerilen strateji.
- Kırmızı çizgi / müzakere kaldıracı notu.

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
