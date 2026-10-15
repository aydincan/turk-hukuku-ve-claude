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
