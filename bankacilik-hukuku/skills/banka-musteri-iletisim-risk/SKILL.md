---
name: banka-musteri-iletisim-risk
description: "Banka veya müşteri adına ihtarname, başvuru, şikâyet yanıtı, sulh/yapılandırma teklifi hazırlamak ve uyuşmazlık öncesi/sırasında iletişim ile risk stratejisini kurmak gerektiğinde kullanılır."
---

# Banka-Müşteri İletişimi, İhtarname ve Müzakere Yönetimi

## Görev
Uyuşmazlık öncesi ve sırasında banka ya da müşteri adına yazılı iletişimi (ihtarname, başvuru, şikâyet yanıtı, sulh/yeniden yapılandırma teklifi) hukuken sağlam ve stratejik biçimde kurmak.

## Soğuk başlangıç (intake)
- Müvekkil banka mı, müşteri/kefil mi; amaç tahsilat, savunma, iade talebi mi?
- İletişimin hedefi: temerrüt ihtarı, muacceliyet bildirimi, ücret iadesi başvurusu, sulh teklifi?
- Karşı tarafın önceki yazışmaları ve tutumu nedir; süre/zamanaşımı baskısı var mı?
- İletişim delil olarak kullanılacak mı (ihtar ile temerrüt/zamanaşımı kesilmesi)?

## Denetim şeması
1. **Amaç ve hukuki etki**: İhtarın hangi sonucu doğuracağını belirle: temerrüt kurma (TBK m.117), muacceliyet tetikleme, zamanaşımını kesme (TBK m.154 — dava/icra/ihtar etkileri), cayma/itiraz süresini koruma. Yazının her cümlesi bu hukuki etkiyle hizalanmalı.
2. **Şekil ve ispat**: Sonuç doğuran ihtarlar için noter/iadeli taahhüt/KEP gibi ispatlanabilir kanal seçilir; tebliğ tarihi süre hesabı için kritiktir.
3. **İçerik dengesi**: Bankaya tavsiye edilen üslup ölçülü ve sır rejimine uygun (5411 m.73) olmalı; müşteri tarafında ise talep, dayanak (madde atfı) ve süre açıkça belirtilmeli. Tehdit/aşırı baskı içeren ifadelerden kaçınılır.
4. **Risk-strateji**: Sulh/yeniden yapılandırma teklifinde tahsil kabiliyeti, teminat durumu, dava maliyeti ve süre riski tartılır; "ihtirazi kayıt" ve "haklar saklıdır" kayıtları uygun yerlere konur. Yapılandırma kabulünün ikrar/feragat etkisi değerlendirilir.
5. **Sonraki adım köprüsü**: Yanıt alınmazsa izlenecek dava/takip yoluna ve süresine bağlanır. Ara sonuç olarak iletişim aracının doğurduğu hukuki etkiyi ve sonraki adımı yaz.

## Çıktı modülleri
- İhtarname / başvuru / şikâyet yanıtı taslağı ([doldurulacak] alanlarla).
- Sulh/yeniden yapılandırma teklif çerçevesi ve ihtirazi kayıtlar.
- Süre ve delil etkisi notu.

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
