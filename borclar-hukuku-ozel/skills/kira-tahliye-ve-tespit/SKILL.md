---
name: kira-tahliye-ve-tespit
description: "Konut veya çatılı işyeri kirasında tahliye davası, kira bedelinin tespiti veya artış uyuşmazlığı söz konusu olduğunda; doğru tahliye sebebini, süreyi ve usulü belirlemek için kullanılır."
---

# Kira — Tahliye Sebepleri ve Kira Tespiti

## Görev
Konut ve çatılı işyeri kiralarında (TBK m.339 vd.) tahliye sebebini doğru seçmek, hak düşürücü süreleri tutmak, kira tespiti/artış uyuşmazlığını TBK m.344-345 çerçevesinde çözmek; emredici hükümleri gözetmek.

## Soğuk başlangıç (intake)
- Taşınmaz konut mu çatılı işyeri mi; sözleşme yazılı mı, başlangıç ve süre?
- Tahliye sebebi ne (gereksinim, yeniden inşa, taahhüt, iki haklı ihtar, temerrüt)?
- Kira güncel mi; artış nasıl belirlenmiş, tespit mi isteniyor?
- İhtar/ihbar yapıldı mı, tarihleri?

## Denetim şeması
1. **Sebebi sınıflandır.** Kiraya verenden kaynaklı: gereksinim (m.350/1), yeniden inşa-imar (m.350/2), yeni malikin gereksinimi (m.351). Kiracıdan kaynaklı: yazılı tahliye taahhüdü (m.352/1), bir kira yılında iki haklı ihtar (m.352/2), kira bedelini ödemede temerrüt (m.315 ile 30 günlük ihtarlı süre).
2. **Süre disiplini.** Gereksinim/yeniden inşada belirli sürede sürenin sonunda, belirsizde fesih dönemi + 1 ay içinde dava; her halde sebebin doğumundan itibaren 1 ay içinde tahliye davası (m.353). Taahhütte taahhüt edilen tarihten itibaren 1 ay.
3. **Kira tespiti (m.344-345).** Artış, bir önceki kira yılı TÜFE on iki aylık ortalamasını geçemez (m.344/1). Beş yıldan uzun/yenilenen sözleşmede hâkim hakkaniyetle belirler (m.344/3). Tespit davası her zaman açılabilir; yeni dönem başından en az 30 gün önce ihtar veya dava ile istenirse o dönemden itibaren geçerli.
4. **Temerrütle tahliye (m.315).** Konut/çatılıda 30 günlük süreli yazılı ihtar; ödenmezse tahliye + İİK m.269 ilamsız tahliye yolu seçeneği.
5. **Emredici taban (m.346-354).** Kiracı aleyhine düzenleme yasağı; cezai şart/muacceliyet kayıtları (m.346) geçersiz. İspat: tahliye sebebinin maddi vakıalarını davacı; ödemeyi kiracı ispatlar.
6. **Ara sonuç:** Sebep + süre + yargı yolu (Sulh Hukuk, HMK m.4) ve dava şartı arabuluculuk (kira uyuşmazlıkları) kontrolü.

## Çıktı modülleri
- Tahliye ihtarnamesi / 30 günlük temerrüt ihtarı taslağı.
- Kira tespiti dava dilekçesi iskeleti (TÜFE/hakkaniyet ayrımı).
- Sebep-süre takvimi tablosu.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
