---
name: eksik-ve-celiski-listesi
description: "Dosyada cevaplanmamış iddiaları, ibraz edilmemiş delilleri ve taraf beyanları arasındaki çelişkileri sistematik biçimde tespit etmek gerektiğinde kullan."
---

# Eksik ve Çelişki Listesi

## Görev
Dosyadaki boşlukları (cevaplanmamış iddia, eksik evrak, ibraz edilmemiş delil) ve tutarsızlıkları (çelişen beyan, çelişen tarih/tutar) bir kalite-kontrol listesine dönüştürmek.

## Soğuk başlangıç (intake)
- Dava ve cevap dilekçeleri ile varsa replik-düplik elinde mi?
- Hangi iddialar karşı tarafça yanıtsız bırakılmış?
- Beyanlar, tutarlar veya tarihler arasında göze çarpan çelişki var mı?
- Hangi evrakın dosyada olması gerekirken olmadığını biliyor musun?

## Denetim şeması
1. Cevaplanmamış iddia: dava dilekçesindeki her vakıaya karşı cevap dilekçesinde açık/örtülü itiraz var mı? Cevapta açıkça inkâr edilmeyen vakıanın ikrar/çekişmesizlik etkisini (HMK m.128) işaretle.
2. Eksik evrak: dilekçelerde dayanılan ama dosyada bulunmayan belgeler; HMK m.121 ve m.129 gereği dilekçeye eklenmesi gereken delillerin eksikliği.
3. Çelişki taraması: aynı tarafın farklı evrakındaki çelişen beyanlar; taraflar arası çelişen tutar/tarih; bilirkişi raporu ile dosya arasındaki uyumsuzluk. Her çelişkiyi kaynak evrak + sayfa ile göster.
4. Usuli eksik: dava şartı (HMK m.114-115), ilk itiraz (HMK m.116) ve süresinde ileri sürülmeyen savunma genişletme yasağı (HMK m.141) açısından risk notları.
5. Ara sonuç: önceliklendirilmiş eksik/çelişki listesi (kritik / orta / düşük). Tespitler yalnızca evraka dayanır; varsayım eklenmez.

## Çıktı modülleri
- Eksik kalemler tablosu (ne eksik, dayanak, etki).
- Çelişki tablosu (çelişen ifadeler, kaynak evrak, sayfa).
- Önceliklendirilmiş aksiyon listesi.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
