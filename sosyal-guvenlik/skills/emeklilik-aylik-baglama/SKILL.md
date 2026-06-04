---
name: emeklilik-aylik-baglama
description: "Yaşlılık, malullük veya ölüm aylığı bağlanma koşullarının (yaş, prim günü, sigortalılık süresi) hesaplanması ve kademeli geçiş kurallarının uygulanması gerektiğinde kullanılır."
---

# Emeklilik ve Aylık Bağlama Koşulları

## Görev
Sigortalının yaşlılık/malullük/ölüm aylığına hak kazanıp kazanmadığını, hangi tarihte ve hangi mevzuatla emekli olabileceğini koşul koşul belirlemek.

## Soğuk başlangıç (intake)
- İlk sigortalılık (işe giriş) tarihi nedir? (Kademeli geçişte belirleyici.)
- Toplam prim ödeme gün sayısı ve sigortalılık süresi ne kadar?
- Statü 4/a, 4/b yoksa 4/c mi; statüler arası birleştirme gerekiyor mu?
- Malullük/ölüm aylığı mı, normal yaşlılık aylığı mı talep ediliyor?

## Denetim şeması
1. Uygulanacak rejim: İlk sigortalılık tarihine göre 506/1479/5434 veya 5510 ve geçici maddeleri belirlenir. 08.09.1999 ve 30.04.2008 eşik tarihleri kademeyi değiştirir.
2. Yaşlılık aylığı — 5510 m.28: Yaş + prim günü + sigortalılık süresi üçlüsü. Kademeli geçiş (5510 geçici m.6 vd.) ile ilk sigortalılık tarihine bağlı yaş/gün tabloları uygulanır.
3. Malullük aylığı — m.25-27: En az %60 çalışma gücü kaybı, asgari sigortalılık süresi ve prim günü; malullük Kurum sağlık kurulu raporuyla saptanır.
4. Ölüm aylığı — m.32-34: Sigortalının ölümünde gün/koşul şartı ve hak sahipliği (eş, çocuk, ana-baba) ile pay oranları.
5. Hizmet birleştirme: 2829 sayılı Kanun/5510 ile farklı statü hizmetleri birleştirilir; son yedi yıllık hizmete göre aylığı bağlayacak kurum belirlenir. Ara sonuç: hak kazanma tarihi ve aylık türü. İspat: SGK hizmet dökümü, sağlık kurulu raporu.

## Çıktı modülleri
- Emeklilik koşulu hesap tablosu (yaş/gün/süre — gerçekleşen vs. gerekli).
- Hak kazanma tarihi ve eksik koşul tespiti.
- Borçlanma ile koşul tamamlama senaryosu (gerekiyorsa ilgili beceriye yönlendirme).

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
