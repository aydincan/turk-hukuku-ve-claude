---
name: ihtiyati-tedbir-delil-tespiti
description: "Dava açılmadan veya yargılama sırasında bir hakkın güvence altına alınması (HMK m.389-399) ya da kaybolma riski olan delilin tespiti (m.400-405) gerektiğinde; teminat, itiraz ve tedbirin uygulanması süreçleri için."
---

# İhtiyati Tedbir ve Delil Tespiti

## Görev
Hak veya delili korumak için geçici hukuki koruma talebi kurmak; tedbir şartlarını, teminatı, uygulama ve itiraz sürelerini yönetmek.

## Soğuk başlangıç (intake)
- Korunacak menfaat ne? (mevcut durumun değişme/zarar riski var mı?)
- Tedbir dava açılmadan mı, dava sırasında mı isteniyor?
- Hakkın varlığı yaklaşık olarak ispatlanabilir mi (m.390/3)?
- Kaybolma riski olan delil mi söz konusu (tanık yaşlı/hasta, durum değişecek)?

## Denetim şeması
1. **Tedbir sebebi** (HMK m.389): Mevcut durumda meydana gelebilecek bir değişme nedeniyle hakkın elde edilmesinin önemli ölçüde zorlaşacağı veya tamamen imkânsız hâle geleceği ya da gecikme sebebiyle ciddi zarar doğacağı hallerde tedbir istenir.
2. **Yaklaşık ispat** (m.390/3): Talep eden, davanın esası yönünden kendisinin haklılığını **yaklaşık olarak** ispat etmek zorundadır; kesin ispat aranmaz.
3. **Talep ve karar** (m.390-391): Tedbir, dava açılmadan önce esas hakkında görevli/yetkili mahkemeden; dava sırasında davaya bakan mahkemeden istenir. Karar gerekçeli olur.
4. **Teminat** (m.392): Tedbir kural olarak teminat karşılığı verilir; resmi belgeye/kesin delile dayanan haklarda teminattan vazgeçilebilir.
5. **Uygulama ve dava açma zorunluluğu** (m.393-397): Tedbir kararı **bir hafta** içinde uygulanması istenmezse kendiliğinden kalkar (m.393); **dava açılmadan** alınan tedbirde **iki hafta** içinde esas dava açılmazsa tedbir kendiliğinden kalkar (m.397/1).
6. **İtiraz** (m.394): Aleyhine tedbir kararı verilen, tedbirin uygulanmasından itibaren bir hafta içinde itiraz edebilir.
7. **Delil tespiti** (m.400-405): Henüz inceleme sırası gelmemiş veya ileride elde edilmesi imkânsızlaşacak delil için tespit istenir; hukuki yarar (m.401) gerekir.

Ara sonuç: "Tedbir şartı + teminat + uygulama ve dava açma süreleri" çizelgesi.

## Çıktı modülleri
- Tedbir/delil tespiti talep dilekçesi iskeleti (yaklaşık ispat gerekçeli).
- Süre kontrol listesi (1 hafta uygulama, 2 hafta esas dava, 1 hafta itiraz).
- Teminat değerlendirmesi.

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
