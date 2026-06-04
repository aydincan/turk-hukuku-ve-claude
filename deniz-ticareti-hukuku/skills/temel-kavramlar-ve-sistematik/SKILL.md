---
name: temel-kavramlar-ve-sistematik
description: "Deniz ticareti hukukunun temel kavramlarını (gemi, donatan, taşıyan, navlun, konişmento) ve TTK Beşinci Kitap sistematiğini ilk kez bir dosyaya çerçevelerken; uyuşmazlığın hangi alt alana girdiğini ve hangi norm rejiminin uygulanacağını belirlemek için kullan."
---

# Temel Kavramlar ve Sistematik

## Görev
Deniz ticaretine ilişkin bir olayı doğru vasıflandırmak, ilgili tarafları ve sözleşme/kaza ilişkisini tanımlamak, TTK Beşinci Kitap içinde hangi rejimin uygulanacağını ve hangi milletlerarası kaynakların devreye gireceğini belirlemek.

## Soğuk başlangıç (intake)
- İlişki bir taşıma mı (navlun/konişmento), bir deniz kazası mı (çatma/kurtarma/avarya), yoksa ayni hak/icra meselesi mi (gemi ipoteği/ihtiyati haciz)?
- Geminin bayrağı, sicili ve adı; taraflar tacir mi; sözleşmede tahkim veya yabancı hukuk kaydı var mı?
- Elinizde hangi belgeler var (konişmento, çarter parti, sörvey raporu, gemi jurnali)?
- Olayın tarihi ve zarar/ihbar tarihleri nedir (zamanaşımı için kritik)?

## Denetim şeması
1. **Gemi ve ticaret gemisi nitelendirmesi**: Aracın TTK m.931 anlamında gemi ve ticaret gemisi olup olmadığını belirle; sicile tescilli olup olmadığı (TTK m.954 vd.) ayni hak ve ipotek sonuçlarını etkiler.
2. **Tarafların belirlenmesi**: Donatan (TTK m.1061), gemi işletme müteahhidi (TTK m.1065), taşıyan ve taşıtan, gönderilen; konişmentoda kimin "taşıyan" olduğunu lafza göre tespit et. Donatanın adamlarının kusurundan sorumluluğu (TTK m.1062) kapsamını not et.
3. **İlişki tipinin vasıflandırılması**: Navlun sözleşmesi (yolculuk çarteri / kırkambar — TTK m.1138 vd.) mı, yolcu taşıma mı, yoksa kaza ilişkisi mi? Vasıflandırma, sorumluluk rejimini ve süreyi belirler.
4. **Uygulanacak norm katmanı**: TTK Beşinci Kitap esas; konişmentolu taşımada Lahey-Visby kaynaklı hükümler (TTK m.1178 vd.), müşterek avaryada York-Anvers Kuralları (TTK m.1272 vd.), ihtiyati hacizde 1952 Sözleşmesi ile uyumlu TTK m.1352 vd. Ara sonuç olarak uygulanacak madde setini sabitleyin.
5. **İspat yükü ve ara sonuç**: Kural olarak zararı ve ilişkiyi ileri süren ispatlar; taşıyanın özen borcunun ihlali bakımından ispat yükünün yer değiştirdiği özel haller (denize elverişlilik, m.1141) ayrıca incelenir. Çıktıda hangi rejimin neden seçildiğini gerekçelendirin.

## Çıktı modülleri
- İlişki haritası (taraflar, sıfatlar, sözleşme/kaza zinciri)
- Uygulanacak normlar tablosu (TTK maddeleri + milletlerarası kaynak)
- Vasıflandırma notu ve bir sonraki uzman beceriye yönlendirme

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
