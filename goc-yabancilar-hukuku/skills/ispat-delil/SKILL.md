---
name: ispat-delil
description: "Göç dosyasında ispat yükünün kimde olduğu, hangi belge ve delillerin gerektiği veya risk anlatısının nasıl belgeleneceği değerlendirileceğinde kullanılır."
---

# İspat ve Delil Yönetimi

## Görev
Göç ve yabancılar uyuşmazlığında ispat yükünü doğru dağıtmak, gereken belge ve delilleri toplamak, risk/koruma anlatısını doğrulanabilir biçimde belgelemek ve idarenin tespitlerine karşı delil üretmek.

## Soğuk başlangıç (intake)
1. İspatlanacak temel iddia nedir (şart sağlandı, risk var, çalışma izinsiz değil vb.)?
2. Eldeki belgeler nelerdir (pasaport, ikamet, evlilik, gelir, sigorta, tıbbi rapor)?
3. İdarenin dayandığı tespit/tutanak/istihbarat var mı, içeriği biliniyor mu?
4. Yabancı dildeki belgeler için yeminli tercüme/apostil yapıldı mı?

## Denetim şeması
1. **İspat yükü dağılımı**: İdari yargıda re'sen araştırma ilkesi geçerli olsa da, lehe şartların varlığını (ikamet süresi, evlilik birliği, geçim, koruma riski) yabancı; işlemin maddi dayanağını ve kamu düzeni-güvenliği gerekçesini idare ortaya koyar.
2. **Belge delili**: Resmî belgeler (nüfus, tapu, sigorta, banka), yabancı resmî belgelerde apostil/konsolosluk onayı ve yeminli tercüme; sahtelik iddiası ayrıca incelenir.
3. **Koruma riskinin ispatı**: Uluslararası korumada güncel ülke menşe bilgisi, raporlar, tıbbi/psikolojik değerlendirme; standart inandırıcı kılma + tereddütte lehe yorum.
4. **İdarenin gizli/istihbari dayanağı**: Kamu düzeni-güvenliği gerekçeli işlemlerde dayanak çoğu kez soyut kalır; savunmaya esas teşkil eden somut maddi vakıa talep edilir, soyut nitelendirme yeterli sayılamaz (silahların eşitliği/AİHS m.6-13 ekseni).
5. **Delil tespiti/ara karar**: Mahkemeden işlem dosyasının (idari işlem dayanak belgeleri) celbi istenir.
**Ara sonuç**: İddia-delil eşleştirme tablosu ve eksik delil için toplama planı.

## Çıktı modülleri
- İddia/ispat yükü/delil eşleştirme matrisi.
- Eksik belge ve tercüme/apostil yapılacaklar listesi.
- Mahkemeye ara karar/işlem dosyası celbi talep metni.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
