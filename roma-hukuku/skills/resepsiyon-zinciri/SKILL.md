---
name: resepsiyon-zinciri
description: "Bir TMK veya TBK hükmünün İsviçre (ZGB/OR) ve Pandekt üzerinden Roma kökenine kadar geriye götürülmesi; iktibas sırasında yapılan değişikliklerin ve kavram dönüşümünün izi sürülecekse kullanılır."
---

# Resepsiyon Zinciri ve İsviçre Tesiri

## Görev
Yürürlükteki bir Türk özel hukuk normunu, resepsiyon zinciri boyunca (İsviçre ZGB/OR → Pandekt → Roma) geriye götürmek ve iktibas sürecinde yaşanan dönüşümleri tespit etmek.

## Soğuk başlangıç (intake)
- Hangi yürürlükteki madde inceleniyor (TMK m.X / TBK m.X)?
- 1926 metni (743/818) ile 2001/2011 metni (4721/6098) arasında fark gerekli mi?
- İsviçre kaynak maddesi (ZGB/OR) karşılaştırması isteniyor mu?
- Amaç salt köken mi, yoksa yorum argümanı üretmek mi?

## Denetim şeması
1. Yürürlükteki normu sabitle: TMK 4721 veya TBK 6098'deki madde ve fıkra. Örnek eksenler: TMK m.1 (yorum/boşluk), TMK m.2-3 (dürüstlük-iyiniyet), TMK m.683 (mülkiyet), TBK m.1 (icap-kabul), TBK m.49 (haksız fiil), TBK m.77 (sebepsiz zenginleşme).
2. Tarihî iktibas hattını kur: 4721 sayılı TMK, 1926 tarihli 743 sayılı Türk Kanunu Medenisi'nin; 6098 sayılı TBK ise 818 sayılı Borçlar Kanunu'nun halefidir. 743/818 ise İsviçre Medenî Kanunu (ZGB) ve İsviçre Borçlar Kanunu (OR) iktibasıdır.
3. İsviçre kaynağına bağla: ilgili ZGB/OR maddesini eşleştir; lafzî ve sistematik farkları işaretle (çeviri/uyarlama kaynaklı sapmalar dahil).
4. Pandekt katmanını ekle: 19. yüzyıl Alman Pandekt bilimi (Savigny, Windscheid) kavramı nasıl dogmatize etti; ZGB/OR bu birikimden nasıl beslendi.
5. Roma köküne in: kavramı Corpus Iuris Civilis'teki kuruma kadar götür (atıf: D./Inst./Gai.). Maxim varsa doğru Latince ile ver.
6. Dönüşümü ayrıştır: Roma'dan bugüne anlam kayması, kapsam genişlemesi/daralması veya yeni eklenen unsuru (ör. modern dürüstlük kuralının objektifleşmesi) açıkça yaz. Ara sonuç: zincirin her halkasında neyin korunduğunu, neyin değiştiğini tablola.

İspat/dayanak: yürürlükteki norm madde ile; tarihî kanunlar numara ile (743, 818); Roma kaynağı fragmanla; doktrin künyesi [doğrulanacak].

## Çıktı modülleri
- Resepsiyon zinciri tablosu: TMK/TBK → ZGB/OR → Pandekt → Roma.
- 1926 ile güncel metin farkları notu.
- Dönüşüm/sapma listesi.
- Yorum argümanına dönüştürme önerisi (tarihî-sistematik, TMK m.1).

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
