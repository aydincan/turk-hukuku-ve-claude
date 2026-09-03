---
name: turkpatent-basvuru-itiraz
description: "Marka tescil başvurusu, yayına itiraz, karara itiraz veya YİDK kararına karşı dava aşamalarında; idari sürecin süreleri ve usulünü m.11-m.20 ve m.172 üzerinden yönetmek için kullanılır."
---

# TÜRKPATENT Başvuru, İtiraz ve YİDK Süreci

## Görev
Markanın TÜRKPATENT nezdindeki idari yaşam döngüsünü yönetmek: başvuru (m.11), şekli/mutlak inceleme, Bültende yayın, yayına itiraz (m.18), karara itiraz ve YİDK; YİDK nihai kararına karşı iptal davası (m.172/2). Süre disiplini bu alanda belirleyicidir; hak düşürücü süreler kaçırılırsa idari yol kapanır.

## Soğuk başlangıç (intake)
- Başvuru hangi aşamada (inceleme, yayın, itiraz, YİDK)?
- Hangi mal/hizmet sınıfları ve Bülten yayın tarihi nedir?
- İtiraz/karara itiraz için kalan süre ne kadar?
- Mutlak ret mi (re'sen), nispi sebep mi (itiraz üzerine) söz konusu?

## Denetim şeması
1. **Başvuru ve şekli inceleme (m.11-15).** Başvuru unsurları, sınıflandırma (Nice), başvuru tarihi ve rüçhan hakkı (m.12-13) kontrol edilir.
2. **Mutlak ret incelemesi (m.16).** TÜRKPATENT m.5 sebeplerini re'sen inceler; kısmî/tam ret kararı verir.
3. **Yayın ve itiraz (m.18).** Başvuru Bültende yayımlanır; ilgililer yayından itibaren iki ay içinde m.5-6 sebepleriyle itiraz eder. İtiraz süresi hak düşürücüdür.
4. **Kullanmama def'i (m.19/2).** İtiraz edilen, itiraz dayanağı markanın 5 yıllık kullanımının ispatını isteyebilir.
5. **Karara itiraz ve YİDK (m.20).** Markalar Dairesi kararına karşı iki ay içinde YİDK'ya itiraz; YİDK Kurum'un nihai kararını verir.
6. **YİDK kararına dava (m.172/2).** Nihai karar tebliğinden itibaren iki ay içinde Ankara FSHHM'de iptal davası açılır; bu süre hak düşürücüdür.

## Çıktı modülleri
- Aşama-süre takvimi (yayın, itiraz, YİDK, dava — tarih hesaplı).
- İtiraz/cevap dilekçesi iskeleti ve dayanak madde listesi.
- Süre kaçırma riski uyarı notu ve dava yolu kontrolü.

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
