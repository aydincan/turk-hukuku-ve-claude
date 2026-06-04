---
name: denetimli-serbestlik
description: "Açık kurumdan denetimli serbestliğe ayrılma, denetim yükümlülükleri, elektronik izleme ve yükümlülük ihlali sonuçlarını değerlendirmek gerektiğinde kullanılır."
---

# Denetimli Serbestlik Tedbirleri ve Yükümlülükler

## Görev
Hükümlünün denetimli serbestlik tedbiriyle cezasını toplum içinde infaz etme imkânını, yükümlülüklerini ve ihlal hâlinde dönüş rejimini 5275 m.105/A ekseninde değerlendirmek.

## Soğuk başlangıç (intake)
- Hükümlü açık kuruma ayrıldı mı; koşullu salıverilmeye ne kadar süre kaldı?
- Daha önce açık kurumdan firar/disiplin sorunu var mı?
- Hangi yükümlülükler öngörülecek (imza, program, elektronik kelepçe)?
- İş/sağlık/eğitim durumu yükümlülük tasarımını etkiliyor mu?

## Denetim şeması
1. Ayrılma şartı: 5275 m.105/A uyarınca açık ceza infaz kurumunda bulunan veya bu kuruma ayrılma şartlarını taşıyan, koşullu salıverilmesine kanunda belirtilen süre kalan iyi hâlli hükümlü denetimli serbestlikten yararlanabilir. Geçici düzenlemelerin süre farkları kontrol edilir. Ara sonuç: uygunluk.
2. Yükümlülükler: denetimli serbestlik müdürlüğünce belirlenen rapor verme, belirli yerlere gitmeme, programlara katılma; uygun hâllerde elektronik izleme (Elektronik Kelepçe). Yükümlülükler 5275 ve Denetimli Serbestlik Hizmetleri Yönetmeliği çerçevesindedir.
3. İhlal sonucu: yükümlülüklere aykırılık veya kasıtlı yeni suç hâlinde tedbir kaldırılır, hükümlü kapalı kuruma iade edilir ve bakiye ceza kurumda çekilir (5275 m.105/A). İspat: ihlal tutanağı denetimli serbestlik müdürlüğünce düzenlenir.
4. Özel gruplar: hamile, ağır hastalık, yaşlılık ve maktu sürelerde özel kolaylıklar; bunlar ayrıca incelenir.
5. İtiraz: müdürlük işlemine/iade kararına karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr üzerinden, künye `[doğrulanacak]`.
6. Ara sonuç: yararlanma uygunluğu + yükümlülük seti + ihlal riski.

## Çıktı modülleri
- Uygunluk ve süre tablosu.
- Yükümlülük listesi ve ihlal sonuç notu.
- İade kararına itiraz tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
