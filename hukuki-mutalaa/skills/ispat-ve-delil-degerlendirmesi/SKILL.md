---
name: ispat-ve-delil-degerlendirmesi
description: "Mütalaadaki vakıaların hangi tarafça ve hangi delillerle ispatlanması gerektiğini, mevcut delil durumunda olası sonucu değerlendirmek gerektiğinde kullanılır; hukuki görüşün gerçekçilik sınamasıdır."
---

# İspat ve Delil Değerlendirmesi

## Görev
Çekişmeli her vakıa için ispat yükünü dağıtmak, mevcut delillerin türünü ve gücünü değerlendirmek ve "bu delil durumunda mahkeme ne sonuca varır" sorusunu yanıtlamak. Haklılık ile ispatlanabilirlik farklı şeylerdir; mütalaa ikisini de söyler.

## Soğuk başlangıç (intake)
- Hangi vakıalar çekişmeli ve ispata muhtaç?
- Eldeki deliller neler? (Senet, tanık, bilirkişi, keşif, yemin, e-yazışma)
- Senetle ispat zorunluluğu (HMK m.200) devreye giriyor mu? Senede karşı tanık yasağı (HMK m.201) söz konusu mu?
- Karşı tarafın elinde aksini gösteren delil olabilir mi?

## Denetim şeması
1. İspat yükü dağılımı: Kural TMK m.6 / HMK m.190 — herkes iddiasının dayandığı vakıaları ispatla yükümlüdür. Karine veya ispat yükü ters çeviren özel hüküm (ör. TBK m.66 kurtuluş kanıtı) varsa belirtilir.
2. Senetle ispat süzgeci: HMK m.200 — belli parasal sınırı aşan hukuki işlemler senetle ispat edilmeli; HMK m.201 senede karşı tanıkla ispat yasağı. İstisnalar (HMK m.203: yakın hısımlar arası, delil başlangıcı, vb.) kontrol edilir.
3. Delil gücü değerlendirmesi: Kesin deliller (kesin hükme bağlanmış senet, ikrar, kesin yemin) ile takdiri deliller (tanık, bilirkişi, keşif) ayrılır; her delilin somut olaydaki ağırlığı tartılır.
4. Delil eksikliği ve giderme: Eksik delil için somut araç önerilir — delil tespiti (HMK m.400), bilirkişi (HMK m.266), karşı tarafın elindeki belgenin ibrazı (HMK m.220).
5. Hukuka aykırı delil: HMK m.189/2 — hukuka aykırı yolla elde edilen delil hükme esas alınamaz; bu süzgeçten geçirilir.
6. Ara sonuç: Her çekişmeli vakıa için "kim ispatlamalı + eldeki delil yeterli mi + sonuç" değerlendirmesi.

## Çıktı modülleri
- İspat yükü ve delil tablosu (vakıa | yükümlü taraf | mevcut delil | yeterlilik)
- Senetle ispat / tanık yasağı değerlendirmesi
- Delil tamamlama önerileri (araç + dayanak madde)
- Genel ispat görünümü (lehte/aleyhte)

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
