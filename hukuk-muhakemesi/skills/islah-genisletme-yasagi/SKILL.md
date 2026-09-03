---
name: islah-genisletme-yasagi
description: "Talep sonucunu, vakıaları veya tarafı sonradan değiştirmek/genişletmek gerektiğinde ıslah (HMK m.176-182), karşı tarafın muvafakati ve genişletme yasağının (m.141) sınırlarını yönetmek; özellikle belirsiz alacakta artırım stratejisi için."
---

# Islah ve İddia/Savunmanın Genişletilmesi Yasağı

## Görev
Dilekçeler aşaması kapandıktan sonra iddia/savunmayı değiştirme ihtiyacını doğru araçla (ıslah, açık muvafakat, belirsiz alacakta artırım) karşılamak; yasağa takılıp hak kaybetmeyi önlemek.

## Soğuk başlangıç (intake)
- Değiştirilmek istenen ne? (talep miktarı, vakıa, hukuki sebep, taraf?)
- Dosya hangi aşamada (dilekçeler bitti mi, tahkikat sürüyor mu)?
- Daha önce ıslah hakkı kullanıldı mı?
- Alacak belirsiz alacak davası (m.107) olarak mı açılmıştı?

## Denetim şeması
1. **Yasağın doğumu** (m.141): Taraflar, cevaba cevap ve ikinci cevap dilekçeleri ile **serbestçe**; ondan sonra **ancak karşı tarafın açık muvafakati veya ıslahla** iddia/savunmasını genişletip değiştirebilir. Ön inceleme tutanağı bu sınırı belirginleştirir.
2. **Islah** (m.176): Taraflardan her biri yapmış olduğu usul işlemlerini **kısmen veya tamamen** ıslah edebilir; aynı davada **yalnız bir kez** (m.176/2).
3. **Islahın zamanı ve kapsamı** (m.177-180): Tahkikatın sona ermesine kadar yapılır; ıslahla talep sonucu artırılabilir, dava sebebi değiştirilebilir; ancak ıslah, ıslah edilen işlemden sonrakileri geçersiz kılar (m.179).
4. **Hukuki sebepte serbestlik**: Hâkim hukuku re'sen uygular; salt **hukuki niteleme** değişikliği genişletme yasağına girmez. Yasak, **vakıa** ve **talep sonucu** içindir.
5. **Belirsiz alacak alternatifi** (m.107): Dava belirsiz alacak olarak açılmışsa, miktar belirlendiğinde **ıslaha gerek olmadan** talep artırılabilir; bu, zamanaşımı ve faiz açısından ıslaha göre daha korunaklıdır.
6. **Islah harcı**: Talep artırımında ek nispi harç tamamlanmazsa artırım sonuç doğurmaz.

Ara sonuç: "İhtiyaç ıslahla mı, muvafakatle mi, m.107 artırımıyla mı karşılanır" kararı.

## Çıktı modülleri
- Değişiklik türü–uygun araç eşlemesi.
- Islah dilekçesi iskeleti veya artırım dilekçesi (harç notlu).
- Zamanaşımı/faiz etkisi uyarısı.

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
