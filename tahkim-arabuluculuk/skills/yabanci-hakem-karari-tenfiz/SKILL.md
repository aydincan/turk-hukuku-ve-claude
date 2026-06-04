---
name: yabanci-hakem-karari-tenfiz
description: "Yabancı bir hakem kararını Türkiye'de icra ettirmek veya tenfiz talebine itiraz etmek; New York Sözleşmesi ve MÖHUK çerçevesinde ret sebeplerini denetlemek gerektiğinde kullanılır."
---

# Yabancı Hakem Kararının Tanınması ve Tenfizi

## Görev
Yurt dışında verilmiş bir hakem kararının Türkiye'de hüküm ifade etmesini sağlamak veya
karşı tarafsanız tenfizi engelleyecek ret sebeplerini ortaya koymak. Tenfiz, esasın
yeniden yargılanması değil, sınırlı bir denetimdir.

## Soğuk başlangıç (intake)
1. Karar hangi ülkede, hangi kurum/ad hoc tahkimde verildi?
2. Karar kesinleşti/bağlayıcı mı, taraflara usulüne uygun tebliğ edildi mi?
3. Türkiye veya tahkim yeri New York Sözleşmesi'ne taraf mı?
4. Kararın aslı/onaylı örneği ve tahkim sözleşmesi mevcut mu, yeminli çevirileri var mı?

## Denetim şeması
1. **Uygulanacak rejim**: Türkiye'nin tarafı olduğu **New York Sözleşmesi (1958)** ve
   tamamlayıcı olarak **MÖHUK m.60-63**. Görevli mahkeme asliye (ticaret) mahkemesidir,
   yetki **MÖHUK m.60** uyarınca belirlenir.
2. **Şekli şartlar**: Karar ve tahkim sözleşmesinin aslı/onaylı örneği ve yeminli tercümesi
   sunulur (**NY Sözleşmesi m.IV**, **MÖHUK m.61**).
3. **Ret sebepleri (sınırlı)**: **NY Sözleşmesi m.V** / **MÖHUK m.62** — tahkim
   sözleşmesinin geçersizliği, savunma hakkının ihlali (usulüne uygun bildirim yokluğu),
   hakemlerin yetki aşımı, heyet oluşumunun aykırılığı, kararın bağlayıcı olmaması veya
   iptal edilmesi. **Re'sen** incelenen: uyuşmazlığın Türk hukukuna göre tahkime
   elverişsizliği ve **kamu düzenine açık aykırılık**.
4. **İspat yükü**: m.V/1 (m.62/1) sebeplerini **tenfize itiraz eden** ispatlar; m.V/2
   (elverişlilik, kamu düzeni) mahkemece re'sen gözetilir. Revizyon yasağı (esasa girme
   yasağı) geçerlidir.
5. **Ara sonuç**: Tenfiz edilebilirlik değerlendirmesi ve itiraz dayanakları.

## Çıktı modülleri
- Belge kontrol listesi (aslı/örnek/tercüme).
- Tenfiz dilekçesi taslağı veya tenfize itiraz dilekçesi taslağı (madde atıflı).
- Ret sebebi-ispat yükü tablosu.

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
