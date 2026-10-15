---
name: algoritmik-seffaflik-aciklanabilirlik
description: "İlgili kişinin veya denetçinin bir yapay zekâ kararının mantığına, kullanılan verilere ve karara dair açıklama talep etmesi durumunda aydınlatma ve bilgi verme yükümlülüğünün kapsamı ile ticari sır sınırı dengelendiğinde kullanılır."
---

# Algoritmik Şeffaflık ve Açıklanabilirlik

## Görev
Bir yapay zekâ sisteminin işleyişi ve ürettiği karar hakkında açıklama yükümlülüğünün kapsamını belirlemek; ilgili kişinin bilgi hakkı ile geliştiricinin ticari sır/fikri mülkiyet menfaatini dengeleyerek uygun şeffaflık seviyesini tasarlamak.

## Soğuk başlangıç (intake)
1. Talep eden kim: ilgili kişi, Kurul/denetçi, sözleşmenin karşı tarafı, mahkeme?
2. Ne isteniyor: kararın gerekçesi, kullanılan veri kategorileri, modelin mantığı, kaynak kod?
3. Sistemde aydınlatma metni ve karar gerekçesi loglanıyor mu?
4. Ticari sır/lisans kısıtı veya üçüncü kişi modeli (kapalı API) var mı?

## Denetim şeması
1. **Yükümlülüğün kaynağı**: KVKK m.10 aydınlatma (işlemenin amacı, otomatik karar varlığı), m.11 bilgi talep hakkı ve m.13 başvuru. Bu, kaynak kodun teslimini değil, kararın mantığı ve sonuçları konusunda anlamlı bilgiyi gerektirir. Ara sonuç: talep edilen şeffaflık seviyesi.
2. **Kapsam sınırı**: Şeffaflık, ticari sır ve fikri mülkiyetle (FSEK/SMK, TTK haksız rekabet) sınırlanır; ancak bu sınır bilgi hakkını tamamen bertaraf edemez — "anlamlı açıklama" verilmelidir. Denge ölçülülükle kurulur.
3. **Yargısal talepte**: HMK m.219-220 belgelerin ibrazı ve bilirkişi incelemesi yoluyla teknik açıklama sağlanabilir; mahkeme önünde ticari sır tedbirleriyle inceleme istenebilir.
4. **Kamu kararında**: İdarenin otomatik işleminde gerekçe yükümlülüğü ve İYUK kapsamında bilgi edinme/savunma hakları; gerekçesiz idari işlem sakatlık sebebi.
5. **Belgeleme**: Karar gerekçesinin ve model versiyonunun loglanması, sonradan açıklanabilirliği ve ispatı sağlar.

Kurul rehberleri için kvkk.gov.tr; yargı uygulaması için karararama portalları, künye [doğrulanacak].

## Çıktı modülleri
- Şeffaflık seviyesi matrisi (talep eden / verilecek bilgi / sınır).
- Açıklama metni taslağı (ticari sır korunarak).
- Logging/açıklanabilirlik öneri listesi.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
