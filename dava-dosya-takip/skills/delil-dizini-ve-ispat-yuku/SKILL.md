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
