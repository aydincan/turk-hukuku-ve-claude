---
name: emanet-para-mali-yukumluluk
description: "Avukatın tahsil ettiği müvekkil parasını saklama ve ödeme, emanet hesabı, gecikme faizi ve güveni kötüye kullanma riski ile makbuz-serbest meslek makbuzu düzeni söz konusu olduğunda kullanılır."
---

# Müvekkil Parası, Emanet ve Mali Yükümlülükler

## Görev
Avukatın iş sahibi adına aldığı paraları yönetme, ayırma ve zamanında ödeme yükümlülüklerini
uygulamak; güveni kötüye kullanma ve disiplin riskini önlemek.

## Soğuk başlangıç (intake)
1. Avukat müvekkil adına ne tür bir para tahsil etti (icra tahsilatı, dava sonucu, emanet)?
2. Para müvekkile ne zaman, nasıl ödenecek/ödendi?
3. Avukatın bu paradan ücret/masraf mahsubu var mı; yazılı dayanağı var mı?
4. Serbest meslek makbuzu/fatura düzeni nasıl işliyor?

## Denetim şeması
1. **Ayırma ve teslim yükümü.** Avukat, iş sahibi adına aldığı paraları ve değerleri kendi
   malvarlığından ayrı tutmak ve geciktirmeden iş sahibine ödemekle yükümlüdür (Av. K. m.34;
   TBB Meslek Kuralları m.43; TBK m.508 hesap verme). Ara sonuç: para zamanında ve eksiksiz
   teslim/ayrı tutuluyor mu?
2. **Mahsup sınırı.** Avukat, kendi ücret ve masraf alacağını ancak yazılı dayanak ve
   müvekkilin bilgisi/muvafakati çerçevesinde mahsup edebilir; tek taraflı, belgesiz alıkoyma
   ihtilaf doğurur. Hapis hakkı (Av. K. m.166) sınırlı ve şartlıdır.
3. **Gecikmenin sonucu.** Geciktirilen ödeme için temerrüt faizi (TBK m.120) ve müvekkilin
   uğradığı zarar talep edilebilir.
4. **Cezai/disiplin riski.** Müvekkil parasını mal edinme güveni kötüye kullanmadır (TCK
   m.155, meslek/sanat icabı tevdi nedeniyle nitelikli hal); aynı fiil ağır disiplin suçu
   oluşturur ve meslekten çıkarmaya kadar gidebilir (Av. K. m.34, m.135). İspat: tahsilat ve
   ödeme kayıtları belirleyicidir; düzenli kasa/emanet defteri tutulması savunma değeri taşır.
5. **Belge düzeni.** Ücret için serbest meslek makbuzu düzenlenir; tahsilat-ödeme makbuzları
   dosyalanır. Eksik belge hem mali hem disiplin riskini büyütür.

## Çıktı modülleri
- Emanet/ödeme akışının uygunluk denetimi ve risk işaretleri.
- Mahsup/ödeme mutabakat tutanağı taslağı.
- Emanet kayıt ve makbuz düzeni kontrol listesi.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
