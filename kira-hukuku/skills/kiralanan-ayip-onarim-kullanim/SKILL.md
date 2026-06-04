---
name: kiralanan-ayip-onarim-kullanim
description: "Kiralananda teslimden önce/sonra ayıp, onarım yükümlülüğü, kira indirimi, giderlerin kime ait olduğu veya kiracının kullanımdan yoksun kalması söz konusu olduğunda bu beceriyi kullan."
---

# Kiralananın Ayıbı, Onarım ve Kullanıma Elverişlilik

## Görev
Kiralananın sözleşmeye uygun, kullanıma elverişli halde tutulması yükümlülüğünü ve ayıp hükümlerini uygulamak; kiracının kira indirimi, onarım, gider ve tazminat taleplerini; tarafların bakım-onarım yükünü saptamak.

## Soğuk başlangıç (intake)
- Ayıp teslim anında mı vardı, sonra mı doğdu?
- Ayıbın niteliği ne (kullanımı engelleyen mi, küçük mü)?
- Kiracı kiraya vereni bildirim/ihtarla uyardı mı?
- Hangi onarımlar yapıldı, masrafı kim karşıladı?

## Denetim şeması
1. **Teslim ve elverişli halde bulundurma (TBK m.301)**: Kiraya veren, kiralananı sözleşmede amaçlanan kullanıma elverişli halde teslim eder ve kira süresince bu halde **bulundurur**.
2. **Teslim sırasında ayıp (TBK m.304)**: Kiralanan önemli ayıpla teslim edilirse, kiracı genel hükümlere (ifa etmeme) başvurabilir; önemsiz ayıpta kullanım sürerken ayıbın giderilmesi istenebilir.
3. **Sonradan doğan ayıp (TBK m.305-306)**: Kiracı seçimlik haklar kullanabilir — ayıbın giderilmesi, kira bedelinden **orantılı indirim** (m.307), **zararın giderimi** (m.308) ve şartları varsa **fesih**. Ayıbı kiraya verene bildirme yükü kiracıdadır.
4. **Ayıbın giderilmesi/kiracının onarımı (m.306)**: Kiraya veren makul sürede gidermezse, kiracı ayıbı giderip masrafı kiradan düşebilir veya benzer kiralanan temin edebilir.
5. **Temizlik ve küçük onarımlar (TBK m.317)**: Olağan kullanımın gerektirdiği temizlik ve bakım giderleri kiracıya; esaslı onarım kiraya verene aittir.
6. **Üçüncü kişinin/üstün hakkın ileri sürülmesi (TBK m.309-312)**: Zapt benzeri durumlarda kiracının hakları.
7. **İspat ve ara sonuç**: Ayıbın varlığı ve niteliği (keşif/bilirkişi), bildirim, indirim/gider hesabı.

## Çıktı modülleri
- Ayıp türü-seçimlik hak eşleştirmesi.
- Kira indirimi/gider hesabı taslağı.
- Kiraya verene ayıp bildirim ihtarnamesi.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
