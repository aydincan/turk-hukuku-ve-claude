---
name: gecici-kesin-muhlet
description: "Geçici mühletin alınması, kesin mühlete geçiş, mühletin uzatılması veya kaldırılması ile mühletin alacaklılar ve sözleşmeler üzerindeki etkilerini yönetmek gerektiğinde kullanılır."
---

# Geçici ve Kesin Mühlet Yönetimi

## Görev
Mühlet aşamasını uçtan uca yönetmek: geçici mühletin alınması, kesin mühlete geçiş kararının hazırlanması, mühletin uzatılması veya kaldırılması (m.291, m.292) ve mühletin hukuki sonuçlarının takibi.

## Soğuk başlangıç (intake)
- Geçici mühlet kararı tarihli mi, ne kadar süre kaldı?
- Komiserin ara raporu hazırlandı mı?
- Mühlet sırasında borçlunun aleyhine yeni takip/ihtiyati haciz girişimi var mı?
- Borçlunun rehinli/imtiyazlı alacaklıları kim?

## Denetim şeması
1. **Geçici mühletin sonuçları (m.288).** Geçici mühlet, kesin mühletin sonuçlarını doğurur. İlan ve ilgili sicillere bildirim yapılmış mı kontrol edilir.
2. **Kesin mühlete geçiş (m.289).** Komiser raporu, borçlu ve varsa talep eden alacaklı dinlenir; başarı ihtimali değerlendirilir. İspat yükü borçluda.
3. **Mühletin takipler bakımından sonucu (m.294).** Mühlet içinde borçluya karşı icra takibi yapılamaz, başlamış takipler durur; istisnalar: rehnin paraya çevrilmesi yoluyla takip başlatılabilir ancak muhafaza tedbirleri ve satış yapılamaz (m.295). İmtiyazlı alacaklar için ihtiyati haciz/tedbir sınırlamaları denetlenir.
4. **Sözleşmeler bakımından (m.296).** Borçlunun taraf olduğu sözleşmelerin mühlet nedeniyle feshini sınırlayan hükümler uygulanır; sürekli edimli sözleşmelerin akıbeti değerlendirilir.
5. **Tasarruf yetkisinin sınırlanması (m.297).** Borçlu, komiserin onayı olmadan rehin tesisi, kefil olma, taşınmaz/işletme devri gibi işlemleri yapamaz; aksi işlem hükümsüzdür. İhlal halinde mühletin kaldırılması (m.292) gündeme gelir.
6. **Mühletin kaldırılması (m.291-292).** Konkordatonun başarıya ulaşamayacağı anlaşılır veya borçlu kötüye kullanırsa mühlet kaldırılır, iflasa tabi borçlu için iflas açılır. Ara sonuç: mühlet devam mı, kaldırma mı.

## Çıktı modülleri
- Mühlet süre takvimi ve uzatma/kaldırma senaryoları.
- Tasarruf yetkisi kısıtı için onay-gerektiren işlemler listesi.
- Rehinli/imtiyazlı alacaklı haritası.
- Komisere/mahkemeye sunulacak ara rapor taslağı.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
