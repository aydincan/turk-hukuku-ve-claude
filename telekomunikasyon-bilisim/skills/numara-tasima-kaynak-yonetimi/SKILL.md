---
name: numara-tasima-kaynak-yonetimi
description: "Numara taşıma talepleri, taşıma reddi, frekans ve numara gibi kıt kaynak tahsisi, geri alımı ve bu kaynaklara ilişkin BTK işlemleri söz konusu olduğunda kullanılır."
---

# Numara Taşınabilirliği ve Kaynak Yönetimi

## Görev
Numara taşıma ve kaynak (frekans/numara) tahsis-iade işlemlerini 5809 ve BTK Numaralandırma/Numara Taşınabilirliği düzenlemeleri çerçevesinde denetlemek; taşıma reddi veya kaynak uyuşmazlığında çözüm yolunu kurmak.

## Soğuk başlangıç (intake)
1. Talep numara taşıma mı, kaynak (frekans/numara bloğu) tahsisi/iadesi mi?
2. Taşıma talebi hangi gerekçeyle reddedildi (borç, kimlik, teknik)?
3. Müvekkil abone mi, alıcı/veren işletmeci mi?
4. İlgili BTK işlemi/karar tarihi var mı?

## Denetim şeması
1. **Kaynak rejimi**: 5809 m.34 ve devamı — numara ve frekans BTK tarafından yönetilen kıt kaynaktır; tahsis kullanım hakkına bağlıdır, mülkiyet doğurmaz. Ara sonuç: işlem kaynak yönetimi kapsamında mı.
2. **Numara taşınabilirliği**: BTK Numara Taşınabilirliği düzenlemesi — abonenin numarasını koruyarak işletmeci değiştirme hakkı; taşıma süresi ve reddedilebilir haller (geçerli borç, kimlik/sahiplik uyuşmazlığı) sınırlı sayıdadır. Geçersiz ret tüketici hakkını ihlal eder.
3. **Ret denetimi**: Ret gerekçesinin düzenlemedeki sınırlı sebeplerden birine dayanıp dayanmadığı; borç gerekçesinde borcun muaccel ve tartışmasız olması aranır. İspat yükü reddeden işletmecidedir.
4. **Kaynak tahsisi/geri alımı**: Numara bloğu/frekans tahsisinde ücret, kullanım koşulu ve etkin kullanılmama halinde geri alım; geri alım idari işlemdir.
5. **Yol ayrımı**: Abone-işletmeci taşıma uyuşmazlığında BTK şikâyet ve gerekirse tüketici yolu; BTK'nın kaynak tahsis/geri alım işlemine karşı İYUK m.7 süresinde idari dava.

## Çıktı modülleri
- Taşıma/kaynak işlemi uygunluk notu.
- Taşıma reddine itiraz veya BTK şikâyet taslağı.
- Kaynak geri alımına karşı dava değerlendirmesi.

## Plugin bağlamı

Bu beceri `telekomunikasyon-bilisim` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
