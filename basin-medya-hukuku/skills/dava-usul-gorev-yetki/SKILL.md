---
name: dava-usul-gorev-yetki
description: "Basın-medya uyuşmazlıklarında doğru yargı kolunu, görevli ve yetkili mahkemeyi, dava türünü ve ihtiyati tedbir imkânını belirlemek gerektiğinde kullanılır."
---

# Dava, Usul, Görev ve Yetki

## Görev
Uyuşmazlığın hangi yargı kolunda (adli/idari), hangi görevli mahkemede ve nerede açılacağını belirlemek; uygun dava türünü ve ihtiyati tedbiri kurgulamak.

## Soğuk başlangıç (intake)
1. Talep ne (tazminat, men, erişim engelleme, idari işlem iptali)?
2. Karşı taraf özel hukuk kişisi mi, idare (RTÜK) mi?
3. Davacı/davalı yerleşim yeri ve haksız fiilin işlendiği yer neresi?
4. Acil ve telafisi güç zarar tehlikesi var mı (ihtiyati tedbir)?

## Denetim şeması
1. **Yargı kolu**: Kişilik hakkı/tazminat davaları adli yargıda; RTÜK ve BTK işlemlerinin iptali idari yargıda (İYUK). 5651 m.9 erişim engelleme sulh ceza hâkimliğinde; ceza şikâyeti ceza yargısında.
2. **Görev**: Kişilik hakkı ve tazminat davalarında genel görevli mahkeme asliye hukuk mahkemesidir (HMK m.2). Cevap-düzeltme ve erişim engelleme talepleri sulh ceza hâkimliğindedir.
3. **Yetki**: Genel yetki davalının yerleşim yeri (HMK m.6); haksız fiilde fiilin işlendiği veya zararın doğduğu ya da doğma ihtimalinin bulunduğu yer mahkemesi de yetkilidir (HMK m.16).
4. **Dava türü ve dilekçe**: Talep sonucu net olmalı (tespit/men/önleme/tazminat); dilekçe HMK m.119 unsurlarını taşımalıdır.
5. **İhtiyati tedbir**: HMK m.389 vd. çerçevesinde, devam eden veya tekrarlanacak ihlalde içeriğin yayımının/erişiminin durdurulması istenebilir; ifade özgürlüğü nedeniyle ölçülülük sıkı denetlenir.
6. **Ara sonuç**: Doğru yargı kolu + görevli/yetkili mahkeme + uygun dava türü belirlenince layiha hazırlanır.

## Çıktı modülleri
- Yargı kolu/görev/yetki karar ağacı
- İhtiyati tedbir talebi gerekçesi
- Dilekçe başlığı ve talep sonucu taslağı

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
