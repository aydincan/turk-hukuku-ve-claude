---
name: prim-pek-ve-borc
description: "Prim oranları, prime esas kazancın hesabı, eksik/geç bildirim, idari para cezası ve SGK prim borcuna itiraz konularında; işveren veya sigortalı prim yükümlülüğünü değerlendirmek gerektiğinde kullanılır."
---

# Prim, Prime Esas Kazanç ve Borç İhtilafları

## Görev
Prime esas kazancın doğru hesaplanması, prim borcunun ve sorumluluğun tespiti, eksik bildirim ve idari para cezalarına karşı itiraz stratejisini kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlık prim oranı, PEK unsuru, eksik gün/kazanç bildirimi mi, idari para cezası mı?
- Borç hangi döneme ait; SGK'dan tebliğ edilen belge (ödeme emri, idari para cezası, resen tahakkuk) var mı?
- İşveren asıl işveren-alt işveren ilişkisi içinde mi?
- Yapılandırma/af kanunu kapsamına giren dönem var mı?

## Denetim şeması
1. Prime esas kazanç — 5510 m.80: Hangi ödemelerin PEK'e dahil (ücret, prim, ikramiye) hangilerinin istisna (yemek, çocuk, aile yardımı sınırları) olduğu belirlenir.
2. Prim oranları ve sınırlar — m.81 ve m.82: Kısa-uzun vade ve GSS oranları; PEK alt sınırı (asgari ücret) ve üst sınırı (tavan) uygulanır.
3. Sorumluluk — m.88: Prim borcundan işveren sorumludur; alt işveren çalışması varsa asıl işverenin müteselsil sorumluluğu (4857 m.2 ile birlikte) değerlendirilir.
4. İdari para cezası — m.102: Bildirge ve belgelerin süresinde verilmemesi cezayı doğurur; tebliğden itibaren süresinde önce SGK'ya itiraz (idari aşama), reddi/sükut halinde dava.
5. Zamanaşımı — m.93: Kurum prim alacaklarında 10 yıllık zamanaşımı. Ara sonuç: borcun doğruluğu, miktarı ve takip edilebilirliği belirlenir. İspat: SGK tahakkuk kayıtları ve işyeri muhasebe belgeleri.

## Çıktı modülleri
- PEK hesap tablosu (dahil/istisna kalemler).
- İdari para cezasına itiraz/dava dilekçesi iskeleti.
- Zamanaşımı ve yapılandırma değerlendirme notu.

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
