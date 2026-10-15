---
name: dogal-gaz-piyasasi
description: "4646 sayılı Kanun kapsamında doğal gaz lisansları, iletim-dağıtım-depolama-ithalat faaliyetleri, tarife ve dağıtım bölgesi uyuşmazlıkları ele alındığında kullanılır."
---

# Doğal Gaz Piyasası Uygulaması

## Görev
Doğal gaz piyasasındaki faaliyetleri 4646 sayılı Kanun ve ikincil mevzuat çerçevesinde lisans, tarife ve faaliyet ayrımı yönünden denetlemek; dağıtım ve ithalat/toptan uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
1. Faaliyet türü: ithalat, toptan satış, iletim, dağıtım, depolama, CNG/LNG?
2. Müvekkil lisans sahibi mi; dağıtım bölgesi/ihale durumu?
3. Uyuşmazlık tarife, abonelik, bağlantı bedeli mi, yoksa lisans/yaptırım mı?
4. Tartışmalı dönem ve EPDK işlemi var mı?

## Denetim şeması
1. **Faaliyet ayrımı**: 4646 — iletim, dağıtım, depolama, ithalat, toptan ve perakende satış faaliyetlerinin ayrılığı (unbundling) ilkesi ve her biri için ayrı lisans. Ara sonuç: faaliyet doğru lisansla mı yürütülüyor.
2. **Dağıtım bölgesi**: Dağıtım lisansının ihale ile verilmesi, bölge tekeli, yatırım ve hizmet yükümlülükleri; bölge dışı faaliyet ve devir sınırları.
3. **Tarife**: Bağlantı, iletim, dağıtım, depolama ve satış tarifeleri EPDK onayına tabi; abone bağlantı bedeli ve güvence bedeli uygulamaları yönetmelikle sınırlıdır. Onaylı tarife dışı bedel itiraza açık.
4. **Abonelik ve bağlantı**: Dağıtım şirketinin bağlantı/abonelik yükümlülüğü ve red sebepleri; teknik uygunluk ispatı dağıtıcıda.
5. **Yaptırım ve dava**: 4646 idari yaptırımları; EPDK işlemine karşı İYUK m.7 süresinde idari dava. Özel hukuk nitelikli abonelik/bedel uyuşmazlığı adli yargıda görülebilir; görev ayrımı netleştirilir.

## Çıktı modülleri
- Faaliyet/lisans uyum notu.
- Tarife/abonelik bedeli itiraz değerlendirmesi.
- İlgili merci ve dava/başvuru yol haritası.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
