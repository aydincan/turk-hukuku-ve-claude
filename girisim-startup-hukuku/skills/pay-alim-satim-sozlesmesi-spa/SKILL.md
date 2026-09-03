---
name: pay-alim-satim-sozlesmesi-spa
description: "Bir turda veya çıkışta pay devri (SPA) ya da yeni pay iştiraki (SSA) sözleşmesi hazırlanırken; satın alma fiyatı, beyan ve tekeffüller, tazminat rejimi, kapanış ön şartları ve kapanış mekaniği kurgulanırken kullanılır."
---

# Pay Alım/Satım ve İştirak Sözleşmesi (SPA/SSA)

## Görev
İşlemin kesin sözleşmesini kurmak: mevcut paylar devrediliyorsa SPA, yeni pay ihraç ediliyorsa SSA; fiyat, beyan-tekeffül, tazminat, ön şart ve kapanış mekaniğini dengeli biçimde yazmak.

## Soğuk başlangıç (intake)
1. İşlem mevcut pay devri mi (SPA), yeni pay iştiraki mi (SSA)?
2. Satın alma bedeli sabit mi; earn-out, fiyat düzeltmesi (locked box / completion accounts) var mı?
3. Beyan ve tekeffüllerin kapsamı; sınır (cap), eşik (de minimis/basket), süre?
4. Kapanış ön şartları neler (DD, onaylar, rekabet izni, üçüncü kişi onayları)?
5. İmza-kapanış aynı anda mı, araya süre mi giriyor (interim period)?

## Denetim şeması
1. Konu ve tip: Pay devri SPA — devir TTK m.490 şekli + pay defteri (m.499); yeni pay SSA — sermaye artırımına iştirak (m.456). Hangi yapı, hangi kurumsal kararı gerektirir baştan belirle.
2. Bedel ve düzeltme: Sabit bedel; locked box (referans bilanço + leakage yasağı) veya completion accounts (kapanış hesapları); earn-out hedef ve ödeme koşulları. Müzakere riski earn-out tetikleyicilerinde toplanır.
3. Beyan ve tekeffüller (R&W): Satıcının/şirketin kurumsal, IP, iş hukuku, vergi, KVKK beyanları. Bilgiye dayalı (knowledge) ve maddilik (materiality) eşikleri; açıklama mektubu (disclosure letter) ile sınırlama.
4. Tazminat (indemnity): R&W ihlalinde tazminat — TBK genel hükümleri (sözleşmeye aykırılık m.112 vd.) üzerine inşa; cap (tavan), basket/de minimis, zamanaşımı süreleri sözleşmesel. Özel tazminatlar (specific indemnity) bilinen riskler için.
5. Ön şartlar ve ara dönem: Kapanış ön şartları (rekabet izni 4054 m.7, onaylar); ara dönemde olağan işleyiş taahhüdü (conduct of business) ve MAC (material adverse change) maddesi.
6. Kapanış mekaniği: Eşzamanlı veya ertelenmiş kapanış; teslim listesi (kararlar, pay defteri kaydı, imza sirküleri, tescil); SHA ve esas sözleşmenin eş zamanlı yürürlüğü.
7. İhtilaf ve hukuk: Uygulanacak hukuk, tahkim (6325/4686) veya asliye ticaret mahkemesi (TTK m.5).
8. İspat/şekil: Yazılı; pay devri için TTK m.490 şekli; sayısal değerler [doldurulacak].

## Çıktı modülleri
- SPA/SSA iskeleti (bedel, R&W, tazminat, ön şart, kapanış).
- Beyan-tekeffül listesi ve açıklama mektubu çerçevesi.
- Kapanış teslim listesi (closing checklist).

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
