---
name: veri-gizlilik-trafik-konum
description: "Trafik ve konum verisi işleme, abone verisinin gizliliği, haberleşmenin gizliliği, ticari elektronik iletide rıza ve KVKK ile 5809 m.51 kesişimi söz konusu olduğunda kullanılır."
---

# Elektronik Haberleşmede Veri, Gizlilik ve Ticari İleti

## Görev
Telekom/internet faaliyetinde kişisel veri, trafik-konum verisi ve haberleşmenin gizliliği yükümlülüklerini 5809 m.51, KVKK (6698) ve ticari ileti rejimi (6563) çerçevesinde denetlemek; uyum veya ihlal sorumluluğunu belirlemek.

## Soğuk başlangıç (intake)
1. İşlenen veri türü: abone kimlik, trafik, konum, içerik/haberleşme verisi mi?
2. İşleme amacı (faturalama, pazarlama, güvenlik, yasal talep) ve dayanağı nedir?
3. Ticari elektronik ileti gönderiliyor mu; İYS kaydı ve rıza var mı?
4. Bir veri ihlali, talep (ilgili kişi/adli/idari) veya Kurul incelemesi var mı?

## Denetim şeması
1. **Çerçeve kesişimi**: 5809 m.51 — kişisel veri ve gizlilik; trafik/konum verisinin sınırlı amaçla işlenmesi ve anonimleştirme/silme. KVKK genel rejimi (6698 m.4-6 işleme şartları, m.5-6 hukuki sebepler) birlikte uygulanır. Ara sonuç: işleme dayanağı geçerli mi.
2. **Trafik ve konum verisi**: Faturalama ve hizmet dışında işleme için kural olarak abone/kullanıcı rızası; sürenin sonunda silme/anonimleştirme. Konum verisi katma değerli hizmette ek rıza gerektirir.
3. **Haberleşmenin gizliliği**: Anayasa m.22 ve 5809 — içeriğe erişim ancak hâkim kararı/yasal yetkiyle; yetkisiz dinleme/kayıt TCK m.132-138 ve m.243-245 ile yarışabilir.
4. **Ticari elektronik ileti**: 6563 — önceden onay (İYS kaydı), ileti içeriği ve red (ICODE/abonelikten çıkma) hakkı; onaysız ileti idari para cezası doğurur. KVKK pazarlama rızasıyla birlikte değerlendirilir.
5. **İhlal ve bildirim**: Veri ihlalinde KVKK m.12 bildirim (Kurul ve ilgili kişi); 5809 kapsamında BTK bildirim yükümlülükleri ayrıca işler. Yasal talepte (adli/idari) yetki ve ölçülülük denetlenir.

İspat açısından rıza kayıtları, İYS onayı, log ve silme/anonimleştirme süreçleri belirleyicidir.

## Çıktı modülleri
- Veri işleme uyum/boşluk notu (dayanak/süre/rıza).
- İhlal bildirimi veya ilgili kişi başvurusu yanıt taslağı.
- Ticari ileti ve İYS uyum kontrol listesi.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
