---
name: konut-isyeri-rejimi-koruyucu-hukumler
description: "Sözleşmedeki güvence bedeli, bağlantılı sözleşme, gecikme cezası, muacceliyet veya kiracı aleyhine kayıtların geçerliliği tartışıldığında ya da kiracının emredici korumalardan yararlanıp yararlanamayacağı sorulduğunda bu beceriyi kullan."
---

# Konut ve Çatılı İşyeri Kiralarında Koruyucu Hükümler

## Görev
Konut/çatılı işyeri kiralarına özgü emredici koruma kalkanını uygulamak: sözleşmedeki hangi kayıtların geçerli, hangilerinin kiracı yönünden geçersiz olduğunu saptamak ve buna göre tarafların hareket alanını çizmek.

## Soğuk başlangıç (intake)
- Sözleşmede depozito/güvence var mı, tutarı ve şekli ne (nakit, teminat mektubu)?
- Kira ile birlikte dayatılan başka bir edim/sözleşme var mı?
- Gecikme cezası, muacceliyet (bir kira ödenmezse tümü muaccel) kaydı var mı?
- Kiracı aleyhine, kanundan ağır yükümlülük getiren madde var mı?

## Denetim şeması
1. **Güvence bedeli (TBK m.342)**: En çok üç aylık kira bedeli istenebilir. Para veya kıymetli evrak ise kiracı, kiraya verenin onayı olmadan çekilmemek üzere bankaya yatırır; banka, kiraya verenin onayı veya kesinleşmiş icra takibi/dava olmadan ödeme yapmaz. Aşan kısım ve aykırı düzenleme geçersizdir.
2. **Bağlantılı sözleşme yasağı (TBK m.340)**: Kira sözleşmesi, kiracının yararına olmayan ve doğrudan kiralananın kullanımıyla ilgisi olmayan bir borç altına sokulmasına bağlanamaz; aksi kayıt geçersiz.
3. **Kiracı aleyhine düzenleme yasağı (TBK m.346)**: Kiracıya kira bedeli ve yan giderler dışında ödeme yükümlülüğü getirilemez; özellikle **gecikme cezası** ve **muacceliyet** (ödenmeyen kira için diğer dönemlerin de muaccel sayılması) kayıtları geçersizdir.
4. **Kira bedelinde değişiklik yasağı (TBK m.343)**: Kira bedeli dışında kiracı aleyhine sözleşme değişikliği yapılamaz; artış hükümleri saklıdır (bkz. kira tespiti becerisi).
5. **İspat yükü**: Geçersizliği ileri süren kiracı, sözleşme metnini ve dayatılan edimi gösterir; emredici hükme aykırılık def'i resen de gözetilebilir.
6. **Ara sonuç**: Geçerli kalan ve elenen kayıtların listesi; kiraya verenin bu kayıtlara dayanarak talep edemeyeceği kalemler.

## Çıktı modülleri
- Madde madde geçerlilik tablosu (geçerli / kiracı yönünden geçersiz).
- Depozito iadesi/banka prosedürü notu.
- Sözleşmeye redline önerisi (gerekirse).

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
