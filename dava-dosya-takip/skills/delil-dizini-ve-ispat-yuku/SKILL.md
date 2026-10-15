---
name: delil-dizini-ve-ispat-yuku
description: "Dosyadaki delilleri dizinleyip her birini ilgili vakıaya ve ispat yüküne bağlamak, sunulan-beklenen-itirazlı delilleri ayırt etmek gerektiğinde kullan."
---

# Delil Dizini ve İspat Yükü

## Görev
Dosyadaki tüm delilleri türü, ibraz edeni, dayandığı vakıa ve durumuyla dizinlemek; her çekişmeli vakıada ispat yükünün kimde olduğunu eşlemek.

## Soğuk başlangıç (intake)
- Hangi deliller dosyada (senet, fatura, tanık listesi, bilirkişi raporu, keşif tutanağı, yazışma)?
- Hangi vakıalar çekişmeli, hangileri ikrar edilmiş?
- Henüz sunulmamış ama dayanılan delil var mı?
- Karşı tarafın delillerine itiraz edilmiş mi?

## Denetim şeması
1. Delil satırı: delil adı, türü, ibraz eden, dayandığı vakıa, durum (sunuldu / beklenen / itirazlı). Delil türleri: senet (HMK m.199 vd.), tanık (HMK m.240 vd.), bilirkişi (HMK m.266 vd.), keşif (HMK m.288), yemin.
2. İspat yükü eşlemesi: HMK m.190 ve TMK m.6 uyarınca bir vakıadan lehine hak çıkaran tarafın ispatla yükümlü olduğunu uygula; her çekişmeli vakıanın karşısına yükümlü tarafı yaz.
3. Senetle ispat kuralı: belirli tutarı aşan hukuki işlemlerde senetle ispat zorunluluğu (HMK m.200) ve tanıkla ispat sınırı (HMK m.201) gözetilerek tanık deliline güvenilirlik notu düşülür.
4. Eksik delil: dayanılan ama sunulmamış delil ve celbi gereken belge (HMK m.219-221 ibraz yükümlülüğü, müzekkere) ayrı liste.
5. Ara sonuç: hangi vakıa hangi delille ispatlanıyor, hangisi açıkta — boşluk haritası. Delil içeriği evraktan alınır; var olmayan delil yazılmaz.

## Çıktı modülleri
- Delil-tür-ibraz eden-vakıa-durum kolonlu dizin tablosu.
- İspat yükü eşleme tablosu (çekişmeli vakıa → yükümlü taraf).
- Eksik/celbi gereken delil listesi.

## Plugin bağlamı

Bu beceri `dava-dosya-takip` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
