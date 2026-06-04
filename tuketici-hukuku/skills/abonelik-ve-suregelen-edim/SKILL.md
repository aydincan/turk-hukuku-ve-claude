---
name: abonelik-ve-suregelen-edim
description: "Cep telefonu, internet, dijital platform, spor salonu gibi abonelik sözleşmelerinde tüketicinin her zaman fesih hakkını, bedel iadesini ve taahhüt/cezai şart denetimini değerlendirmek gerektiğinde kullanılır."
---

# Abonelik ve Sürekli Edimli Sözleşmeler

## Görev
Abonelik ve sürekli edimli tüketici sözleşmelerinde tüketicinin fesih hakkını, fesih usulünü, peşin alınan bedelin iadesini ve taahhütlü aboneliklerdeki cezai şart/erken cayma bedeli denetimini altlamak.

## Soğuk başlangıç (intake)
- Abonelik konusu ne (haberleşme, internet, dijital içerik, üyelik) ve süresi belirli mi?
- Taahhüt/kampanya var mı; erken çıkışta bedel öngörülmüş mü?
- Tüketici feshetmek mi istiyor, yoksa fesih engelleniyor mu?
- Peşin ödenen bir bedel var mı, fesih usulü sözleşmede nasıl düzenlenmiş?

## Denetim şeması
1. **Fesih hakkı (TKHK m.52):** Tüketici, belirsiz süreli veya süresi bir yıldan uzun belirli süreli abonelik sözleşmesini herhangi bir gerekçe göstermeden ve cezai şart ödemeden istediği zaman feshedebilir.
2. **Fesih usulü ve kolaylığı (m.52):** Sağlayıcı, aboneliğin kurulduğu yöntemi/araçları ile aynı kolaylıkta fesih imkânı sunmak zorundadır; fesih, talebin ulaşmasından itibaren kısa sürede (Yönetmelikte öngörülen gün) hüküm doğurur.
3. **Bedel iadesi:** Fesih halinde tüketici, ifa edilmemiş kısma ilişkin peşin ödediği bedelin iadesini isteyebilir; kullanılmayan dönem orantılı biçimde geri verilir.
4. **Taahhüt ve cezai şart denetimi:** Taahhütlü aboneliklerde erken fesih bedeli, ancak sağlayıcının sunduğu cihaz/indirim gibi somut bir avantajla orantılıysa ve önceden açıkça bildirilmişse geçerlidir; orantısız ya da müzakere edilmemiş cezai şart m.5 haksız şart denetimine tabidir.
5. **Sektörel mevzuat:** Elektronik haberleşmede BTK düzenlemeleri tamamlayıcıdır; ancak TKHK m.52'nin tüketici lehine emredici fesih hakkı saklıdır.
6. **Ara sonuç:** Fesih hakkı doğmuş mu, erken çıkış bedeli geçerli mi, ne kadar bedel iade edilmeli?

## Çıktı modülleri
- Fesih hakkı ve usul değerlendirmesi.
- Fesih bildirimi taslağı.
- İade edilecek bedel hesabı.
- Cezai şart geçerlilik analizi.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
