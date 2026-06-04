---
name: layiha-mimarisi-ve-secim
description: "Hangi yargı kolunda hangi dilekçe türünün yazılacağını saptamak, doğru iskeleti (HMK/İYUK/CMK) kurmak ve vakıa-hukuki sebep-talep sonucu omurgasını oturtmak gerektiğinde kullanılır."
---

# Layiha Mimarisi ve Dilekçe Türü Seçimi

## Görev
Somut talebe uygun yargı kolunu ve dilekçe türünü belirlemek; doğru biçim iskeletini seçip vakıa-hukuki sebep-talep sonucu omurgasını kurmak. Yanlış iskelet, baştan usulden ret veya hak kaybı doğurur; bu beceri tüm atölyenin giriş kapısıdır.

## Soğuk başlangıç (intake)
- Uyuşmazlık özel hukuk mu, idari mi, cezai mı? (taraflardan biri kamu idaresi mi?)
- İlk dilekçe mi, cevap/replik mi, yoksa kanun yolu (istinaf/temyiz) dilekçesi mi?
- Hak düşürücü süre veya dava açma süresi işliyor mu, son gün ne?
- Talep para alacağı mı, tespit mi, iptal mi, eda mı?

## Denetim şeması
1. Yargı kolu tespiti: Taraflardan biri idare ve uyuşmazlık idari işlem/eylemden doğuyorsa İYUK (2577) iskeleti. Suç isnadı varsa CMK (5271). Aksi halde HMK (6100). Karma durumlarda (ör. idari para cezasına itiraz) özel kanun yolunu kontrol edin (Kabahatler K. m.27 — sulh ceza hâkimliği).
2. Dilekçe türü: İlk dava (HMK m.119 / İYUK m.3), cevap (HMK m.126-129), replik-düplik (m.136), istinaf (HMK m.342 / İYUK m.45), temyiz (HMK m.361 / İYUK m.46).
3. İskelet seçimi: HMK m.119 zorunlu unsurları başlık olarak yerleştirin; idari dilekçede İYUK m.3 unsurları (idarenin işlemi, tarihi, tebliğ tarihi) eklenir.
4. Omurga: Vakıalar (numaralı, kronolojik) → her vakıaya delil → hukuki sebep (altlama) → talep sonucu. Ara sonuç: omurga eksiksizse türe özgü beceriye devredin.
5. İspat yükü ön kontrolü (HMK m.190): iddia eden ispatla yükümlüdür; vakıaları bu yüke göre seçin.

## Çıktı modülleri
- Yargı kolu + dilekçe türü kararı (gerekçeli, bir paragraf)
- Seçilen iskeletin başlık listesi (madde atıflı)
- Doldurulması gereken zorunlu unsur kontrol listesi
- İlgili türe özgü beceriye yönlendirme notu

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
