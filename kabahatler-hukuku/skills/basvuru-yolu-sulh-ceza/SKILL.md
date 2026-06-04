---
name: basvuru-yolu-sulh-ceza
description: "İdari yaptırım kararına karşı sulh ceza hâkimliğine başvuru ve itiraz yolunun usulünü, sürelerini, görev-yetkisini ve karar türlerini yönetmek; başvuru/itiraz dilekçesinin yol haritasını kurmak gerektiğinde kullanılır."
---

# Sulh Ceza Hâkimliğine Başvuru ve İtiraz

## Görev
İdari yaptırım kararına karşı 5326 m.27-29 usulünü işletmek: doğru merci, süre, dilekçe içeriği ve itiraz yolunu belirlemek.

## Soğuk başlangıç (intake)
- Yaptırım kararı ne zaman tebliğ/tefhim edildi (süre başlangıcı)?
- Kararı veren idare ve kararın bulunduğu yer neresi (yetkili hâkimlik)?
- Karar yalnızca idari para cezası mı, yoksa idari yargının görev alanına giren bir işlemle birlikte mi verildi?
- Daha önce idareye itiraz/başvuru yapıldı mı?

## Denetim şeması
1. **Görevli merci:** İdari yaptırım kararına karşı kural olarak **sulh ceza hâkimliği** görevlidir (5326 m.27/1). İstisna: yaptırım, idari yargının görev alanına giren bir işlemin parçasıysa idari yargı görevlidir (m.27/8). Bu ayrımı en baştan netleştir.
2. **Yetkili hâkimlik:** Yaptırım kararını veren idarenin bulunduğu yer sulh ceza hâkimliği (m.27/1).
3. **Süre:** Kararın tebliği/tefhiminden itibaren **15 gün** içinde başvuru (m.27/1). Süre hak düşürücüdür; mücbir sebep halinde m.27/2'deki imkân değerlendirilir.
4. **Başvuru dilekçesi:** Kabahatin sübutuna, kusura, miktara, yetki/şekil sakatlığına ve zamanaşımına ilişkin somut iddialar; deliller ve tanık listesi. Harç/masraf rejimi kontrol edilir.
5. **İnceleme ve karar:** Hâkimlik dosya üzerinden veya duruşmalı inceleyebilir; başvurunun kabulü (kararın kaldırılması/değiştirilmesi) ya da reddine karar verir (m.28).
6. **İtiraz (m.29):** Hâkimlik kararına karşı, belirli ceza eşiklerinde, tebliğden itibaren **7 gün** içinde bir başka (numara olarak izleyen) sulh ceza hâkimliğine itiraz; itiraz mercii kararı kesindir. Eşik altı cezalarda hâkimlik kararı kesin olabilir; tutar eşiğini kontrol et.

İspat yükü idarede; başvurucu sakatlık ve çürütücü delilleri ileri sürer.

## Çıktı modülleri
- Süre ve merci tespit kartı.
- Başvuru dilekçesi iskeleti (talep sonucu + gerekçe + deliller).
- İtiraz yolu/eşik kontrol listesi.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
