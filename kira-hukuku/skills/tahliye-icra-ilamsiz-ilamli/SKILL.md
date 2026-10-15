---
name: tahliye-icra-ilamsiz-ilamli
description: "Kesinleşen tahliye kararının veya yazılı sözleşme/tahliye taahhüdünün icrası, ödeme/tahliye emrine itiraz, itirazın kaldırılması veya fiili tahliye/icra süreci söz konusu olduğunda bu beceriyi kullan."
---

# Tahliye İcrası — İlamsız ve İlamlı Yollar

## Görev
Tahliyeyi fiilen gerçekleştirmek için doğru icra yolunu seçmek: İİK m.269 vd. (temerrüt nedeniyle ilamsız tahliye), İİK m.272 vd. (yazılı sözleşme/taahhütle ilamsız tahliye) veya kesinleşmiş ilamın icrası; itiraz ve itirazın kaldırılması rejimini yürütmek.

## Soğuk başlangıç (intake)
- Elde ilam var mı, yoksa yazılı sözleşme/taahhüt mü?
- Talep sebebi temerrüt mü, süre/taahhüt mü?
- Kiracıya emir tebliğ edildi mi; itiraz edildi mi?
- İtirazın dayanağı ne (borç yok, taahhüt geçersiz)?

## Denetim şeması
1. **Temerrüt nedeniyle ilamsız tahliye (İİK m.269)**: Kira borcunun ödenmemesi üzerine tahliye talepli takip; ödeme emrinde otuz günlük (kira borcu için) ödeme ve yedi günlük itiraz süresi belirtilir. Süresinde ödenmez/itiraz edilmezse icra mahkemesinden tahliye istenir.
2. **Sözleşme/taahhütle ilamsız tahliye (İİK m.272)**: Kira süresinin bitmesi veya yazılı tahliye taahhüdü hallerinde tahliye emri; kiracı **itiraz** ederse takip durur, alacaklı icra mahkemesinde **itirazın kaldırılmasını** ister.
3. **İtiraz incelemesi (İİK m.275)**: İcra mahkemesi, itirazın kaldırılması talebini sözleşme/taahhüt belgesi ve imzaya dayalı olarak inceler; imza inkârı veya yazılı belge yoksa genel mahkemeye yollar.
4. **İlamlı tahliye**: Sulh hukukun verdiği kesinleşmiş tahliye kararı icra dairesince infaz edilir; tahliye için kiracıya **on beş günlük** süreli icra emri (İİK m.24 benzeri tahliye hükümleri) tebliğ edilir.
5. **Eşyaların durumu / kolluk**: Fiili tahliyede çilingir-kolluk hazır bulunur; kiracının eşyaları muhafaza altına alınır.
6. **Ara sonuç**: Seçilen yol + tebliğ-itiraz durumu + sıradaki adım (icra mahkemesi/fiili tahliye).

## Çıktı modülleri
- Takip yolu seçim şeması.
- İcra/ödeme/tahliye emri ve takip talebi taslağı.
- İtirazın kaldırılması dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
