---
name: pay-sahipleri-sozlesmesi-sha
description: "Yatırımcı ve kurucular arasındaki yönetişim ve çıkış dengesini kuran pay sahipleri sözleşmesi (SHA) hazırlanır veya müzakere edilirken; veto, bilgi alma, sürükleme-birlikte satış, önalım gibi hükümlerin Türk hukukundaki geçerliliği ve esas sözleşmeyle ilişkisi denetlenirken kullanılır."
---

# Pay Sahipleri Sözleşmesi (SHA) Kurgusu

## Görev
Kurucu-yatırımcı ilişkisinin yönetişim, kontrol, koruma ve çıkış mekanizmalarını SHA'da TBK serbestisi içinde kurgulamak; hangi hükmün esas sözleşmeye taşınması (ayni etki için) gerektiğini saptamak.

## Soğuk başlangıç (intake)
1. Taraflar ve pay oranları; kim çoğunluk, kim azınlık/yatırımcı?
2. İstenen mekanizmalar: veto/onay konuları, yönetim koltuğu, bilgi alma?
3. Çıkış hükümleri: drag-along, tag-along, önalım, IPO/satış senaryosu?
4. Vesting (kurucu ve çalışan) ve rekabet/devamlılık yükümlülüğü isteniyor mu?
5. İhtilaf çözümü: tahkim mi, mahkeme mi; uygulanacak hukuk?

## Denetim şeması
1. Geçerlilik temeli: SHA hükümleri taraflar arası borç sözleşmesidir (TBK m.26-27 serbestisi). Bunlar şirkete karşı doğrudan etki etmez; ayni etki (devir engeli, imtiyaz) için esas sözleşme/bağlam (TTK m.491-493, m.478-479) gerekir.
2. Yönetişim: Veto/olumlu oy konuları, yönetim kurulu temsili — oy sözleşmesi geçerli; ancak oy hakkının payla bütünlüğü (m.434) ve dürüstlük (TMK m.2) sınırı. Devredilemez YK yetkileri (m.375) sözleşmeyle kurucudan alınamaz.
3. Çıkış mekanizmaları: Drag-along (sürükleme), tag-along (birlikte satış), önalım — taraflar arası borç olarak geçerli; ihlalde cezai şart (TBK m.179) ve aynen ifa/tazminat. Payın üçüncü kişiye geçişini şirkete karşı engellemek için esas sözleşmesel bağlam (m.491-493) eklenmeli.
4. Vesting/ters vesting: Kurucu paylarının hak edilmesi; ayrılma halinde geri alım veya zorunlu satış — TBK serbestisi + esas sözleşmesel devir mekanizması ile kurulur.
5. Çıkmaz (deadlock): Eşit ortaklıkta tıkanma çözümü (shotgun/rus ruleti, üçüncü kişi, fesih); haklı sebeple fesih hakkı saklı (TTK m.531).
6. Uyum/çatışma: SHA-esas sözleşme çelişkisinde şirkete karşı esas sözleşme; taraflar arası SHA. Çatışmayı baştan haritala.
7. İspat/şekil: Yazılı; gerekirse imza onaylı. İhlalde def'i ve cezai şart kanıt zinciri.

## Çıktı modülleri
- SHA hüküm seti taslağı (veto/drag/tag/önalım/vesting + cezai şart).
- Esas sözleşmeye taşınması gereken hükümlerin listesi (ayni etki notu).
- SHA-esas sözleşme uyum/çatışma matrisi.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
