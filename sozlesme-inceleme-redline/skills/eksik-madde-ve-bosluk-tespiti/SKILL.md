---
name: eksik-madde-ve-bosluk-tespiti
description: "Sözleşmede bulunması gereken ama eksik bırakılan koruyucu maddeleri, belirsiz tanımları ve çapraz atıf hatalarını tespit etmek gerektiğinde kullanılır."
---

# Eksik Madde, Boşluk ve Tanım Denetimi

## Görev
Sözleşmede bulunması gereken standart koruyucu maddelerin eksikliğini, tanım belirsizliklerini, çapraz atıf ve tutarlılık hatalarını tespit etmek; tamamlayıcı taslak önermek.

## Soğuk başlangıç (intake)
- Sözleşme tipine göre olması gereken standart maddeler hangileri?
- Tanımlar bölümü var mı; kullanılan terimler tanımlanmış mı?
- Ek/anex, fiyat listesi, hizmet seviyesi gibi referanslı belgeler mevcut mu?
- Bildirim, devir, değişiklik gibi "boilerplate" maddeler eksik mi?

## Denetim şeması
1. **Standart madde envanteri**: Süre/yenileme, fesih, sorumluluk-tazminat, cezai şart, gizlilik, KVKK/veri (6698), fikri mülkiyet, devir yasağı (TBK m.183 vd.), mücbir sebep, uyarlama (m.138), bildirim, uygulanacak hukuk-yetki/tahkim, bölünebilirlik, tüm sözleşme (entire agreement), değişiklik şekli. Eksikler işaretlenir.
2. **Boşluk doldurma riski**: Eksik nokta hâkim tarafından tamamlayıcı hukuk kurallarıyla (TBK genel/özel hükümler) doldurulur; bu müvekkil aleyhine sonuç verirse açık hüküm önerilir.
3. **Tanım denetimi**: Kullanılan ama tanımlanmayan terimler; tanımlı ama metinde tutarsız kullanılan terimler; "dahil ancak bunlarla sınırlı olmamak üzere" gibi kapsam ifadeleri.
4. **Çapraz atıf/ek tutarlılığı**: Madde numarası atıfları, eklere yapılan referanslar ve eklerin fiilen var olup olmadığı; çelişkide aleyhe yorum (TBK m.23) riski.
5. **Şekil/yürürlük boşluğu**: İmza, tarih, yürürlük tarihi, nüsha, yetkili imza ve vekâlet teyidi.
6. **İspat etkisi**: Eksik bildirim/şekil maddesi ileride ispat ve hak kullanımını zorlaştırır; somutlaştırma önerilir.

## Çıktı modülleri
- Eksik standart madde kontrol listesi (tip bazlı).
- Tanım ve çapraz atıf hata listesi.
- Tamamlayıcı madde taslakları (`[doldurulacak]` yer tutucularıyla).

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
