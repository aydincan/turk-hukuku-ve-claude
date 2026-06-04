---
name: anonim-sirket-organlar-yonetim-kurulu
description: "Anonim şirkette yönetim kurulunun oluşumu, görev-yetki dağılımı, temsil, devredilemez yetkiler, toplantı ve karar nisapları ile iç yönerge konuları gündeme geldiğinde; yönetim ve temsil ilişkilerini doğru kurmak için kullanılır."
---

# AŞ Organları ve Yönetim Kurulu

## Görev
Anonim şirkette yönetim ve temsil yapısını TTK'ya uygun kurmak: YK oluşumu, devredilemez yetkiler, yetki devri (iç yönerge), temsil ve bağlayıcılık, toplantı/karar usulü.

## Soğuk başlangıç (intake)
1. YK kaç üyeli; tüzel kişi üye var mı (m.359/2)?
2. Yetki devri/iç yönerge mevcut mu; murahhas üye/müdür atandı mı?
3. Somut işlem hangi yetkiye giriyor (olağan yönetim mi, devredilemez yetki mi)?
4. Temsil yetkisi nasıl düzenlenmiş (çift imza, münferit, sınırlama)?
5. Karar fiziki toplantıyla mı, elden dolaştırmayla mı (m.390/4) alındı?

## Denetim şeması
1. Oluşum: YK en az bir üye (m.359); üyelerin tescil-ilanı m.359-360; tüzel kişi üyenin gerçek kişi temsilcisi m.359/2.
2. Devredilemez görev ve yetkiler: m.375 (üst gözetim, muhasebe-finans denetim düzeni, müdürlerin atanması, genel kurulun hazırlanması vb.) — bunlar devredilemez.
3. Yetki devri: Yönetim yetkisi iç yönergeyle murahhaslara/üçüncü kişilere devredilebilir (m.367); en az bir üyenin temsil yetkisi kalmalı (m.370/1).
4. Temsil: m.370-371; şirket, temsilcilerin işletme konusu dışındaki işlemleriyle de bağlanır, iyiniyetli üçüncü kişiye karşı konu sınırı ileri sürülemez (m.371/2 ultra vires'in yumuşatılması). Temsil yetkisinin sınırlandırılması iyiniyetli üçüncü kişiye karşı geçersiz (m.371/3), ancak merkez/şube ve birlikte imza tescil edilmişse geçerli (m.371/3).
5. Toplantı ve nisap: Aksi esas sözleşmede yoksa üye tam sayısının çoğunluğuyla toplanır, toplantıda hazır üyelerin çoğunluğuyla karar alınır (m.390/1); oyların eşitliği m.390/3; elden dolaştırma m.390/4.
6. Menfaat çatışması/işlem yasakları: m.393 (müzakereye katılma yasağı), m.395 (şirketle işlem/borçlanma yasağı), m.396 (rekabet yasağı).
7. İspat: Geçerli karar ve yetki, kararı dayanak yapan tarafça; usulsüzlük iddiası iddia edence ispatlanır.

## Çıktı modülleri
- YK kararı/iç yönerge taslağı.
- Temsil ve imza sirküleri uyum notu.
- Devredilemez yetki ve menfaat çatışması kontrol listesi.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
