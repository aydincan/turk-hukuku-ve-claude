---
name: imar-para-cezalari
description: "3194 sayılı Kanun m.42 uyarınca verilen idari para cezalarına karşı dava açılacağında; ceza miktarının hesabı, ağırlaştırıcı katsayılar, ceza muhatabı, zamanaşımı ve usul denetimi sorulduğunda kullanılır."
---

# İmar Para Cezaları (m.42)

## Görev
İmar mevzuatına aykırılıktan verilen idari para cezasının hukuka uygunluğunu (muhatap, hesap, usul, süre) denetlemek ve iptal yolunu kurmak.

## Soğuk başlangıç (intake)
- Ceza hangi aykırılığa dayanıyor (ruhsatsız, ruhsata aykırı, yapı denetim eksiği)?
- Ceza kararının tarihi, miktarı ve hesaplama kalemleri neler?
- Muhatap kim (yapı sahibi, müteahhit, fenni mesul, yapı denetim)?
- Aynı fiile başka işlem (yıkım, başka ceza) uygulandı mı?

## Denetim şeması
1. **Cezanın dayanağı (3194 m.42)**: Ruhsatsız/ruhsata aykırı yapı ve mevzuata aykırı eylemler için idari para cezası; ceza yapının türü, yüzölçümü, sınıfı, kullanım amacı ve aykırılığın niteliğine göre belirlenen katsayılarla hesaplanır.
2. **Hesabın denetimi**: m.42'deki taban ceza ve **ağırlaştırıcı katsayılar** (yapının çevre ve görüntü kirliliğine etkisi, kullanım amacı değişikliği, kat ilavesi, hisseli/komşu parsele tecavüz vb.) tek tek incelenir; her katsayının somut gerekçesi aranır. Yanlış/dayanaksız katsayı kısmen iptal sebebidir.
3. **Ceza muhatabı**: Ceza ilgili yapı sahibine, ayrıca müteahhit ve fenni mesul/yapı denetim kuruluşuna ayrı ayrı kesilebilir; muhatabın doğru tespiti ve sorumluluk derecesi denetlenir. Yanlış muhatap iptal sebebidir.
4. **Usul ve yetki**: Cezayı belediye/il encümeni verir; karar gerekçeli, hesabı gösterir ve usulüne uygun tebliğ edilmiş olmalıdır. Eksik gerekçe/tebliğ şekil sakatlığı doğurur.
5. **Zamanaşımı ve ne bis in idem**: İdari yaptırımlarda 5326 sayılı Kabahatler Kanunu'nun genel hükümleri yardımcı kaynak olabilir; aynı fiile mükerrer ceza ve cezanın yıkımla ilişkisi (cezanın yıkıma engel olmaması) tartışılır.
6. **İspat ve dava**: Yapı tatil tutanağı ve teknik tespit idarenin delili; davacı hesap hatasını/aykırılığın yokluğunu somutlaştırır. İYUK m.7'de 60 gün içinde iptal davası; hesabın bir kısmı sakatsa kısmen iptal istenir.

## Çıktı modülleri
- Ceza hesabı kalem kalem denetim tablosu.
- Muhatap/sorumluluk değerlendirmesi.
- Usul ve gerekçe denetim notu.
- Kısmen/tamamen iptal talepli dilekçe iskeleti.

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
