---
name: dava-gorev-yetki-ve-ispat
description: "Tazminat davasının hangi mahkemede ve nerede açılacağı, dava şartlarının sağlanıp sağlanmadığı ve ispat yükünün nasıl dağılacağı belirlenmek istendiğinde kullanılır."
---

# Dava, Görev-Yetki ve İspat Düzeni

## Görev
Haksız fiil tazminat davasında görevli ve yetkili mahkemeyi (HMK), dava şartlarını, ispat yükünün dağılımını ve delil rejimini belirlemek; talep sonucunu (belirsiz alacak/kısmi dava) doğru kurmak. Usuldeki hata, esasa girilmeden ret riski doğurur.

## Soğuk başlangıç (intake)
- Taraflar kim (gerçek/tüzel kişi, tacir mi); uyuşmazlık ticari mi?
- Fiil nerede işlendi, zarar nerede doğdu, davalının yerleşim yeri neresi?
- Zarar miktarı baştan belirlenebiliyor mu (belirsiz alacak ihtimali)?
- Eldeki deliller neler; ceza dosyası/bilirkişi raporu var mı?

## Denetim şeması
1. **Görev.** Kural olarak Asliye Hukuk Mahkemesi görevlidir (HMK m.2). Taraflar tacir ve uyuşmazlık ticari işten doğuyorsa Asliye Ticaret Mahkemesi (TTK m.4-5); trafik/sigorta gibi özel rejimlerde özel görev kuralları kontrol edilir.
2. **Yetki.** Genel yetki davalının yerleşim yeri (HMK m.6); haksız fiilde ek olarak fiilin işlendiği veya zararın meydana geldiği ya da gelme ihtimalinin bulunduğu yahut zarar görenin yerleşim yeri mahkemesi de yetkilidir (HMK m.16).
3. **Dava şartları ve türü.** Hukuki yarar, taraf/dava ehliyeti (HMK m.114) kontrol edilir. Miktar baştan tam belirlenemiyorsa belirsiz alacak davası (HMK m.107); aksi halde kısmi/tam eda davası tercih edilir; ıslah imkânı (HMK m.176) gözetilir.
4. **İspat yükü.** Genel kural: iddia eden ispatlar (TMK m.6, HMK m.190). Zarar gören fiil-zarar-illiyet ve kusuru; davalı hukuka uygunluk sebebini, kurtuluş kanıtını ve indirim sebeplerini ispatlar. Kusursuz sorumlulukta kusur aranmaz.
5. **Deliller.** Senet, tanık, bilirkişi (zarar/maluliyet/hesap), keşif; ceza mahkemesi kararının hukuk hâkimini bağlama sınırı (TBK m.74) değerlendirilir.
6. **Ara sonuç.** Görev-yetki-dava türü-ispat dağılımı netleştirilir; harç (nispi), faiz türü ve dava şartı arabuluculuk (ticari/uygulanan hallerde) kontrolü yapılır.

## Çıktı modülleri
- Görev-yetki gerekçe notu (dayanak maddelerle).
- Dava türü seçimi (belirsiz/kısmi/tam) ve ıslah notu.
- İspat yükü dağılım tablosu (taraf-unsur-delil).

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
