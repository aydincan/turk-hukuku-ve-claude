---
name: temel-kavramlar-ve-sistem
description: "Kişisel veri, veri sorumlusu, veri işleyen, ilgili kişi, açık rıza ve özel nitelikli veri ayrımlarının netleştirilmesi gereken her başlangıçta; rol ve kavram tespiti yapılırken kullanılır."
---

# KVKK Temel Kavramlar ve Sistematik

## Görev
KVKK uyuşmazlık veya uyum çalışmasının daha en başında kavramsal zemini doğru kurmak: kişisel veri/özel nitelikli veri ayrımı, veri sorumlusu/veri işleyen/ilgili kişi rolleri, işleme ve aktarım kavramları, açık rızanın gerçek hukuki yeri.

## Soğuk başlangıç (intake)
1. Hangi gerçek kişiye ait, hangi tür veriler söz konusu (kimlik, iletişim, sağlık, biyometrik, finansal)?
2. Müvekkil bu verilerin işlenmesinde kim — sorumlu mu, işleyen mi, ilgili kişi mi?
3. Veriler nereden geliyor, hangi amaçla işleniyor, kime aktarılıyor?
4. İşleme tek seferlik mi, süreklilik gösteren bir faaliyet mi?

## Denetim şeması
1. **Kişisel veri mi?** KVKK m.3/1-d: kimliği belirli veya belirlenebilir gerçek kişiye ilişkin her türlü bilgi. Tüzel kişi verisi KVKK kapsamı dışıdır; anonim hale getirilmiş veri kişisel veri değildir.
2. **Özel nitelikli mi?** KVKK m.6/1: ırk, etnik köken, siyasi düşünce, din-mezhep, kılık-kıyafet, dernek-vakıf-sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti/güvenlik tedbiri, biyometrik ve genetik veriler. Bu liste sınırlıdır (numerus clausus); kıyasla genişletilmez.
3. **Rol tespiti** (m.3): Veri sorumlusu işleme amaç ve vasıtalarını belirleyen; veri işleyen onun adına işleyen kişidir. Yükümlülükler asıl olarak sorumluya yüklenir; aralarında m.12 uyarınca yazılı sözleşme zorunludur.
4. **İşleme şartı var mı?** Genel veride m.5, özel nitelikli veride m.6. Açık rıza tek değil, son çare şarttır — m.3/1-a anlamında özgür irade, belirli konu ve aydınlatmaya dayalı bilgi unsurlarını taşımalıdır; aksi halde geçersizdir.
5. **Ara sonuç**: Kavram ve rol netleşmeden m.4 ilkeleri ve yaptırım katmanına geçilmez.

İspat yükü: İşlemenin hukuka uygunluğunu (geçerli şarta dayandığını) veri sorumlusu ispatlar; açık rızanın varlığını da sorumlu kanıtlamak zorundadır.

## Çıktı modülleri
- Rol ve veri kategorisi tablosu (genel/özel nitelikli; sorumlu/işleyen).
- İşleme faaliyeti tanım fişi (amaç-veri-sebep-süre-aktarım).
- Açık rızanın gerekip gerekmediğine dair kısa değerlendirme notu.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
