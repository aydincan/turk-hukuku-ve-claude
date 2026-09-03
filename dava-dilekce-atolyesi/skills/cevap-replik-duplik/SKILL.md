---
name: cevap-replik-duplik
description: "Davalı vekili olarak cevap dilekçesi, ilk itirazlar ve karşı dava; ardından replik-düplik dilekçeleri hazırlamak ve teksif ilkesini gözetmek gerektiğinde kullanılır."
---

# Cevap, Replik ve Düplik Dilekçeleri

## Görev
Davalı savunmasını HMK m.126-129 çerçevesinde kurmak; ilk itirazları, esasa cevabı ve varsa karşı davayı doğru zamanda ileri sürmek; dilekçeler aşamasını teksif ilkesine uygun tamamlamak.

## Soğuk başlangıç (intake)
- Dava dilekçesi tebliğ tarihi ne, cevap süresi doluyor mu?
- İlk itiraz var mı (yetki, derdestlik, tahkim, m.116)?
- Karşı dava şartları oluştu mu (HMK m.132-134)?
- Hangi vakıalar inkâr, hangileri itiraf edilecek?

## Denetim şeması
1. Cevap süresi (HMK m.127): Kural iki hafta; gerekçeli talep ve hâkim takdiriyle bir defaya mahsus uzatma. Basit yargılamada iki hafta (m.317). Süre geçerse cevap hakkı düşer, davacının dava dilekçesindeki vakıalar inkâr edilmiş sayılır (m.128 değil; cevap vermeyen davalı vakıaları inkâr etmiş sayılır).
2. İlk itirazlar (HMK m.116-117): Kesin olmayan yetki, derdestlik, tahkim itirazı, iş bölümü; hepsi cevap dilekçesinde birlikte ileri sürülür, sonradan ileri sürülemez.
3. Esasa cevap (m.129): Davacının her vakıasına karşı açık tutum (kabul/inkâr/bilmeme); savunma sebepleri ve karşı deliller. Zamanaşımı def'i mutlaka burada ileri sürülmeli (TBK m.161 — hâkim re'sen dikkate almaz).
4. Karşı dava (m.132-134): Asıl dava ile bağlantı veya takas/mahsup şartı; süresinde ve aynı dilekçede.
5. Replik-düplik (m.136): Davacı cevaba cevap, davalı ikinci cevap verir; teksif ilkesi (m.141) gereği bundan sonra iddia/savunma genişletilemez (ıslah ve karşı tarafın açık muvafakati hariç). Ara sonuç: süre/itiraz/def'i eksiksizse imzaya hazır.

## Çıktı modülleri
- Cevap dilekçesi taslağı (ilk itiraz + esasa cevap + def'iler)
- Karşı dava bloğu (varsa)
- Replik/düplik taslağı
- Süre ve teksif uyarı notu

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
