---
name: riziko-tazminat
description: "Riziko gerçekleştikten sonra ihbar yükümlülüğü, teminat-istisna değerlendirmesi ve zarar/tazminat hesabı yapılması gerektiğinde kullanılır; eksik/aşkın sigorta ve muafiyet düşümlerini içeren tazminat denetimi için temel beceridir."
---

# Rizikonun Gerçekleşmesi, İhbar ve Tazminatın Belirlenmesi

## Görev
Gerçekleşen olayın teminat kapsamına girip girmediğini, ihbar yükümlülüğünün yerine getirilip getirilmediğini ve ödenecek tazminatın miktarını (tazminat ilkesi, eksik/aşkın sigorta, muafiyet) belirlemek.

## Soğuk başlangıç (intake)
1. Riziko ne zaman, nerede ve nasıl gerçekleşti; olay teminat tanımına uyuyor mu?
2. Sigortacıya ihbar yapıldı mı, ne zaman?
3. Sigorta bedeli ile rizikoya konu malın gerçek değeri nedir (eksik/aşkın sigorta)?
4. Muafiyet, sovtaj (kurtarılan kıymet), eksper raporu var mı?

## Denetim şeması
1. **Riziko-teminat eşleştirmesi.** Olay, poliçe ve genel şartlardaki teminat tanımına giriyor mu? İstisna kapsamında mı (örn. kasko genel şartlarında alkollü araç kullanımı)? İspat: teminatı sigortalı, istisnayı sigortacı.
2. **İhbar yükümlülüğü.** TTK m.1446: sigorta ettiren, rizikonun gerçekleştiğini öğrendikten sonra gecikmeksizin sigortacıya bildirir. m.1447: ihbarın ihmali, sigortacının ödeyeceği tazminatı artırdığı ölçüde indirim sebebidir (kasıtta tam, kusurda artış oranında). Ara sonuç: ihbar zamanında mı?
3. **Tazminat ilkesi.** TTK m.1459: zarar sigortasında sigortalı, gerçek zararından fazlasını isteyemez (zenginleşme yasağı).
4. **Eksik/aşkın sigorta.** TTK m.1462 (eksik sigorta — sigorta bedeli değerden düşükse oranlama/nispet kuralı); m.1463 (aşkın sigorta — bedel değeri aşarsa aşan kısım geçersiz, kötüniyet halinde sonuçları). m.1461 birden çok sigorta.
5. **Düşümler.** Muafiyet (tenzili/entegral), sovtaj değeri, daha önce ödenen tazminat düşülür. Can sigortasında tazminat ilkesi uygulanmaz; sigorta bedeli ödenir (TTK m.1487 vd.).

## Çıktı modülleri
- Riziko-teminat-istisna eşleştirme tablosu.
- İhbar zamanlaması ve indirim değerlendirmesi.
- Tazminat hesabı (gerçek zarar / oranlama / muafiyet / sovtaj).
- Talep edilebilir net tutar ve dayanak maddeleri.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
