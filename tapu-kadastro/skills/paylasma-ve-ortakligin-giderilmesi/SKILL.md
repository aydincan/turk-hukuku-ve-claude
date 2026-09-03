---
name: paylasma-ve-ortakligin-giderilmesi
description: "Birden çok kişiye ait taşınmazda paydaşlar arası uyuşmazlık, payın devri, yönetim, ortaklığın aynen taksim veya satış yoluyla giderilmesi (izale-i şuyu) söz konusu olduğunda; paylı ile elbirliği mülkiyet ayrımı ve önalım hakkı değerlendirilirken kullanılır."
---

# Paylı/Elbirliği Mülkiyet ve Ortaklığın Giderilmesi

## Görev
Ortak mülkiyet türünü belirlemek, paydaşların yetki ve yükümlülüklerini saptamak ve ortaklığın giderilmesini (aynen taksim/satış) doğru usulle yürütmek.

## Soğuk başlangıç (intake)
- Mülkiyet türü: paylı (müşterek) mı, elbirliği (iştirak/tereke) mi?
- Talep: payın devri, yönetim/kullanım, önalım, ortaklığın giderilmesi mi?
- Aynen taksim mümkün mü (yüzölçüm, imar, bölünebilirlik) yoksa satış mı gerekecek?
- Yasal önalım hakkı kullanılacak bir pay devri var mı; süre işliyor mu?

## Denetim şeması
1. **Mülkiyet türünü ayır.** Paylı mülkiyette her paydaşın belirli bir payı vardır, payını serbestçe devredebilir (TMK m.688-689). Elbirliği mülkiyette pay belirsizdir, tasarruf oybirliği gerektirir (TMK m.701-703); tereke önce paylı mülkiyete çevrilmeden tek tek pay devri yapılamaz.
2. **Yönetim/kullanımı çöz.** Olağan yönetim çoğunluk, önemli işler ve tasarruf nitelikli kararlar nitelikli çoğunluk/oybirliği (TMK m.690-692). Paydaş giderlere payı oranında katlanır (TMK m.694).
3. **Yasal önalımı denetle.** Paylı mülkiyette paydaş, payın üçüncü kişiye satışında yasal önalım hakkını kullanabilir (TMK m.732-733); satışın bildiriminden 3 ay ve her halde 2 yıl içinde dava (TMK m.733/3) hak düşürücü süresi. Önalım davası alıcıya karşı açılır.
4. **Ortaklığın giderilmesini planla.** Her paydaş paylaşmayı isteyebilir (TMK m.698); öncelik aynen taksim (TMK m.699), bölünemiyorsa satış suretiyle (açık artırma) giderilir. Paylaşmayı engelleyen sözleşme/amaç (en çok 10 yıl) ve uygun olmayan zaman istisnası gözetilir.
5. **Usul.** Ortaklığın giderilmesi davası sulh hukuk mahkemesinde (HMK m.4) görülür; tüm paydaşlar davaya dahil edilir (zorunlu dava arkadaşlığı). Aynen taksimde fen ve kıymet bilirkişisi.
6. **Ara sonuç.** Aynen taksim mi satış mı, önalım süresi, husumet çevresi netleştirilir.

## Çıktı modülleri
- Mülkiyet türü–yetki–talep tablosu.
- Önalım veya ortaklığın giderilmesi dava dilekçesi iskeleti.
- Aynen taksim/satış fizibilitesi ve önalım hak düşürücü süre notu.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
