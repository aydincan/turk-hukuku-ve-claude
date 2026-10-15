---
name: tapu-sicili-ve-ayni-hak-sistematigi
description: "Taşınmaz üzerindeki ayni hakların kuruluş ve devir mantığını, tescilin kurucu etkisini, tescilli ve tescilsiz kazanım ayrımını ve sicil ilkelerini çözümlerken; bir tapu kaydının ne anlama geldiğini ve hangi hakkın nasıl doğduğunu anlamak gerektiğinde kullanılır."
---

# Tapu Sicili ve Ayni Hak Sistematiği

## Görev
Taşınmaz üzerindeki ayni hakkın hangi yolla doğduğunu, sicile nasıl yansıdığını ve sicilin sağladığı korumayı sistematik biçimde ortaya koymak; sonraki tüm dava/işlem becerilerine zemin hazırlamak.

## Soğuk başlangıç (intake)
- Taşınmazın güncel tapu kaydını (ada-parsel, malik, edinme sebebi/tarihi, takyidatlar) ve akit tablosu tarihçesini görüyor muyuz?
- İhtilaf hangi hakka ilişkin: mülkiyet mi, sınırlı ayni hak (ipotek/irtifak/intifa) mı, kişisel hakkın şerhi mi?
- Hak nasıl kazanılmış: resmi senetle devir mi, miras/mahkeme kararı/cebri icra (tescilsiz) mi?
- Tapuda görünen malik ile fiili durum (zilyet) örtüşüyor mu?

## Denetim şeması
1. **Kazanım türünü ayır.** Kural: ayni hak ancak tescil ile doğar (TMK m.705/1). İstisna: miras, mahkeme kararı, cebri icra, işgal, kamulaştırma hallerinde hak tescilden önce doğar, tescil açıklayıcıdır (m.705/2) — ancak tasarruf için tescil gerekir.
2. **Resmi şekil şartını denetle.** Taşınmaz mülkiyetini devir borcu doğuran sözleşmeler resmi şekilde, tapu müdürlüğünde yapılır (TMK m.706, TBK m.237, 2644 sayılı Tapu Kanunu m.26). Adi yazılı/harici satış mülkiyet geçirmez; en çok kişisel hak/sebepsiz zenginleşme doğurur.
3. **İllilik (sebebe bağlılık) ilkesini uygula.** Tescil geçerli bir hukuki sebebe (satış, bağış vb.) dayanmazsa yolsuzdur; sebep geçersizse tescil de yolsuz hale gelir.
4. **Aleniyet ve güveni değerlendir.** Sicil aleni kabul edilir (TMK m.1020); kimse sicildeki bir kaydı bilmediğini ileri süremez. İyiniyetli üçüncü kişinin yolsuz tescile güvenerek kazanımı korunur (TMK m.1023) — bu, düzeltme talebinin sınırıdır.
5. **Sınırlı ayni hakları yerleştir.** İpotek (TMK m.881 vd.), intifa/oturma, geçit/kaynak gibi irtifaklar (m.779 vd.) sicildeki sıraya ve içeriğe göre değerlendirilir.
6. **Ara sonuç.** Hakkın türü, kazanım anı, geçerliliği ve üçüncü kişilere karşı durumu tek cümlede sabitlenir.

## Çıktı modülleri
- Taşınmazın hukuki durum özeti (hak türü / malik / edinme sebebi / takyidat tablosu).
- Kazanım türü ve geçerlilik değerlendirmesi (tescilli/tescilsiz, illilik notu).
- Üçüncü kişiye karşı koruma haritası ve sonraki adım önerisi (iptal-tescil, düzeltim, tescil davası).

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
