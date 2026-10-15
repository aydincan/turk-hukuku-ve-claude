---
name: toplu-gorusme-ve-arabuluculuk
description: "Yetki belgesinden TIS imzasina veya uyusmazlik tutanagina kadar olan toplu gorusme surecini, cagri usulunu, surelerini ve 6356 m.50 kapsaminda resmi arabuluculugu ele alir; pazarlik takvimi ve uyusmazlik tutanagi asamasinda kullanilir."
---

# Toplu Görüşme ve Resmî Arabuluculuk

## Görev
Toplu görüşmenin başlatılması, sürdürülmesi ve tıkanması halinde resmî arabuluculuğa geçişin usul-süre yönetimi. Menfaat uyuşmazlığının barışçıl çözüm hattıdır.

## Soğuk başlangıç (intake)
- Yetki belgesi tebliğ edildi mi, tarihi nedir?
- Çağrı yapıldı mı; ilk toplantı gerçekleşti mi?
- Görüşmeler kaç gündür sürüyor; uyuşmazlık tutanağı tutuldu mu?
- Hangi konularda anlaşmazlık var?

## Denetim şeması
1. **Çağrı:** 6356 m.46 — yetki belgesini alan taraf, **15 gün** içinde karşı tarafı toplu görüşmeye çağırır; çağrı tarihinden itibaren **30 gün** içinde toplanılmazsa veya görüşmeye başlanmazsa yetki düşebilir (m.46/2-3 kontrol edilir).
2. **Görüşme süresi:** 6356 m.47 — toplu görüşme süresi, ilk toplantı tarihinden itibaren **60 gün**dür.
3. **Uyuşmazlık tutanağı:** Anlaşma sağlanamaz veya taraflardan biri görüşmeye gelmezse uyuşmazlık tutanağı tutulur; bu, arabuluculuk ve grev sürecinin tetikleyicisidir.
4. **Resmî arabuluculuk:** 6356 m.50 — uyuşmazlığın görevli makama (görevli birim) bildirilmesi üzerine resmî listeden bir arabulucu görevlendirilir; arabulucu **15 gün** (gerekirse 6 işgünü uzatmayla) içinde tarafları uzlaştırmaya çalışır, sonuçta tutanak düzenler.
5. **Ara sonuç:** Arabuluculukta anlaşma olursa TİS imzalanır. Anlaşma olmazsa menfaat uyuşmazlığı grev/lokavt veya (kamu hizmeti gibi yasak hallerde) yüksek hakem yoluna açılır.

Not: Toplu menfaat uyuşmazlığında **6325 sayılı HUAK dava şartı arabuluculuk uygulanmaz**; 6356'nın kendi resmî arabuluculuk rejimi işler.

## Çıktı modülleri
- Toplu görüşme süre/aşama takvimi (15-30-60 gün eşikleri).
- Çağrı yazısı ve uyuşmazlık tutanağı iskeleti.
- Arabuluculuk sonrası yol haritası (grev / yüksek hakem / imza).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
