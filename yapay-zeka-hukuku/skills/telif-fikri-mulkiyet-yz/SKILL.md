---
name: telif-fikri-mulkiyet-yz
description: "Üretken yapay zekânın eğitiminde eser kullanımı, ürettiği içeriğin eser/tasarım/marka sahipliği, telif ihlali iddiası veya açık kaynak lisans uyumu gündeme geldiğinde FSEK ve SMK çerçevesinde değerlendirme yapıldığında kullanılır."
---

# Yapay Zekâ ve Fikri Mülkiyet

## Görev
Yapay zekâ ile eser/içerik ilişkisini iki yönden çözmek: girdi tarafında eğitim verisi olarak eser kullanımının telif boyutu; çıktı tarafında üretilen içeriğin hak sahipliği ve ihlal değerlendirmesi.

## Soğuk başlangıç (intake)
1. Sorun girdi tarafında mı (eğitim verisinde eser kullanımı) yoksa çıktı tarafında mı (üretilen içerik)?
2. Üretilen çıktı esere benzer mi; somut bir eserin kopyası/işlemesi iddiası var mı?
3. Modelin lisansı/açık kaynak bileşenleri ve kullanım koşulları neler?
4. Müvekkil hak sahibi mi, kullanıcı mı, geliştirici mi?

## Denetim şeması
1. **Çıktıda eser sahipliği**: FSEK m.1/B ve m.8 — eser, sahibinin hususiyetini taşıyan fikrî üründür ve sahibi gerçek kişidir. Tamamen otomatik üretilen çıktı, insan hususiyeti yoksa "eser" sayılmayabilir; insanın yaratıcı katkısı oranında koruma tartışılır. Ara sonuç: çıktı korunan eser mi.
2. **Eğitim verisinde kullanım**: Korunan eserlerin izinsiz model eğitiminde çoğaltılması (m.22) ve işlenmesi (m.21) mali hakları ilgilendirir; FSEK istisnaları (m.30 vd.) dar yorumlanır, genel "metin-veri madenciliği" istisnası Türk hukukunda açıkça düzenlenmemiştir.
3. **İhlal değerlendirmesi**: Çıktı somut bir eserin kopyası/işlemesi ise tecavüz; benzerlik ve esinlenme ayrımı yapılır. Tecavüzde ref/men (FSEK m.66-67) ve tazminat (m.68 — üç kata kadar) gündeme gelir.
4. **Marka/tasarım/buluş**: SMK kapsamında YZ üretimi tasarım/markada gerçek hak sahipliği; buluşta mucit gerçek kişi olmalıdır.
5. **Lisans uyumu**: Açık kaynak ve veri seti lisans şartlarına uyum sözleşmesel ve telifsel olarak ayrı denetlenir.

FSHM uygulaması için karararama.yargitay.gov.tr; AB ve ABD'deki davalar yalnız karşılaştırmalı kaynaktır, künye [doğrulanacak].

## Çıktı modülleri
- Girdi/çıktı telif risk haritası.
- Eser/koruma değerlendirme notu.
- İhlal iddiasına karşı savunma veya hak talebi taslağı.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
