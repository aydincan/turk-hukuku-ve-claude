---
name: duzenleyici-islem-denetimi
description: "Yönetmelik, tebliğ, genelge gibi düzenleyici idari işlemlerin üst normlara (kanun, Anayasa) aykırılığını denetlemek ve iptalini değerlendirmek için kullanılır; bireysel işlemin dayanağı düzenleme tartışmalıysa başvurulur."
---

# Düzenleyici İşlemler ve Norm Denetimi

## Görev
Düzenleyici idari işlemleri (yönetmelik, tebliğ, genelge) normlar hiyerarşisi içinde denetlemek; kanuna/Anayasaya aykırılığı tespit edip iptal yolunu ve uygulama işlemiyle birlikte dava imkânını kurmak.

## Soğuk başlangıç (intake)
1. Tartışılan düzenleme türü nedir (yönetmelik/tebliğ/genelge) ve dayanağı hangi kanun?
2. Düzenleme bir bireysel işleme dayanak mı oluşturuyor (uygulama işlemi var mı)?
3. Düzenleme süresinde mi, yoksa yayımı üzerinden 60 gün geçti mi?
4. Düzenleme usulüne uygun çıkarılmış mı (Danıştay incelemesi, yayım)?

## Denetim şeması
1. **Normlar hiyerarşisi.** Anayasa > kanun > CBK > yönetmelik > diğer düzenlemeler. Düzenleyici işlem, dayandığı kanunun çizdiği çerçeveyi aşamaz; kanunda olmayan yükümlülük getiremez (kanunilik, Anayasa m.123/m.124).
2. **Yetki ve usul.** Düzenlemeyi yapan makam yetkili mi; belirli yönetmelikler için Danıştay'ın incelemesi ve Resmî Gazete'de yayım şartı yerine gelmiş mi?
3. **Üst norma uygunluk.** İçerik kanuna/Anayasaya aykırı mı; eşitlik ve ölçülülük (Anayasa m.13) ölçütlerini karşılıyor mu? İdarenin düzenleme yetkisinin sınırı kamu yararı ve kanunîliktir.
4. **Dava yolu ve süre.** Düzenleyici işleme karşı doğrudan iptal (İYUK m.7) **veya** uygulama işlemiyle birlikte düzenlemeye karşı dava (m.7/4). İlk derecede Danıştay'da görülecek düzenlemeleri ayır (2575 sayılı K.).
5. **İhmal yoluyla uygulamama.** Hâkim, kanuna aykırı düzenlemeyi olaya uygulamayabilir; bunu uygulama işlemi davasında ileri sür.
6. **İspat.** Aykırılık hukuki bir değerlendirme olduğundan üst norm-alt norm karşılaştırmasını metinle göster.
7. **Ara sonuç.** Düzenlemenin hangi üst norma, hangi yönden aykırı olduğu + uygun dava stratejisi (doğrudan/uygulama ile birlikte).

## Çıktı modülleri
- Normlar hiyerarşisi karşılaştırma tablosu (üst norm vs. düzenleme).
- Aykırılık gerekçeleri listesi.
- Dava yolu seçimi (doğrudan / uygulama işlemiyle birlikte).
- Danıştay görevi/yer yetkisi notu.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
