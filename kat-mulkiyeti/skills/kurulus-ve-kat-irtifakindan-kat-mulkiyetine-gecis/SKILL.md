---
name: kurulus-ve-kat-irtifakindan-kat-mulkiyetine-gecis
description: "Bir arsa veya yeni tamamlanan yapı üzerinde kat irtifakı ya da kat mülkiyeti tesis edilmesi, kat irtifakından kat mülkiyetine geçiş ya da kuruluş belgelerindeki eksiklik/uyuşmazlık gündeme geldiğinde; resmî senet, yönetim planı, proje ve tescil zincirini kurmak için kullanılır."
---

# Kat İrtifakı ve Kat Mülkiyetinin Kurulması

## Görev
Bir taşınmaz üzerinde kat irtifakı veya kat mülkiyetinin geçerli biçimde kurulmasını sağlamak; kat irtifakından kat mülkiyetine geçişi yönetmek ve kuruluş belgelerindeki (resmî senet, proje, yönetim planı) eksiklik veya uyuşmazlıkları gidermek.

## Soğuk başlangıç (intake)
- Yapı hangi aşamada: arsa hâlinde mi, inşaat sürüyor mu, tamamlanmış/iskânlı mı?
- Kuruluş tek malikin istemiyle mi yoksa paydaşların ortak istemiyle mi yapılacak?
- Onaylı mimari proje, vaziyet planı ve yapı kullanma izni (iskân) mevcut mu?
- Yönetim planı hazırlandı ve tüm maliklerce imzalandı mı?

## Denetim şeması
1. **Kuruluş yolu (KMK m.10, m.12)**: Kat mülkiyeti/irtifakı, malik veya bütün paydaşların istemiyle, tapuda **resmî senet** düzenlenip tescil edilerek kurulur (m.13). Tek taraflı tesis ancak tek malik için mümkündür; paydaşlar varsa oybirliği gerekir.
2. **Zorunlu belgeler (m.12)**: (a) Genel inşaat projesi ve yetkili merci onayı, (b) bağımsız bölümleri gösteren liste (m.12/a), (c) **yönetim planı** (m.12/b, m.28), (d) tek malik değilse paydaşların istemi. Eksik belge tescili engeller.
3. **Kat irtifakı kuruluşu (m.2/c, m.10/son)**: Yapı henüz tamamlanmamışken arsa payına bağlı kat irtifakı kurulur; tapuda "kat irtifakı" olarak gösterilir. İrtifak sahibi, yapının projeye uygun bitirilmesini isteyebilir (m.26).
4. **Kat mülkiyetine geçiş (m.14)**: Yapı tamamlanıp yapı kullanma izni alınınca, kat irtifakına konu yapıda ilgililerin istemiyle kat mülkiyetine geçilir. Yapı fiilen tamamlanmışsa, kat irtifakı sahiplerinden biri dahi resen geçiş için başvurabilir (m.14/son uygulaması).
5. **Arsa payı belirlemesi (m.3/2)**: Resmî senette her bağımsız bölüme değeriyle orantılı arsa payı verilmelidir; orantısızlık sonradan arsa payı düzeltme davasına konu olur.
6. **Ara sonuç**: Belgeler tam ve proje onaylıysa tescil; eksikse tamamlama listesi; kat irtifakı varsa geçiş başvurusu.

## Çıktı modülleri
- Kuruluş belge kontrol listesi (proje, iskân, liste, yönetim planı).
- Kat mülkiyetine geçiş başvuru dilekçesi iskeleti.
- Eksiklik/uyuşmazlık halinde mahkemeye başvuru veya arsa payı düzeltme yönlendirmesi.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
