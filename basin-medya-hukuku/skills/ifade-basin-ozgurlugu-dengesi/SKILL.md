---
name: ifade-basin-ozgurlugu-dengesi
description: "Bir haber veya yayının ifade özgürlüğü kapsamında korunup korunmadığını, kişilik hakkı ihlali oluşturup oluşturmadığını AYM ve AİHM ölçütleriyle değerlendirmek gerektiğinde kullanılır."
---

# İfade ve Basın Özgürlüğü ile Kişilik Hakkı Dengesi

## Görev
Somut yayının Anayasa m.26/m.28 ve AİHS m.10 koruması altında olup olmadığını; kişilik hakkı (TMK m.24, Anayasa m.17) ile çatışmada hangi menfaatin üstün geldiğini ölçütlü biçimde belirlemek.

## Soğuk başlangıç (intake)
1. İçerik maddi vakıa iddiası mı, değer yargısı mı, karikatür/abartılı eleştiri mi?
2. Konu kamusal tartışmaya katkı sunuyor mu (kamu yararı)?
3. Hedef kişi siyasetçi/kamu görevlisi mi, sıradan birey mi?
4. İddianın olgusal temeli (kaynak, doğrulama) var mı?

## Denetim şeması
1. **Koruma alanı**: Haber, eleştiri ve değer yargıları Anayasa m.26 kapsamındadır; basın için m.28 ek güvence sağlar. Sınırlama Anayasa m.13 ölçütlerine (kanunilik, meşru amaç, ölçülülük) tabidir.
2. **Çatışan menfaatlerin tartımı**: AİHM ve AYM içtihadında kullanılan ölçütler — kamuya katkı, kişinin tanınırlığı ve önceki davranışı, haberin elde ediliş yöntemi, içeriğin biçimi ve sonuçları, yaptırımın ağırlığı [doğrulanacak — kararlarbilgibankasi.anayasa.gov.tr ve hudoc.echr.coe.int].
3. **Vakıa-değer yargısı ayrımı**: Maddi vakıa iddiası ispata elverişlidir; gerçek değilse koruma zayıflar. Değer yargısı ispata tabi değildir ancak yeterli olgusal temel gerektirir.
4. **Görünür gerçeklik ve özen**: Yayın anında mevcut verilere göre özenli davranılmış, kamu yararı, güncellik ve öz-biçim dengesi sağlanmışsa hukuka uygunluk doğar.
5. **Ara sonuç**: Üstün menfaat ifade özgürlüğü lehineyse talep reddedilir; kişilik hakkı lehineyse ihlal tespit edilir.

## Çıktı modülleri
- Tartım tablosu (ölçüt bazında lehe/aleyhe)
- Vakıa/değer yargısı sınıflandırması
- Üstün menfaat sonucu ve gerekçe taslağı

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
