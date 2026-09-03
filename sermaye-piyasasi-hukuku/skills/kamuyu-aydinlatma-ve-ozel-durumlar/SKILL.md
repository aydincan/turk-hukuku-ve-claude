---
name: kamuyu-aydinlatma-ve-ozel-durumlar
description: "Halka açık ortaklığın sürekli kamuyu aydınlatma yükümlülükleri, özel durum açıklamaları, içsel bilginin ertelenmesi ve KAP açıklamalarından doğan sorumluluk değerlendirileceğinde kullanılır."
---

# Kamuyu Aydınlatma ve Özel Durumlar

## Görev
İhraççının sürekli kamuyu aydınlatma yükümlülüklerini (özel durumlar, finansal raporlama) SPK m.14-15 ve özel durumlar tebliği çerçevesinde denetlemek; açıklama zamanlaması, erteleme ve sorumluluk (m.32) konularını yönetmek.

## Soğuk başlangıç (intake)
- Açıklanması tartışılan bilgi nedir; içsel bilgi (fiyat/yatırım kararı etkili) niteliği taşıyor mu?
- Bilgi ne zaman doğdu, kimler biliyor; açıklama yapıldı mı, ertelendi mi?
- Açıklama eksik/yanlış/gecikmeli mi yapıldı; yatırımcı zararı veya Kurul incelemesi var mı?
- İhraççı, yönetici/imza yetkilisi mi yoksa zarar gören yatırımcı mı danışıyor?

## Denetim şeması
1. **İçsel bilgi tespiti:** Bilginin henüz kamuya açıklanmamış, ortaklık/araçla ilgili, açıklandığında fiyatı veya yatırım kararını etkileyebilecek nitelikte olup olmadığı belirlenir (SPK m.15, m.106 tanımı ile uyumlu). Değilse özel durum açıklaması yükümlülüğü doğmaz.
2. **Açıklama zamanı:** İçsel bilgi oluştuğunda gecikmeksizin KAP üzerinden açıklama esastır; ara sonuç olarak yükümlülüğün doğduğu an tespit edilir.
3. **Erteleme rejimi:** Meşru menfaat, yatırımcının yanıltılmaması ve gizliliğin sağlanması koşullarıyla açıklamanın ertelenebileceği; erteleme kararının ve gerekçesinin belgelenmesi, içsel bilgiye erişenler listesinin tutulması aranır (m.15 ve tebliğ).
4. **Sorumluluk (m.32):** Kamuyu aydınlatma belgelerindeki yanlış/yanıltıcı/eksik bilgiden doğan zarardan ihraççı ve kusurlu yöneticiler sorumludur; ispatta bilginin yanlışlığı ve illiyet yatırımcıda, özen ispatı ihraççıdadır.
5. **Yaptırım ekseni:** İhlal hem idari yaptırım (m.103 vd.) hem -koşulları varsa- piyasa suçu (m.107/2 bilgiye dayalı piyasa dolandırıcılığı) doğurabilir; idari ve cezai süreç ayrıştırılır.

## Çıktı modülleri
- İçsel bilgi/özel durum nitelendirme notu
- Açıklama/erteleme karar ve belgeleme kontrol listesi
- Sorumluluk değerlendirmesi (m.32) ve muhatap analizi
- KAP açıklama taslağı iskeleti veya yatırımcı talep çerçevesi

## Plugin bağlamı

Bu beceri `sermaye-piyasasi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
