---
name: yargi-yolu-ve-gorev
description: "Bir idari yaptırım kararına karşı adli yargı (sulh ceza hâkimliği) ile idari yargı arasındaki görev ayrımını çözmek, görevsizlik/yetkisizlik ve olumlu-olumsuz görev uyuşmazlığı risklerini yönetmek gerektiğinde kullanılır."
---

# Yargı Yolu ve Görev-Yetki Ayrımı

## Görev
İdari yaptırıma karşı doğru yargı yolunu (sulh ceza hâkimliği mi, idari yargı mı) belirlemek ve görev uyuşmazlığı/süre kaybı riskini önlemek.

## Soğuk başlangıç (intake)
- Yaptırım yalnızca idari para cezası mı, yoksa ruhsat iptali/faaliyet durdurma gibi bir idari işlemle birlikte mi?
- Özel kanun, başvuru yolunu ayrıca düzenlemiş mi?
- Karar tek bir işlemden mi, yoksa zincirleme idari işlemlerden mi doğuyor?
- Daha önce verilmiş görevsizlik/yetkisizlik kararı var mı?

## Denetim şeması
1. **Genel kural (5326 m.27/1):** İdari yaptırım kararlarına karşı sulh ceza hâkimliği görevlidir. Bu, idari para cezalarında ana yoldur.
2. **İstisna — idari yargı (5326 m.27/8):** İdari yaptırım, idari yargının görev alanına giren bir işlemin parçası ise (örn. ruhsat iptali, faaliyet durdurma ile birlikte verilen ceza), uyuşmazlığın bütünü idari yargıda (2577 İYUK) görülür. Bu halde dava açma süresi ve usul İYUK'a tabidir.
3. **Bölünme riski:** Aynı kararın idari para cezası kısmı sulh ceza, idari işlem kısmı idari yargı olabilir; içtihat bütünlük lehine yorumlar — ilkesel atıf yapılır, künye `[doğrulanacak]`.
4. **Görev uyuşmazlığı:** Olumlu/olumsuz görev uyuşmazlığında Uyuşmazlık Mahkemesi devreye girer; bu nedenle baştan doğru mercii seçmek süre kaybını önler.
5. **Süre koruması:** Mercide tereddüt varsa, süreyi korumak için doğru kabul edilen yola başvururken alternatif yolun süresini de takip et.
6. **Ara sonuç:** Yargı yolunu, dayanak işlemin niteliğine göre tek cümlede sabitle ve gerekçesini yaz.

## Çıktı modülleri
- Yargı yolu karar ağacı (m.27/1 vs m.27/8).
- Görevsizlik/yetkisizlik riski notu.
- Süre koruma planı (paralel takip gerekiyorsa).

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
