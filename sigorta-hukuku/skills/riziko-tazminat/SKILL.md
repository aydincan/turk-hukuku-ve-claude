---
name: riziko-tazminat
description: "Riziko gerçekleştikten sonra ihbar yükümlülüğü, teminat-istisna değerlendirmesi ve zarar/tazminat hesabı yapılması gerektiğinde kullanılır; eksik/aşkın sigorta ve muafiyet düşümlerini içeren tazminat denetimi için temel beceridir."
---

# Rizikonun Gerçekleşmesi, İhbar ve Tazminatın Belirlenmesi

## Görev
Gerçekleşen olayın teminat kapsamına girip girmediğini, ihbar yükümlülüğünün yerine getirilip getirilmediğini ve ödenecek tazminatın miktarını (tazminat ilkesi, eksik/aşkın sigorta, muafiyet) belirlemek.

## Soğuk başlangıç (intake)
1. Riziko ne zaman, nerede ve nasıl gerçekleşti; olay teminat tanımına uyuyor mu?
2. Sigortacıya ihbar yapıldı mı, ne zaman?
3. Sigorta bedeli ile rizikoya konu malın gerçek değeri nedir (eksik/aşkın sigorta)?
4. Muafiyet, sovtaj (kurtarılan kıymet), eksper raporu var mı?

## Denetim şeması
1. **Riziko-teminat eşleştirmesi.** Olay, poliçe ve genel şartlardaki teminat tanımına giriyor mu? İstisna kapsamında mı (örn. kasko genel şartlarında alkollü araç kullanımı)? İspat: teminatı sigortalı, istisnayı sigortacı.
2. **İhbar yükümlülüğü.** TTK m.1446: sigorta ettiren, rizikonun gerçekleştiğini öğrendikten sonra gecikmeksizin sigortacıya bildirir. m.1447: ihbarın ihmali, sigortacının ödeyeceği tazminatı artırdığı ölçüde indirim sebebidir (kasıtta tam, kusurda artış oranında). Ara sonuç: ihbar zamanında mı?
3. **Tazminat ilkesi.** TTK m.1459: zarar sigortasında sigortalı, gerçek zararından fazlasını isteyemez (zenginleşme yasağı).
4. **Eksik/aşkın sigorta.** TTK m.1462 (eksik sigorta — sigorta bedeli değerden düşükse oranlama/nispet kuralı); m.1463 (aşkın sigorta — bedel değeri aşarsa aşan kısım geçersiz, kötüniyet halinde sonuçları). m.1461 birden çok sigorta.
5. **Düşümler.** Muafiyet (tenzili/entegral), sovtaj değeri, daha önce ödenen tazminat düşülür. Can sigortasında tazminat ilkesi uygulanmaz; sigorta bedeli ödenir (TTK m.1487 vd.).

## Çıktı modülleri
- Riziko-teminat-istisna eşleştirme tablosu.
- İhbar zamanlaması ve indirim değerlendirmesi.
- Tazminat hesabı (gerçek zarar / oranlama / muafiyet / sovtaj).
- Talep edilebilir net tutar ve dayanak maddeleri.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
