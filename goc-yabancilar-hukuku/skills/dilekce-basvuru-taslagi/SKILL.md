---
name: dilekce-basvuru-taslagi
description: "İkamet/çalışma/vatandaşlık başvuru dilekçesi, idari itiraz veya iptal dava dilekçesi hazırlanacağında; yer tutucu disiplini ve doğru madde atıflarıyla taslak üretmek için kullanılır."
---

# Dilekçe ve Başvuru Taslağı

## Görev
Göç ve yabancılar alanında idari başvuru, idari itiraz ve idari dava dilekçelerini doğru biçim, madde atfı ve yer tutucu disipliniyle üretmek; her belgenin makamına ve süresine uygun olmasını sağlamak.

## Soğuk başlangıç (intake)
1. Hangi belge hazırlanacak (başvuru, uzatma, itiraz, iptal davası dilekçesi)?
2. Muhatap makam kim (Göç İdaresi il müdürlüğü, Bakanlık, Komisyon, idare mahkemesi)?
3. Eldeki belgeler ve dayanılacak vakıalar nelerdir?
4. Süre durumu nedir (son gün)?

## Denetim şeması
1. **Belge-makam eşleşmesi**: Başvuru/uzatma → Göç İdaresi/Bakanlık; ret kararına itiraz → öngörülmüşse ilgili komisyon; iptal davası → idare mahkemesi (İYUK m.3'teki dilekçe unsurları); idari gözetim itirazı → sulh ceza hâkimliği.
2. **İdari dava dilekçesi unsurları**: İYUK m.3 — tarafların kimliği, dava konusu işlem ve tebliğ tarihi, açıklama (vakıalar), hukuki sebepler, deliller, sonuç-talep ve YD talebi. Sınır dışı/gözetimde aciliyet vurgusu.
3. **Madde atıf disiplini**: Talep YUKK/6735/5901'in ilgili maddesine; geri gönderme yasağı için m.4/m.55 ve AİHS m.3'e; usul için İYUK m.2/7/27'ye bağlanır.
4. **Yer tutucu disiplini**: Bilinmeyen tarih, sayı, ad ve tutar `[doldurulacak]` ile işaretlenir; uydurma karar/işlem numarası yazılmaz. İçtihat ihtiyacı varsa ilkesel atıf + `[doğrulanacak]`.
**Ara sonuç**: Eksiksiz, makamına ve süresine uygun, doğrulanabilir kaynaklı bir taslak.

## Çıktı modülleri
- Hedef belgenin tam taslağı (başlık, taraf, vakıa, hukuki sebep, talep).
- Ek belge/delil listesi ve sunulacak suret sayısı notu.
- İmza-tebliğ-harç ve son gün hatırlatması.

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
