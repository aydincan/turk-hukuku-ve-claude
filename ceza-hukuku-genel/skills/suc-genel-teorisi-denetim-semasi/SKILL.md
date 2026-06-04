---
name: suc-genel-teorisi-denetim-semasi
description: "Bir fiilin suç oluşturup oluşturmadığını TCK genel hükümleri üzerinden katmanlı denetlemek; tipiklik, hukuka aykırılık ve kusurluluk süzgecini sırayla uygulamak gerektiğinde kullanılır."
---

# Suç Genel Teorisi ve Suç Denetim Şeması

## Görev
İsnat edilen somut bir fiilin TCK anlamında suç oluşturup oluşturmadığını, üç katmanlı suç teorisiyle (tipiklik — hukuka aykırılık — kusurluluk) adım adım denetlemek ve niteleme önerisi sunmak.

## Soğuk başlangıç (intake)
- İsnat edilen fiil tam olarak nedir; sevk/uygulanan TCK maddesi belirli mi?
- Fiilin tarihi, yeri, mağduru ve failin sıfatı (kamu görevlisi vb.) nedir?
- Netice gerçekleşti mi, yoksa teşebbüs aşamasında mı kaldı?
- Bir hukuka uygunluk sebebi (meşru savunma, rıza, görev) ileri sürülüyor mu?

## Denetim şeması
1. **Kanunilik ön denetimi (TCK m.2):** Fiilin işlendiği tarihte kanunda açıkça suç olarak tanımlanıp tanımlanmadığı; kıyas yasağı. İşlenme/karar tarihi farklıysa lehe kanun (m.7).
2. **Tipiklik — maddi unsur:** Fail, mağdur, suçun konusu, fiil, varsa netice ve nedensellik/objektif isnadiyet. Netice yoksa teşebbüs (m.35) ekseni açılır. Ara sonuç: maddi unsur tamam mı?
3. **Tipiklik — manevi unsur:** Kast (m.21, olası kast dahil) mi, taksir (m.22, bilinçli taksir) mi; suç tipi taksirle işlenebiliyor mu? Neticesi sebebiyle ağırlaşmış suçta en azından taksir (m.23) aranır. İspat yükü iddia makamındadır; kast karinesi yoktur.
4. **Hukuka aykırılık:** Bir hukuka uygunluk sebebi var mı? Kanun hükmü/amirin emri (m.24), meşru savunma (m.25), hak kullanma ve ilgilinin rızası (m.26), sınırın aşılması (m.27). Varsa fiil suç olmaktan çıkar; ara sonuç kaydedilir.
5. **Kusurluluk:** Kusur yeteneği (yaş m.31, akıl hastalığı m.32, sağır-dilsiz m.33, geçici neden m.34) ve kusurluluğu kaldıran/azaltan hâller: cebir-zorunluluk (m.25/2, m.28), haksız tahrik (m.29), hata (m.30), kaçınılmaz kanunu bilmeme (m.4/son içtihadı).
6. **Ara sonuç ve nitelik:** Tüm katmanlar olumluysa suç oluşur; ardından teşebbüs/iştirak/içtima ve yaptırım modülüne yönlendirin.

## Çıktı modülleri
- Katman katman gerekçeli tablo (madde atıflı, ara sonuçlu).
- Lehe/aleyhe argüman özeti ve ispat yükü notu.
- Eksik vakıa ve `[doğrulanacak]` içtihat ihtiyacı listesi.
- Olası niteleme alternatifleri ve sonraki adım önerisi.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
