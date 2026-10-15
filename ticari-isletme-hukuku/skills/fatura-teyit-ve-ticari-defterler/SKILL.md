---
name: fatura-teyit-ve-ticari-defterler
description: "Faturaya veya teyit mektubuna itiraz suresinin kacirilmasinin sonuclari, ticari defterlerin sahibi lehine/aleyhine delil olusturmasi ve defter ibrazi gerektiginde kullanilir."
---

# Fatura, Teyit Mektubu ve Ticari Defterler

## Görev
Fatura ve teyit mektubunun ispat gücünü ve itiraz sürelerinin sonuçlarını belirlemek; ticari defterlerin hangi hallerde sahibi lehine ya da aleyhine delil olduğunu değerlendirmek. Bu araçlar ticari uyuşmazlıkta ispatın belkemiğidir.

## Soğuk başlangıç (intake)
1. Fatura/teyit mektubu kim tarafından, ne zaman gönderildi ve tebliğ edildi?
2. Alıcı tacir mi; 8 gün içinde itiraz etmiş mi?
3. Uyuşmazlık faturanın bedeli mi, içeriği (ödeme, vade, miktar) mi?
4. Taraflar usulüne uygun, tasdikli ticari defter tutuyor mu?

## Denetim şeması
1. **Fatura ve ispat:** TTK m.21/1 — ticari işletmesi gereği bir mal/hizmet veren tacir, isteme bağlı fatura verir. TTK m.21/2 — faturayı alan kişi, aldığı tarihten itibaren 8 gün içinde içeriği hakkında itiraz etmezse, içeriğini kabul etmiş sayılır. Bu karine yalnızca faturanın "içeriğine" ilişkindir; sözleşmenin kurulduğunu tek başına ispatlamaz, ancak içerik (miktar, fiyat, vade) yönünden güçlü karine doğurur.
2. **Teyit mektubu:** TTK m.21/3 — sözlü veya yazışmayla yapılan sözleşmenin teyidi için gönderilen mektuba 8 gün içinde itiraz edilmezse mektubun sözleşmeye uygun sayılacağı kabul edilir.
3. **Ticari defterler:** TTK m.64-88 tutma ve saklama (10 yıl) yükümü; usulüne uygun tutulan ve açılış/kapanış onayları yapılmış defterler. İspat değeri HMK m.222'ye göre belirlenir: tacirin ticari defterleri kendi lehine delil olabileceği gibi (karşı tarafın defterleriyle uyumlu, çelişmiyor ve karşı taraf aksini muteber defterle çürütemiyorsa), aleyhine de delildir; defterler sahibinin aleyhine her zaman delil olur.
4. **Defter ibrazı:** Mahkeme re'sen veya talep üzerine defterlerin ibrazını ister (HMK m.222/1); ibrazdan kaçınma aleyhe değerlendirilebilir.
5. **Ara sonuç:** Süresinde itiraz edilmeyen fatura içeriği kabul sayılır; usulüne uygun defter, HMK m.222 şartlarıyla sahibi lehine delil olur.

## Çıktı modülleri
- Süre/itiraz değerlendirme notu (fatura/teyit, 8 gün hesabı).
- Defterlerin delil değeri analizi (HMK m.222 koşulları).
- İtiraz dilekçesi veya defter ibrazı talebi taslağı.

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
