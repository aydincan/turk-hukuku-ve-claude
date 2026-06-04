---
name: birlesme-devralma-izni
description: "Bir birleşme, devralma, ortak girişim veya kontrol değişikliği işleminin Rekabet Kurulu iznine tabi olup olmadığını, bildirim eşiklerini ve esas inceleme riskini değerlendirmek istendiğinde kullanılır."
---

# Birleşme ve Devralma İzni (m.7)

## Görev
İşlemin 4054 m.7 ve Birleşme/Devralma Tebliği (2010/4) kapsamında bildirime tabi bir yoğunlaşma oluşturup oluşturmadığını, ciro eşiklerini ve etkin rekabetin önemli ölçüde azalıp azalmayacağını değerlendirmek.

## Soğuk başlangıç (intake)
- İşlem türü: birleşme, hisse/varlık devri, ortak girişim kuruluşu?
- Kontrolde kalıcı değişiklik doğuyor mu (tek/ortak kontrol)?
- Tarafların Türkiye ve dünya ciroları yaklaşık ne düzeyde?
- Taraflar aynı pazarda rakip mi (yatay), tedarik zincirinde mi (dikey)?

## Denetim şeması
1. **Yoğunlaşma var mı (m.7, Tebliğ 2010/4)** — kontrolde kalıcı değişiklik gerekir. Geçici/finansal işlemler, grup içi yeniden yapılanmalar kural olarak yoğunlaşma sayılmaz. Tam işlevsel ortak girişimler bildirime tabidir.
2. **Bildirim eşikleri** — Tebliğ 2010/4'teki ciro eşiklerinin aşılıp aşılmadığı kontrol edilir (Türkiye ciroları ve taraf bazlı eşikler; teknoloji teşebbüsleri için özel eşik kuralı). **Eşik tutarları periyodik güncellendiğinden güncel Tebliğ metninden doğrulanır.**
3. **Zorunlu bildirim ve bekleme** — eşik aşılıyorsa işlem Kurul izni olmadan hukuken geçerlilik kazanmaz (m.7); izinden önce kapanış (gun-jumping) yaptırım riskidir.
4. **Esas inceleme** — etkin rekabetin özellikle hâkim durum yaratılması/güçlendirilmesi yoluyla önemli ölçüde azalıp azalmayacağı; yatay örtüşme, dikey/portföy etkileri, koordinasyon riski incelenir. HHI ve pazar payı eşikleri ön eleme aracıdır.
5. **Çözümler (taahhüt)** — rekabet endişesi varsa yapısal (elden çıkarma) veya davranışsal taahhütler sunulabilir; koşullu izin verilebilir.
6. **Ara sonuç** — bildirime tabi değil / koşulsuz izin beklenir / endişeli (taahhüt gerekli) / yasaklama riski şeklinde sonuçlandırılır.

## Çıktı modülleri
- Bildirim gerekliliği kararı ve eşik hesabı (güncel Tebliğ ile doğrulanacak).
- Yatay/dikey örtüşme ve risk haritası.
- Bildirim formu için bilgi/veri ihtiyaç listesi.
- Olası taahhüt senaryoları ve gun-jumping uyarısı.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
