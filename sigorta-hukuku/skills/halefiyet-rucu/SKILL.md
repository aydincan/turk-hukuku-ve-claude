---
name: halefiyet-rucu
description: "Zarar sigortacısının ödediği tazminat için zarar veren üçüncü kişiye veya kusurlu sigortalıya başvurması (rücu) söz konusu olduğunda kullanılır; halefiyetin şartları, kapsamı ve sınırlarını denetler."
---

# Halefiyet ve Rücu (Sigortacının Geri Alım Hakkı)

## Görev
Tazminatı ödeyen zarar sigortacısının, sigortalının üçüncü kişiye karşı haklarına halef olarak rücu edip edemeyeceğini; zorunlu sorumluluk sigortalarında sigortalıya/işletene rücu şartlarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi sigortacı kime ödeme yaptı, ne kadar?
2. Zarara kim sebep oldu (üçüncü kişi, karşı taraf sürücüsü/işleteni)?
3. Rücu zarar sigortasından mı doğuyor yoksa zorunlu sorumluluk sigortasından mı?
4. Sigortalının zarar verene karşı talep hakkı mevcut/sona ermiş mi?

## Denetim şeması
1. **Halefiyetin doğumu.** TTK m.1472: zarar sigortacısı, ödediği tazminat tutarınca hukuken sigortalının yerine geçer; sigortalının zarardan sorumlu üçüncü kişilere karşı taleplerine halef olur. Ödeme yapılmadan halefiyet doğmaz. Ara sonuç: ödeme gerçekleşti mi?
2. **Kapsam ve sınır.** Halefiyet, ödenen tazminatla sınırlıdır ve sigortalının hakkından fazlasını içermez. Sigortalının dava/zamanaşımı durumu sigortacıya geçer (mevcut hakkın devri mantığı).
3. **Aile/birlikte yaşayan istisnası.** TTK m.1472/2: sigortalı ile birlikte yaşayan ve hareketlerinden sorumlu olduğu kişilere, kasıt yoksa rücu edilemez.
4. **Zorunlu sorumluluk sigortasında rücu.** Karayolları Motorlu Araçlar Zorunlu Mali Sorumluluk Sigortası Genel Şartları (alkol, ehliyetsizlik, çalınan araç, sürat vb. sayılı haller) ve KTK m.95 çerçevesinde sigortacı, zarar görene ödediği tazminatı kusurlu sigortalıya/işletene rücu edebilir. İstisnalar sınırlı ve dar yorumlanır.
5. **Zamanaşımı.** Rücu talebi, sigortacının ödeme yaptığı tarihten itibaren işler (TTK m.1420 ve ilgili özel süreler); zorunlu sigortalarda KTK m.109 dikkate alınır.

## Çıktı modülleri
- Rücu hukuki dayanağı (TTK m.1472 / KTK m.95 / genel şart maddesi).
- Rücu edilebilir tutar ve muhatap.
- İstisna/sınır değerlendirmesi (aile, kusur derecesi).
- Zamanaşımı başlangıç tarihi ve dava planı.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
