---
name: sureler-ve-zamanasimi
description: "Konkordato sürecindeki tüm kanuni süreleri, mühlet ve uzatma takvimini, faiz ve zamanaşımı etkilerini hesaplamak ve takip etmek gerektiğinde kullanılır."
---

# Süreler, Mühlet Takvimi ve Zamanaşımı

## Görev
Konkordatonun süre yoğun yapısını kontrol altına almak: geçici/kesin mühlet süreleri ve uzatmaları, alacak bildirim ve toplantı süreleri, kanun yolu süreleri, mühletin zamanaşımı ve faize etkisi.

## Soğuk başlangıç (intake)
- Hangi kararın tarihi referans alınacak (geçici mühlet, kesin mühlet, tasdik)?
- Mühlet uzatması talep edildi mi?
- Bir kanun yolu süresi mi hesaplanacak?
- Faiz ve zamanaşımı bakımından hangi alacaklar inceleniyor?

## Denetim şeması
1. **Geçici mühlet (m.287).** Kural üç ay; mahkeme bir ay daha uzatabilir (toplam en çok dört ay). Başlangıç: geçici mühlet kararı tarihi.
2. **Kesin mühlet (m.289).** Bir yıl; güçlük halinde komiser raporuyla altı aya kadar uzatma (toplam en çok bir buçuk yıl). Uzatma talebinin mühlet bitmeden yapılması gerekir.
3. **Alacak bildirim ve toplantı süreleri (m.299, m.302).** Davet ilanındaki bildirim süresi ve projenin kabulü için tanınan süre takip edilir; sürelerin kaçırılması çoğunluk hesabını etkiler.
4. **Faiz (m.294).** Kesin mühlet içinde faiz işlemeye devam edip etmeyeceği alacağın türüne göre (rehinli/rehinsiz, sözleşme/kanun) değerlendirilir; faizin durması/işlemesi tasdik projesinde gösterilir.
5. **Zamanaşımı ve hak düşürücü süreler.** Mühletin zamanaşımını ve hak düşürücü süreleri durdurması/kesmesi (İİK ve TBK genel hükümleriyle birlikte) incelenir. Kanun yolu süreleri (istinaf/temyiz) gün gün hesaplanır; resmi tatil ve adli tatil etkisi gözetilir (HMK m.104, m.92-93). İspat: kararın tebliğ/ilan tarihi esas alınır. Ara sonuç: bağlayıcı tarihler takvimi.

## Çıktı modülleri
- Mühlet ve uzatma süre takvimi (tarih bazlı).
- Kanun yolu süre hesabı.
- Faiz ve zamanaşımı etki notu.
- Kritik tarih hatırlatma listesi.

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
