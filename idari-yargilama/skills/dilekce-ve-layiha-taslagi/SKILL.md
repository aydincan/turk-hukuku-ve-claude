---
name: dilekce-ve-layiha-taslagi
description: "İYUK'a uygun iptal/tam yargı dava dilekçesi, savunmaya cevap ve diğer layihaların hazırlanmasında kullanılır; dilekçenin zorunlu unsurları, talep sonucu ve delil bağlama disiplini gerektiğinde başvurulur."
---

# Dava Dilekçesi ve Layiha Taslağı

## Görev
İYUK m.3 ve m.5'e uygun, zorunlu unsurları eksiksiz, vakıa-hukuki sebep-talep mimarisi oturmuş bir dava dilekçesi veya layiha taslağı üretmek; bilinmeyen bilgileri [doldurulacak] yer tutucusuyla işaretlemek.

## Soğuk başlangıç (intake)
- Davacı ve davalı idare kim; işlemin tarih/sayısı nedir?
- Talep iptal mi, tam yargı mı, her ikisi mi; tazminat tutarı belirli mi?
- YD talep edilecek mi?
- Eldeki deliller (işlem örneği, tebliğ belgesi, yazışmalar) neler?

## Denetim şeması
1. **Zorunlu unsurlar** (İYUK m.3): Tarafların ad-soyad/unvan ve adresleri, davanın konusu ve sebepleri ile dayandığı deliller, dava konusu işlemin yazılı bildirim tarihi, vergi davalarında ihbarnamenin tarih ve numarası gibi bilgiler. Eksik dilekçe m.15/1-d uyarınca reddedilebilir.
2. **Aynı dilekçeyle birden çok işlem** (İYUK m.5): Aralarında maddi/hukuki bağlılık ya da sebep-sonuç ilişkisi bulunan birden fazla işlem aynı dilekçeyle dava edilebilir; birden fazla kişi müşterek dilekçeyle dava açabilir.
3. **Vakıa-hukuki sebep-talep**: Olaylar kronolojik ve sade; hukuki sebepler iptalde beş unsura, tam yargıda sorumluluk-illiyet-zarara bağlanır; talep sonucu net (işlemin iptali / belirli tutarda tazminat / YD).
4. **Delil bağlama**: Her iddianın yanına dayandığı belge eklenir; resen araştırma ilkesine güvenmeden temel belgeler sunulur. İdaredeki belgeler için mahkemeden getirtilmesi talep edilir.
5. **Islah/talep artırımı** (İYUK m.16/4): Tam yargıda bilirkişi sonrası talep ıslahla bir kez artırılabilir; dilekçede bu hak saklı tutulur.
6. **Ara sonuç — usul disiplini**: Harç, dilekçe sayısı (davalı sayısı + 1 nüsha esprisi UYAP'ta elektronik karşılığıyla) ve süre bilgileri kontrol edilir; uydurma esas/karar no'ya yer verilmez, içtihat ilkesel atıfla ve [doğrulanacak] işaretiyle anılır.

## Çıktı modülleri
- Başlık, taraflar, konu, açıklamalar, hukuki sebepler, deliller, talep sonucu bölümleriyle tam taslak
- YD talep paragrafı (gerekirse)
- Eksik bilgi/[doldurulacak] listesi ve ekler dizini

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
