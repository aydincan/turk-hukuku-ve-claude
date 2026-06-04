---
name: gorev-yetki-arabuluculuk-usul
description: "Kira uyuşmazlığında hangi mahkemenin görevli ve yetkili olduğu, dava açmadan önce arabuluculuğa başvuru zorunluluğu, basit yargılama usulü veya süreler söz konusu olduğunda bu beceriyi kullan."
---

# Görev, Yetki, Dava Şartı Arabuluculuk ve Usul

## Görev
Kira uyuşmazlığını doğru mahkeme önüne ve doğru usule oturtmak: görev (sulh hukuk), yetki, zorunlu arabuluculuk dava şartı ve uygulanacak yargılama usulünü belirlemek; usuli ön engelleri baştan elemek.

## Soğuk başlangıç (intake)
- Talep ne (tahliye, kira tespiti, alacak, depozito iadesi)?
- Taşınmaz nerede, taraflar nerede ikamet ediyor?
- Arabuluculuğa başvuruldu mu; son tutanak var mı?
- Sözleşmede yetki kaydı veya tahkim şartı var mı?

## Denetim şeması
1. **Görev (HMK m.4/1-a)**: Kira ilişkisinden doğan **alacak ve tahliye** davaları ile kira tespiti davalarında **sulh hukuk mahkemesi** görevlidir; değer ve miktara bakılmaz.
2. **Yetki (HMK m.6, m.10)**: Genel yetki davalının yerleşim yeri; sözleşmeden doğan davalarda **ifa yeri** mahkemesi de yetkilidir (m.10). Taşınmaza ilişkin ayni nitelik taşımadığından kira davalarında kesin yetki kural değildir; sözleşmesel yetki kaydı denetlenir.
3. **Dava şartı arabuluculuk (HUAK m.18/A)**: 1.9.2023'ten itibaren **kira ilişkisinden kaynaklanan uyuşmazlıklar** (tahliye dahil, taşınmazın aynına ilişkin olmayanlar) dava açmadan önce **arabuluculuğa başvuru** dava şartıdır. Son tutanak dilekçeye eklenmezse dava usulden reddedilir. İlamsız icra/ihtiyati tedbir bu şartın istisnasıdır.
4. **Yargılama usulü (HMK m.316)**: Kira ilişkisinden doğan tahliye dahil uyuşmazlıklar **basit yargılama usulüne** tabidir; dilekçeler tek, süreler kısa, ön inceleme ve tahkikat sıkışıktır.
5. **Süreler ve hak düşürücü kontrol**: Tahliye sebebine bağlı bir aylık dava süreleri (TBK m.353), tespit davası süre penceresi (m.345) baştan takvimlenir.
6. **Ara sonuç**: Görevli-yetkili mahkeme + arabuluculuk durumu + usul + kritik süreler.

## Çıktı modülleri
- Görev-yetki tespit notu.
- Arabuluculuk başvuru/uygunluk kontrol listesi.
- Usul ve süre takvimi.

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
