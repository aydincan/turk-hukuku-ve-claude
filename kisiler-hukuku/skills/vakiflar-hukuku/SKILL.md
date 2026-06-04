---
name: vakiflar-hukuku
description: "Yeni (yerleşik) bir vakfın kurulması, vakıf senedinin hazırlanması, tescil/teftiş süreçleri ya da vakfın amacının/mallarının değiştirilmesi sorunları için kullanılır."
---

# Vakıflar Hukuku (Kuruluş, Tescil, Amaca Tahsis)

## Görev
Bir vakfın kuruluşunu TMK m.101-117 ve 5737 sayılı Vakıflar Kanunu çerçevesinde kurmak/denetlemek: vakıf senedi, mal tahsisi, tescil ve amaç/yönetim değişikliği taleplerini doğru usulle yapılandırmak.

## Soğuk başlangıç (intake)
- Vakfın amacı belirli ve sürekli mi; kanunun yasakladığı bir amaç taşıyor mu?
- Amaca özgülenen (tahsis edilen) malvarlığı amacı gerçekleştirmeye yeterli mi?
- Kuruluş resmî senetle/ölüme bağlı tasarrufla mı yapılıyor?
- Talep yeni kuruluş mu, yoksa mevcut vakıfta amaç/yönetim/mal değişikliği mi?

## Denetim şeması
1. **Kuruluş ve amaç** — TMK m.101: vakıf, kişilerin belirli ve sürekli bir amaca özgüledikleri yeterli mal ve hakların topluluğudur. Üyesi olmaz. Cumhuriyetin niteliklerine, kanuna/ahlaka aykırı, siyasi/ırk-cemaat esasına dayalı veya belli bir ırkın/cemaatin desteklenmesi amacıyla vakıf kurulamaz (m.101/son).
2. **Vakıf senedi** — TMK m.102: kuruluş, resmî senetle veya ölüme bağlı tasarrufla yapılır. Senet; vakfın amacını, özgülenen mal ve hakları, organlarını ve yerleşim yerini gösterir; eksiklik mahkemece tamamlattırılabilir.
3. **Tescil** — TMK m.102-104: vakfın yerleşim yeri asliye hukuk mahkemesine başvurularak tescil istenir; mahkeme, Vakıflar Genel Müdürlüğü'nün görüşünü alır ve tescile karar verir; vakıf, mahkeme siciline tescille tüzel kişilik kazanır, ayrıca merkezi sicile kaydolunur.
4. **Mal tahsisi** — Özgülenen malların mülkiyeti tescille vakfa geçer (m.101/3); amaca yeterlilik denetlenir.
5. **Değişiklik ve denetim** — TMK m.112-113: amacın değiştirilmesi/genişletilmesi ancak özgülenme amacının değişen koşullar altında gerçekleşmesine imkân kalmaması gibi hâllerde, vakıf yönetiminin başvurusu ve denetim makamının görüşüyle mahkeme kararıyla olur. Vakıflar Genel Müdürlüğü teftiş ve gözetim yetkisine sahiptir (5737 SK).
6. **Sona erme** — TMK m.116: amacın gerçekleşmesi imkânsızlaşır ve değiştirilemezse vakıf kendiliğinden sona erer; mahkeme kararıyla sicilden silinir.

## Çıktı modülleri
- Amaç/mal yeterliliği değerlendirmesi + dayanak.
- Vakıf senedi zorunlu içerik kontrol listesi.
- Tescil/başvuru iskeleti (asliye hukuk, VGM görüşü).
- Değişiklik/sona erme yolu notu + `[doldurulacak]` yerleri.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
