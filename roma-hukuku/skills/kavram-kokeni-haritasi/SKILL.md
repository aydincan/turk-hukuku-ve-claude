---
name: kavram-kokeni-haritasi
description: "Belirli bir modern kuruma (mülkiyet, zilyetlik, sözleşme tipleri, temsil, ayni-şahsi hak) ilişkin Roma karşılığını ve dönüşümünü eşleştiren hızlı soykütüğü çıkarımı; doktrin notu veya ders materyali hazırlanırken kullanılır."
---

# Modern Kavramların Roma Soykütüğü

## Görev
Yürürlükteki Türk hukukundaki tekil bir kurumun Roma karşılığını, Latince adıyla ve dönüşüm çizgisiyle eşleştirerek hızlı bir soykütüğü kartı üretmek.

## Soğuk başlangıç (intake)
- Hangi kurum (mülkiyet, zilyetlik, kazandırıcı zamanaşımı, satış, kira, vekâlet, temsil, kefalet)?
- Latince terim ve kaynak fragman gerekli mi?
- Çıktı ders notu mu, mütalaa eki mi, akademik metin mi?

## Denetim şeması
1. Modern kurumu ve madde dayanağını sabitle (ör. mülkiyet TMK m.683; zilyetlik TMK m.973; kazandırıcı zamanaşımı TMK m.712-713; satış TBK m.207; kira TBK m.299; vekâlet TBK m.502; temsil TBK m.40).
2. Roma karşılığını eşleştir ve Latince adını ver:
   - Mülkiyet → dominium / proprietas; ayni dava → rei vindicatio.
   - Zilyetlik → possessio; possessio civilis / naturalis ayrımı.
   - Kazandırıcı zamanaşımı → usucapio (ve longi temporis praescriptio).
   - Satış → emptio venditio (consensu doğan).
   - Kira/hizmet/eser → locatio conductio (rei/operarum/operis).
   - Vekâlet → mandatum; ortaklık → societas.
   - Kefalet → fideiussio; rehin → pignus/hypotheca.
   - Temsil → Roma'da doğrudan temsil ilkesel olarak yoktu; bu farkı vurgula (modern doğrudan temsil sonraki bir gelişmedir).
3. Unsur karşılaştırması yap: Roma kurumunun şartları ile modern maddenin şartlarını yan yana koy; eklenen/çıkarılan unsuru işaretle (ör. usucapio'da iyiniyet ve haklı sebep — TMK m.712 olağan zamanaşımındaki iyiniyet ve tapu kaydı şartlarıyla kıyasla).
4. Maxim bağla (varsa, doğru Latince): nemo plus iuris ad alium transferre potest quam ipse haberet (ayni hak devri sınırı); res perit domino (hasara katlanma); prior tempore potior iure (önceki tarihli hakkın üstünlüğü). Maximin yürürlükteki maddenin yorumuna katkısını yaz, hükmün yerine koyma.
5. Ara sonuç: soykütüğü kartını netleştir; varsa anlam kayması notunu ekle.

İspat/dayanak: modern norm madde ile; Roma kurumu fragman/maxim ile; doktrin [doğrulanacak].

## Çıktı modülleri
- Soykütüğü kartı: modern kurum + madde / Roma adı (Latince) / kaynak / dönüşüm notu.
- Unsur karşılaştırma tablosu.
- İlgili Latince maxim ve doğru çevirisi.

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
