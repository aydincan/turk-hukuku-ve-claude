---
name: serh-beyan-ve-takyidat
description: "Tapu kaydına kişisel hak, tasarruf kısıtlaması, aile konutu, satış vaadi, kira, önalım gibi bir şerh veya beyan işlenmesi, terkin edilmesi ya da var olan takyidatın hukuki etkisinin değerlendirilmesi gerektiğinde kullanılır."
---

# Şerh, Beyan ve Takyidat İşlemleri

## Görev
Tapu kaydına işlenecek/terkin edilecek şerh ve beyanları doğru hukuki dayanakla belirlemek ve mevcut takyidatların üçüncü kişilere etki gücünü çözümlemek.

## Soğuk başlangıç (intake)
- İşlem türü ne: şerh/beyan tesisi mi, terkin mi, mevcut takyidatın yorumu mu?
- Hangi hak: taşınmaz satış vaadi, kira, önalım/alım/geri alım, aile konutu, ihtiyati tedbir/haciz?
- Şerhin amacı kişisel hakkı güçlendirmek mi, tasarrufu kısıtlamak mı, durumu açıklamak mı?
- Lehine/aleyhine işlenecek kişi ve dayanak belge (sözleşme, mahkeme kararı) nedir?

## Denetim şeması
1. **Şerh türünü ayır (TMK m.1009-1010).** (a) Kişisel hakların şerhi: satış vaadi, kira, önalım/alım/geri alım, bağışlamadan dönme — şerhle kişisel hak güçlendirilir, sonraki maliklere ileri sürülebilir hale gelir (TMK m.1009). (b) Tasarruf yetkisi kısıtlamaları: ihtiyati tedbir, haciz, konkordato mühleti, çekişmeli hakların korunması (TMK m.1010). (c) Geçici tescil şerhi (TMK m.1011).
2. **Beyanı ayır.** Beyanlar hak kurmaz; mevcut fiili/hukuki durumu açıklar (ör. aile konutu beyanı, eklenti, kamulaştırma şerhi). Aile konutu için TMK m.194 — diğer eşin rızası ve şerh imkânı.
3. **Etki gücünü değerlendir.** Şerhli kişisel hak, taşınmazı sonradan edinen herkese karşı ileri sürülebilir; şerhsiz kişisel hak yalnızca taraf arasında etkilidir. İhtiyati tedbir/haciz şerhi sonraki kazanımları sakatlar.
4. **Süre ve geçerlilik.** Bazı şerhlerin süreyle sınırı vardır (ör. satış vaadi şerhinin etkisi — 2644 sayılı Tapu Kanunu ve TMK uygulaması; süre dolunca terkin edilebilir). Şerhin dayanağı sona ererse terkin istenir.
5. **Usul.** Şerh/terkin tapu müdürlüğünde talep ve dayanak belgeyle; mahkeme kararına dayanan şerhlerde ilam/tedbir kararı gerekir. Reddi halinde Tapu Kanunu m.26 işlemlerine karşı yol ve dava.
6. **Ara sonuç.** İstenen sonuç için şerh mi beyan mı, dayanağı ve etkisi netleştirilir.

## Çıktı modülleri
- Şerh/beyan türü–dayanak–etki tablosu.
- Tapu müdürlüğü talep dilekçesi veya terkin talebi iskeleti.
- Mevcut takyidatların alıcı/müvekkil açısından risk değerlendirmesi.

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
