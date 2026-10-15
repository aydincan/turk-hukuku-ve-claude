---
name: zamanasimi-ve-sureler
description: "Haksız fiil tazminat talebinin süre yönünden hâlâ ileri sürülebilir olup olmadığı tartışmalıysa; iki yıllık, on yıllık ve daha uzun ceza zamanaşımı sürelerini hesaplamak için kullanılır."
---

# Zamanaşımı ve Süreler

## Görev
Tazminat talebinin TBK m.72 zamanaşımı süreleri içinde olup olmadığını belirlemek: zarar ve failin öğrenilmesinden 2 yıl; her hâlde fiilden 10 yıl; fiil aynı zamanda suç oluşturuyorsa daha uzun ceza zamanaşımı. Süre, davanın kaderini doğrudan belirlediğinden ilk kontrol edilen unsurlardandır.

## Soğuk başlangıç (intake)
- Fiil/zarar hangi tarihte gerçekleşti?
- Zarar gören zararı ve faili ne zaman öğrendi (öğrenme tarihi belgeli mi)?
- Fiil aynı zamanda suç oluşturuyor mu (ceza zamanaşımı imkânı)?
- Daha önce ihtar, dava, takip ile zamanaşımı kesildi mi?

## Denetim şeması
1. **İki yıllık nispi süre (m.72/1).** Zarar görenin hem zararı hem tazminat yükümlüsünü (faili) öğrendiği tarihten itibaren 2 yıl. İkisi birlikte öğrenilmeden süre başlamaz.
2. **On yıllık mutlak süre (m.72/1).** Öğrenme olmasa dahi fiilin gerçekleştiği tarihten itibaren 10 yılda zamanaşımı dolar; bu, üst sınırdır.
3. **Ceza zamanaşımı (m.72/1 son cümle).** Fiil aynı zamanda bir suç oluşturuyor ve ceza kanunu daha uzun bir zamanaşımı öngörüyorsa, tazminat talebine de bu daha uzun süre uygulanır (TCK m.66 süreleri). Suç vasfı ayrıca değerlendirilir.
4. **Kesme ve durma.** Dava açılması, takip, borçlunun ikrarı zamanaşımını keser (TBK m.154); kesilmeyle yeni süre işler (m.156). Durma sebepleri (m.153) ayrıca kontrol edilir.
5. **Rücu zamanaşımı.** Müteselsil sorumlular arası rücu talebinde özel süre rejimi (m.73) işletilir; ödeme tarihi esas alınır.
6. **Ara sonuç.** Süre tablosu kurulur (başlangıç-bitiş, kesme/durma); süre yakınsa ihtiyati önlem (dava/ihtar) önerilir, dolmuşsa def'i riski açıkça yazılır. Zamanaşımı def'i ileri sürülmedikçe hâkim resen dikkate almaz.

## Çıktı modülleri
- Süre takvimi (öğrenme/fiil tarihi + 2/10/ceza süresi).
- Kesme-durma olayları zaman çizelgesi.
- Süre riski uyarısı ve önerilen acil adım.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
