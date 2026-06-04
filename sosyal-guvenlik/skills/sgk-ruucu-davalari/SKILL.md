---
name: sgk-ruucu-davalari
description: "SGK'nın iş kazası, meslek hastalığı, trafik kazası veya üçüncü kişinin haksız fiili sonucu yaptığı ödemeleri kusurlu işveren ya da üçüncü kişiden geri istemesi söz konusu olduğunda; işveren/sigorta şirketi savunması dahil kullanılır."
---

# SGK Rücu Davaları

## Görev
SGK'nın bağladığı gelir ve yaptığı masrafları kusurlu işveren, üçüncü kişi veya sorumlu sigortacıdan geri alma davasını kurmak veya bu davaya karşı savunma stratejisi geliştirmek.

## Soğuk başlangıç (intake)
- Rücuya konu olay iş kazası/meslek hastalığı mı, trafik kazası mı, başka bir haksız fiil mi?
- SGK hangi edimleri ödedi (geçici/sürekli iş göremezlik geliri, ölüm geliri, sağlık masrafı)?
- Sorumlu kim: işveren mi, üçüncü kişi mi, trafik sigortacısı mı?
- Kusur oranı belirlendi mi; ceza/hukuk dosyası var mı?

## Denetim şeması
1. Dayanak — 5510 m.21 (iş kazası/meslek hastalığı için işverene/üçüncü kişiye rücu) ve m.39/trafik kazasında ilgili hükümler; genel hükümler bakımından TBK m.49 vd. (haksız fiil) ve halefiyet.
2. Sorumluluğun kapsamı: Rücu, Kurumun ilk peşin sermaye değeri (bağlanan gelirin sermayeye çevrilmiş tutarı) ile sınırlıdır; bağlanan gelir miktarının tamamı değil, sigortalının zararı ve kusur oranı süzgecinden geçer.
3. Kusur tespiti: İşverenin İSG ihlali (6331) veya üçüncü kişinin haksız fiili bilirkişiyle saptanır; müterafik kusur (sigortalının kusuru) indirim sebebidir.
4. Sigortacıya yöneltme: Trafik kazalarında Zorunlu Mali Sorumluluk Sigortası kapsamı ve teminat limiti gözetilir (2918 sayılı Kanun ile bağlantı).
5. Zamanaşımı: Rücu alacağında haksız fiil zamanaşımı ve özel hükümler birlikte değerlendirilir; başlangıç anı (gelirin bağlandığı/onay tarihi) tartışmalıdır, içtihat kontrol edilir [doğrulanacak]. Ara sonuç: rücu edilebilir tutar ve sorumlu çevresi. İspat: ödeme/onay belgeleri, kusur raporu.

## Çıktı modülleri
- Rücu tutarı ve sorumluluk dağılımı tablosu.
- İşveren/sigortacı savunma argümanları (kusur, limit, peşin sermaye değeri).
- Dava/savunma dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
