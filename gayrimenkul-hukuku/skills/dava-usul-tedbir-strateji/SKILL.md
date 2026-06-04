---
name: dava-usul-tedbir-strateji
description: "Taşınmaz davası açılmadan önce doğru mahkeme, dava şartları, harç-değer, süreler ve taşınmazın elden çıkmasını önleyici ihtiyati tedbir/şerh stratejisi belirlenmesi gerektiğinde kullanılır."
---

# Gayrimenkulde Usul, Görev-Yetki, İhtiyati Tedbir ve Strateji

## Görev
Taşınmaz uyuşmazlığının usulî iskeletini kurmak: görevli ve yetkili mahkemeyi, dava şartlarını, harç ve değeri, süreleri ve karşı tarafın taşınmazı devretmesini önleyecek ihtiyati tedbir/şerh stratejisini belirlemek; davayı en etkili sıra ve biçimde kurgulamak.

## Soğuk başlangıç (intake)
- Talep türü ne (tapu iptali-tescil, satış vaadi ifası, el atma, ortaklığın giderilmesi, kamulaştırma bedeli, tüketici)?
- Uyuşmazlığın değeri ve taraf sıfatları (tüketici/tacir/idare) ne?
- Karşı tarafın taşınmazı üçüncü kişiye devretme veya kayıt değiştirme riski var mı?
- İşleyen süreler var mı (satış vaadi 10 yıl, İYUK 60 gün, tüketici/cayma süreleri)?

## Denetim şeması
1. **Yetki**: Taşınmazın aynına ilişkin davalarda (mülkiyet, tapu iptali-tescil, el atma, ortaklığın giderilmesi, irtifak) kesin yetki taşınmazın bulunduğu yer mahkemesidir (HMK m.12). Birden çok taşınmazda biri yeterlidir.
2. **Görev**: Kural asliye hukuk (HMK m.2). Ortaklığın giderilmesi ve kat mülkiyetinden doğan davalar sulh hukuk (HMK m.4; KMK Ek m.1). Tüketici sıfatı varsa tüketici mahkemesi (6502 m.73). İmar/kamulaştırma iptali idari yargı (İYUK). Görev kesindir, re'sen gözetilir.
3. **Dava şartları (HMK m.114-115)**: Hukuki yarar, taraf-dava ehliyeti, husumet; elbirliği mülkiyeti ve ortaklığın giderilmesinde zorunlu dava arkadaşlığı eksik husumet doğurabilir.
4. **İspat (TMK m.6; HMK m.190 vd.)**: Hakkı iddia eden ispatla yükümlüdür; tapu kaydı doğruluk karinesi taşır. Taşınmaz davalarında keşif ve bilirkişi (harita-fen, değerleme, inşaat) çoğunlukla zorunludur. Resmî senetle yapılan işlemler güçlü delildir; tanıkla aksinin ispatı sınırlıdır (HMK m.201).
5. **İhtiyati tedbir (HMK m.389 vd.)**: Taşınmazın devrini/üzerine işlem yapılmasını önlemek için tapuya tedbir şerhi istenir; yaklaşık ispat ve teminat gerekir. Satış vaadi/kişisel haklarda m.1010 (TMK) tasarruf kısıtlaması şerhi düşünülür.
6. **Harç ve değer**: Aynı ilişkin davalar nispi harca tabidir; dava değeri taşınmazın güncel değerine göre belirlenir; eksik harç dava şartı sorunu doğurur.
7. **Ara sonuç**: Doğru mahkeme + tam dava şartları + gerekiyorsa devri önleyici tedbir; talepler arasında terditli/kademeli kurgu.

## Çıktı modülleri
- Görev/yetki, yargı kolu ve harç-değer kontrol listesi.
- İhtiyati tedbir/şerh dilekçesi iskeleti (yaklaşık ispat, teminat).
- Süre ve husumet (zorunlu dava arkadaşlığı) uyarı notu ve dava kurgu planı.

## Plugin bağlamı

Bu beceri `gayrimenkul-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
