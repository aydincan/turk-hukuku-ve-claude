---
name: tahkim-yargilamasi-usul
description: "Hakem heyetinin oluşumu, tahkim yargılamasının yürütülmesi, süreler ve geçici hukuki koruma gibi tahkim sürecinin işleyişini planlamak veya yönetmek gerektiğinde kullanılır."
---

# Tahkim Yargılaması Usulü

## Görev
Tahkim sürecini başlatmaktan hakem kararına kadar usul adımlarını, süreleri ve risk
noktalarını yönetmek; hakem atama, davanın açılması, delil sunumu ve geçici koruma
talepleri için yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Tahkim iç tahkim (HMK) mi milletlerarası (MTK) mi, kurumsal mı ad hoc mı?
2. Hakem sayısı ve atama usulü anlaşmada nasıl belirlenmiş?
3. Tahkim süresi başladı mı, kararın verilmesi için süre işliyor mu?
4. Geçici tedbir/ihtiyati haciz ihtiyacı var mı?

## Denetim şeması
1. **Hakem sayısı ve atama**: **HMK m.415-417** / **MTK m.7** — sayı tek olmalı;
   belirlenmemişse hakem sayısı ve atama mahkeme veya kurum eliyle tamamlanır. Hakemin
   tarafsızlık/bağımsızlık açıklaması ve **ret sebepleri** (**HMK m.417**, **MTK m.7/C-D**)
   denetlenir.
2. **Davanın açılması ve dilekçeler**: Tahkim davası, talep tarihiyle açılır; iddia ve
   savunma dilekçeleri, deliller hakem heyetinin belirlediği takvime göre sunulur
   (**HMK m.426-428**, **MTK m.10**).
3. **Tahkim süresi**: İç tahkimde kural olarak **1 yıl** (**HMK m.427**), MTK'da **1 yıl**
   (**MTK m.10/B**); taraf anlaşması veya mahkeme kararıyla uzatılabilir. Süre aşımı iptal
   sebebidir; bu yüzden takvim sıkı tutulur.
4. **Geçici hukuki koruma**: Hakem heyeti ihtiyati tedbire karar verebilir ama cebri icra
   gerektiren tedbirler için mahkeme yetkilidir (**HMK m.414**, **MTK m.6**). Mahkemeden
   tedbir istemek tahkim iradesinden vazgeçme sayılmaz.
5. **Ara sonuç**: Usul takvimi, hakem heyeti durumu ve açık eksikler listesi.

## Çıktı modülleri
- Tahkim usul takvimi (atama, dilekçeler, duruşma, karar süresi).
- Hakem atama/ret dilekçesi taslağı.
- Geçici hukuki koruma başvuru notu (yetkili merci ayrımıyla).

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
