---
name: ihtiyati-tedbir-delil-tespiti
description: "İhlali durdurmak veya delilleri korumak için acil koruma tedbiri istenmesi gerektiğinde; FSEK m.77 ihtiyati tedbir, toplatma, el koyma ve HMK delil tespiti şartlarını ve dilekçesini hazırlamak için kullanılır."
---

# İhtiyati Tedbir ve Delil Tespiti

## Görev
Süregelen veya yakın tehlike arz eden ihlale karşı ihtiyati tedbir, toplatma/el koyma ve delil tespiti yollarını değerlendirmek, şartlarını test edip taslağını üretmek.

## Soğuk başlangıç (intake)
- İhlal halen sürüyor mu; gecikme telafisi güç zarar doğurur mu?
- Tedbir konusu nedir (satışın durdurulması, çoğaltma nüshalarına/araçlara el koyma, içeriğin kaldırılması)?
- Delil kaybolma riski var mı (çevrimiçi içerik, geçici ürün)?
- Yaklaşık ispat için hangi belgeler mevcut?

## Denetim şeması
1. Yaklaşık ispat (m.77, HMK m.390/3): Tedbir isteyen, hakkının ve ihlalin/ihlal tehlikesinin varlığını yaklaşık olarak ispatlar. FSEK m.77, esaslı zarar/ani tehlike hâlinde ihtiyati tedbir ve gümrükte/sınırda durdurma dâhil önlemleri öngörür.
2. Tedbir türü: Çoğaltılmış nüshalara, çoğaltmaya yarayan araçlara el koyma/imha veya satışın-yayımın durdurulması; çevrimiçi içerikte erişimin/kullanımın engellenmesi. Ölçülülük gözetilir (HMK m.391); en az müdahaleyle amaca ulaşan tedbir seçilir.
3. Teminat: Kural olarak teminat karşılığı verilir (HMK m.392); haklılığın yüksek olasılığı teminattan muafiyet gerekçesi olabilir.
4. Delil tespiti (HMK m.400-405): İleride ispatın zorlaşacağı hâllerde mevcut durumun (kod, nüsha, ekran görüntüsü, web arşivi) tespiti; bilirkişi ve keşifle desteklenir.
5. Usul ve süre: Dava açılmadan istenen tedbirde, kararın ardından iki hafta içinde esas dava açma yükümlülüğü (HMK m.397/1); aksi hâlde tedbir kalkar. İtiraz yolu (HMK m.394) hatırlanır.
6. Ara sonuç: Uygun tedbir türü, dayanağı, teminat ve süre takvimi belirlenir.

İspat yükü: yaklaşık ispat tedbir isteyene aittir; haksız tedbirden doğan zarardan sorumluluk (HMK m.399) hatırlatılır.

## Çıktı modülleri
- İhtiyati tedbir/delil tespiti dilekçe taslağı (yaklaşık ispat, tedbir türü, teminat).
- Süre takvimi (esas dava açma, itiraz).
- Toplatma/el koyma ve çevrimiçi içerik kaldırma seçenek notu.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
