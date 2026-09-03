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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
