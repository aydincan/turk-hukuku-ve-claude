---
name: gelir-kurumlar-vergisi
description: "Gelir unsurlarının tespiti, matrah belirleme, gider-istisna-indirim denetimi ve örtülü kazanç/sermaye sorunlarını çözmek; GVK ve KVK matrah uyuşmazlıklarında kullanılır."
---

# Gelir ve Kurumlar Vergisi Uygulaması

## Görev
Gerçek kişi ya da kurum kazancının vergilendirilmesinde gelir unsurunu, matrahı, indirilebilir giderleri ve istisnaları doğru tespit ederek matrah uyuşmazlığını çözmek veya planlamayı yönlendirmek.

## Soğuk başlangıç (intake)
1. Mükellef gerçek kişi mi (GVK) yoksa kurum mu (KVK)?
2. Gelir hangi unsurdan (ticari, zirai, ücret, serbest meslek, GMSİ, MSİ, diğer kazanç)?
3. Tam mükellef mi, dar mükellef mi; çifte vergilendirme anlaşması var mı?
4. İhtilaf gider reddi, istisna, transfer fiyatlandırması veya örtülü dağıtım mı?
5. İlgili dönem ve beyan durumu nedir?

## Denetim şeması
1. **Gelir unsuru tespiti:** GVK m.2 — yedi gelir unsuru sınırlı sayıdadır; unsura giren kazanç farklı kural ve istisnalara tabidir. Önce hangi unsur olduğunu sabitle.
2. **Ticari kazançta gerçek/basit usul:** GVK m.37 vd.; kurumlarda kazanç KVK m.6 uyarınca GVK ticari kazanç hükümlerine göre tespit edilir (mali kâr = ticari kâr ± kanunen kabul edilmeyen giderler ± istisnalar).
3. **Gider denetimi:** GVK m.40 (indirilebilecek giderler) ile KKEG ayrımı; GVK m.41 ve KVK m.11 (kabul edilmeyen indirimler). Giderin işle illiyeti ve belgelendirilmesi (VUK m.227, m.229) aranır.
4. **İstisna/indirim:** KVK m.5 (iştirak kazançları, taşınmaz/iştirak satış istisnası), KVK m.10 indirimler; GVK istisnaları. İstisna iddiasının ispatı mükelleftedir.
5. **Örtülü sermaye ve örtülü kazanç:** KVK m.12 (örtülü sermaye — borç/özkaynak oranı), KVK m.13 (transfer fiyatlandırması yoluyla örtülü kazanç dağıtımı — emsallere uygunluk). İlişkili kişi ve emsal analizi yap. Ara sonuç: matrah farkı hangi kalemden ve hangi tutarda?
6. **Stopaj ilişkisi:** Bazı ödemelerde GVK m.94 / KVK m.15, m.30 tevkifatı; sorumlu sıfatıyla ödeme yükümlülüğünü kontrol et.

## Çıktı modülleri
- Gelir unsuru ve matrah hesap tablosu (ticari kâr → mali kâr köprüsü).
- Gider/istisna kabul-ret listesi (madde dayanağı ve belge durumu).
- Transfer fiyatlandırması/örtülü sermaye risk notu.
- Beyan düzeltme veya dava argümanı taslağı.

## Plugin bağlamı

Bu beceri `vergi-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
