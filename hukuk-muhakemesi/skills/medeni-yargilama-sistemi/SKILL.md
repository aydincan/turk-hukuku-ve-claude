---
name: medeni-yargilama-sistemi
description: "Bir hukuk davasının HMK'daki bütün iskeletini (yargı yolu, dava şartı, dilekçeler, ön inceleme, tahkikat, hüküm, kanun yolu) tanımak ve dosyayı doğru aşamaya yerleştirmek gerektiğinde; usulün hangi adımında olunduğu belirsizse başvurulur."
---

# Medeni Yargılama Sistematiği ve Aşamalar

## Görev
Bir hukuk uyuşmazlığını 6100 sayılı HMK'nın aşamalı yargılama mimarisine oturtmak; dosyanın hangi aşamada olduğunu, sıradaki adımı ve o adımdaki usuli imkân/kısıtları belirlemek.

## Soğuk başlangıç (intake)
- Talep maddi hukukta ne? (alacak, tazminat, tespit, tescil, men, terditli mi?)
- Dosya hangi aşamada? (dilekçeler / ön inceleme / tahkikat / hüküm / kanun yolu)
- Yargılama usulü hangisi? (yazılı m.118 vd. mı, basit m.316 vd. mı?)
- Dava şartı arabuluculuk kapsamında mı, son tutanak var mı?

## Denetim şeması
1. **Yargı yolu**: Uyuşmazlık adli yargıda mı? İdari/ceza/özel mahkeme görevi dışlanır mı? (HMK m.114/1-b dava şartı).
2. **Usul tipi**: Basit yargılamada (m.316-322) cevap süresi iki hafta (m.317), delillerin dilekçeyle sunulması ve ön inceleme + tahkikatın bütünleşmesi; yazılıda dört aşama ayrı işler.
3. **Dilekçeler aşaması**: Dava dilekçesi (m.119) → cevap (m.126-129, süre m.127) → cevaba cevap/ikinci cevap (m.136). Bu aşama bitince iddia/savunma genişletme yasağı (m.141) doğar.
4. **Ön inceleme** (m.137-142): Dava şartları ve ilk itirazlar (m.116) incelenir; uyuşmazlık konuları tespit edilir; sulh teşviki; deliller bağlanır; tutanak (m.140) düzenlenir. Tutanak yargılamanın çerçevesini dondurur.
5. **Tahkikat** (m.143 vd.): Bağlanan deliller toplanır, tanık-bilirkişi-keşif icra edilir; ispat yükü dağılımına göre ilerlenir.
6. **Sözlü yargılama ve hüküm** (m.184-186, m.294 vd.): Gerekçeli karar (m.297) yazılır; hüküm fıkrası talep sonucuyla örtüşmeli.
7. **Kanun yolu**: İstinaf iki hafta (m.345), temyiz iki hafta (m.361); kesinlik (parasal had) yıllık tarifeden teyit edilir.

Ara sonuç: Her aşama geçişinde bir hak/yasak doğar; özellikle ön inceleme tutanağı sonrası genişletme yasağı en sık hak kaybı noktasıdır.

## Çıktı modülleri
- Aşama tespit tablosu (mevcut aşama, tamamlanan/eksik işlemler).
- Sıradaki adım ve son işlem tarihi/süre uyarısı.
- Usuli risk notu (genişletme yasağı, ıslah ihtiyacı, eksik delil bağlama).

## Plugin bağlamı

Bu beceri `hukuk-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
