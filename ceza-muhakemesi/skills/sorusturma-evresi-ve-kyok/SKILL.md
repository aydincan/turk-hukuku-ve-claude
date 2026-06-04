---
name: sorusturma-evresi-ve-kyok
description: "Soruşturmanın başlaması, savcının delil toplaması, ifade/şüpheli hakları, iddianame veya takipsizlik kararı ile takipsizliğe itiraz süreçlerinde kullanılır."
---

# Soruşturma Evresi ve Kovuşturmaya Yer Olmadığı Kararı

## Görev
Soruşturmanın hukuka uygun yürütülüp yürütülmediğini denetlemek; şüpheli/müşteki lehine talepleri belirlemek; iddianame ya da kovuşturmaya yer olmadığı (KYOK) kararına karşı strateji üretmek.

## Soğuk başlangıç (intake)
- Soruşturma neyle başladı: ihbar, şikâyet, suçüstü, resen?
- Şüpheli ifadesi alındı mı, müdafi hazır mıydı?
- Hangi deliller toplandı, eksik delil/araştırma var mı?
- Şikâyete bağlı suç mu (süre işliyor olabilir, TCK m.73)?
- KYOK verildiyse tebliğ tarihi nedir (itiraz süresi için)?

## Denetim şeması
1. **Başlama ve yürütme.** Savcı, ihbar veya şikâyetle suç şüphesini öğrenince soruşturmaya başlar ve maddi gerçeği araştırır; şüphelinin lehine delilleri de toplamak zorundadır (CMK m.158, m.160/2). Kolluk savcının emrinde çalışır (m.161).
2. **Şüpheli hakları.** İfade alınmadan önce haklar hatırlatılır: susma hakkı, müdafi, yakınına haber verme (m.147). Hukuka aykırı yöntemlerle alınan ifade delil olamaz (m.148).
3. **Şikâyet ve süre.** Şikâyete bağlı suçlarda fail ve fiilin öğrenilmesinden itibaren 6 ay içinde şikâyet gerekir (TCK m.73); aksi halde soruşturma şartı yoktur.
4. **Sonuç kararı.** Yeterli şüphe varsa iddianame düzenlenir (m.170); yoksa kovuşturmaya yer olmadığına karar verilir (m.172). Yeni delil olmadıkça aynı fiilden yeniden soruşturma açılamaz (m.172/2).
5. **KYOK'a itiraz.** Karara karşı tebliğden itibaren 15 gün içinde sulh ceza hâkimliğine itiraz edilir (m.173); hâkimlik kovuşturmaya yer olduğuna karar verirse savcı iddianame düzenler.
6. **Ara sonuç.** Eksik soruşturma, hak ihlali veya hatalı takipsizlik tespit edilirse itiraz dilekçesi; aksi halde kovuşturma savunması hazırlığına geçilir.

## Çıktı modülleri
- Soruşturma kronolojisi ve eksik işlem/delil listesi.
- Ek soruşturma/delil toplama talep dilekçesi taslağı.
- KYOK'a itiraz dilekçesi iskeleti (gerekçe + dayanak m.173).
- Şikâyet/zamanaşımı süresi uyarısı.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
