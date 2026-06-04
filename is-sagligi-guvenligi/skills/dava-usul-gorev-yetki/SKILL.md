---
name: dava-usul-gorev-yetki
description: "İş kazası tazminatı, SGK rücuu, idari ceza itirazı ve ceza yargılaması gibi farklı yolların görevli-yetkili mercilerini, dava şartlarını ve usul yolunu belirlemek için kullanılır."
---

# İSG Uyuşmazlıklarında Dava, Görev ve Yetki

## Görev
İSG kaynaklı her uyuşmazlığı doğru yargı koluna ve mercie yönlendirmek; görev, yetki, dava şartı (özellikle arabuluculuk) ve usul yolunu netleştirmek.

## Soğuk başlangıç (intake)
- Talep türü: işçi/hak sahibi tazminatı mı, SGK rücuu mu, idari ceza itirazı mı, ceza soruşturması mı?
- Taraflar kim; alt işveren-asıl işveren birlikte mi davalı?
- Olayın ve tebligatın tarihleri (süre ve zamanaşımı için)?
- Arabuluculuğa başvuruldu mu (işçilik alacağı/işe iade dava şartı)?

## Denetim şeması
1. **İş kazası tazminatı:** Görevli mahkeme iş mahkemesidir (7036 sayılı Kanun); yetki kural olarak davalının yerleşim yeri ile işin/işyerinin bulunduğu yer mahkemesi. İşçinin işverenden tazminat talebinde **dava şartı arabuluculuk** uygulanır; ancak iş kazasından kaynaklanan maddi-manevi tazminat ve rücu davaları arabuluculuk dava şartının istisnasıdır (doğrudan dava açılır) — bu istisnayı her dosyada güncel mevzuatla doğrula.
2. **SGK rücu davası:** Görevli mahkeme iş mahkemesi; davacı SGK, davalı kusurlu işveren/üçüncü kişi.
3. **İdari para cezası:** Adli yargı — sulh ceza hâkimliğine itiraz (5326 m.27), idari yargı değil. Bu ayrım sık karıştırılır; yanlış mercie başvuru süre kaybına yol açar.
4. **Ceza yargılaması:** Taksirle öldürme/yaralama (TCK m.85-89) için asliye ceza/ağır ceza; şikâyet ve uzlaşma rejimi suç tipine göre değişir.
5. **Dava şartı ve süre denetimi:** Husumet (asıl işveren-alt işveren birlikte), ehliyet, harç ve süreler. **Ara sonuç:** Her talep için merci-yol-süre üçlüsünü tablola; mevzuata dayalı doğrula.

## Çıktı modülleri
- Talep türü → görevli/yetkili merci → usul yolu tablosu.
- Dava şartı (arabuluculuk) ve istisna notu.
- Husumet ve taraf teşkili kontrol listesi.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
