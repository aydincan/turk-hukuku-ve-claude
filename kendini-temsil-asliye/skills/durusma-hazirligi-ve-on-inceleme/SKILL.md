---
name: durusma-hazirligi-ve-on-inceleme
description: "Duruşmaya kendisi katılacak taraf ön inceleme ve tahkikat duruşmasına nasıl hazırlanacağını, ne söyleyeceğini, hangi belgeleri götüreceğini ve davranış kurallarını öğrenmek istediğinde kullanılır."
---

# Duruşma Hazırlığı ve Ön İnceleme

## Görev
Tarafı duruşmaya hazır göndermek: ön incelemenin işlevini anlatmak, sulh ihtimalini değerlendirmek, savunma ve soru notlarını hazırlamak.

## Soğuk başlangıç (intake)
- Duruşma türü nedir (ön inceleme, tahkikat, sözlü yargılama)?
- Duruşma günü ve mahkeme bilgisi nedir?
- Tarafların üzerinde anlaştığı ve çekiştiği hususlar neler?
- Dinletmek istediğiniz tanık var mı, geldi mi?
- Sulh/uzlaşma ihtimaliniz var mı, sınırınız nedir?

## Denetim şeması
1. **Ön inceleme (HMK m.137-142):** Mahkeme önce dava şartları ve ilk itirazları inceler; sonra tarafların **anlaştığı ve anlaşamadığı hususları** tespit eder (m.140) ve tarafları sulhe/arabuluculuğa teşvik eder. Bu duruşma kritiktir; uyuşmazlığın çerçevesi burada çizilir.
2. **İddia/savunmanın genişletilmesi (m.141):** Ön inceleme duruşmasında, karşı taraf muvafakat etmedikçe veya ıslah yoluyla olmadıkça yeni iddia/savunma serbestçe eklenemez. Bu nedenle eksik kalan bir husus varsa bu aşama son fırsattır.
3. **Tahkikat:** Deliller toplanır; tanıklar dinlenir, bilirkişi raporu tartışılır. Taraf, tanığa sorulmasını istediği soruları ve rapora itirazlarını hazırlar.
4. **Usul disiplini:** Duruşmaya zamanında gidilir; mazeretsiz gelinmezse dosya işlemden kalkabilir veya yokluğunda karar verilebilir (HMK m.150). Söz hâkim tarafından verilir; saygı kurallarına uyulur.
5. **Sözlü yargılama:** Tahkikat bitince taraflar son sözlerini sunar; talep özetle yinelenir.
6. **Ara sonuç:** Anlaşılan/anlaşılamayan hususlar listesi + delil durumu + sulh sınırı netse taraf duruşmaya hazırdır.

## Çıktı modülleri
- Duruşma hazırlık notu (anlaşma/çekişme listesi, talep özeti).
- Tanığa soru taslağı ve rapora itiraz başlıkları.
- Duruşma davranış ve evrak kontrol listesi.

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
