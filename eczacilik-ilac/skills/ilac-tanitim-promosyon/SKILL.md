---
name: ilac-tanitim-promosyon
description: "Reçeteli ilacın halka tanıtım yasağı, ürün tanıtım temsilcileri, bilimsel toplantı ve promosyon kuralları ile TİTCK idari yaptırımlarına ilişkin uyuşmazlıklarda kullanılır."
---

# İlaç Tanıtımı ve Promosyon Kuralları

## Görev
Bir tanıtım faaliyetinin (UTT ziyareti, bilimsel toplantı, dijital içerik, numune, değer aktarımı) Beşeri Tıbbi Ürünlerin Tanıtım Faaliyetleri Yönetmeliği’ne uygunluğunu denetlemek ve idari yaptırıma karşı savunma kurmak.

## Soğuk başlangıç (intake)
- Tanıtım kime yönelik: sağlık meslek mensubu mu, halk mı (reçeteli üründe halka tanıtım yasaktır)?
- Faaliyet türü: UTT ziyareti, toplantı sponsorluğu, numune dağıtımı, dijital/sosyal medya, değer aktarımı?
- TİTCK denetim tutanağı/yaptırımı var mı; gerekçesi nedir?
- İçerik onaylı KÜB/KT ile uyumlu mu, endikasyon dışı vurgu var mı?

## Denetim şeması
1. **Dayanak.** Beşeri Tıbbi Ürünlerin Tanıtım Faaliyetleri Hakkında Yönetmelik (2015) ve TİTCK kılavuzları; reçeteli ürünün halka tanıtımı 1262 ve Yönetmelikle yasaktır.
2. **Hedef kitle kapısı.** Reçeteli ürün → yalnızca sağlık meslek mensubuna; reçetesiz (OTC) için sınırlı koşullar. Ara sonuç: faaliyet yasak kitleye mi ulaştı?
3. **İçerik denetimi.** Tanıtım onaylı Kısa Ürün Bilgisi (KÜB) ile uyumlu, dengeli, abartısız olmalı; endikasyon dışı kullanım teşviki yasak. Değer aktarımı şeffaflık kurallarına tabi.
4. **Yaptırım ve yol.** İhlalde TİTCK idari yaptırım (uyarı, tanıtım durdurma, idari para cezası) uygular; bu birel idari işlemdir → idari yargı, İYUK m.7 (60 gün). İdari para cezasının özel kanun mu 5326 mı çerçevesinde olduğu kontrol edilir. İspat: ihlali idare tutanakla; aykırılığın yokluğunu/ölçüsüzlüğü davacı gösterir.
5. **Uyum boyutu.** İleriye dönük: SOP, onay akışı, materyal arşivi, değer aktarımı kaydı.

## Çıktı modülleri
- Tanıtım materyali/uygulama uyum kontrol listesi.
- İdari yaptırıma karşı iptal dilekçesi iskeleti [doldurulacak].
- Uyum programı (onay akışı, arşiv, eğitim) önerisi.

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
