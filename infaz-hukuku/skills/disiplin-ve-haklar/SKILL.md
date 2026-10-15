---
name: disiplin-ve-haklar
description: "Ceza infaz kurumunda verilen disiplin cezalarını, savunma hakkını, disiplin cezasının kaldırılmasını ve hükümlü haklarına yönelik ihlalleri denetlemek gerektiğinde kullanılır."
---

# İnfaz Disiplin Cezaları ve Hükümlü Hakları

## Görev
Kurum içi disiplin cezalarının hukuka uygunluğunu, savunma hakkına riayeti ve hükümlü haklarına müdahaleleri 5275 disiplin hükümleri çerçevesinde denetlemek.

## Soğuk başlangıç (intake)
- Hangi disiplin cezası verildi (kınama, ziyaret/haberleşme kısıtlama, hücre vb.)?
- Savunma alındı mı; disiplin kurulu kararı gerekçeli mi?
- Eylem hangi disiplin fiiline karşılık geliyor?
- Cezanın koşullu salıverilmeye/iyi hâle etkisi var mı?

## Denetim şeması
1. Disiplin cezası kataloğu: 5275 m.38-44 kınamadan hücreye kadar dereceli cezaları, m.37 ölçülülük ilkesini düzenler; kıyas yasağına benzer biçimde fiil-ceza eşleşmesi denetlenir. Ara sonuç: ceza türü mevzuata uygun mu?
2. Usul güvenceleri: disiplin soruşturmasında savunma hakkı tanınması, disiplin kurulu kararının gerekçeli olması zorunludur (5275 m.47). İspat yükü: eylemin sübutunu idare ortaya koymalıdır.
3. Çocuk ve özel durumlar: çocuk hükümlülerde farklı disiplin rejimi (5275 m.46) ve özel koruma.
4. Cezanın kaldırılması/ortadan kalkması: iyi hâl ve süre şartıyla disiplin cezalarının kaldırılması (5275 m.48); bu, koşullu salıverilme değerlendirmesini etkiler.
5. Hak ihlali boyutu: ziyaret, haberleşme, sağlık ve insan onuruna uygun tutulma haklarına orantısız müdahale, AYM bireysel başvuru konusu olabilir (kararlarbilgibankasi.anayasa.gov.tr).
6. İtiraz: disiplin cezasına karşı infaz hâkimliği ve itiraz mercii yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[doğrulanacak]`.
7. Ara sonuç: cezanın hukuka uygunluğu + itiraz dayanakları.

## Çıktı modülleri
- Disiplin cezası hukuka uygunluk çizelgesi.
- Savunma/usul eksiği listesi.
- İnfaz hâkimliğine şikâyet dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
