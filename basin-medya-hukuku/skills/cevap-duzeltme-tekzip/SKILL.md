---
name: cevap-duzeltme-tekzip
description: "Bir yayına karşı cevap ve düzeltme metni hazırlamak, yayımlatmak veya yayımlamama hâlinde sulh ceza hâkimliğine başvurmak gerektiğinde; süre ve usul disiplinini kurmak için kullanılır."
---

# Cevap ve Düzeltme (Tekzip)

## Görev
5187 sayılı Kanun m.14 (basılı) ve 6112 sayılı Kanun m.18 (radyo-TV) uyarınca cevap-düzeltme metnini hazırlamak, yayımlatmak ve reddi/ihmali hâlinde sulh ceza hâkimliğine başvuru sürecini yürütmek.

## Soğuk başlangıç (intake)
1. Yayın tarihi ve mecra nedir (basılı/işitsel-görsel/internet)?
2. Düzeltilecek somut ifadeler ve gerçek durum nedir?
3. Başvurucu kişilik hakkı zedelenen kişi mi?
4. Yayından bu yana ne kadar süre geçti?

## Denetim şeması
1. **Hak ve süre**: Basın Kanunu m.14'e göre kişilik hakkı zedelenen kişi, yayından itibaren iki ay içinde, sorumlu müdüre cevap ve düzeltme metnini gönderir. İçeriğin yayını ücretsizdir, hakaret/suç içermemeli ve üçüncü kişilerin haklarını ihlal etmemelidir.
2. **Yayım usulü**: Metin, ilgili yayında (aynı sayfa/sütun, aynı puntoyla) gecikmeksizin yayımlanır. Süreli yayında günlük ise üç gün içinde, diğerlerinde takip eden ilk sayıda yayım kuralı uygulanır (m.14).
3. **Reddi/ihmali**: Sorumlu müdür yayımlamaz veya kurallara aykırı yayımlarsa, ilgili kişi süresi içinde sulh ceza hâkimliğine başvurarak yayım kararı ister. Karara karşı itiraz yolu açıktır.
4. **İnternet**: 5651 sayılı Kanun kapsamındaki içerik için cevap-düzeltme yanında m.9 erişim engelleme/içeriği çıkarma yolu da değerlendirilir.
5. **Ara sonuç**: Metin hukuka uygun, süresinde ve ölçülü ise yayım zorunludur; aksi hâlde hâkimlik kararıyla yayım sağlanır.

## Çıktı modülleri
- Cevap-düzeltme metni taslağı (ölçülü, suç içermeyen)
- Sorumlu müdüre gönderim üst yazısı
- Sulh ceza hâkimliğine başvuru dilekçesi iskeleti

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
