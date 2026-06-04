---
name: kacak-yapi-yikim-ve-muhurleme
description: "Ruhsatsız veya ruhsata aykırı yapı nedeniyle mühürleme, yapı tatil tutanağı, encümen yıkım kararı veya yıkımın infazı söz konusu olduğunda; aykırılığın giderilmesi süreci ve yıkıma karşı dava sorulduğunda kullanılır."
---

# Kaçak Yapı, Mühürleme ve Yıkım Kararı

## Görev
Ruhsatsız/ruhsata aykırı yapı sürecinin idari adımlarını denetlemek ve yıkım kararına karşı savunma/iptal stratejisi kurmak.

## Soğuk başlangıç (intake)
- Yapı tatil tutanağı (mühürleme) tutuldu mu, tarihi ve içeriği ne?
- Aykırılık ruhsatsızlık mı, ruhsata/projeye aykırılık mı, hangi imalatlar?
- Encümen yıkım kararı çıktı mı, tebliğ edildi mi?
- Aykırılığı giderme/ruhsata bağlama imkânı var mı, Yapı Kayıt Belgesi var mı?

## Denetim şeması
1. **Tespit ve durdurma (3194 m.32)**: İdare ruhsatsız/ruhsata aykırı yapıyı tespit edince inşaatı **mühürleyip durdurur** ve yapı tatil tutanağı düzenler. Tutanağın usulüne uygunluğu (tarih, imalat tarifi, tebliğ) ilk denetim noktasıdır; eksik tutanak sonraki işlemleri sakatlar.
2. **Aykırılığın giderilmesi süresi**: Mühürlemeden sonra ilgilisine aykırılığı giderme veya ruhsat alma için süre tanınır. Süre içinde aykırılık giderilir/ruhsata bağlanırsa mühür kaldırılır; aksi halde **yıkım** gündeme gelir.
3. **Encümen yıkım kararı (m.32)**: Süre sonunda belediye/il encümeni yıkıma karar verir. Karar yetki, gerekçe ve aykırılığın somut tespitiyle bağlıdır; ölçülülük (aykırı kısmın ayrılabilirliği — tüm yapı yerine aykırı imalatın yıkımı) denetlenir.
4. **Yapı Kayıt Belgesi etkisi (3194 geçici m.16)**: Geçerli YKB varsa yıkım ve ilgili para cezaları durur; ancak YKB belirli istisnaları (kıyı, başkasının taşınmazı, riskli alan vb.) kapsamaz ve mülkiyet uyuşmazlığını çözmez. YKB'nin kapsamı ve geçerliliği denetlenir.
5. **İspat yükü ve dava**: İdare aykırılığı tutanak ve teknik tespitle ispatlar; davacı ruhsata uygunluğu/giderilebilirliği savunur. Yıkım kararına karşı İYUK m.7'de 60 günde iptal davası ve **yürütmenin durdurulması** (yıkım telafisi imkânsız zarar) istenir.
6. **Ara sonuç**: Usul/yetki/ölçülülük sakatlığı varsa iptal + YD; aksi halde aykırılığın giderilmesi yoluyla idari çözüm önerilir. Danıştay 6./14. Daire ilkesel atıfları `[doğrulanacak]` ile.

## Çıktı modülleri
- İdari süreç kronolojisi (tutanak-süre-encümen-tebliğ).
- Yapı tatil tutanağı ve yıkım kararı usul denetim notu.
- Ölçülülük/ayrılabilirlik değerlendirmesi.
- YD talepli yıkım iptali dilekçe iskeleti.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
