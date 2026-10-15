---
name: zamanasimi-sureler
description: "Sigorta tazminatı, rücu veya zorunlu sigorta taleplerinde zamanaşımı süresinin hesaplanması, başlangıç anı, kesilme-durma ve uzamış ceza zamanaşımı tartışıldığında kullanılır; süre kaybı riskini önlemek için başvurulacak beceri."
---

# Süreler ve Zamanaşımı (Sigorta İstemleri)

## Görev
Sigorta sözleşmesinden ve zorunlu sigortalardan doğan istemlerin zamanaşımını doğru hesaplamak: süre, başlangıç anı, kesilme/durma ve uzamış ceza zamanaşımının uygulanıp uygulanmayacağı.

## Soğuk başlangıç (intake)
1. İstem türü ne: tazminat, prim, rücu, zorunlu trafik sigortası tazminatı?
2. Riziko/ödeme tarihi ve talep tarihi nedir?
3. Olay aynı zamanda suç oluşturuyor mu (ceza zamanaşımı?)
4. Daha önce başvuru/ihtar/dava ile süre kesildi mi?

## Denetim şeması
1. **Genel kural — TTK m.1420.** Sigorta sözleşmesinden doğan bütün istemler iki yılda; sigorta tazminatına/bedeline ilişkin istemler her halde rizikonun gerçekleştiği tarihten itibaren altı yılda zamanaşımına uğrar. Ara sonuç: hangi sürelerden hangisi önce dolar?
2. **Sorumluluk sigortaları.** Sorumluluk sigortalarında zarar görenin doğrudan talebi ve özel süreler; rücu istemlerinde başlangıç ödeme tarihidir.
3. **Zorunlu trafik sigortası — KTK m.109.** Kural iki yıl (zararın ve sorumlunun öğrenildiği tarihten) ve her halde kaza tarihinden sekiz yıl. **Uzamış ceza zamanaşımı:** fiil suç oluşturup TCK'da daha uzun zamanaşımı öngörülüyorsa o (daha uzun) süre tazminat istemi için de uygulanır (KTK m.109/3).
4. **Kesilme ve durma.** TBK m.154-158 ve m.153 (durma); sigortacıya başvuru, dava, tahkim başvurusu, borç ikrarı süreyi keser. İhtar tek başına kesmez; usulüne uygun talep gerekir.
5. **Hak düşürücü süreler.** Cayma için on beş gün (TTK m.1440), prim ihtar süresi (m.1434); bunlar zamanaşımından farklı, durmaz/kesilmez. İspat: zamanaşımı definin koşullarını ileri süren taraf.

## Çıktı modülleri
- İstem bazında zamanaşımı tablosu (süre / başlangıç / dolma tarihi).
- Uzamış ceza zamanaşımı değerlendirmesi (KTK m.109/3).
- Kesilme/durma olayları kronolojisi.
- Acil süre uyarısı ve önerilen koruyucu işlem (dava/başvuru).

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
