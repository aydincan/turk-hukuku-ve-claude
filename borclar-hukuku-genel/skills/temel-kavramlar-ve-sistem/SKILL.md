---
name: temel-kavramlar-ve-sistem
description: "Borç ilişkisinin kaynağını ve yapısını çözmek; sözleşme mi haksız fiil mi sebepsiz zenginleşme mi olduğunu ve hangi genel hükmün uygulanacağını saptamak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Borç İlişkisinin Sistematiği

## Görev
Önündeki olayda borç ilişkisinin kaynağını, taraflarını, edimin türünü ve uygulanacak genel hüküm bloğunu doğru saptamak; sonraki tüm analizin altyapısını kurmak.

## Soğuk başlangıç (intake)
- Talep neye dayanıyor: bir sözleşme mi, bir zarar mı, yoksa haksız bir malvarlığı kayması mı?
- Taraflar kim, aralarında önceden hukuki bir ilişki var mı?
- Edim ne: verme, yapma, yapmama? Para borcu mu, parça borcu mu, cins borcu mu?
- Olay ne zaman gerçekleşti (zamanaşımı ve uygulanacak kanun için)?

## Denetim şeması
1. Kaynak tespiti: TBK m.1 vd. (sözleşme), m.49 vd. (haksız fiil), m.77 vd. (sebepsiz zenginleşme). Birden çok kaynak yarışabilir; talep yarışması hâlinde lehe olan değerlendirilir.
2. Sözleşmesel ise: Borç sözleşmeden mi yoksa kanundan mı doğuyor? İsimli sözleşme varsa özel hükümlere (TBK İkinci Kısım) köprü kur; isimsiz/karma ise genel hükümler ve kıyas.
3. Edimin niteliği: Para borcu mu? (faiz, m.88, 120 ve 3095 s.K. gündeme gelir). Parça borcunda imkânsızlık riski (m.136), cins borcunda kural olarak imkânsızlık savunulamaz.
4. Borç-sorumluluk ayrımı: Borç (Schuld) var ama dava/icra edilemiyor mu (eksik borç, örn. zamanaşımına uğramış borç, kumar borcu)? TBK m.604-605.
5. İspat yükü: Hakkını dayandıran iddiasını ispatla yükümlüdür (TMK m.6). Borcun doğduğunu alacaklı, sona erdiğini/ifa edildiğini borçlu ispatlar.
6. Ara sonuç: Uygulanacak norm bloğu ve takip edilecek alt-beceri (geçerlilik, ifa, temerrüt) belirlenir.

## Çıktı modülleri
- Borç ilişkisi künyesi (kaynak, taraf, edim, muacceliyet).
- Uygulanacak madde haritası ve yönlendirilecek alt-beceri.
- İlk bakışta zamanaşımı/hak düşürücü süre uyarısı.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
