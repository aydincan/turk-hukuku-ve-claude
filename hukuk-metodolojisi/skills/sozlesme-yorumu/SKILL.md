---
name: sozlesme-yorumu
description: "Bir sözleşme maddesinin ya da irade beyanının anlamı taraflar arasında çekişmeliyse; lafza mı gerçek ortak iradeye mi üstünlük verileceğini ve boşlukların nasıl doldurulacağını çözmek için kullanılır."
---

# Sözleşme ve İrade Beyanlarının Yorumu

## Görev
Çekişmeli bir sözleşme hükmünü ya da irade beyanını TBK m.19 ve güven ilkesi çerçevesinde yorumlamak, boşlukları tamamlamak ve geçersizlik/uyarlama ihtimallerini gözetmek.

## Soğuk başlangıç (intake)
- Hangi madde/ifade tartışmalı; tarafların ona yüklediği iki anlam ne?
- Sözleşme metni dışında yazışma, teamül, önceki ilişki var mı?
- Hüküm tip sözleşme/genel işlem koşulu mu, bireysel müzakere ürünü mü?
- Bu bir ticari iş mi (ticari teamül ağırlığı) yoksa tüketici işlemi mi?

## Denetim şeması
1. **Gerçek irade önce — TBK m.19** — Yorumda tarafların gerçek ve ortak iradesi esastır; yanlış yazılmış sözcük/deyim tarafları bağlamaz (*falsa demonstratio non nocet*). Lafız, iradenin tespitinde başlangıç noktasıdır, son söz değil.
2. **Güven ilkesi** — Gerçek ortak irade saptanamıyorsa, beyan, dürüst ve makul bir muhatabın anlayacağı şekilde (güven teorisi) yorumlanır.
3. **Yardımcı ölçütler** — Sözleşmenin amacı, bütünlüğü (maddeler birbirini açıklar), kuruluş öncesi/sonrası davranışlar, teamül ve ticari örf; tereddütte düzenleyenin aleyhine yorum (genel işlem koşullarında).
4. **Boşluk tamamlama** — Düzenlenmeyen nokta için önce yedek hukuk kuralı (tamamlayıcı emredici olmayan hükümler), yoksa TMK m.2 dürüstlük kuralıyla varsayımsal taraf iradesi.
5. **Geçerlilik süzgeci** — Yorumdan sonra: emredici hükümlere, kamu düzenine, ahlaka, kişilik hakkına aykırılık (TBK m.27) ve genel işlem koşullarında haksız şart denetimi (TBK m.20-25) yapılır.
6. **Uyarlama** — Aşırı ifa güçlüğü/öngörülemeyen değişiklikte TBK m.138 (işlem temelinin çökmesi) ile uyarlama/dönme değerlendirilir.

## Çıktı modülleri
- Tartışmalı madde + iki rakip okuma.
- Gerçek irade / güven ilkesi analizi.
- Boşluk varsa tamamlayıcı kural önerisi.
- Geçerlilik ve uyarlama uyarıları + `[doğrulanacak]` içtihat.

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
