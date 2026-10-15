---
name: ihtarname-uzlasma-iletisim
description: "Dava öncesi ihtar çekmek, ihlali durdurma ve lisanslama çözümü için müzakere yürütmek ya da gelen ihtarnameye yanıt vermek gerektiğinde; tebligatlı ihtar ve uzlaşma stratejisini kurmak için kullanılır."
---

# İhtarname, Müzakere ve Karşı Taraf İletişimi

## Görev
İhlali durdurmaya yönelik ihtarname hazırlamak, sonradan lisanslama/uzlaşma müzakeresini yürütmek veya gelen ihtara hukuki ve stratejik yanıt üretmek.

## Soğuk başlangıç (intake)
- Hangi taraftayız (hak sahibi mi, ihlal iddia edilen mi)?
- Hedef ihlalin durması mı, geçmiş kullanım için bedel mi, lisanslama mı?
- Karşı tarafla ticari ilişki sürdürülecek mi?
- Süre/zamanaşımı veya delil kaybı baskısı var mı?

## Denetim şeması
1. Konum tespiti: Hak sahibi tarafında ihlalin hak ve kapsamı (m.20-25) sabitlenir; iddia edilen taraf ise savunma (izin, istisna m.30-40, eser niteliği yokluğu) önceden değerlendirilir.
2. İhtar amacı ve içeriği: İhtarname ihlalin durdurulmasını, nüshaların toplatılmasını ve makul süre talep eder; temerrüt ve faiz başlangıcı için tarih sabitlenir. Noter/KEP ile gönderim ispat değeri sağlar (TBK m.117 temerrüt; tebligat ispatı).
3. Aşırı talepten kaçınma: m.68 üç kat bedel caydırıcı bir koz olsa da müzakerede orantılı, somut emsale dayalı talep güveni artırır; mesnetsiz tehdit karşı tarafa koz verir.
4. Uzlaşma seçenekleri: İhlalin durması + geriye dönük lisans bedeli + ileriye dönük lisans; manevi hak ihlalinde ad belirtilmesi/düzeltme. Anlaşma metni mali hak boyutuyla m.52 yazılı şekle uygun düzenlenir.
5. Gelen ihtara yanıt: Süre tuzaklarından kaçın; ikrar doğuran ifadelerden sakın; eser/sahiplik ve izin/istisna savunmasını ölçülü biçimde bildir, gerekiyorsa ek süre/uzlaşma çağrısı yap.
6. Ara sonuç: Strateji (sert ihtar / müzakere / savunma), mesaj çerçevesi ve sonraki adım takvimi belirlenir.

İspat yükü: ihtar ve içeriğinin tebliği gönderene; izin/istisna savunması iddia edene aittir.

## Çıktı modülleri
- İhtarname taslağı (talep, süre, dayanak, temerrüt notu).
- Müzakere/uzlaşma strateji notu ve sulh metni iskeleti.
- Gelen ihtara yanıt taslağı ve risk uyarıları.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
