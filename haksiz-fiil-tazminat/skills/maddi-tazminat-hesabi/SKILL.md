---
name: maddi-tazminat-hesabi
description: "Sorumluluk kurulduktan sonra maddi zararın kalemlerini ayrıştırmak, fiili zarar ve yoksun kalınan kârı hesaplatmak ve hâkimin takdir yetkisini değerlendirmek gerektiğinde kullanılır."
---

# Maddi Tazminatın Belirlenmesi ve Hesabı

## Görev
Maddi zararı kalem kalem belirlemek (fiili zarar + yoksun kalınan kâr), tazminatın kapsamını TBK m.50-51 çerçevesinde tespit etmek ve hâkimin zararı tam ispatlanamayan hallerde takdir yetkisini (m.50/2) doğru konumlandırmak. Hesaplar daima dayanağıyla gösterilir.

## Soğuk başlangıç (intake)
- Zarar kalemleri neler (onarım/yenileme bedeli, gelir kaybı, masraflar)?
- Belge/fatura/ekspertiz var mı; zarar tam belgelenebiliyor mu?
- Zarar görenin kusuru veya zararı artıran davranışı var mı?
- Sigorta/üçüncü kişi ödemesi yapıldı mı (denkleştirme)?

## Denetim şeması
1. **Zarar kavramı.** Malvarlığında istem dışı azalma; farazi (zarar olmasaydı) malvarlığı ile gerçek malvarlığı arasındaki fark. Fiili zarar (doğrudan kayıp) ve yoksun kalınan kâr (mahrum kalınan kazanç) ayrılır.
2. **Tazminatın kapsamı (m.51).** Hâkim, tazminatın kapsamını ve ödenme biçimini zararın ağırlığı ile kusurun derecesini göz önünde tutarak belirler. Kural tam tazmin; zararı aşan zenginleşme verilmez.
3. **İspat ve takdir (m.50).** Zarar görenin zararını ispatı asıldır; zararın gerçek miktarı kesin ispat edilemiyorsa hâkim olayların olağan akışını ve zarar görenin aldığı önlemleri göz önünde tutarak hakkaniyetle belirler (m.50/2).
4. **Denkleştirme (yararların mahsubu).** Aynı olaydan doğan ve zararı azaltan yararlar (kurtarılan değer, bazı ödemeler) belirli ölçüde mahsup edilebilir; sosyal güvenlik/sigorta ödemelerinin etkisi ve rücu ilişkisi ayrıca incelenir.
5. **Faiz ve dönem.** Haksız fiilde temerrüt kural olarak fiil/zarar tarihinde başlar; talep edilen faiz türü ve başlangıcı belirtilir.
6. **Ara sonuç.** Kalem-tutar-dayanak tablosu kurulur; belgesiz kalemler için bilirkişi/ekspertiz ihtiyacı ve m.50/2 takdiri işaretlenir. Karmaşık hesaplarda aktüer/bilirkişi yönlendirmesi yapılır.

## Çıktı modülleri
- Zarar kalemleri ve tutar-dayanak tablosu.
- Bilirkişi/ekspertiz soru listesi (belirsiz kalemler için).
- Faiz türü-başlangıç notu ve talep sonucu rakamı taslağı.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
