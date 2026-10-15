---
name: hizmet-tespiti-davasi
description: "Kuruma hiç bildirilmemiş veya eksik bildirilmiş çalışma sürelerinin mahkemece tespiti istendiğinde; hak düşürücü süre, re'sen araştırma ve tanık-belge ispatının kritik olduğu durumlarda kullanılır."
---

# Hizmet Tespiti Davası

## Görev
Sigortalının kuruma bildirilmemiş hizmetlerinin tespiti davasını kurmak, hak düşürücü süreyi ve ispat stratejisini yönetmek. Bu dava kamu düzenine ilişkindir; hâkim re'sen araştırma yapar.

## Soğuk başlangıç (intake)
- Tespiti istenen dönem hangi yıllar; işyeri hâlâ faal mi?
- SGK hizmet dökümünde bu dönem hiç mi yok, eksik mi (gün/kazanç eksikliği)?
- Aynı işyerinden kuruma bildirilmiş başka bir gün/dönem var mı?
- O işyerinde birlikte çalışan, tanıklık edebilecek kişiler var mı?

## Denetim şeması
1. Hukuki dayanak — 5510 m.86/9 (mülga 506 m.79/10): Kuruma bildirilmemiş çalışmanın tespiti mahkemeden istenir. Davalılar: işveren ve SGK.
2. Hak düşürücü süre: Hizmetin geçtiği yılın sonundan itibaren 5 yıl. Ancak işverence kuruma verilmiş herhangi bir belge (işe giriş bildirgesi, dönem bordrosu, müfettiş tutanağı) varsa hak düşürücü süre işlemez — bu istisna mutlaka araştırılır.
3. Re'sen araştırma: Mahkeme işyeri SGK sicil dosyasını, dönem bordrolarını, varsa müfettiş raporlarını getirtir; komşu işyeri tanıklarını dinler. İspat yükü davacıda olmakla birlikte hâkim resen delil toplar.
4. İspat hiyerarşisi: Önce yazılı/resmi belge (bordro, ücret tediye, SGK kaydı), sonra bordro tanıkları, en son komşu işyeri/resmi kurum tanıkları. Salt tanıkla tespitte güçlü/destekleyici delil aranır.
5. Ara sonuç: Tespit edilen dönem, gün sayısı ve prime esas kazanç belirlenir; karar SGK kayıtlarına işlenir.

## Çıktı modülleri
- Dava dilekçesi iskeleti (taraflar, dönem, talep sonucu, deliller).
- Delil ve tanık listesi; getirtilecek belgeler dizini.
- Hak düşürücü süre değerlendirme notu (istisna var/yok).

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
