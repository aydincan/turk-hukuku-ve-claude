---
name: tahkime-elverislilik-kapsam
description: "Bir uyuşmazlığın konu itibarıyla tahkime veya arabuluculuğa elverişli olup olmadığını, kamu düzeni ve emredici hükümler süzgecinden geçirerek belirlemek gerektiğinde kullanılır."
---

# Tahkime ve Arabuluculuğa Elverişlilik

## Görev
Uyuşmazlığın alternatif çözüm yoluna konu edilip edilemeyeceğini kapı eşiğinde
belirlemek. Elverişsiz bir konu için kurulan tahkim/arabuluculuk emek ve süre kaybı
doğurur; bu süzgeç en başta uygulanır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık konusu nedir (ayni hak, statü, alacak, idari işlem)?
2. Taraflar bu hak üzerinde serbestçe tasarruf edebilir mi?
3. Konu bir kamu düzeni alanına mı (boşanma statüsü, ceza, vergi tarhı) giriyor?
4. Hedef yol tahkim mi arabuluculuk mu?

## Denetim şeması
1. **Tahkim elverişliliği**: **HMK m.408** — taşınmaz üzerindeki **ayni haklara** ilişkin
   ve **iki tarafın iradesine tabi olmayan** uyuşmazlıklar tahkime elverişsizdir.
   Milletlerarası tahkimde de aynı çekirdek geçerlidir (**MTK m.1/4**).
2. **Arabuluculuk elverişliliği**: **HUAK m.1/2** — tarafların üzerinde serbestçe
   tasarruf edebileceği işler. **Aile içi şiddet** iddiası içeren uyuşmazlıklar
   arabuluculuğa elverişsizdir.
3. **Kamu düzeni/emredici hüküm süzgeci**: Boşanma/soybağı gibi **statü** belirleyen
   davalar, ceza yargılaması, idari/vergi uyuşmazlıkları kural olarak dışlanır.
   Tahkim/arabuluculuk yalnızca tarafların tasarrufundaki **maddi sonuçları** (ör. nafaka
   miktarı değil ama mal rejimi tasfiyesindeki alacak gibi tasarruf edilebilir kısımlar)
   yönünden mümkün olabilir; sınır dikkatle çizilir.
4. **Karma uyuşmazlık**: Bir kısmı elverişli bir kısmı değilse ayrıştırma yapılır;
   elverişli kısım tahkim/arabuluculuğa, diğeri devlet yargısına yönlendirilir.
5. **Ara sonuç**: Elverişlilik kararı, dayanak madde ve istisna notu.

## Çıktı modülleri
- Elverişlilik karar tablosu (konu-yol-dayanak-istisna).
- Karma uyuşmazlık ayrıştırma haritası.
- Devlet yargısına yönlendirme gerekiyorsa görev/yetki kısa notu.

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
