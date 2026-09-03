---
name: temel-kavramlar-ve-sistem
description: "Yabancının statüsünü (vize, ikamet, koruma, çalışma, düzensiz göçmen) belirleyip hangi rejim ve makamın uygulanacağını saptamak gerektiğinde; göç hukukunun temel kavram ve kurum haritasına ihtiyaç duyulduğunda kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Somut olayda yabancının hukuki statüsünü doğru sınıflandırmak, uygulanacak normu (6458 YUKK, 6735 İşgücü K., 5901 Vatandaşlık K.) ve yetkili makamı belirlemek; sonraki tüm işlemlerin dayanacağı statü zeminini kurmak.

## Soğuk başlangıç (intake)
1. Yabancının uyruğu ve Türkiye'ye giriş şekli/tarihi nedir (vizeli, vizesiz, düzensiz)?
2. Hâlihazırda geçerli bir ikamet izni, çalışma izni veya koruma kaydı var mı; varsa türü ve bitiş tarihi?
3. Eline tebliğ edilen bir idari işlem (ikamet ret, sınır dışı, gözetim, çalışma izni ret) var mı, tarihi?
4. Talep nedir: kalışın düzenlenmesi, çalışma, koruma, uzaklaştırmaya itiraz, vatandaşlık?

## Denetim şeması
1. **Giriş ve vize ekseni**: YUKK m.11-17. Vize muafiyeti, vize ihlali, giriş yasağı (m.9) kontrol edilir.
2. **Yasal kalış ekseni**: İkamet izni türü ayrımı — kısa dönem (m.31), aile (m.34), öğrenci (m.38), uzun dönem (m.42), insani (m.46), insan ticareti mağduru (m.48). Hangi türün şartlarını taşıdığı belirlenir; uzun dönem için kesintisiz 8 yıl ikamet (m.42/1) gibi eşikler değerlendirilir.
3. **Koruma ekseni**: Uluslararası koruma (mülteci m.61, şartlı mülteci m.62, ikincil koruma m.63) ile geçici koruma (Geçici Koruma Yönetmeliği) ayrılır. Bu eksende olan yabancı için ikamet/sınır dışı rejimi farklı işler.
4. **Çalışma ekseni**: 6735 m.6 vd. — çalışma izni ikamet yerine geçer mi (m.13), kim başvurabilir.
5. **Düzensizlik ve yaptırım ekseni**: Statüsüz kalış sınır dışı (m.52) ve gözetim (m.57) riski doğurur; geri gönderme yasağı (m.4, m.55) süzgeci uygulanır.
**Ara sonuç**: Yabancı tek bir eksene yerleştirilir; çoklu statü çatışması varsa lehe olan ve aktif koruma sağlayan statü esas alınır.

## Çıktı modülleri
- Statü tespit tablosu (eksen, dayanak madde, geçerlilik, riskler).
- Yetkili makam ve yargı mercii haritası.
- Bir sonraki adım önerisi ve yönlendirilecek uzman beceri.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
