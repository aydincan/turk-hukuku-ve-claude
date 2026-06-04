---
name: kira-temel-kavramlar-ve-sistem
description: "Kullanıcı bir kira uyuşmazlığını ilk kez sunduğunda, sözleşmeyi nitelendirmek (konut, çatılı işyeri, ürün kirası), genel ve özel hükümler ayrımını kurmak ve hangi rejimin uygulanacağını saptamak için bu beceriyi kullan."
---

# Temel Kavramlar ve Kira Sözleşmesi Sistematiği

## Görev
Önüne gelen kira ilişkisini doğru hukuki rejime oturtmak: TBK genel hükümleri (m.299-338), konut/çatılı işyeri kiraları (m.339-356) ve ürün kirası (m.357 vd.) arasında ayrım yapmak; emredici-koruyucu kuralların devreye girip girmediğini belirlemek.

## Soğuk başlangıç (intake)
- Kiralanan taşınmaz konut mu, işyeri mi, arsa/depo/tarım arazisi mi; çatılı bir yapı mı?
- Sözleşme yazılı mı, tarihi nedir (1.7.2012 öncesi/sonrası)?
- Belirli süreli mi, belirsiz süreli mi; kaç yıldır devam ediyor?
- Taraflar kim (gerçek/tüzel kişi), kiraya veren malik mi?
- Talep ne: tahliye mi, kira tespiti/alacak mı, ayıp/onarım mı?

## Denetim şeması
1. **Tür tespiti**: TBK m.299 kira sözleşmesinin genel tanımıdır. Konut ve çatılı işyeri kiraları için koruyucu rejim (m.339 vd.) uygulanır. m.339/2: geçici kullanım amaçlı en çok altı aylık kiralar bu özel hükümlerin dışındadır. Ürün/hasılat kirasında (m.357) bağımsız bir rejim işler.
2. **Çatılı işyeri/konut niteliği**: Üstü örtülü, bağımsız kullanıma elverişli yer. Niteleme yanlışsa tüm denetim şeması kayar; bu yüzden tapu, kullanım amacı ve fiili durum birlikte değerlendirilir.
3. **Emredici süzgeç**: m.343 (kiracı aleyhine değişiklik), m.346 (kiracı aleyhine düzenleme — gecikme cezası/muacceliyet yasağı), m.342 (güvence en çok üç aylık kira). Sözleşmedeki aykırı kayıtlar kiracı yönünden geçersizdir.
4. **Geçiş hükmü**: 6101 sayılı Kanun, 6098'in kira hükümlerinin eski sözleşmelere uygulanma esaslarını belirler; özellikle m.344 ve m.346'nın yürürlüğü açısından doğrula.
5. **Ara sonuç**: Uygulanacak rejim + tarafın sıfatı + koruyucu kuralların etkisi tek paragrafta sabitlenir; sonraki tüm becerilerin temeli budur.

## Çıktı modülleri
- Niteleme notu (tür + rejim + emredici kurallar).
- Tespit edilen eksik bilgi listesi.
- İlgili özel beceriye yönlendirme (tahliye, kira tespiti, ayıp vb.).

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
