---
name: cevre-ceza-hukuku
description: "Çevrenin kasten veya taksirle kirletilmesi, atıkların izinsiz işlenmesi ve gürültü suçlarında ceza sorumluluğunu değerlendirmek; soruşturma, etkin pişmanlık ve şirket yöneticilerinin ceza riski yönetiminde kullan."
---

# Çevreye Karşı Suçlar (Ceza Boyutu)

## Görev
Çevreyi kirletme fiillerinin ceza hukuku boyutunu değerlendirmek; suç tipini, kast/taksir ayrımını ve etkin pişmanlık imkânını belirleyerek sanık veya şikâyetçi tarafı yönlendirmek.

## Soğuk başlangıç (intake)
1. Fiil ne: atık/artık verme, izinsiz tehlikeli atık işleme, gürültü, çevre kirliliği?
2. Fiil kasten mi taksirle mi işlendi; çevreye/insan sağlığına etki kalıcı mı?
3. Şüpheli gerçek kişi mi; tüzel kişi (şirket) bünyesinde hangi yetkili sorumlu?
4. Etkin pişmanlık (kirliliğin giderilmesi) imkânı var mı?

## Denetim şeması
1. **Suç tipi**: TCK m.181 çevrenin kasten kirletilmesini, m.182 taksirle kirletilmesini suç sayar; atığın veya artığın toprağa, suya, havaya verilmesi tipikliğin çekirdeğidir. Tehlikeli atıklarda nitelikli haller ve ağırlaştırılmış cezalar gündeme gelir.
2. **Manevi unsur**: Kast ile taksir ayrımı ceza miktarını belirler; "kalıcı etki" ve "insan/hayvan sağlığına zarar" nitelikli hal yaratır.
3. **Failin belirlenmesi**: Tüzel kişilerde fiili işleyen/önlemeyen yetkili gerçek kişi sorumludur; TCK m.20/2 uyarınca tüzel kişiye ceza verilemese de güvenlik tedbiri (TCK m.60) uygulanabilir.
4. **Etkin pişmanlık ve giderim**: Kirliliğin giderilmesi cezada indirim/etkin pişmanlık bakımından değerlendirilir; idari ve cezai süreç paralel yürür, biri diğerini bekletmez.
5. **Usul, ispat ve ara sonuç**: Bilirkişi ve teknik tespit (numune, ölçüm) deliller arasında merkezdedir; usulsüz numune ceza yargısında da delili sakatlar. İdari yaptırım ile cezanın ayrı süreçler olduğu (non bis in idem tartışması) gözetilir.

## Çıktı modülleri
- Suç vasfı ve unsur analizi (m.181/182)
- Kast/taksir ve nitelikli hal değerlendirmesi
- Yönetici ceza riski notu (şirket)
- Savunma/şikâyet ve etkin pişmanlık stratejisi

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
