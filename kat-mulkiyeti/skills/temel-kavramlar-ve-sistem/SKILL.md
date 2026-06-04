---
name: temel-kavramlar-ve-sistem
description: "Bir gayrimenkul uyuşmazlığında KMK rejiminin uygulanıp uygulanmayacağını ilk kez tayin ederken; kat mülkiyeti mi kat irtifakı mı adi paylı mülkiyet mi, bağımsız bölüm mü ortak yer mi, arsa payı oranının rolü gibi temel ayrımları kurmak için kullanılır."
---

# Temel Kavramlar ve Kat Mülkiyeti Sistematiği

## Görev
Önündeki olayı doğru rejime oturtmak: yapı üzerinde kat mülkiyeti mi, kat irtifakı mı, yoksa KMK dışı adi paylı mülkiyet mi kurulu olduğunu; uyuşmazlığın bağımsız bölüme mi ortak yere mi ilişkin olduğunu ve arsa payının fonksiyonunu belirlemek. Bu nitelendirme uygulanacak kanunu, görevli mahkemeyi ve tüm sonraki adımları belirler.

## Soğuk başlangıç (intake)
- Tapuda kayıt türü nedir: kat mülkiyeti, kat irtifakı yoksa hisseli (arsa) tapu mu?
- Uyuşmazlık bir bağımsız bölüme mi (daire, dükkân) yoksa ortak yere mi (çatı, asansör, bahçe, sığınak) ilişkin?
- Yapı tamamlanmış ve iskânlı mı; kat irtifakından kat mülkiyetine geçilmiş mi?
- Yönetim planı, kat malikleri kurulu kararları ve işletme projesi mevcut mu?

## Denetim şeması
1. **Rejim tespiti**: Kat mülkiyeti, tamamlanmış yapıda bağımsız bölüm + arsa payı + ortak yer payı üçlüsünden oluşan bütünleşik bir mülkiyettir (KMK m.1, m.3). Tapuda kat mülkiyeti/kat irtifakı kurulu değilse KMK uygulanmaz; TMK paylı mülkiyet hükümleri ve ortaklığın giderilmesi gündeme gelir.
2. **Bağımsız bölüm / ortak yer ayrımı**: Ayrı kullanılmaya elverişli, başlı başına bölüm bağımsız bölümdür (KMK m.3, m.5). Ortak yerler m.4'te sayılır (temeller, ana duvarlar, çatı, bacalar, avlu, asansör, sığınak, ısıtma sistemi vb.); bunlar zorunlu/eklenti ortak yer ayrımına tabidir ve paylı mülkiyete konudur (m.4, m.16).
3. **Arsa payının rolü**: Her bağımsız bölüme, değeriyle orantılı arsa payı özgülenir (KMK m.3/2). Arsa payı; ortak gider/avans katılımının, ortak yerden yararlanmanın ve kuruldaki oy ağırlığının ölçüsüdür. Oransız tespit edilmişse arsa payı düzeltme davası açılır (m.3/son).
4. **Kat irtifakı / kat mülkiyeti farkı**: Kat irtifakı, henüz yapılmamış/tamamlanmamış yapı için arsa payına bağlı kurulan bir irtifaktır (m.2/c, m.10/son); yapı bitince kat mülkiyetine çevrilir (m.14). Kat irtifakı aşamasında da KMK'nın yönetim ve gider hükümleri kıyasen uygulanır (m.17).
5. **Ara sonuç**: Rejim ve uyuşmazlık konusu (bağımsız bölüm/ortak yer) belirlendikten sonra ilgili uzman beceriye (kuruluş, karar, gider, projeye aykırılık) yönlendir.

## Çıktı modülleri
- Statü/rejim tespiti notu (kat mülkiyeti/irtifakı/adi paylı mülkiyet).
- Bağımsız bölüm-ortak yer-arsa payı haritası.
- Eksik belge listesi (yönetim planı, karar defteri, işletme projesi).
- Bir sonraki uzman beceriye yönlendirme.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
