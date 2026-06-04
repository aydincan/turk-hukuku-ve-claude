---
name: temel-kavramlar-ve-sistem
description: "Bilişim/siber bir olayın hangi hukuk katmanlarına (ceza, KVKK, 5651, tazminat) dokunduğunu çözmek, kavramları yerli yerine oturtmak ve doğru başlığa yönlendirmek gerektiğinde kullanılır."
---

# Bilişim Hukukunun Temel Kavramları ve Sistematiği

## Görev
Bilişim/siber bir vakıayı doğru hukuki katmanlara ayırmak; bilişim sistemi, veri, içerik/yer/erişim sağlayıcı, dijital delil gibi temel kavramları tanımlayıp olayı isabetli alt-becerilere yönlendirmek.

## Soğuk başlangıç (intake)
1. Olay ne? (yetkisiz erişim, veri sızıntısı, dolandırıcılık, içerik ihlali, sistem kesintisi?)
2. Etkilenen ne? (bilişim sistemi mi, kişisel veri mi, banka/kart verisi mi, itibar/içerik mi?)
3. Taraf kim? (mağdur birey, kurum/veri sorumlusu, hizmet sağlayıcı, şüpheli?)
4. Beklenti? (şikâyet/ceza, uyum/idari savunma, tazminat, içerik kaldırma?)

## Denetim şeması
1. **Katman tespiti.** Olayı üç eksende sorgula: cezai (TCK m.243-245, m.135-140, m.158/1-f), idari/düzenleyici (KVKK m.12; 5651 m.8-9; BTK), özel hukuk (TBK m.49 vd. haksız fiil; sözleşmesel sorumluluk). Bir olay birden çok eksende sonuç doğurabilir.
2. **Bilişim sistemi kavramı.** TCK uygulamasında bilişim sistemi, verileri toplayıp işleyen manyetik/elektronik her türlü sistemdir; cep telefonu, sunucu, bulut hesabı dahil. Fiilin bir bilişim sistemi üzerinde gerçekleşip gerçekleşmediği tipikliğin ön şartıdır.
3. **Veri ayrımı.** Kişisel veri (KVKK/TCK m.135-140) ile sistem verisi (TCK m.244) ayrılır; banka/kredi kartı verisi için özel norm TCK m.245 önceliklidir.
4. **Sağlayıcı kavramı.** 5651 kapsamında içerik, yer, erişim ve toplu kullanım sağlayıcı ayrımı sorumluluk rejimini belirler; doğru sıfat saptanmadan tedbir/sorumluluk tartışılamaz.
5. **Ara sonuç.** Hangi katmanların devrede olduğu ve hangi alt-becerinin (suçlar, ihlal müdahalesi, dijital delil, sorumluluk, içerik kaldırma) öncelikli olacağı belirlenir. İspat yükü her katmanda ayrıdır: cezada iddia makamında, idari uyumda veri sorumlusunda (KVKK m.12 tedbirlerini aldığını ispat), tazminatta zarar görende.

## Çıktı modülleri
- Katman haritası (ceza / KVKK / 5651 / tazminat) ve öncelik sırası.
- Kavram tablosu: etkilenen sistem, veri türü, taraf sıfatları.
- Yönlendirme notu: hangi alt-beceriyle devam edileceği ve ilk aksiyonlar.

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
