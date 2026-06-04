---
name: dis-ticaret-mevzuati
description: "İthalat-ihracat rejimi, ithal lisansları, antidamping ve korunma önlemleri, ek mali yükümlülük ve gözetim uygulamaları söz konusu olduğunda; dış ticaret düzenlemeleri ile gümrük işlemini birlikte değerlendirmek için kullanılır."
---

# Dış Ticaret Mevzuatı ve Ticaret Politikası Önlemleri

## Görev
İthalat/ihracat rejim kararları, ithal lisansları, gözetim ve kayda alma, antidamping/sübvansiyon ve korunma önlemleri ile ek mali yükümlülük uygulamalarını gümrük işlemiyle bütünleşik biçimde değerlendirmek.

## Soğuk başlangıç (intake)
- Eşya hangi GTİP'te; ithalat lisansı, gözetim belgesi veya izin gerekiyor mu?
- Eşya antidamping, korunma önlemi veya ek mali yükümlülük (EMY/İGV) kapsamında mı?
- Gözetim uygulamasında referans kıymetin altında beyan mı söz konusu?
- Önlemin dayanağı tebliğ/karar sayı ve tarihi belirlendi mi?

## Denetim şeması
1. Rejim ve izin: İthalat Rejim Kararı ve ilgili tebliğlerle eşyanın ithalinin serbest, izne/lisansa bağlı veya yasak olup olmadığı belirlenir. Gerekli belge yoksa eşya teslim edilmez ve m.235 yaptırımları gündeme gelir.
2. Gözetim ve kayda alma: Referans kıymetin altında beyanda gözetim belgesi aranır; belge yoksa kıymet farkı üzerinden ek mali yük ve vergi doğabilir. Gözetimin kıymet belirleme yöntemiyle ilişkisi denetlenir.
3. Ticaret politikası önlemleri: Antidamping ve sübvansiyona karşı önlemler ile korunma önlemleri ilgili tebliğlerle belirli menşe/GTİP'lere uygulanır; menşe tespiti (bkz. menşe becerisi) bu önlemler için belirleyicidir. EMY ve İGV oranları güncel mevzuatla teyit edilir.
4. Süre ve geçiş: Önlem kararlarının yürürlük tarihi, geçiş hükümleri ve yoldaki eşya istisnaları kontrol edilir; tescil tarihi belirleyicidir.
5. İspat: Eşyanın önlem kapsamında olup olmadığı menşe ve sınıflandırma belgeleriyle ortaya konur; idare aksini teknik tespit ve menşe sonradan kontrol sonucuyla ileri sürer.
6. Ara sonuç: Uygulanacak önlem, oran ve belgeler belirlenir; gümrük işlemine etkisi ve doğacak mali yük ile ihtilaf riski saptanır. Güncel oran/önlem değerleri Resmi Gazete ve mevzuat ile doğrulanmalıdır.

## Çıktı modülleri
- Önlem-belge-oran uygunluk kontrol listesi
- Gözetim/EMY kaynaklı kıymet etkisi notu
- Önleme itiraz veya uygulama dışı kalma argüman taslağı

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
