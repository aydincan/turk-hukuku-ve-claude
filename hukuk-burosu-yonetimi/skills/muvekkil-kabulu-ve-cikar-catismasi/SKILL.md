---
name: muvekkil-kabulu-ve-cikar-catismasi
description: "Yeni bir iş veya müvekkil teklifi geldiğinde dosya açmadan önce çıkar çatışması taraması, kabul-ret kararı ve kabul koşullarının belirlenmesi gerektiğinde kullanılır."
---

# Müvekkil Kabulü ve Çıkar Çatışması Taraması

## Görev
Yeni bir müvekkil/iş teklifi geldiğinde, işin kabul edilip edilemeyeceğini meslek hukuku açısından denetlemek; çıkar çatışmasını taramak; kabul edilebilirse kabul koşullarını (kapsam, ücret, masraf) çerçevelemek.

## Soğuk başlangıç (intake)
1. Karşı taraf(lar) ve gerçek lehtar kim? Tam kimlik/unvan nedir?
2. Büro daha önce bu işte, karşı tarafta veya bağlantılı bir uyuşmazlıkta yer aldı mı?
3. İşin türü, değeri ve aciliyeti (yaklaşan bir süre var mı) nedir?
4. Müvekkil başka bir avukattan bu iş için vekâlet aldı/azletti mi?

## Denetim şeması
1. **Çıkar çatışması (1136 m.38; TBB Meslek Kuralları m.35-37)**: Aynı işte karşı tarafa hukuki yardım, ya da menfaati çatışan başka bir müvekkilin temsili yasaktır. Büro müvekkil/karşı taraf veri tabanı taranır. Çatışma varsa iş REDDEDİLİR; geçmiş müvekkile ait sır söz konusuysa m.36 sır saklama yükümlülüğü devam eder.
2. **Sır ve bilgi engeli**: Çatışma "olası" düzeydeyse, bilgi bariyeri yeterli değildir; Türk hukukunda kural ret yönündedir.
3. **Yetki/uzmanlık ve kapasite**: İşin gerektirdiği süre/uzmanlık karşılanamıyorsa kabul edilmez (özen borcu, TBK m.506).
4. **Süre kontrolü**: Yaklaşan zamanaşımı/hak düşürücü süre/dava süresi varsa, kabul ancak süreye yetişilebiliyorsa anlamlıdır; aksi halde müvekkil derhal uyarılır.
5. **Ücret ve sözleşme (1136 m.163-164)**: Avukatlık ücreti sözleşme ile belirlenir; yazılılık esastır. Asgari Ücret Tarifesi altına inilemez. Karşı taraf vekâlet ücreti avukata aittir (m.164/son).
6. **Ara sonuç**: Çatışma yok + kapasite var + süreye yetişilir ise KABUL; aksi halde gerekçeli RET ve gerekirse yönlendirme.

## Çıktı modülleri
- Çatışma tarama sonucu (taranan isimler, sonuç).
- Kabul/ret kararı ve gerekçesi.
- Kabul halinde: avukatlık sözleşmesi taslağı, vekâletname kalemi listesi, kritik süre uyarısı.
- Reddedilen işte sır saklama hatırlatması.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
