---
name: dosya-ve-sure-yonetimi
description: "Yeni bir dosya açılırken veya mevcut dosyada kritik usul sürelerinin takvimlenmesi, izlenmesi ve kaçırma riskinin önlenmesi gerektiğinde kullanılır."
---

# Dosya Açılışı ve Süre Yönetimi

## Görev
Kabul edilen her iş için standart dosya açılışı yapmak ve büronun en yüksek meslekî riski olan süre kaçırma riskini takvimleyerek yönetmek.

## Soğuk başlangıç (intake)
1. Dosyanın yargı kolu nedir (hukuk/ceza/idari/icra/tüketici hakem heyeti)?
2. Hangi olay tetikleyici (tebliğ, öğrenme, ihlal tarihi) ve tarihi nedir?
3. Şu an dosya hangi aşamada (dava açma öncesi, dilekçeler, istinaf vb.)?
4. Halihazırda işleyen bir süre var mı, varsa bitiş tarihi?

## Denetim şeması
1. **Tetikleyici tarih tespiti**: Sürenin başladığı an (tebliğ tarihi, öğrenme, ihlal) belgeyle sabitlenir; tebliğ tarihi tebligat zarfından doğrulanır.
2. **Süre tipi**: İlgili sürenin niteliği belirlenir — usul süresi mi (HMK cevap m.127: kural 2 hafta; istinaf m.345: 2 hafta; temyiz m.361: 2 hafta), idari dava süresi mi (İYUK m.7: 60/30 gün), icra süreleri mi (İİK m.62 ödeme emrine itiraz 7 gün; m.67 itirazın iptali 1 yıl), ceza kanun yolu süresi mi, yoksa maddi hukuk süresi mi (zamanaşımı/hak düşürücü).
3. **Hesaplama (HMK m.92-93)**: Gün/hafta/ay olarak hesap; sürenin son gününün tatile gelmesi halinde izleyen ilk iş gününe uzaması; adli tatil etkisi (HMK m.102 vd.) değerlendirilir.
4. **Tampon ilkesi**: Her kritik süreye iç son tarih (örn. yasal sürenin 3-5 gün öncesi) konur; ön uyarı kademeleri (15/7/3/1 gün) kurulur.
5. **Sorumlu atama**: Her süre için sorumlu avukat ve yedek atanır; çift kontrol (four-eyes) uygulanır.
6. **Ara sonuç**: Tetikleyici + süre tipi + hesaplanmış son tarih + tampon + sorumlu tanımlanınca süre "kapatılmış" sayılır.

## Çıktı modülleri
- Standart dosya açılış formu (taraflar, vekiller, yargı kolu, dosya no).
- Süre takvimi tablosu (süre, dayanak madde, tetikleyici tarih, yasal son tarih, iç son tarih, sorumlu).
- Yaklaşan süreler uyarı listesi.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
