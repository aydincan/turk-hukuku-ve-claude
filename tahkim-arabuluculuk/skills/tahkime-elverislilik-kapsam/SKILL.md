---
name: tahkime-elverislilik-kapsam
description: "Bir uyuşmazlığın konu itibarıyla tahkime veya arabuluculuğa elverişli olup olmadığını, kamu düzeni ve emredici hükümler süzgecinden geçirerek belirlemek gerektiğinde kullanılır."
---

# Tahkime ve Arabuluculuğa Elverişlilik

## Görev
Uyuşmazlığın alternatif çözüm yoluna konu edilip edilemeyeceğini kapı eşiğinde
belirlemek. Elverişsiz bir konu için kurulan tahkim/arabuluculuk emek ve süre kaybı
doğurur; bu süzgeç en başta uygulanır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık konusu nedir (ayni hak, statü, alacak, idari işlem)?
2. Taraflar bu hak üzerinde serbestçe tasarruf edebilir mi?
3. Konu bir kamu düzeni alanına mı (boşanma statüsü, ceza, vergi tarhı) giriyor?
4. Hedef yol tahkim mi arabuluculuk mu?

## Denetim şeması
1. **Tahkim elverişliliği**: **HMK m.408** — taşınmaz üzerindeki **ayni haklara** ilişkin
   ve **iki tarafın iradesine tabi olmayan** uyuşmazlıklar tahkime elverişsizdir.
   Milletlerarası tahkimde de aynı çekirdek geçerlidir (**MTK m.1/4**).
2. **Arabuluculuk elverişliliği**: **HUAK m.1/2** — tarafların üzerinde serbestçe
   tasarruf edebileceği işler. **Aile içi şiddet** iddiası içeren uyuşmazlıklar
   arabuluculuğa elverişsizdir.
3. **Kamu düzeni/emredici hüküm süzgeci**: Boşanma/soybağı gibi **statü** belirleyen
   davalar, ceza yargılaması, idari/vergi uyuşmazlıkları kural olarak dışlanır.
   Tahkim/arabuluculuk yalnızca tarafların tasarrufundaki **maddi sonuçları** (ör. nafaka
   miktarı değil ama mal rejimi tasfiyesindeki alacak gibi tasarruf edilebilir kısımlar)
   yönünden mümkün olabilir; sınır dikkatle çizilir.
4. **Karma uyuşmazlık**: Bir kısmı elverişli bir kısmı değilse ayrıştırma yapılır;
   elverişli kısım tahkim/arabuluculuğa, diğeri devlet yargısına yönlendirilir.
5. **Ara sonuç**: Elverişlilik kararı, dayanak madde ve istisna notu.

## Çıktı modülleri
- Elverişlilik karar tablosu (konu-yol-dayanak-istisna).
- Karma uyuşmazlık ayrıştırma haritası.
- Devlet yargısına yönlendirme gerekiyorsa görev/yetki kısa notu.

## Plugin bağlamı

Bu beceri `tahkim-arabuluculuk` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
