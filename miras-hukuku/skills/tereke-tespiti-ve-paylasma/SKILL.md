---
name: tereke-tespiti-ve-paylasma
description: "Terekenin envanterini çıkarmak, mirasçılık belgesi almak ve elbirliği mülkiyetini sona erdirip paylaşmayı veya ortaklığın giderilmesini sağlamak gerektiğinde; iştirak halinin çözümü, paylaşma sözleşmesi ve satış suretiyle giderme konularında kullanılır."
---

# Tereke Tespiti, Mirasçılık Belgesi ve Paylaşma

## Görev
Terekeyi tespit ve koruma altına almak, mirasçılık belgesini temin etmek ve mirasçılar arasındaki elbirliği mülkiyetini paylaşma sözleşmesi veya ortaklığın giderilmesi davasıyla tasfiye etmek (TMK m.640-676).

## Soğuk başlangıç (intake)
- Mirasçılar belli mi? Mirasçılık belgesi (veraset ilamı) alındı mı?
- Tereke kalemleri neler? (taşınmaz, banka, araç, şirket payı, alacak)
- Mirasçılar paylaşmada anlaşıyor mu, anlaşmazlık mı var?
- Taşınmaz fiilen bölünebilir mi, yoksa satış mı gerekir?
- Denkleştirilecek sağlararası kazandırma var mı (m.669)?

## Denetim şeması
1. **Mirasçılık belgesi (m.598):** Sulh hukuk mahkemesinden veya noterden; çekişme varsa mahkeme. Belge mirasçı sıfatını ve payları gösterir, aksi ispatlanana dek karine teşkil eder.
2. **Tereke tespiti/koruma (m.589-592):** Sulh hukuk mahkemesinden defter tutma, mühürleme, terekenin yönetimi; mirasçı belirsizse temsilci atanması.
3. **Elbirliği mülkiyeti (m.640, m.701 vd.):** Miras ortaklığı elbirliği mülkiyetidir; mirasçılar terekeye birlikte malik olup birlikte tasarruf ederler. Oybirliği gerekir.
4. **Paylaşmaya geçiş (m.642-647):** Her mirasçı paylaşmayı isteyebilir (m.642); sözleşmeyle paylaşma yazılı şekle tabidir (m.676). Anlaşma sağlanamazsa ortaklığın giderilmesi davası açılır.
5. **Ortaklığın giderilmesi (m.642 vd., HMK m.4 — sulh hukuk):** Önce aynen taksim araştırılır; mümkün değilse satış suretiyle giderme. Denkleştirme talepleri burada karşılanır (m.669).
6. **Ara sonuç:** mirasçılık belgesi + envanter + paylaşma yolu (sözleşme/dava). İspat: tapu, banka, sicil kayıtları; pay kesirleri belge ile (m.6).

## Çıktı modülleri
- Mirasçılık belgesi talebi dilekçesi
- Tereke envanteri tablosu (aktif/pasif, değer)
- Paylaşma sözleşmesi taslağı (yazılı şekilli)
- Ortaklığın giderilmesi (izale-i şuyu) dava dilekçesi taslağı

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
