---
name: dava-usul-gorev-yetki
description: "Taşıma uyuşmazlığında görevli-yetkili mahkemenin belirlenmesi, ticari dava ve arabuluculuk dava şartının değerlendirilmesi, CMR yetki kuralları ve uygulanacak hukukun tespiti gerektiğinde kullanılır."
---

# Taşıma Davalarında Usul, Görev ve Yetki

## Görev
Taşıma uyuşmazlığında doğru mahkemeyi (görev-yetki), dava şartlarını ve CMR'ye özgü yetki/uygulanacak hukuk kurallarını belirlemek.

## Soğuk başlangıç (intake)
1. Uyuşmazlık ticari mi (taraflar tacir / TTK kapsamı)?
2. Taşıma iç mi, CMR'ye tabi sınır aşan mı?
3. Tarafların yerleşim yeri, teslim alma ve teslim yerleri nerede?
4. Sözleşmede yetki, tahkim veya uygulanacak hukuk şartı var mı?

## Denetim şeması
1. **Görev:** Taşıma işleri TTK'da düzenlendiğinden uyuşmazlık mutlak ticari davadır (TTK m.4/1); görevli mahkeme Asliye Ticaret Mahkemesidir. Ticaret mahkemesi bulunmayan yerde asliye hukuk ticaret sıfatıyla bakar.
2. **Arabuluculuk dava şartı:** Ticari davalarda konusu para alacağı/tazminat olan uyuşmazlıklarda dava şartı arabuluculuk uygulanır (TTK m.5/A; HUAK m.18/A). Dava açmadan önce başvuru zorunludur.
3. **Yetki (iç taşıma):** HMK genel yetki — davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davada ifa yeri (HMK m.10). Yetki sözleşmesi tacirler arası geçerli (HMK m.17).
4. **Yetki (CMR):** CMR m.31 — davacı, tarafların kararlaştırdığı mahkeme ile davalının mutat meskeni/işletme merkezi, eşyanın teslim alındığı yer veya teslim için belirlenen yer mahkemelerinde dava açabilir; bu mahkemeler münhasırdır.
5. **Uygulanacak hukuk:** Sınır aşan taşımada CMR doğrudan uygulanır; boşlukta MÖHUK'a göre tespit edilen hukuk. Sözleşmesel hukuk seçimi MÖHUK m.24 sınırında geçerli.
6. **İhtiyati tedbir/delil tespiti:** Eşyanın durumunun tespiti için delil tespiti (HMK m.400) ve gerekirse ihtiyati haciz (İİK m.257) değerlendirilir.
7. **Ara sonuç:** Görevli-yetkili mahkeme, dava şartı arabuluculuk gerekliliği ve uygulanacak hukuk netleşir.

## Çıktı modülleri
- Görev-yetki belirleme tablosu (iç taşıma / CMR m.31).
- Dava şartı arabuluculuk ve süre kontrol listesi.
- Uygulanacak hukuk ve yetki şartı geçerlilik notu.

## Plugin bağlamı

Bu beceri `tasima-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
