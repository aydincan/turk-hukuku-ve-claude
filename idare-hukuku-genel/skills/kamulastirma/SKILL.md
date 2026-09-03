---
name: kamulastirma
description: "Taşınmazın kamulaştırılması, kamulaştırmasız el atma, acele kamulaştırma ve kamulaştırma bedelinin tespiti süreçlerini değerlendirmek için kullanılır; idarenin mülkiyete müdahalesi söz konusuysa başvurulur."
---

# Kamulaştırma ve Bedel Davaları

## Görev
Kamulaştırma işleminin hukuka uygunluğunu, bedel tespiti sürecini ve kamulaştırmasız el atma hallerini değerlendirmek; mülkiyet hakkı (Anayasa m.35, m.46) ile kamu yararı dengesini kurmak.

## Soğuk başlangıç (intake)
1. Usulüne uygun kamulaştırma kararı ve kamu yararı kararı var mı?
2. Süreç hangi aşamada (kıymet takdiri, uzlaşma, bedel tespiti/tescil davası, acele kamulaştırma)?
3. Fiilen el atılmış ama kamulaştırma yapılmamış mı (kamulaştırmasız el atma)?
4. Tebliğ ve süreler korunmuş mu?

## Denetim şeması
1. **Dayanak ve kamu yararı.** Anayasa m.46 ve 2942 sayılı Kamulaştırma Kanunu. Kamu yararı kararı, onay ve kıymet takdiri usulüne uygun mu? Kamu yararı yoksa veya amaç dışıysa iptal yolu (idari yargı) açık.
2. **Bedel tespiti ve tescil.** Uzlaşma sağlanamazsa idare, asliye hukuk mahkemesinde bedel tespiti ve tescil davası açar (2942 m.10). Bedel **gerçek karşılık** olmalı; değerleme bilirkişi ile yapılır; bedel artırımı talep edilebilir.
3. **İki yargı yolu ayrımı.** Kamulaştırma **işleminin iptali** idari yargıda; **bedel** uyuşmazlığı adli yargıda (asliye hukuk) görülür. Bu ayrımı baştan kur.
4. **Acele kamulaştırma.** 2942 m.27: acele el koyma kararı ve bilirkişi bedeli; sonradan esas bedel davası. Acelelik koşullarının denetimi.
5. **Kamulaştırmasız el atma.** Fiili el atma → adli yargıda tazminat (bedel) davası; hukuki el atma (imar kısıtlaması) → idari yargı. Süreç ve yargı yolu seçimi kritik.
6. **İspat.** Taşınmazın niteliği, emsal, değer artırıcı unsurlar; değerleme raporuna gerekçeli itiraz.
7. **Ara sonuç.** Hedef iptal mi, bedel mi, kamulaştırmasız el atma tazminatı mı; yargı yolu ve mahkeme.

## Çıktı modülleri
- Yargı yolu ayrımı tablosu (iptal/bedel/el atma).
- Süreç aşaması ve eksik işlem listesi.
- Bedele/değerleme raporuna itiraz notu.
- İlgili dava dilekçesi için iskelet.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
