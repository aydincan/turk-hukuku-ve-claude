---
name: yarisma-ve-talep-secimi
description: "Aynı olayda sebepsiz zenginleşme yanında istihkak, haksız fiil, sözleşmesel iade veya vekâletsiz iş görme talebi de mümkün olduğunda hangi talebin öncelikli ve avantajlı olduğunu belirlemek için kullanılır."
---

# Diğer Taleplerle Yarışma ve Talep Seçimi

## Görev
Sebepsiz zenginleşmenin tali (ikincil) niteliğini gözeterek, aynı maddi olayda mümkün olan diğer taleplerle (aynî istihkak, sözleşmesel iade, haksız fiil, vekâletsiz iş görme) yarışmayı çözmek ve müvekkil için en avantajlı talebi seçmek. Yanlış talep seçimi süre, faiz ve ispat dezavantajı doğurur.

## Soğuk başlangıç (intake)
- Olayda ayakta bir sözleşme veya geçersiz sözleşmenin tasfiyesi var mı?
- İade konusu hâlâ aynen mevcut, belirli bir şey mi (istihkak mümkün mü)?
- Karşı tarafın kusurlu/hukuka aykırı fiili var mı (haksız fiil mümkün mü)?
- Bir kişi başkasının işini yetkisiz mi gördü (vekâletsiz iş görme)?

## Denetim şeması
1. **Tali nitelik kuralı.** Sebepsiz zenginleşme, başka bir talep mümkünse kural olarak geri planda kalır; mümkün olan diğer talep yoksa veya tükenmişse devreye girer. Önce öncelikli talepler taranır.
2. **Aynî istihkak (TMK m.683).** İade konusu belirli bir şey ve mülkiyet devredilmemişse, malik istihkakla aynen iade isteyebilir; bu talep süre ve aynen iade bakımından avantajlıdır. Zamanaşımına da kural olarak tâbi değildir.
3. **Sözleşmesel iade/dönme.** Geçersiz veya dönülmüş sözleşmede iade çoğu kez sözleşmenin kendi tasfiye rejimiyle (TBK m.125/2 dönme) çözülür; bu daha geniş tazminat imkânı sağlayabilir.
4. **Haksız fiil (TBK m.49 vd.).** Karşı tarafın kusurlu ve hukuka aykırı fiili zarara yol açtıysa haksız fiil tazminatı zenginleşmeden bağımsız ve genellikle daha geniş kapsamlıdır; ölçü "zarar"dır, "zenginleşme" değil.
5. **Vekâletsiz iş görme (TBK m.526-531).** Bir kişi başkasının işini onun menfaatine/iradesine göre yetkisiz görmüşse, sebepsiz zenginleşme yerine bu özel hükümler uygulanır.
6. **Seçim ve ara sonuç.** Süre, faiz başlangıcı, ispat kolaylığı ve talep miktarı karşılaştırılır; gerekiyorsa terditli (kademeli) talep kurulur. Ara sonuç: birincil talep + yedek sebepsiz zenginleşme talebi.

## Çıktı modülleri
- Talep karşılaştırma matrisi (süre/faiz/ispat/miktar).
- Terditli talep kurgusu önerisi.
- Seçilen talep gerekçe notu.

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
