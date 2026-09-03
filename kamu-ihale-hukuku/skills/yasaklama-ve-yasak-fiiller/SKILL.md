---
name: yasaklama-ve-yasak-fiiller
description: "İhalelere katılmaktan yasaklama kararı, yasak fiil ve davranışların (m.17) tespiti, yasaklamanın kapsamı, süresi ve iptali tartışıldığında kullanılacak yaptırım becerisidir."
---

# Yasaklama Kararları ve Yasak Fiiller

## Görev
İhale sürecinde veya sözleşme aşamasında işlenen yasak fiiller nedeniyle verilen ihalelere katılmaktan yasaklama kararının hukuka uygunluğunu, kapsamını, süresini ve iptal yolunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Yasaklama hangi fiile dayanıyor: ihale sürecindeki yasak fiil (4734 m.17) mi, sözleşme ihlali (4735 m.25) mi?
2. Kararı veren idare yetkili mi; karar Resmî Gazete'de yayımlandı mı?
3. Yasaklama süresi (1-2 yıl) fiile uygun mu?
4. Yasaklamanın kapsamına giren gerçek/tüzel kişiler ve ortaklar doğru belirlenmiş mi?

## Denetim şeması
1. **Yasak fiiller (4734 m.17):** Hile, vaat, tehdit, nüfuz kullanma, rekabeti/ihale kararını etkileyecek davranış, sahte belge düzenleme, alternatif teklif verme yasağı ihlali vb. somut delille ortaya konmalıdır.
2. **Sözleşme aşaması fiilleri (4735 m.25):** Sözleşme uygulamasındaki yasak fiil ve davranışlar (taahhüdü yerine getirmeme, sahtecilik vb.) ayrı yasaklama sebebidir.
3. **Yaptırım (4734 m.58, 4735 m.26):** İlgililer hakkında bir yıldan az olmamak üzere iki yıla kadar ihalelere katılmaktan yasaklama kararı verilir; karar Resmî Gazete'de yayımlanır ve yayımdan itibaren hüküm doğurur. Yasaklama kapsamı tüzel kişide ortakları/yetkilileri de etkileyebilir.
4. **Ölçülülük ve sebep:** Fiil ile yasaklama süresi orantılı olmalı; sebep yokluğu/eksikliği veya yetki/şekil sakatlığı iptal sebebidir.
5. **İptal yolu:** Yasaklama bir idari işlemdir; 2577 sayılı İYUK'a göre yetkili idare mahkemesinde iptal davası açılır (yürütmenin durdurulması talep edilebilir). Ayrıca fiil suç teşkil ediyorsa ceza soruşturması paralel yürüyebilir.
6. **Ara sonuç:** Yasaklamanın kapsamı (kişi/süre) ve dava süresi dikkatle hesaplanır.

İspat yükü: Yasak fiili iddia eden idare somut delille ispatlar; ilgili savunma ve aksini ortaya koyar.

## Çıktı modülleri
- Fiil-yaptırım uyum (ölçülülük) değerlendirmesi.
- Yasaklama kapsamı (kişi/süre) tablosu.
- İptal davası dilekçe iskeleti ve YD talebi.

## Plugin bağlamı

Bu beceri `kamu-ihale-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
