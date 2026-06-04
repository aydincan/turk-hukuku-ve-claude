---
name: sgk-rucu-davalari
description: "İş kazası veya meslek hastalığında SGK'nın yaptığı yardımları işverene rücu etmesini, kusur oranı ve peşin sermaye değeri hesabını değerlendirmek için kullanılır."
---

# SGK Rücu Davaları

## Görev
İş kazası/meslek hastalığında SGK'nın sigortalıya veya hak sahiplerine yaptığı/yapacağı yardımları 5510 m.21 uyarınca kusurlu işverene (ve varsa üçüncü kişiye) rücuunu değerlendirmek; talep kapsamını ve savunmaları çıkarmak.

## Soğuk başlangıç (intake)
- SGK hangi yardımları yaptı/bağladı (geçici iş göremezlik, sürekli iş göremezlik geliri, ölüm geliri, cenaze/emzirme)?
- Kusur oranı tespiti var mı; işverenin İSG yükümlülük ihlali somutlaştı mı?
- Alt işveren-asıl işveren veya üçüncü kişi kusuru söz konusu mu?
- Bildirim yükümlülüğüne aykırılık (geç/eksik bildirim) iddiası var mı?

## Denetim şeması
1. **Rücunun şartı (5510 m.21/1):** İş kazası/meslek hastalığı, işverenin kasıt veya sigortalının sağlığını koruma ve İSG mevzuatına aykırı hareketi sonucu meydana gelmişse SGK, yaptığı/ileride yapacağı ödemeleri işverenden ister. Sorumluluk kusurla sınırlıdır; kusursuz işverene rücu edilmez.
2. **Üçüncü kişi sorumluluğu (m.21/4) ve bildirim aykırılığı (m.21/2):** Olay üçüncü kişi kusuruyla olduysa ona rücu; işveren bildirim yükümlülüğünü ihlal ettiyse bildirime kadarki ödemeler ayrıca işverene yüklenebilir.
3. **Kusur tespiti:** Mahkeme, dosyaya özgü bilirkişi/İSG raporuyla kusur dağılımını belirler; SGK talebi işverenin kusuru oranıyla sınırlıdır.
4. **Hesap:** Bağlanan gelirlerin ilk peşin sermaye değeri esas alınır; daha önce iş kazası tazminat davasında belirlenen kusur ve tavan (tazminat miktarı) ile bağlantı kurulur — SGK rücuu sigortalının işverenden isteyebileceği miktarı aşamaz (tavan/halefiyet ilkesi). **Ara sonuç:** Rücua konu kalemleri ve kusur oranını netleştir.
5. **Zamanaşımı:** Genel kurallar ve halefiyetin niteliğine göre; künye gerekiyorsa içtihadı karararama.yargitay.gov.tr'den `[doğrulanacak]` olarak doğrula.

## Çıktı modülleri
- Rücua konu yardım kalemleri tablosu.
- Kusur oranı ve peşin sermaye değeri hesap notu.
- İşveren savunması (tavan, kusur, bildirim, üçüncü kişi) listesi.

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
