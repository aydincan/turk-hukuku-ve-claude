---
name: durusma-hazirlik-ve-ara-karar-takibi
description: "Yaklaşan duruşmaya hazırlanmak, tensip ve ara kararların gereklerini izlemek, her celse için yapılacaklar ve verilecek beyanları listelemek gerektiğinde kullan."
---

# Duruşma Hazırlığı ve Ara Karar Takibi

## Görev
Her duruşma öncesi dosyanın güncel durumunu, ara kararların gereğini ve celsede yapılacak işlemleri bir hazırlık çek-listesine dönüştürmek; ara kararların kaçırılmasını önlemek.

## Soğuk başlangıç (intake)
- Bir sonraki duruşma tarihi ve aşaması (ön inceleme, tahkikat, sözlü yargılama) ne?
- En son ara karar ne idi ve gereği yerine getirildi mi?
- Bu celsede sunulacak beyan, delil veya itiraz var mı?
- Tanık/bilirkişi/keşif gibi bekleyen işlem var mı?

## Denetim şeması
1. Ara karar dökümü: tensip zaptı ve her celse zaptındaki ara kararları madde madde çıkar; her birinin muhatabı, gereği ve süresi (ör. iki hafta kesin süre, HMK m.94 kesin süre sonucu) ile takip et.
2. Aşamaya göre gündem: ön inceleme celsesinde sulh teşviki, ilk itiraz ve dava şartı incelemesi (HMK m.137-140); tahkikatta delil toplama ve tanık dinleme; sözlü yargılamada esas hakkında beyan.
3. Kesin süre riski: kesin süreye bağlanan işlemler (delil avansı, gider avansı HMK m.120, delil bildirimi) yerine getirilmedi ise hak kaybı uyarısı.
4. Sunulacaklar: bu celsede ibraz edilecek beyan/delil listesi ve dayanağı; mazeret gerekiyorsa mazeret dilekçesi notu.
5. Ara sonuç: celse-bazlı hazırlık çek-listesi ve açık ara karar gerekleri. Tarih ve ara karar metni evraktan alınır.

## Çıktı modülleri
- Ara karar takip tablosu (karar, muhatap, gereği, süre, durum).
- Duruşma hazırlık çek-listesi.
- Kesin süre / hak kaybı uyarıları.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
