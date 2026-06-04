---
name: avukatin-yetkileri-guvenceleri
description: "Avukatın bilgi-belge isteme, dosya inceleme, örnek alma yetkileri ile büro/üst aramasına ilişkin güvenceler ve görevden doğan dokunulmazlık söz konusu olduğunda kullanılır."
---

# Avukatın Yetkileri, Güvenceleri ve Büro Dokunulmazlığı

## Görev
Avukatın görevini yerine getirirken sahip olduğu yetki ve güvenceleri somut duruma
uygulamak; engellenme veya hukuka aykırı arama hallerinde başvuru yolunu göstermek.

## Soğuk başlangıç (intake)
1. Talep bir kurumdan bilgi/belge/dosya inceleme mi reddedildi?
2. Avukat görevi sırasında mı, görevi nedeniyle mi bir işleme maruz kaldı?
3. Büroda/konutta arama-elkoyma mı söz konusu?
4. İşleme baro temsilcisi katıldı mı; karar var mı?

## Denetim şeması
1. **Bilgi ve belge isteme.** Avukat, işini görmek için gerekli bilgi ve belgeleri kurum ve
   kuruluşlardan isteyebilir; bu talepler kanunda öngörülen istisnalar dışında reddedilemez
   (Av. K. m.2/3). Reddin gerekçesi ve dayanağı sorgulanır.
2. **Dosya inceleme ve örnek.** Avukat, görevli olduğu işlerde ilgili dosyaları inceleyebilir,
   örnek/suret alabilir (Av. K. m.46; CMK m.153 soruşturma dosyası için özel rejim ve
   kısıtlama kararı koşulları). Ara sonuç: kısıtlama kararı var mı, kapsamı ne?
3. **Görevden doğan güvenceler.** Avukatın görevi nedeniyle işlediği iddia edilen suçlarda
   soruşturma usulü ve yetkili merciler özeldir (Av. K. m.58-59); görevi sırasında ve görevden
   dolayı işlenen fiillerde ağırlaştırıcı koruma söz konusudur. Avukata karşı görevi
   dolayısıyla işlenen suçlar hâkime karşı işlenmiş gibi cezalandırılır (Av. K. m.57).
4. **Büro araması.** Avukat bürosu ancak mahkeme kararıyla, kararda yazılı olayla sınırlı
   aranır; arama sırasında baro başkanı/temsilcisi hazır bulunur; sır kapsamı iddia edilen
   şey mühürlenip hâkime gönderilir (CMK m.130). Bu güvencelere aykırı arama hukuka aykırı
   delil sorununu doğurur (CMK m.206/2-a, m.217/2).
5. **Engellenme.** Yetkinin engellenmesi tutanakla belgelenir; idari işleme karşı dava,
   ceza boyutunda suç duyurusu ve baroya bildirim seçenekleri değerlendirilir.

## Çıktı modülleri
- Yetki/engel değerlendirmesi ve dayanak maddeler.
- Arama anı kontrol listesi (karar, baro temsilcisi, mühürleme).
- Engellenmeye karşı başvuru/tutanak taslağı.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
