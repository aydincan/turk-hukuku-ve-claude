---
name: beyan-tekefful-ve-tazminat
description: "SPA'daki beyan ve tekeffülleri (R&W) kapsam ve katalog olarak tasarlamak, disclosure letter ile sınırlamak ve ihlal halinde tazminat-sınırlama (cap, basket, süre) mimarisini kurmak için kullanılır."
---

# Beyan ve Tekeffüller ile Tazminat Rejimi

## Görev
Satıcı beyan-tekeffül kataloğunu hazırlamak, disclosure letter ile istisnaları yönetmek ve ihlal halinde tazminat ve sorumluluk sınırlamalarını dengeli kurmak.

## Soğuk başlangıç (intake)
- Müvekkil beyanı veren (satıcı) mı, alan (alıcı) mı?
- Beyanlar imza ve/veya kapanış tarihinde tekrarlanacak mı?
- Disclosure letter (açıklama mektubu) hazırlanacak mı?
- Bilgi standardı (best knowledge / fairly disclosed) nasıl tanımlanacak?

## Denetim şeması
1. **Beyan kataloğu**: Kurumsal yetki, pay mülkiyeti ve takyidatsızlık, finansal tablolar, vergi, iş hukuku, fikri mülkiyet, sözleşmeler, dava, uyum, KVKK başlıklarında temel ve operasyonel beyanlar.
2. **Hukuki nitelik**: Türk hukukunda R&W, satımda ayıba karşı tekeffül (TBK m.219 vd.) ile zapttan sorumluluk (TBK m.214 vd.) mantığına benzer; sözleşmeyle bağımsız bir tazminat (indemnity) borcu olarak da kurulabilir.
3. **Disclosure (açıklama)**: Beyanlar disclosure letter ile sınırlandırılır; açıklanan hususlar ihlal sayılmaz. Genel ve özel açıklamalar ayrılır.
4. **İhlal ve tazminat**: İhlal halinde gerçek zarar TBK m.112 (gereği gibi ifa etmeme) çerçevesinde; hile varsa TBK m.36 ile iptal/tazminat hakları saklıdır ve sözleşmesel sınırlamalar hileyi kapsayamaz.
5. **Sınırlamalar**: Azami sorumluluk (cap), eşik (de minimis / basket), zaman sınırı (genel beyanlar için kısa, vergi/temel beyanlar için uzun), sandbagging düzenlemesi.
6. **İspat yükü**: İhlali ve zarar miktarını talep eden taraf ispatlar (HMK m.190).
7. **Ara sonuç**: Müvekkil satıcı ise sınırlamalar genişletilir; alıcı ise temel beyanlar sınırlama dışı bırakılır.

## Çıktı modülleri
- Beyan-tekeffül kataloğu taslağı
- Disclosure letter şablonu (genel + özel açıklamalar)
- Tazminat ve sınırlama klozları (cap/basket/süre)
- Risk dağılım tablosu

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
