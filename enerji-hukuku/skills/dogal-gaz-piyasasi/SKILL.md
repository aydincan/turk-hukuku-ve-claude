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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
