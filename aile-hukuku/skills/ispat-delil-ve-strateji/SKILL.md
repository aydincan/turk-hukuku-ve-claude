---
name: ispat-delil-ve-strateji
description: "Aile davalarında kusurun, gelir-malvarlığının veya soybağının ispatı, delil toplama ve kabul edilebilirliği, gizlilik ve hukuka aykırı delil sorunları ile genel dava stratejisi gerektiğinde kullanılır."
---

# İspat, Delil ve Dava Stratejisi

## Görev
Aile hukuku uyuşmazlığında ispat yükünü dağıtmak, her vakıa için uygun ve kabul edilebilir delili belirlemek, hukuka aykırı delil ve gizlilik risklerini yönetmek ve genel stratejiyi kurmak.

## Soğuk başlangıç (intake)
1. İspatlanacak çekişmeli vakıalar neler (kusur, gelir, katkı, soybağı, yoksulluk)?
2. Eldeki deliller hangileri ve nasıl elde edildi (kayıt, mesaj, tanık, kamera)?
3. Karşı tarafın olası savunması ve karşı delilleri ne olabilir?
4. Müvekkilin kırmızı çizgileri ve önceliği (çocuk mu, para mı, hız mı) nedir?

## Denetim şeması
1. **İspat yükü.** Kanunun aksini öngörmedikçe, iddia eden ispatla yükümlüdür (TMK m.6, HMK m.190). Kusura dayalı talepte kusuru iddia eden; katılma alacağında malın edinilmiş olmadığını iddia eden ispatlar (TMK m.222 karinesi: aksi ispatlanamayan mal edinilmiş sayılır).
2. **Delil eşleştirme.** Kusur: tanık (HMK m.240 vd.), mesaj/yazışma, kamera, sosyal medya, ceza/koruma dosyası. Gelir-malvarlığı: SGK/işyeri kaydı, banka hareketleri, tapu-trafik kaydı, vergi beyanı; mahkemeden müzekkere ile celp. Soybağı: DNA tespiti (m.284, hâkim re'sen). Yoksulluk: ekonomik-sosyal durum araştırması. Çocuk: pedagog/uzman raporu, idrak çağında çocuğun dinlenmesi.
3. **Kabul edilebilirlik ve gizlilik.** Hukuka aykırı yolla elde edilen delil kural olarak değerlendirilemez (HMK m.189/2; AY m.38/6). Karşı eşin telefonuna izinsiz erişim, gizli ses/görüntü kaydı TCK m.132-134 ve m.135 vd. kapsamında suç oluşturabilir; bu deliller hem reddedilebilir hem müvekkili ceza riskine sokar — uyarı şart. Yargıtay uygulamasında "tesadüfen/aynı konutta" elde edilen bazı kayıtların değerlendirildiği istisnalar ilkesel olarak anlatılır, somut karar künyesi `[doğrulanacak]` (karararama.yargitay.gov.tr).
4. **Strateji.** Önce tür/sebep seçimi, sonra delil yeterliliği; zayıf kusur dosyasında genel sebep (m.166) tercih edilir; tasfiye için mal kaçırma riskine karşı ihtiyati tedbir/haciz öngörülür; çocuk önceliğinde uzlaşma ve uzman desteği değerlendirilir.
5. **Ara sonuç.** Vakıa-delil-ispat yükü matrisi + risk uyarıları + strateji önerisi.

## Çıktı modülleri
- İspat planı tablosu (vakıa / ispat yükü / delil / temin yolu).
- Hukuka aykırı delil ve ceza riski uyarı notu.
- Strateji ve müzekkere/tedbir talep listesi.

## Plugin bağlamı

Bu beceri `aile-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
