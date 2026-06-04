---
name: idari-cozum-uzlasma-duzeltme
description: "Dava açmadan önce uzlaşma, düzeltme-şikâyet ve izaha davet gibi idari çözüm yollarının uygunluğunu, süre ve dava hakkına etkisini değerlendirip seçim yapmak için kullanılır."
---

# İdari Çözüm Yolları (Uzlaşma, Düzeltme, İzaha Davet)

## Görev
Uyuşmazlığı dava yoluna taşımadan önce idari çözüm seçeneklerini (uzlaşma, düzeltme-şikâyet, izaha davet) maliyet-fayda ve dava hakkına etki bakımından değerlendirmek; doğru yolu seçerek ceza ve süre avantajını kullanmak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık bir hukuki yorum farkından mı, yoksa açık bir hesap/maddi hatadan mı kaynaklanıyor?
2. Henüz ihbarname tebliğ edildi mi, yoksa inceleme aşamasında mı (izaha davet imkânı var mı)?
3. Vergi aslı + ceza tutarı ne; uzlaşmada makul indirim beklenir mi?
4. Müvekkilin önceliği hızlı kesinlik mi, yoksa esasta haklılığın tescili mi?

## Denetim şeması
1. **Vergi hatası mı, ihtilaf mı.** Açık vergi hatası (hesap hatası, mükellefte/konuda/dönemde yanılma — VUK m.117-118) varsa düzeltme-şikâyet yolu (m.116-126) daha hızlı ve ucuzdur. Hukuki yorum farkı düzeltmeye konu olmaz, dava/uzlaşma gerekir.
2. **Uzlaşma.** Tarhiyat öncesi (VUK Ek m.11) inceleme sonrası ihbarname öncesinde; tarhiyat sonrası (Ek m.1 vd.) ihbarname tebliğinden sonra 30 gün içinde. Uzlaşmanın vaki olması dava hakkını sona erdirir (Ek m.7); kapsamı ve ceza indirimi tartılır. VUK m.359 fiilleri ve usulsüzlük cezalarının uzlaşma kapsamı dışı kaldığı not edilir.
3. **İzaha davet.** VUK m.370 — ön tespit aşamasında izah ile vergi ziyaı cezasında indirimli kapanış imkânı; sahte belge sınırlamaları kontrol edilir.
4. **Süreye etki.** Uzlaşma talebi dava süresini durdurur (Ek m.7); uzlaşma temin edilemezse kalan süre (en az 15 gün) içinde dava. Düzeltme-şikâyet reddi sonrası dava süresi ayrı işler (VUK m.124). Ara sonuç: seçilen yolun süreyi nasıl etkilediği takvime işlenir.
5. **Seçim.** Ceza indirimi (VUK m.376), uzlaşma indirimi ve dava şansı yan yana konularak öneri yapılır; yollar birbirini dışlayabildiğinden tek bir strateji seçilir.

## Çıktı modülleri
- İdari yol karşılaştırma tablosu (kapsam / indirim / dava hakkı / süre).
- Uzlaşma veya düzeltme-şikâyet başvuru taslağı.
- Strateji önerisi ve süre uyarısı.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
