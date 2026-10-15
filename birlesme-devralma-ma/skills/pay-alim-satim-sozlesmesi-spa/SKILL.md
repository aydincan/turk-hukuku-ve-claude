---
name: pay-alim-satim-sozlesmesi-spa
description: "Pay veya varlık devri için SPA taslağını kurmak, bedel mekaniği, kapanış öncesi ve sonrası taahhütler, beyan-tekeffül ve tazminat mimarisini madde madde tasarlamak için kullanılır."
---

# Pay Alım Satım Sözleşmesi (SPA) Tasarımı

## Görev
TBK temelinde, işlem yapısına uygun bir SPA iskeleti kurmak; bedel, kapanış, beyan-tekeffül ve tazminat hükümlerini dengeli biçimde tasarlamak.

## Soğuk başlangıç (intake)
- Müvekkil alıcı mı satıcı mı; pazarlık gücü nasıl?
- Bedel sabit mi, kapanış bilançosuna göre düzeltmeli mi (locked-box / completion accounts)?
- Earn-out, escrow veya vadeli ödeme var mı?
- Tabi hukuk Türk hukuku mu, uyuşmazlık tahkim mi mahkeme mi?

## Denetim şeması
1. **Konu ve devir taahhüdü**: Devredilen pay/varlığın tanımı, mülkiyetin geçiş anı, pay defteri kaydı taahhüdü (TTK m.499).
2. **Bedel ve düzeltme**: Sabit bedel veya kapanış hesaplarına göre düzeltme; earn-out formülü ve ölçüm; escrow ile teminat. TBK m.207 vd. satış hükümleri kıyasen.
3. **Kapanış öncesi taahhütler (covenants)**: İmza-kapanış arası olağan işletme yürütümü, negatif taahhütler, CP'lerin sağlanması (rekabet/sektörel izin).
4. **Kapanış mekaniği (closing)**: Eş zamanlı teslim edilecek belgeler, ödeme, pay devri işlemleri; eksik kapanış halinde sonuçlar.
5. **MAC klozu**: Önemli olumsuz değişiklik halinde kapanıştan dönme hakkı.
6. **Tazminat rejimi**: Beyan-tekeffül ihlalinde TBK m.112 vd. çerçevesinde tazminat; cezai şart eklenirse TBK m.179-182 ve hâkimin indirim yetkisi (TBK m.182/3) gözetilir.
7. **İspat yükü**: İhlali ve zararı ileri süren taraf ispatlar (TMK m.6, HMK m.190).
8. **Ara sonuç**: Risk dağılımı (cap, basket, sandbagging) müvekkilin tarafına göre ayarlanır.

## Çıktı modülleri
- SPA madde başlıkları iskeleti ([doldurulacak] yer tutucularla)
- Bedel/earn-out/escrow mekaniği şeması
- CP ve closing deliverables listesi
- Müzakere notu (asimetrik/riskli klozlar)

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
