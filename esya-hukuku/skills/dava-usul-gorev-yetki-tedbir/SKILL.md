---
name: dava-usul-gorev-yetki-tedbir
description: "Eşya hukuku davası açılmadan önce görevli/yetkili mahkeme, dava şartları, harç-değer, ispat yükü ve taşınmazın devrini önleyici ihtiyati tedbir/şerh stratejisinin belirlenmesi gerektiğinde kullanılır."
---

# Eşya Hukukunda Usul, Görev-Yetki ve İhtiyati Tedbir

## Görev
Eşya hukuku davasının usulî çerçevesini kurmak: görevli ve yetkili mahkemeyi, dava şartlarını, ispat yükünü ve taşınmazın elden çıkmasını önleyecek ihtiyati tedbir/şerh stratejisini belirlemek.

## Soğuk başlangıç (intake)
- Talep türü ne (istihkak, el atma, tapu iptali-tescil, ortaklığın giderilmesi, zilyetlik)?
- Dava konusu taşınmaz mı, taşınır mı; uyuşmazlık değeri nedir?
- Karşı tarafın taşınmazı üçüncü kişiye devretme veya kaydı değiştirme riski var mı?
- Süreler işliyor mu (zilyetlikte 2 ay/1 yıl, ecrimisilde zamanaşımı)?

## Denetim şeması
1. **Yetki**: Taşınmazın aynına ilişkin davalarda (mülkiyet, tapu iptali-tescil, el atma, ortaklığın giderilmesi) kesin yetki taşınmazın bulunduğu yer mahkemesidir (HMK m.12). Birden çok taşınmazda biri yeterlidir.
2. **Görev (HMK m.2-4)**: Kural asliye hukuk mahkemesi (m.2). Ortaklığın giderilmesi ve taşınmaz/taşınır paylaştırılmasına ilişkin davalar sulh hukuk mahkemesinde görülür (m.4). Görev kesindir, re'sen gözetilir.
3. **Dava şartları (HMK m.114-115)**: Hukuki yarar, taraf-dava ehliyeti, husumet; ortaklığın giderilmesi ve elbirliği mülkiyetinde zorunlu dava arkadaşlığı eksik husumet sorununa yol açar.
4. **İspat yükü (TMK m.6; HMK m.190)**: Hakkı iddia eden ispatla yükümlüdür; tapu kaydı ve zilyetlik karineleri ispat yükünü kaydırır. Taşınmaz uyuşmazlıklarında keşif ve bilirkişi (özellikle harita/fen, değer) sıklıkla zorunludur.
5. **İhtiyati tedbir (HMK m.389 vd.)**: Taşınmazın devri/üzerine işlem yapılmasının önlenmesi için tedbiren tapuya şerh konulması istenebilir; ayrıca m.1010 kapsamında tasarruf yetkisi kısıtlamasının şerhi düşünülür. Yaklaşık ispat ve teminat gerekir.
6. **Harç ve değer**: Aynı ilişkin davalar nispi harca tabidir; dava değeri taşınmazın değerine göre belirlenir.
7. **Ara sonuç**: Doğru mahkeme + dava şartlarının tamamlığı + gerekiyorsa devri önleyici tedbir.

## Çıktı modülleri
- Görev/yetki ve harç kontrol listesi.
- İhtiyati tedbir/şerh dilekçesi iskeleti (yaklaşık ispat, teminat).
- Dava şartı ve husumet (zorunlu dava arkadaşlığı) kontrol notu.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
