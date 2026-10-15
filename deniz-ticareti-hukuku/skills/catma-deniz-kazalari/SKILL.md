---
name: catma-deniz-kazalari
description: "İki ya da daha çok geminin çarpışması (çatma) veya başka bir deniz kazasından kaynaklanan zararlarda; kusur paylaşımını, zararın dağıtımını ve üçüncü kişilere karşı sorumluluğu belirlemek için kullan."
---

# Çatma ve Deniz Kazaları

## Görev
Çatma veya benzeri bir deniz kazasında zararın hangi gemiye/donatana yükleneceğini, kusurun nasıl paylaştırılacağını ve üçüncü kişiler (yük ve can zararı) bakımından sorumluluğun nasıl dağıtılacağını belirlemek.

## Soğuk başlangıç (intake)
- Kaç gemi karıştı; çarpışma fiziksel mi yoksa manevra/dalga etkisiyle dolaylı mı?
- Kaza anındaki seyir verileri (rota, hız, AIS/VDR kayıtları, gemi jurnali) mevcut mu?
- Kusur tek tarafta mı, karşılıklı mı, yoksa belirsiz mi; mücbir sebep iddiası var mı?
- Zarar yalnızca gemilerde mi, yoksa yük ve can zararı da var mı?

## Denetim şeması
1. **Çatma kavramı ve kapsam**: Olayın TTK m.1286 vd. anlamında çatma olup olmadığını belirle; doğrudan temas olmadan manevra/dalga etkisiyle verilen zararlar da çatma hükümlerine girebilir.
2. **Kusur tespiti ve paylaşım**: Kusursuz/mücbir sebep halinde zarara herkes kendi katlanır; tek taraf kusurluysa o donatan sorumludur; karşılıklı kusurda zarar **kusur oranına göre** paylaştırılır (TTK m.1289 vd.). Kusur oranı belirlenemezse eşit paylaşım esasını uygula.
3. **Üçüncü kişi zararları**: Yük zararlarında donatanların sorumluluğunun kusur oranıyla sınırlı (kısmi/müteselsil olmayan) niteliğini; can ve beden zararlarında ise müteselsil sorumluluk ve iç ilişkide rücu mekanizmasını ayrıştır.
4. **Kılavuz ve teknik kusur etkisi**: Zorunlu kılavuzun kusuru, geminin kendi gemi adamlarının seyir kusuru gibi hususların sorumluluğa etkisini değerlendir.
5. **İspat ve ara sonuç**: Kusur, seyir kayıtları ve bilirkişi/sörvey raporlarıyla ispatlanır; deniz raporu (gemi jurnali, kaptan ifadesi) önemli delildir. Çatmadan doğan taleplerde **iki yıllık** zamanaşımını (TTK m.1297) hesapla. Çıktıda kusur oranını ve zarar dağıtım tablosunu gerekçelendir.

## Çıktı modülleri
- Kusur oranı ve zarar dağıtım tablosu
- Delil/seyir kaydı dizini (AIS, VDR, jurnal, sörvey)
- Rücu ve sorumluluk sınırı stratejisi notu

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
