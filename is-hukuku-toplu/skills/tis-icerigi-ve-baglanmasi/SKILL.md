---
name: tis-icerigi-ve-baglanmasi
description: "Toplu is sozlesmesinin normatif ve borc dogurucu hukumlerini, suresini, duzeyini, yararlanma-dayanisma aidati rejimini ve sozlesmenin sona ermesini ele alir; TIS metni hazirlama, yorumlama veya uygulama sorunlarinda kullanilir."
---

# TİS İçeriği, Düzeyi ve Bağıtlanması

## Görev
TİS'in hukuki yapısını çözümlemek: hangi hükümler normatif (iş sözleşmesine doğrudan etki eden), hangileri borç doğurucu (taraflar arası); yararlanma rejimi, süre ve sona erme. TİS metni okuma, kaleme alma ve yorumlama işidir.

## Soğuk başlangıç (intake)
- Hangi düzeyde TİS (işyeri/işletme/grup)?
- TİS imzalandı mı, süresi ve yürürlük tarihi nedir?
- Talepte bulunan işçi sendika üyesi mi, değilse dayanışma aidatı ödüyor mu?
- Sorun bir hükmün yorumu mu yoksa boşluğu mu?

## Denetim şeması
1. **TİS'in niteliği:** 6356 m.36 — TİS'in **normatif hükümleri** (ücret, ikramiye, çalışma süreleri) iş sözleşmesinin yerini alır, doğrudan ve emredici etki gösterir; **borç doğurucu hükümler** sadece tarafları bağlar.
2. **Art etki (ardçıl etki):** 6356 m.36/2 — TİS sona erse de, yeni TİS yapılana kadar normatif hükümler iş sözleşmesi hükmü olarak devam eder.
3. **Düzey kuralı:** 6356 m.34 — bir işyerinde aynı dönem için yalnızca bir TİS uygulanabilir; işletme düzeyinde toplu sözleşme bütünlüğü esastır.
4. **Süre:** 6356 m.35 — TİS en az **1**, en çok **3** yıl süreli yapılır; süre sonradan değiştirilemez (faaliyet/işletme TİS'lerinde özel istisnalar saklı).
5. **Yararlanma:** 6356 m.39 — kural olarak TİS'ten taraf işçi sendikasının üyeleri yararlanır. Üye olmayanlar **dayanışma aidatı** ödeyerek yararlanabilir; üyelikten farklı olarak grev kararına katılma gibi sonuçlar doğmaz.
6. **Teşmil:** 6356 m.40 — Cumhurbaşkanı, bir işkolundaki TİS'i o işkolundaki üye olmayan işyerlerine teşmil edebilir (sınırlı, istisnai yol).

Ara sonuç: Sorun normatif hükmün uygulanması ise hak uyuşmazlığı → yargı; metin oluşturma ise pazarlık/taslak çalışması yapılır.

## Çıktı modülleri
- TİS hüküm ayrıştırması (normatif / borç doğurucu).
- Yararlanma ve dayanışma aidatı değerlendirmesi.
- Taslak madde önerileri ([doldurulacak] yer tutucularıyla).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
