---
name: harc-gider-ve-adli-yardim
description: "Kullanıcı dava açmanın maliyetini (harç, gider avansı, delil avansı), tutarın nasıl belirlendiğini veya ödeme gücü yoksa adli yardımdan nasıl yararlanacağını öğrenmek istediğinde kullanılır."
---

# Harç, Gider Avansı ve Adli Yardım

## Görev
Dava açma maliyetini öngörmek; harç ve avansları doğru yatırmak; ödeme gücü yetersizse adli yardım yolunu açmak.

## Soğuk başlangıç (intake)
- Davanın türü ve talep tutarı (değeri) nedir?
- Kaç tanık, kaç davalı ve tebligat söz konusu?
- Bilirkişi/keşif gerekecek mi?
- Maddi durumunuz harçları karşılamaya yeterli mi?
- İhtiyaç durumunuzu gösteren belge (gelir, mal varlığı) var mı?

## Denetim şeması
1. **Harçlar (492 sayılı Harçlar Kanunu):** Başvurma harcı (maktu) ve karar-ilam harcı alınır. Konusu para olan davalarda karar-ilam harcı nispîdir (talep edilen değer üzerinden); dörtte biri peşin yatırılır, kalanı karar sonunda. Maktu harçlı işler de vardır. Güncel tarife yıllık güncellenir — **[doğrulanacak]**.
2. **Gider avansı (HMK m.120):** Tebligat, müzekkere, tanık gibi yargılama giderleri için mahkemenin belirlediği avans peşin yatırılır; yatırılmazsa dava işleme alınmaz/usulden reddedilebilir. Miktar yıllık tarifeyle belirlenir.
3. **Delil avansı (HMK m.324):** Bilirkişi/keşif gibi delil için ilgili taraf ayrıca avans yatırır; yatırmazsa o delile dayanmaktan vazgeçmiş sayılır.
4. **Adli yardım (HMK m.334-340):** Yargılama giderlerini kısmen/tamamen karşılayamayacak ve davası açıkça dayanaktan yoksun olmayan kişi adli yardım talep edebilir; kabulde harç ve avanslardan geçici muafiyet sağlanır (m.335). Talep, asıl davanın açılacağı mahkemeye yapılır (m.336) ve ihtiyaç belgelenir.
5. **Kazanma halinde iade:** Yargılama giderleri kural olarak haksız çıkan tarafa yüklenir (HMK m.326); kazanan, yatırdığı harç ve gideri karşı taraftan tahsil edebilir.
6. **Ara sonuç:** Harç + avans hesabı yapılır; ödeme gücü yoksa adli yardım dilekçesi öne alınır.

## Çıktı modülleri
- Tahmini maliyet tablosu (başvurma harcı, peşin karar-ilam harcı, gider/delil avansı) — güncel tarife **[doğrulanacak]** notuyla.
- Adli yardım talep dilekçesi taslağı ve gereken belgeler listesi.
- Kazanma halinde gider tahsili notu.

## Plugin bağlamı

Bu beceri `kendini-temsil-asliye` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
