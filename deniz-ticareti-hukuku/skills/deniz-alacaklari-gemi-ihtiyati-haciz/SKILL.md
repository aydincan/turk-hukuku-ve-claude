---
name: deniz-alacaklari-gemi-ihtiyati-haciz
description: "Bir deniz alacağını teminat altına almak için gemiye ihtiyati haciz koydurmak ya da konulan haczi kaldırmak gerektiğinde; alacağın deniz alacağı niteliğini, yetkili mahkemeyi, teminatı ve serbest bırakma şartlarını belirlemek için kullan."
---

# Deniz Alacakları ve Geminin İhtiyati Haczi

## Görev
Bir alacağın "deniz alacağı" olup olmadığını belirlemek; gemiye ihtiyati haciz koydurmak veya konulan haczi kaldırmak için şartları, yetkiyi, teminatı ve serbest bırakma yollarını çözmek.

## Soğuk başlangıç (intake)
- Alacak hangi olaydan doğuyor (navlun, çatma, kurtarma, yakıt/kumanya, mürettebat ücreti)?
- Gemi hangi limanda; bayrağı ve donatanı kim; alacaklı kime karşı talepte bulunuyor?
- Amaç haciz koydurmak mı yoksa konulan haczi kaldırmak/serbest bıraktırmak mı?
- Teminat (P&I kulüp mektubu, banka teminatı) sunulabilir mi?

## Denetim şeması
1. **Deniz alacağı nitelendirmesi**: Alacağın TTK m.1352'de **sınırlı sayıda** sayılan deniz alacaklarından biri olup olmadığını denetle; yalnızca deniz alacakları için bu özel ihtiyati haciz rejimi işler.
2. **İhtiyati haciz şartları ve sebebi gösterme yükü**: Geminin ihtiyaten haczinde, genel ihtiyati hacizden farklı olarak alacaklı kural olarak alacağın muaccel olduğunu/yaklaşık ispatı sağlar; TTK m.1353 vd. çerçevesinde "alacağın varlığını yaklaşık ispat" ölçütünü uygula.
3. **Yetki ve teminat**: Geminin bulunduğu yer mahkemesinin yetkisini ve haciz için alacaklıdan istenecek teminatı belirle; haksız hacizden doğacak donatan zararı için teminat öngörülür.
4. **Serbest bırakma**: Donatan/borçlu yeterli teminat (P&I LOU, banka mektubu) gösterirse geminin serbest bırakılmasını sağla; teminat tutarının alacak + faiz + masrafı karşılaması gerekir.
5. **İspat ve ara sonuç**: Alacaklı yaklaşık ispat, borçlu ise alacağın bulunmadığını veya teminatın yeterliğini gösterir. Çıktıda haciz talebi/itirazı için gerekçeyi, yetkili mahkemeyi ve teminat tutarını sayısallaştır; esas dava açma süresine dikkat et.

## Çıktı modülleri
- Deniz alacağı niteliği değerlendirme tablosu (m.1352 listesi eşlemesi)
- İhtiyati haciz dilekçesi / serbest bırakma talebi iskeleti
- Teminat hesabı ve esas dava süre takvimi

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
