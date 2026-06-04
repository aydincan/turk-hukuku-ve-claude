---
name: dava-usul-gorev-yetki
description: "Telif uyuşmazlığının hangi mahkemede, hangi yargı kolunda ve nasıl açılacağını belirlemek gerektiğinde; görevli FSHM, yetki, hukuk-ceza yolu ayrımı ve aktif-pasif husumeti kurgulamak için kullanılır."
---

# Telif Davalarında Usul, Görev ve Yetki

## Görev
Telif uyuşmazlığında doğru yargı kolunu, görevli ve yetkili mahkemeyi, taraf sıfatlarını ve usul yolunu belirleyerek davayı doğru kurgulamak.

## Soğuk başlangıç (intake)
- Talep hukuki mi (ref/men/tazminat) yoksa cezai mi (şikâyet)?
- Davacı hangi sıfatla hareket ediyor (sahip, devralan, münhasır lisans sahibi, meslek birliği)?
- Davalı kim; eylem nerede gerçekleşti, eser nerede erişilebilir?
- İhtiyati tedbir/delil tespiti aciliyeti var mı?

## Denetim şeması
1. Yargı kolu: İhlal türüne göre hukuk veya ceza yolu seçilir; ikisi birlikte yürüyebilir (ceza şikâyete bağlı m.75). Hukuk talepleri ref (m.66-68), men (m.69), tespit ve tazminat (m.70).
2. Görev: Fikri ve Sınai Haklar Hukuk Mahkemeleri görevlidir (FSEK m.76); bulunmayan yerde Adalet Bakanlığı tarafından görevlendirilen asliye hukuk mahkemesi (ceza için FSH Ceza/ağır ceza) bakar. Görev kamu düzenindendir, re'sen incelenir (HMK m.114/1-c).
3. Yetki: Genel yetki davalının yerleşim yeri (HMK m.6); haksız fiil niteliğindeki ihlalde eylemin işlendiği veya zararın doğduğu yer mahkemesi de yetkilidir (HMK m.16). İnternet ihlallerinde erişilebilirlik yeri tartışmalıdır; somut bağlantı aranır.
4. Taraf sıfatı: Aktif husumet eser sahibi, mali hak devralanı, münhasır lisans sahibi ve yetkili meslek birliğine (m.42 vd.) aittir. Pasif husumet ihlal eyleminin failine; aracı/yer sağlayıcı sorumluluğu ayrı değerlendirilir.
5. Dava şartları ve arabuluculuk: Ticari nitelikteki para alacaklarında dava şartı arabuluculuk (TTK m.5/A, 6325 HUAK) gündeme gelebilir; fikri mülkiyet ticari dava sayıldığından kontrol edilir.
6. Ara sonuç: Yargı kolu + görevli/yetkili mahkeme + taraflar + ön şartlar sabitlenir.

İspat yükü: görev/yetki itirazını ileri süren açıklar; görev re'sen denetlenir.

## Çıktı modülleri
- Görev-yetki-husumet tespit notu (madde dayanaklı).
- Hukuk/ceza yolu seçim matrisi.
- Dava şartı/arabuluculuk kontrol kalemi.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
