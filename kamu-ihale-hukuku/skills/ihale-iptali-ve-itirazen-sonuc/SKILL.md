---
name: ihale-iptali-ve-itirazen-sonuc
description: "İhalenin idarece veya KİK kararıyla iptali, bütün tekliflerin reddi ya da ihalenin sonuçlanamaması hallerinin sonuçları ve isteklinin hak arama yolları değerlendirilirken kullanılır."
---

# İhalenin İptali ve Sürecin Sonlanması

## Görev
İhalenin iptali (idarece m.39/m.40 veya KİK kararıyla) ve bütün tekliflerin reddi hallerinin hukuka uygunluğunu, sonuçlarını ve isteklinin haklarını (teminat iadesi, masraf) değerlendirmek.

## Soğuk başlangıç (intake)
1. İptal kimden geldi: idarenin kendi kararı mı, KİK kararıyla mı?
2. İptal gerekçesi nedir (yeterli rekabet oluşmaması, doküman aykırılığı, ödenek yokluğu vb.)?
3. İptal kararı kesinleşen ihale kararından önce mi sonra mı?
4. Geçici teminatlar iade edildi mi?

## Denetim şeması
1. **İdarenin takdiri (m.39):** İhale yetkilisi, ihale komisyonunun gerekçeli kararı üzerine ihaleyi yapıp yapmamakta serbesttir; ihale iptal edilirse hiçbir taahhüt altına girmiş sayılmaz. Ancak takdir keyfî olamaz, gerekçe denetlenir.
2. **Bütün tekliflerin reddi (m.40):** Komisyon, gerekçesini belirtmek kaydıyla bütün teklifleri reddederek ihaleyi iptal edebilir. İptal hukuka aykırıysa düzeltici işlem/iptal denetimine konu olur.
3. **KİK kaynaklı iptal:** İtirazen şikâyet sonucu Kurul ihalenin iptaline karar verebilir; bu karar idareyi bağlar.
4. **Sonuçlar:** İptalde isteklilere bildirim yapılır, geçici teminatlar iade edilir; istekli kural olarak masraf/menfi zararını talep edemez, ancak idarenin hukuka aykırı/kusurlu iptalinde tam yargı davası gündeme gelebilir.
5. **Ara sonuç:** İptal kararına karşı da süresinde (gerekçenin öğrenilmesinden itibaren) şikâyet-itirazen şikâyet yolu işletilir; aksi halde dava hakkı düşer.

İspat yükü: İptalin keyfîliğini iddia eden istekli, gerekçenin gerçek dışılığını/orantısızlığını gösterir.

## Çıktı modülleri
- İptal türü ve dayanağı sınıflandırması.
- Teminat iadesi ve masraf/zarar değerlendirmesi.
- İptale karşı başvuru/dava yol haritası.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
