---
name: doping-hukuku
description: "Doping ihlali isnadı, numune süreci, yaptırım veya itiraz konularını WADA Kodu ve ilgili federasyon talimatı çerçevesinde değerlendirmek gerektiğinde kullanın."
---

# Doping Hukuku ve Yaptırım Süreci

## Görev
Bir doping ihlali isnadını WADA Kodu, ulusal doping talimatı ve uluslararası federasyon kuralları çerçevesinde değerlendirmek; numune ve usul güvencelerini denetlemek; savunma ya da yaptırıma itiraz stratejisi hazırlamaktır.

## Soğuk başlangıç (intake)
1. İhlal türü nedir: yasaklı madde bulgusu, numune vermekten kaçınma, bulunulabilirlik (whereabouts) ihlali?
2. Numune hangi tarihte alındı ve A/B numune süreci nasıl işledi?
3. Madde, yasaklılar listesinde hangi kategoride (her zaman/yarışma içi)?
4. Sporcunun açıklaması ve olası kaynak (kontaminasyon, tıbbi kullanım) nedir?
5. Tedavi amaçlı kullanım izni (TUE) var mı?

## Denetim şeması
1. **Norm zemini**: WADA Kodu ve Yasaklılar Listesi, ulusal doping kontrol talimatı ve ilgili uluslararası federasyon kuralları birlikte uygulanır; sıkı (objektif) sorumluluk ilkesi esastır.
2. **Usul güvenceleri**: Numune alma zinciri (chain of custody), A ve B numune analizi, laboratuvar akreditasyonu ve bildirim usulü denetlenir; usul ihlali sonucu etkileyebilir.
3. **Kusur değerlendirmesi**: Sıkı sorumlulukta varlık ispatı yeterlidir; ancak yaptırımın süresi sporcunun kusur derecesine (kasıtlı/kasıtsız, ağır/hafif kusur, hiç kusur yokluğu) göre indirilebilir veya kaldırılabilir.
4. **TUE ve kontaminasyon**: Geçerli tedavi amaçlı kullanım izni veya kanıtlanmış kontaminasyon savunması yaptırımı etkiler; ispat yükü sporcudadır.
5. **Yaptırım ve itiraz**: Müsabakadan men süresi, sonuçların iptali; karara karşı federasyon tahkimi ve milletlerarası boyutta **CAS** yolu, süreler kontrol edilir.
6. **Ara sonuç**: İhlalin sübutu, kusur derecesi ve indirim/itiraz şansı belirlenir.

## Çıktı modülleri
- Usul ve numune zinciri denetim listesi
- Savunma/itiraz dilekçesi iskeleti
- Kusur ve indirim argümanları
- CAS/tahkim süre notu `[doğrulanacak]`

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
