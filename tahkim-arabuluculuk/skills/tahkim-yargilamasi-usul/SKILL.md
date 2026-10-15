---
name: tahkim-yargilamasi-usul
description: "Hakem heyetinin oluşumu, tahkim yargılamasının yürütülmesi, süreler ve geçici hukuki koruma gibi tahkim sürecinin işleyişini planlamak veya yönetmek gerektiğinde kullanılır."
---

# Tahkim Yargılaması Usulü

## Görev
Tahkim sürecini başlatmaktan hakem kararına kadar usul adımlarını, süreleri ve risk
noktalarını yönetmek; hakem atama, davanın açılması, delil sunumu ve geçici koruma
talepleri için yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Tahkim iç tahkim (HMK) mi milletlerarası (MTK) mi, kurumsal mı ad hoc mı?
2. Hakem sayısı ve atama usulü anlaşmada nasıl belirlenmiş?
3. Tahkim süresi başladı mı, kararın verilmesi için süre işliyor mu?
4. Geçici tedbir/ihtiyati haciz ihtiyacı var mı?

## Denetim şeması
1. **Hakem sayısı ve atama**: **HMK m.415-417** / **MTK m.7** — sayı tek olmalı;
   belirlenmemişse hakem sayısı ve atama mahkeme veya kurum eliyle tamamlanır. Hakemin
   tarafsızlık/bağımsızlık açıklaması ve **ret sebepleri** (**HMK m.417**, **MTK m.7/C-D**)
   denetlenir.
2. **Davanın açılması ve dilekçeler**: Tahkim davası, talep tarihiyle açılır; iddia ve
   savunma dilekçeleri, deliller hakem heyetinin belirlediği takvime göre sunulur
   (**HMK m.426-428**, **MTK m.10**).
3. **Tahkim süresi**: İç tahkimde kural olarak **1 yıl** (**HMK m.427**), MTK'da **1 yıl**
   (**MTK m.10/B**); taraf anlaşması veya mahkeme kararıyla uzatılabilir. Süre aşımı iptal
   sebebidir; bu yüzden takvim sıkı tutulur.
4. **Geçici hukuki koruma**: Hakem heyeti ihtiyati tedbire karar verebilir ama cebri icra
   gerektiren tedbirler için mahkeme yetkilidir (**HMK m.414**, **MTK m.6**). Mahkemeden
   tedbir istemek tahkim iradesinden vazgeçme sayılmaz.
5. **Ara sonuç**: Usul takvimi, hakem heyeti durumu ve açık eksikler listesi.

## Çıktı modülleri
- Tahkim usul takvimi (atama, dilekçeler, duruşma, karar süresi).
- Hakem atama/ret dilekçesi taslağı.
- Geçici hukuki koruma başvuru notu (yetkili merci ayrımıyla).

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
