---
name: hakimin-takdir-yetkisi-tmk-4
description: "Kanun hâkime takdir alanı bıraktığında ya da durumun gereğini, haklı sebepleri veya hakkaniyeti gözetmeyi emrettiğinde; bu takdirin hangi ölçütlere göre ve hangi sınırlar içinde kullanılacağını belirlemek için kullanılır."
---

# Hâkimin Takdir Yetkisi ve Hakkaniyet (TMK m.4)

## Görev
Kanunun takdir yetkisi tanıdığı veya hakkaniyeti emrettiği hâllerde, hâkimin hukuka ve hakkaniyete uygun kararının dayanması gereken ölçütleri belirlemek ve takdirin sınırlarını/denetlenebilirliğini göstermek.

## Soğuk başlangıç (intake)
- Hangi kanun hükmü takdir yetkisi/hakkaniyet atfı içeriyor (ör. manevi tazminat TBK m.56, tazminatın indirilmesi TBK m.51-52, nafaka, cezai şartın tenkisi TBK m.182/3)?
- Takdiri etkileyecek somut vakıalar neler (kusur derecesi, ekonomik durum, olayın özellikleri)?
- Taraflar takdir için hangi ölçütleri öne sürüyor?
- Karar gerekçesinde takdir nasıl denetlenebilir kılınacak?

## Denetim şeması
1. **Takdir yetkisinin kaynağı** — TMK m.4: hâkim, kanunun takdir yetkisi tanıdığı veya durumun gereğini ya da haklı sebepleri göz önünde tutmayı emrettiği hâllerde, *hukuka ve hakkaniyete göre* karar verir. Önce kanunun böyle bir alan açıp açmadığı belirlenir.
2. **Keyfîlik yasağı** — Takdir, sınırsız serbestlik değildir; somut olayın özellikleri, tarafların durumu ve hükmün amacı gözetilerek gerekçelendirilir. Gerekçesiz takdir, denetime kapalı olduğu için hukuka aykırıdır.
3. **Tipik uygulama alanları** — Manevi tazminat miktarı (TBK m.56), tazminattan indirim (TBK m.51-52: kusurun ve durumun gereği), cezai şartın aşırılığı (TBK m.182/3), uyarlama, nafaka takdiri; her birinde kendi özel ölçütleri esas alınır.
4. **Hakkaniyet ölçütleri** — Tarafların ekonomik-sosyal durumu, kusur dereceleri, olayın ağırlığı, caydırıcılık ve zenginleşme yasağı dengesi gibi ölçütler somut biçimde tartılır.
5. **Denetlenebilirlik** — İlk derece takdiri, istinaf/temyizde "takdirin sınırlarının aşılıp aşılmadığı" yönünden denetlenir; ölçütler kararda açıkça gösterilmelidir.
6. **m.1 ile fark** — m.1 boşluk hâlinde kural *yaratma*dır; m.4 var olan bir kuralın hâkime bıraktığı alanın *doldurulması*dır.

## Çıktı modülleri
- Takdir/hakkaniyet atfı içeren hükmün tespiti.
- Somut takdir ölçütleri listesi (olaya uyarlanmış).
- Gerekçeli takdir önerisi (denetlenebilir).
- Üst yargı denetimi notu + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
