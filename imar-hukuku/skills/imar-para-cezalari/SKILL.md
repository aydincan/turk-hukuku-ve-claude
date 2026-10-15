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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
