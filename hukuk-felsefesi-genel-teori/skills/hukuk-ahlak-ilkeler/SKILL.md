---
name: hukuk-ahlak-ilkeler
description: "Bir uyuşmazlıkta yazılı norm yetersizken hukukun genel ilkelerine (dürüstlük, iyiniyet, ölçülülük, nemo auditur, venire contra factum proprium) başvurmak veya hukuk-ahlak sınırını çözmek gerektiğinde kullanın."
---

# Hukuk-Ahlak İlişkisi ve Hukukun Genel İlkeleri

## Görev
Hukuk ile ahlak arasındaki ilişkiyi disipline etmek ve hukukun yazılı olmayan genel
ilkelerini pozitif dayanaklarıyla devreye sokmak; bu ilkeleri "duygusal adalet" değil,
uygulanabilir hukuk kuralı düzeyinde kullanmak.

## Soğuk başlangıç (intake)
- Başvurulmak istenen şey bir yazılı norm mu, yoksa genel bir ilke/ahlaki ölçüt mü?
- İlke, mevcut bir normu yorumlamak/sınırlamak için mi, yoksa boşluğu doldurmak için mi gerekli?
- Karşı taraf kendi önceki davranışıyla çelişiyor mu (çelişkili davranış yasağı)?
- Sonuç ahlaken haklı görünse de pozitif dayanak kurulabiliyor mu?

## Denetim şeması
1. **İlişkiyi konumla.** Hukuk ve ahlakın ayrı normatif düzenler olduğu (pozitivist) ile
   kesiştiği (doğal hukuk) görüşünü ayır; Türk hukukunda ahlak, kendi başına değil pozitif
   bir norm (ör. TBK m.27 ahlaka aykırı sözleşmenin kesin hükümsüzlüğü) üzerinden bağlayıcı olur.
2. **Genel ilkeyi pozitife bağla.** Dürüstlük kuralı ve hakkın kötüye kullanılması yasağı
   (TMK m.2), iyiniyetin korunması (TMK m.3), ölçülülük (Anayasa m.13), ahlaka/kamu düzenine
   aykırılık (TBK m.27) ilkeleri yazılı dayanaktır. İlkeyi bu maddelerden birine raptet.
3. **Alt ilkeleri uygula.** Çelişkili davranış yasağı (venire contra factum proprium),
   kendi kusurundan yararlanamama (nemo auditur), hakkın kötüye kullanılmasının korunmaması
   ve dürüstlüğe aykırı kazanımın geri alınması TMK m.2'nin somut görünümleridir; somut
   vakıaya hangisinin uyduğunu seç.
4. **Sınırı koru.** Genel ilke, açık ve emredici bir normu bertaraf etmek için kullanılamaz;
   ancak istisnaî/katlanılmaz sonuçta TMK m.2 düzeltici işlev görür. Ara sonuç: ilke yorum/
   düzeltme aracıdır, norm ikamesi değil.
5. **İspat/gerekçe.** İlkeye dayanan taraf, ilkeyi tetikleyen somut vakıaları ispatla
   yükümlüdür (TMK m.6); soyut "adalet" iddiası yetmez. Yerleşik içtihat varsa künyesiyle
   anılır, doğrulanmadıkça [doğrulanacak].

## Çıktı modülleri
- Hukuk-ahlak ilişkisi konumlandırma notu.
- Genel ilke → pozitif madde eşleştirme tablosu.
- Uygulanabilir alt ilke ve somut vakıa bağı.
- İspat yükü ve sınır uyarısı.

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
