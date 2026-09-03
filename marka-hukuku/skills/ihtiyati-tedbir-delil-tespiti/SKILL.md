---
name: ihtiyati-tedbir-delil-tespiti
description: "Devam eden tecavüzün acilen durdurulması, kanıtların kaybolmadan tespiti veya taklit ürünün ithalat/ihracatta durdurulması gerekiyorsa; m.159 tedbir ve gümrük süreçlerini yürütmek için kullanılır."
---

# İhtiyati Tedbir, Delil Tespiti ve Gümrük Önlemleri

## Görev
Tecavüzün yarattığı acil zararı önlemek için SMK m.159 ihtiyati tedbir, HMK m.400 vd. delil tespiti ve gümrükte el koyma süreçlerini yürütmek. Amaç, esas dava sonuçlanana kadar mevcut durumu korumak ve kanıt kaybını engellemektir.

## Soğuk başlangıç (intake)
- Tecavüz devam ediyor mu, gecikmede tehlike somut mu?
- Taklit ürün üretiliyor/satılıyor/ithal mi ediliyor?
- Kanıtlar kaybolma/değiştirilme riski altında mı?
- Talep esas davadan önce mi, dava sırasında mı?

## Denetim şeması
1. **Tedbir şartları (m.159, HMK m.389).** Tescilli marka hakkına tecavüz veya ciddi tecavüz tehlikesi; verilecek hükmün etkinliğini sağlama gerekliliği; gecikmede tehlike. Yaklaşık ispat yeterlidir.
2. **Tedbir içeriği (m.159/2).** Tecavüz oluşturan fiillerin durdurulması/önlenmesi, taklit ürünlere/araçlara el konulması ve muhafazası, teminat. Talep esas davadan önce de istenebilir; bu halde m.159/HMK uyarınca süresinde dava açılması gerekir.
3. **Teminat ve tazminat.** Tedbir kural olarak teminat karşılığı; haksız tedbirde karşı tarafın zararından sorumluluk doğar.
4. **Delil tespiti (HMK m.400 vd.).** Tecavüz delillerinin (ürün, fatura, üretim) mahkemece tespiti; ileride kaybolma riskine karşı.
5. **Gümrükte el koyma (m.159 ve Gümrük mevzuatı).** Hak sahibinin başvurusuyla, marka hakkını ihlal eden eşyaya gümrük idaresince el konulabilir; süresinde dava/işlem yapılmazsa eşya serbest bırakılır.
6. **Görev/yetki.** FSHHM (m.156); tedbir talebi esas davayı görecek mahkemeden istenir.

## Çıktı modülleri
- Tedbir şartları altlama notu (tecavüz + gecikme tehlikesi + etkinlik).
- Tedbir/delil tespiti talep dilekçesi iskeleti.
- Gümrük başvurusu ve süre takip listesi.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
