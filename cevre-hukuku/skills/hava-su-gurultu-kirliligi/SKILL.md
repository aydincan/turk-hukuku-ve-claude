---
name: hava-su-gurultu-kirliligi
description: "Emisyon, atıksu deşarjı, hava kalitesi ve çevresel gürültü kaynaklı kirlilik iddialarında, limit aşımı tespitinde ve komşuluk hukuku ile kesişen rahatsızlık uyuşmazlıklarında; ölçüm ve numune usulünün denetiminde kullan."
---

# Hava, Su ve Gürültü Kirliliği

## Görev
Hava emisyonu, su deşarjı ve çevresel gürültü kaynaklı kirlilik iddialarını sınır değerler ve ölçüm usulü üzerinden denetlemek; idari yaptırım, faaliyet durdurma ve özel hukuk taleplerini birlikte ele almak.

## Soğuk başlangıç (intake)
1. Hangi unsur: hava emisyonu, atıksu deşarjı, içme/yüzey suyu, çevresel gürültü?
2. Limit aşımı iddiası hangi ölçüme dayanıyor; ölçümü kim, hangi yöntemle yaptı?
3. Etkilenen taraf var mı (komşu tesis, yerleşim, sulak alan)?
4. Talep idari yaptırım mı, faaliyet durdurma mı, tazminat/el atma mı?

## Denetim şeması
1. **Sınır değerler**: Sanayi Kaynaklı Hava Kirliliğinin Kontrolü ve Su Kirliliği Kontrolü Yönetmelikleri ile Çevresel Gürültü Yönetmeliği sektörel limitleri belirler; 2872 m.8 ve m.11 kirletme yasağı ve arıtma yükümlülüğünün dayanağıdır.
2. **Ölçüm/numune usulü**: Numunenin akredite laboratuvarca, usulüne uygun alınması ve zincirin korunması esastır; usulsüz ölçüm hem yaptırımı hem de iddiayı çürütür.
3. **İdari sonuç**: Limit aşımında 2872 m.20-23 idari para cezası ve m.15 faaliyet durdurma uygulanır; tekerrür ağırlaştırıcıdır.
4. **Özel hukuk kesişimi**: Sürekli kirlilik/rahatsızlık komşuluk hukukunda el atmanın önlenmesi (TMK m.683, m.737 katlanma sınırı) ve TBK m.49 vd. tazminat talebi doğurabilir; görevli mahkeme adli yargıdır.
5. **İspat ve ara sonuç**: Bilirkişi, keşif ve karşı ölçüm belirleyicidir; ölçümler arasındaki çelişki ek/yeniden bilirkişiyi gerektirir.

## Çıktı modülleri
- Limit aşımı tespit tablosu (parametre + sınır + ölçüm)
- Ölçüm/numune usul denetim notu
- İdari yaptırım ve özel hukuk talep ayrımı
- Bilirkişi/keşif delil planı

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
