---
name: algoritmik-seffaflik-aciklanabilirlik
description: "İlgili kişinin veya denetçinin bir yapay zekâ kararının mantığına, kullanılan verilere ve karara dair açıklama talep etmesi durumunda aydınlatma ve bilgi verme yükümlülüğünün kapsamı ile ticari sır sınırı dengelendiğinde kullanılır."
---

# Algoritmik Şeffaflık ve Açıklanabilirlik

## Görev
Bir yapay zekâ sisteminin işleyişi ve ürettiği karar hakkında açıklama yükümlülüğünün kapsamını belirlemek; ilgili kişinin bilgi hakkı ile geliştiricinin ticari sır/fikri mülkiyet menfaatini dengeleyerek uygun şeffaflık seviyesini tasarlamak.

## Soğuk başlangıç (intake)
1. Talep eden kim: ilgili kişi, Kurul/denetçi, sözleşmenin karşı tarafı, mahkeme?
2. Ne isteniyor: kararın gerekçesi, kullanılan veri kategorileri, modelin mantığı, kaynak kod?
3. Sistemde aydınlatma metni ve karar gerekçesi loglanıyor mu?
4. Ticari sır/lisans kısıtı veya üçüncü kişi modeli (kapalı API) var mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: KVKK m.10 aydınlatma (işlemenin amacı, otomatik karar varlığı), m.11 bilgi talep hakkı ve m.13 başvuru. Bu, kaynak kodun teslimini değil, kararın mantığı ve sonuçları konusunda anlamlı bilgiyi gerektirir. Ara sonuç: talep edilen şeffaflık seviyesi.
2. **Kapsam sınırı**: Şeffaflık, ticari sır ve fikri mülkiyetle (FSEK/SMK, TTK haksız rekabet) sınırlanır; ancak bu sınır bilgi hakkını tamamen bertaraf edemez — "anlamlı açıklama" verilmelidir. Denge ölçülülükle kurulur.
3. **Yargısal talepte**: HMK m.219-220 belgelerin ibrazı ve bilirkişi incelemesi yoluyla teknik açıklama sağlanabilir; mahkeme önünde ticari sır tedbirleriyle inceleme istenebilir.
4. **Kamu kararında**: İdarenin otomatik işleminde gerekçe yükümlülüğü ve İYUK kapsamında bilgi edinme/savunma hakları; gerekçesiz idari işlem sakatlık sebebi.
5. **Belgeleme**: Karar gerekçesinin ve model versiyonunun loglanması, sonradan açıklanabilirliği ve ispatı sağlar.

Kurul rehberleri için kvkk.gov.tr; yargı uygulaması için karararama portalları, künye [doğrulanacak].

## Çıktı modülleri
- Şeffaflık seviyesi matrisi (talep eden / verilecek bilgi / sınır).
- Açıklama metni taslağı (ticari sır korunarak).
- Logging/açıklanabilirlik öneri listesi.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
