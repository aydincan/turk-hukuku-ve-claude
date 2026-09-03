---
name: ticari-islerde-faiz-ve-temerrut
description: "Bir ticari alacakta uygulanacak faiz turunu ve oranini (ticari temerrut faizi, avans faizi, kapital faizi), faiz baslangic tarihini ve bilesik faiz sinirlarini belirlemek gerektiginde kullanilir."
---

# Ticari İşlerde Faiz ve Temerrüt

## Görev
Ticari bir alacakta hangi faizin, hangi oranla, hangi tarihten itibaren işleyeceğini doğru hesaplamak. Ticari işlerde faiz rejimi genel hükümlerden ayrılır; yanlış faiz türü talep, eksik tahsil veya ret riskidir.

## Soğuk başlangıç (intake)
1. İş her iki/bir taraf için ticari mi (TTK m.3, m.19)?
2. Sözleşmede faiz oranı kararlaştırılmış mı?
3. Borç para borcu mu; muacceliyet ve temerrüt ne zaman doğdu?
4. Temerrüt için ihtar gerekli mi, yoksa kesin vade var mı?

## Denetim şeması
1. **Faizin niteliği:** İş ticari ise faiz oranı serbestçe belirlenebilir (TTK m.8/1). Oran kararlaştırılmamışsa: kapital (anapara) faizi ve temerrüt faizi için ticari faiz uygulanır — 3095 sayılı Kanun m.1-2 ve TTK m.9 yollamasıyla. Ticari işlerde temerrüt faizinde, TCMB'nin kısa vadeli avanslar için uyguladığı oran (avans faizi) talep edilebilir (3095 m.2/2); bu oran genel temerrüt faizinden yüksekse uygulanır.
2. **Temerrüt anı:** TBK m.117 — kesin vadede vade gelmesiyle, aksi halde ihtarla temerrüt doğar. Faiz başlangıcı temerrüt tarihidir. Tacirler arası bazı işlemlerde sözleşmedeki vade yeterli olabilir.
3. **Bileşik faiz (faize faiz):** Kural yasak (TBK m.388 sınırı); ancak TTK m.8/2 — ticari işlerde, üç aydan aşağı olmamak üzere ve sözleşmede kararlaştırılmışsa cari hesap ile borçlunun her ikisi de tacir olan ödünç sözleşmelerinde bileşik faiz mümkündür. Bu istisna dar yorumlanır.
4. **İspat yükü:** Faiz talep eden işin ticari niteliğini, oran iddiasını ve temerrüt tarihini ispatlar. Karşı taraf ödeme veya faizsizlik anlaşmasını ispatlar.
5. **Ara sonuç:** Ticari iş + para borcu + temerrüt → avans faizi oranıyla temerrüt faizi; sözleşmesel oran varsa o; bileşik faiz ancak m.8/2 şartlarıyla.

## Çıktı modülleri
- Faiz türü/oran/başlangıç tarihi tablosu (dayanak: TTK m.8-9, 3095 m.2).
- Faiz hesabı için bilirkişiye yöneltilecek sorular.
- Talep sonucunda faiz fıkrası lafzı (işleyecek faiz dahil).

## Plugin bağlamı

Bu beceri `ticari-isletme-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
