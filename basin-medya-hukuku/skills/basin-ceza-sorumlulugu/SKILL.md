---
name: basin-ceza-sorumlulugu
description: "Yayın yoluyla hakaret, özel hayatın ihlali, kişisel verilerin yayılması gibi suçlarda ceza sorumluluğu silsilesini, şikâyet ve uzlaştırmayı değerlendirmek gerektiğinde kullanılır."
---

# Basın Yoluyla İşlenen Suçlar ve Ceza Sorumluluğu

## Görev
Yayın içeriğinin TCK suçu oluşturup oluşturmadığını saptamak, 5187 sayılı Kanun m.11 sorumluluk silsilesini uygulamak, şikâyet ve uzlaştırma sürecini yönetmek.

## Soğuk başlangıç (intake)
1. İçerik hangi suçu oluşturabilir (hakaret, özel hayat, veri ihlali)?
2. Mağdur gerçek kişi mi, kamu görevlisi mi; suç görevden mi kaynaklanıyor?
3. Eser sahibi belli mi; sorumlu müdür kim?
4. Yayın tarihi nedir (dava/şikâyet süresi için)?

## Denetim şeması
1. **Suç tipi**: Hakaret TCK m.125 (alenen işlenmesi nitelikli hâl, m.125/IV); kamu görevlisine görevinden dolayı hakaret artırıcı sebep. Özel hayatın gizliliğini ihlal TCK m.134; kişisel verileri hukuka aykırı yayma TCK m.136; haberleşmenin gizliliği m.132.
2. **Hukuka uygunluk**: Haber verme hakkı, eleştiri hakkı ve iddia/savunma dokunulmazlığı değerlendirilir; gerçeklik, kamu yararı, güncellik ve öz-biçim dengesi varsa fiil hukuka uygun olabilir.
3. **Sorumluluk silsilesi (m.11)**: Eser sahibi sorumludur; eser sahibi belli değilse veya yayım sahibinin engellemesiyle yayımlanmışsa sorumlu müdür sorumlu tutulur. Tüzel kişiler için ayrı değerlendirme yapılır.
4. **Şikâyet ve süre**: Hakaret şikâyete bağlıdır; şikâyet süresi fiil ve failin öğrenilmesinden itibaren altı aydır (TCK m.73). Basın Kanunu m.26 dava sürelerini özel olarak düzenler.
5. **Uzlaştırma**: Hakaret uzlaştırmaya tabidir (CMK m.253).
6. **Ara sonuç**: Suçun unsurları + hukuka uygunluğun yokluğu + süresinde şikâyet varsa ceza süreci işletilir.

## Çıktı modülleri
- Suç tipi-unsur altlama tablosu
- Sorumluluk silsilesi şeması
- Şikâyet dilekçesi iskeleti ve süre uyarısı

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
