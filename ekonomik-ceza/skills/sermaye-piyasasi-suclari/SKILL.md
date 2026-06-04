---
name: sermaye-piyasasi-suclari
description: "Bilgi suistimali/içeriden öğrenenlerin ticareti (SPK m.106), piyasa dolandırıcılığı/manipülasyon (SPK m.107) ve sermaye piyasası araçlarıyla işlenen güveni kötüye kullanma/sahtecilik (m.110) iddiaları ile SPK mütalaa/şikâyet şartı söz konusu olduğunda kullanılır."
---

# Sermaye Piyasası Suçları (Manipülasyon ve İçsel Bilgi)

## Görev
6362 sayılı SPK m.106-107-110 suçlarını unsurlarına göre denetlemek; SPK'nın şikâyet/mütalaa şartını (m.115) ve idari yaptırımla ceza yargısı arasındaki ilişkiyi yönetmek.

## Soğuk başlangıç (intake)
- İddia hangi fiile dayanıyor? (içsel bilgiyle işlem, fiyat/işlem hacmi manipülasyonu, yanıltıcı bilgi/yalan haber)
- Failin pozisyonu: yönetici/ortak/aracı kurum çalışanı/yatırımcı?
- SPK incelemesi/raporu ve şikâyeti/mütalaası var mı (m.115)?
- İdari para cezası ayrıca uygulandı mı?

## Denetim şeması
1. **Bilgi suistimali — insider (SPK m.106)**: Henüz kamuya açıklanmamış, açıklandığında araç fiyatını/yatırımcı kararını etkileyebilecek nitelikteki içsel bilgiyi kullanarak işlem yapma/yaptırma/aktarma. Failin bilgiye erişim kaynağı (organ, çalışan, meslek/görev) ve bilginin "içsel/önemli" niteliği tespit edilir.
2. **Piyasa dolandırıcılığı (SPK m.107)**: (1) işlem bazlı manipülasyon — fiyat/talep/arz konusunda yanlış izlenim veren alım-satım; (2) bilgi bazlı manipülasyon — yalan, yanlış, yanıltıcı bilgi verme, dedikodu yayma. İşlem örüntüsü (wash trade, layering vb.) ve yanıltma kastı incelenir.
3. **m.110 suçları**: Sermaye piyasası araçlarıyla güveni kötüye kullanma, izinsiz halka arz/faaliyet, belge sahteciliği — ilgili fıkraya göre ayrılır.
4. **Şikâyet/mütalaa şartı (SPK m.115)**: Bu suçlarda soruşturma SPK'nın Cumhuriyet başsavcılığına yazılı başvurusuna (şikâyet) bağlıdır; SPK'nın mütalaası alınmadan kovuşturma yürütülemez. İlk kontrol budur.
5. **İdari yaptırımla ilişki**: SPK idari para cezası ve işlem yasakları ayrıca uygulanabilir; ceza ve idari yaptırımın paralelliği ile non bis in idem tartışması not edilir.
6. **Ara sonuç**: Fiil tipi (m.106/107/110), içsel bilgi veya manipülasyon kastının kanıtı, şikâyet şartı ve idari süreç netleşir.

## Çıktı modülleri
- Fiil-madde eşleştirme (m.106/107/110)
- İçsel bilgi/önemlilik veya manipülasyon örüntüsü analizi
- m.115 şikâyet/mütalaa şartı kontrolü
- İdari yaptırım-ceza paralel notu
- Savunma stratejisi taslağı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
