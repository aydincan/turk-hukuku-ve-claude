---
name: arama-el-koyma-iletisim
description: "Konut/iş yeri/üst aramasının, el koymanın ve iletişimin/teknik araçlarla izlemenin hukuka uygunluğunu denetlemek ve buradan elde edilen delillerin geçerliliğini değerlendirmek gerektiğinde kullanılır."
---

# Arama, El Koyma ve İletişimin Denetlenmesi

## Görev
Arama, el koyma ve iletişim denetimi tedbirlerinin karar, kapsam ve usul yönünden hukuka uygunluğunu denetlemek; bu yolla elde edilen delillerin kullanılabilirliğini değerlendirmek.

## Soğuk başlangıç (intake)
- Arama nerede yapıldı (konut, iş yeri, üst, araç) ve karar var mıydı?
- Arama gece mi gündüz mü; ihtiyar heyeti/komşu tanık hazır mıydı (m.119)?
- Neye el konuldu; el koymaya hâkim onayı alındı mı?
- İletişim denetimi/teknik takip kararı hangi suçtan ve hangi süreyle verildi?
- Elde edilen delil dosyada hükme esas mı alınıyor?

## Denetim şeması
1. **Arama kararı.** Kural olarak hâkim kararı; gecikmesinde sakınca varsa savcı, savcıya ulaşılamıyorsa kolluk amirinin yazılı emriyle yapılır (CMK m.116, m.119). Karar/emir aramanın konusunu, kapsamını ve sebebini içermelidir.
2. **Usul güvenceleri.** Konut ve iş yeri araması kural olarak gündüz; gece sınırlamaları ve hazır bulunacaklar m.118-120'de düzenlenir. İlgilinin gösterdiği belge müsadereye tabi değilse aleyhe kullanılamaz.
3. **El koyma.** Suç delili eşyaya el konulur; hâkim kararı esastır, gecikmesinde sakınca olan halde savcı/kolluk el koyar ve 24 saat içinde hâkim onayına sunar, hâkim 48 saat içinde karar verir (m.123-127). Avukat bürosu (m.130), basılı eser, postada el koyma için özel rejim vardır.
4. **İletişimin denetlenmesi.** Sadece katalog suçlarda, başka yolla delil elde imkânı yoksa, kuvvetli şüphe sebepleri varsa hâkim/gecikmede savcı kararıyla, azami sürelerle uygulanır (m.135). Tesadüfen elde edilen deliller m.138 sınırına tabidir.
5. **Yaptırım.** Hukuka aykırı arama/el koyma/dinleme ile elde edilen delil hükme esas alınamaz (m.206/2-a, m.217/2; Anayasa m.38/6). Zehirli ağacın meyvesi tartışması burada yürütülür.
6. **Ara sonuç.** Karar/onay/kapsam eksikse delil dışlanması talebi; geçerliyse delilin içeriği değerlendirmesine geçilir.

## Çıktı modülleri
- Tedbir başına hukuka uygunluk denetim tablosu (karar-kapsam-süre-onay).
- Delilin hükümden çıkarılması (dışlama) talebi gerekçesi.
- El konulan eşyanın iadesi talebi taslağı (m.131).
- İhlal tespit edilen güvencelerin maddeyle eşlenmiş listesi.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
