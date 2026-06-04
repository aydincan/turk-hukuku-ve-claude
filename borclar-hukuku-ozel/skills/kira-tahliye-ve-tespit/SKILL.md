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
