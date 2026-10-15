---
name: miras-iliskisinde-isbat-ve-delil
description: "Mirasçı sıfatı, kazandırma, muvazaa, saklı pay zedelenmesi gibi vakıaların ispatını planlamak; hangi delilin kimin yükünde olduğunu, tanık/senet/bilirkişi sınırlarını ve ölüm tarihi değerlemesini netleştirmek gerektiğinde kullanılır."
---

# Miras İlişkisinde İspat ve Delil Yönetimi

## Görev
Miras uyuşmazlığındaki vakıaların ispat yükünü, uygun delil türlerini ve değerleme esaslarını TMK m.6 ve HMK m.187-293 çerçevesinde planlamak.

## Soğuk başlangıç (intake)
- İspatlanacak çekişmeli vakıalar neler? (sıfat, kazandırma, muvazaa, değer)
- Eldeki belgeler: tapu, banka, nüfus, vasiyet, sözleşme?
- Tanık dinletilecek mi, yoksa senetle ispat zorunlu mu?
- Değerleme/hesap gerektiren kalem var mı? (bilirkişi)
- Karşı tarafın elindeki belgeler için ibraz talebi gerekir mi?

## Denetim şeması
1. **İspat yükü (TMK m.6, HMK m.190):** Bir vakıadan lehine hak çıkaran onu ispatlar. Mirasçı sıfatı iddia eden soybağı/nüfusla; tasarrufun geçersizliğini, muvazaayı, irade fesadını iddia eden bunu ispatlar.
2. **Senetle ispat ve istisnası (HMK m.200-201):** Belirli tutarı aşan hukuki işlemler senetle ispatlanır; senede karşı tanık dinlenemez. Ancak muris muvazaası ve ölüme bağlı tasarrufta mirasçılar üçüncü kişi sayıldığından tanık dahil her delille ispat mümkündür (yerleşik içtihat — künye `[doğrulanacak]`).
3. **Karineler:** Mirasçılık belgesi mirasçılığa karine (m.598); tapu kaydı mülkiyete karine (m.7, m.992). Aksini iddia eden ispatla yükümlü.
4. **Bilirkişi (HMK m.266 vd.):** Tenkis/denkleştirme hesabı, ölüm tarihindeki taşınmaz/şirket değeri, el yazısı incelemesi (vasiyette sahtelik) bilirkişiye gider. Rapor, ölüm tarihi değerleri ve doğru oranlarla denetlenmeli.
5. **Belge ibrazı ve delil tespiti (HMK m.219-222, m.400):** Banka kayıtları, hesap hareketleri için üçüncü kişiden/kurumdan celp; kaybolma riski olan delil için tespit.
6. **Ara sonuç:** vakıa-delil-yük matrisi; toplanacak delil listesi ve usulü.

## Çıktı modülleri
- İspat yükü ve delil matrisi (vakıa / yük / delil türü)
- Tanık listesi ve dinletilme gerekçesi
- Bilirkişi sorularının taslağı (ölüm tarihi değerli)
- Belge celbi / müzekkere talepleri listesi

## Plugin bağlamı

Bu beceri `miras-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
