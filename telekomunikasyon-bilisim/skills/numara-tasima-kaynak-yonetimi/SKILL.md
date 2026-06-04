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
