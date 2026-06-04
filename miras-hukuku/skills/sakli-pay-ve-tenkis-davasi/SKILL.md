---
name: sakli-pay-ve-tenkis-davasi
description: "Saklı paylı mirasçının payı ölüme bağlı veya sağlararası kazandırmalarla zedelendiğinde tenkis hesabı, oran tespiti ve dava kurgusu için; tasarruf edilebilir oranın aşılıp aşılmadığını ölçmek gerektiğinde kullanılır."
---

# Saklı Pay ve Tenkis Davası

## Görev
Saklı paylı mirasçının (altsoy, ana-baba, eş) saklı payının zedelenip zedelenmediğini hesaplamak ve aşan tasarrufları TMK m.560-571 uyarınca tenkis ettirmek.

## Soğuk başlangıç (intake)
- Davacı saklı paylı mirasçı mı? (altsoy 1/2, ana-baba 1/4, eş — m.506)
- Zedeleyen işlem ne? Vasiyet/atama mı, sağlararası bağış/devir mi?
- Ölüm tarihi ve o tarihteki tereke ve kazandırma değerleri?
- Saklı payın zedelendiği ne zaman öğrenildi? (süre için kritik)
- Lehine kazandırma yapılan kişi mirasçı mı, üçüncü kişi mi?

## Denetim şeması
1. **Saklı pay oranını belirle (m.505-506):** yasal payın altsoyda 1/2, ana-babada 1/4, eşte zümreye göre tamamı veya 3/4'ü.
2. **Tasarruf edilebilir oranı hesapla (m.505/1):** tereke - saklı paylar toplamı. Hesaba esas tereke: m.507 (ölüm anı malvarlığı + eklenecek değerler + sigorta - borçlar - cenaze gideri vb.).
3. **Eklenecek kazandırmaları belirle (m.564-565):** denkleştirmeye tabi olanlar, mirastan feragat karşılığı alınanlar, serbestçe dönülebilir bağışlar, ölümden önceki bir yıl içindeki olağan dışı bağışlar, saklı payı bertaraf amaçlı kazandırmalar. Değerler ölüm tarihine göre (m.565/son atfı).
4. **Tenkis sırası (m.570):** önce ölüme bağlı tasarruflar, yetmezse sağlararası kazandırmalar en yeniden eskiye doğru orantılı indirilir.
5. **İade kapsamı (m.567-568):** lehine tasarruf yapılan iyiniyetliyse mevcut zenginleşme ölçüsünde iade; ayni veya nakdi tenkis seçimi (m.563).
6. **Süre — hak düşürücü (m.571):** öğrenmeden 1 yıl, her hâlde vasiyetlerde açılmadan, diğerlerinde ölümden 10 yıl. Ara sonuç: zedelenen miktar + tenkis oranı + dava türü (eda/def'i — tenkis def'i süreye bağlı değildir).

## Çıktı modülleri
- Tenkis hesap tablosu (tereke, saklı pay, aşan kısım)
- Tenkis davası dilekçesi taslağı (HMK m.119 unsurlu)
- Süre/hak düşürücü süre uyarı notu
- Tenkis def'i alternatifi değerlendirmesi

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
