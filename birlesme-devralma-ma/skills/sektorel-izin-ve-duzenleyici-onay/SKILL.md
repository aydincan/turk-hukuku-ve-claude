---
name: sektorel-izin-ve-duzenleyici-onay
description: "Düzenlenmiş sektörlerde (bankacılık, enerji, sigorta, telekom, sermaye piyasası) pay devrinin gerektirdiği ön izinleri, halka açık hedeflerde çağrı yükümlülüğünü ve KAP açıklamalarını belirlemek için kullanılır."
---

# Sektörel İzin ve Düzenleyici Onaylar

## Görev
Hedef şirketin faaliyet alanına göre devrin tabi olduğu düzenleyici ön izinleri ve halka açık hedeflerde sermaye piyasası yükümlülüklerini saptamak ve takvimlendirmek.

## Soğuk başlangıç (intake)
- Hedef düzenlenmiş bir sektörde mi (banka, enerji, sigorta, telekom)?
- Hedef halka açık ortaklık mı; eşik aşan pay devri var mı?
- Yabancı yatırımcı söz konusu mu (özel kısıtlı sektörler)?
- İşlem kamuya açıklanacak mı, ne zaman?

## Denetim şeması
1. **Bankacılık**: 5411 sayılı Kanun — bankada belirli eşikleri aşan pay devri **BDDK iznine** tabidir; izinsiz devir oy hakkını askıya alabilir.
2. **Enerji**: 6446 sayılı Kanun ve EPDK düzenlemeleri — lisans sahibi tüzel kişide kontrol/pay değişikliği EPDK onayına tabi olabilir.
3. **Sigorta ve diğer**: İlgili düzenleyicinin (Sigortacılık ve Özel Emeklilik Düzenleme ve Denetleme Kurumu vb.) pay devri onayı.
4. **Sermaye piyasası (halka açık hedef)**: 6362 sayılı SPK — yönetim kontrolünü sağlayan pay edinimi **zorunlu çağrıyı** (pay alım teklifi) tetikleyebilir; KAP'ta özel durum açıklaması ve içeriden öğrenenlerin ticareti yasağı (SPK m.106) gözetilir.
5. **Telekom**: BTK yetkilendirme rejimi kapsamında kontrol değişikliği bildirimi/onayı.
6. **Askı etkisi**: Ön izin alınmadan kapanış, oy hakkının kullanılamaması veya idari yaptırım doğurabilir → izin CP olarak kurgulanır.
7. **İspat/dayanak**: Düzenleyici izin yazısı kapanış belgesidir; güncel mevzuat metni teyit edilir `[doğrulanacak]`.

## Çıktı modülleri
- Sektörel izin matrisi (düzenleyici, eşik, süre)
- Çağrı yükümlülüğü değerlendirme notu (halka açık hedef)
- KAP açıklama takvimi
- Düzenleyici başvuru dosyası kontrol listesi

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
