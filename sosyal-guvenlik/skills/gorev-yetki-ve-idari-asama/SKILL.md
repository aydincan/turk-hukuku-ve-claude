---
name: gorev-yetki-ve-idari-asama
description: "SGK uyuşmazlıklarında görevli mahkeme (iş mahkemesi), yetki, idari başvuru/itiraz zorunluluğu ve dava açma süresi belirlenmesi gerektiğinde; davanın usulden reddini önlemek için ilk kontrol olarak kullanılır."
---

# Görev, Yetki ve İdari Aşama

## Görev
SGK uyuşmazlığında doğru yargı yolunu, görevli/yetkili mahkemeyi, idari başvuru zorunluluğunu ve süreleri saptayarak davanın usulden reddini önlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık SGK ile mi (sigortalılık, prim, aylık), işveren ile mi (rücu, alacak)?
- SGK'nın yazılı bir işlemi/red kararı var mı; tebliğ tarihi nedir?
- İdari itiraz/başvuru yapıldı mı; süresi geçti mi?
- Sigortalının ikametgâhı ve işyeri hangi yer mahkemesi çevresinde?

## Denetim şeması
1. Yargı yolu: Sigortalılık, prim, gelir/aylık ve hizmet tespiti adli yargıda; SGK'nın bazı genel düzenleyici/idari işlemleri idari yargıda görülebilir — işlemin niteliği ayrılır.
2. Görev — 7036 sayılı İş Mahkemeleri Kanunu m.5: SGK ile sigortalı/işveren arasındaki sosyal güvenlik uyuşmazlıkları iş mahkemelerinde görülür.
3. İdari aşama — 5510 m.101 ve İş Mahkemeleri Kanunu m.4: Kurumca verilen kararlara karşı dava açmadan önce SGK'ya itiraz/başvuru ve cevap beklenmesi koşulu; bu dava şartı niteliğindedir, atlanırsa dava usulden reddedilir.
4. Süre: İdari başvurunun reddi veya zımni red üzerine dava açma süresi (İş Mahkemeleri Kanunu m.4'teki süreler) hesaplanır.
5. Yetki — HMK m.6 ve özel kurallar: Genelde davalının yerleşim yeri; sosyal güvenlikte sigortalının ikametgâhı/işyeri yer mahkemesi de yetkili olabilir. Ara sonuç: yargı yolu + görev + yetki + süre haritası. İspat: SGK tebliğ ve başvuru belgeleri.

## Çıktı modülleri
- Yargı yolu/görev/yetki tespit notu.
- İdari başvuru ve süre takvimi (tebliğ-başvuru-red-dava).
- Usul riski uyarı listesi.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
