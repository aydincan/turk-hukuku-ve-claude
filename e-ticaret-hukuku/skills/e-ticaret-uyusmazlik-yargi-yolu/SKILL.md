---
name: e-ticaret-uyusmazlik-yargi-yolu
description: "E-ticaret uyuşmazlığında hangi merciye başvurulacağını (Tüketici Hakem Heyeti, tüketici mahkemesi, asliye ticaret, idari yargı, KVKK Kurulu) ve görev-yetki kurallarını belirlemek gerektiğinde kullanılır."
---

# Uyuşmazlık Çözümü ve Görev-Yetki

## Görev
E-ticaret uyuşmazlığının niteliğine göre doğru çözüm merciini ve görev-yetki kurallarını belirlemek; gerekli ön şartları (dava şartı arabuluculuk, parasal sınır) tespit etmek.

## Soğuk başlangıç (intake)
- Taraflar tüketici-satıcı mı, iki tacir mi, vatandaş-idare mi?
- Uyuşmazlık değeri yaklaşık ne kadar?
- Konu sözleşme/iade mi, ticari ileti yaptırımı mı, veri ihlali mi, içerik mi?
- Daha önce bir başvuru/şikâyet yapıldı mı?

## Denetim şeması
1. Tüketici uyuşmazlıkları (6502): tüketici işlemlerinde parasal sınır altındaki uyuşmazlıklar Tüketici Hakem Heyeti'ne (zorunlu), üzeri Tüketici Mahkemesi'ne gider; sınır her yıl güncellenir. Tüketici davalarında dava şartı arabuluculuk öngörülen hallerde uygulanır.
2. Ticari uyuşmazlıklar (B2B): tacirler arası e-ticaret sözleşmeleri ve haksız rekabet (TTK m.54-55) Asliye Ticaret Mahkemesi'nde; ticari davalarda dava şartı arabuluculuk (TTK m.5/A) uygulanır.
3. İdari yaptırım: 6563 m.12 idari para cezalarına ve Bakanlık işlemlerine karşı 2577 sayılı İYUK kapsamında idari yargı (idare mahkemesi); süre ve dava şartlarına dikkat edilir.
4. Kişisel veri: KVKK ihlallerinde ilgili kişi başvurusu ve KVK Kurulu şikâyeti (6698 m.13-15); Kurul kararına karşı idari yargı yolu açıktır.
5. İçerik/erişim: 5651 kapsamında erişim engelleme ve içerik kaldırma talepleri Sulh Ceza Hâkimliği veya ilgili usule göre yürütülür.
Yetki: HMK genel yetki kuralları + tüketici lehine yerleşim yeri mahkemesi seçeneği; sözleşmedeki yetki şartının tüketiciye karşı geçerliliği denetlenir.
Ara sonuç: mercii + ön şart + süre listesi.

## Çıktı modülleri
- Görev-yetki ve mercii kararı tablosu.
- Dava şartı (arabuluculuk/parasal sınır) kontrolü.
- Başvuru sırası ve süre takvimi.

## Plugin bağlamı

Bu beceri `e-ticaret-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
