---
name: lehe-kanun-infaz
description: "İnfaz oranlarını değiştiren geçici maddeler, 7242 sayılı Kanun türü değişiklikler, af ve lehe kanun uygulamasının infaza etkisini çözümlemek gerektiğinde kullanılır."
---

# Lehe Kanun, Af ve Geçici Düzenlemelerin İnfaza Etkisi

## Görev
Suç tarihi ile infaz tarihi arasında değişen infaz hükümlerinden hangisinin uygulanacağını, af ve geçici düzenlemelerin etkisini lehe kanun ilkesi (TCK m.7) ışığında çözmek.

## Soğuk başlangıç (intake)
- Suç tarihi ile hüküm/kesinleşme tarihleri nedir?
- Aralıkta infaz oranını değiştiren bir kanun (örn. 7242 sayılı Kanun) yürürlüğe girdi mi?
- Suç tipi geçici düzenlemelerin kapsamına giriyor/dışında mı?
- Bir af, özel af veya seçimlik yaptırım düzenlemesi söz konusu mu?

## Denetim şeması
1. Niteliği belirle: TCK m.7/2 sonradan yürürlüğe giren lehe kanunun uygulanmasını öngörür; ancak infaz rejimine ilişkin hükümlerin maddi ceza hükmü mü yoksa usule ilişkin mi sayılacağı tartışmalıdır. Koşullu salıverilme ve denetimli serbestlik oranları, yerleşik yaklaşım uyarınca suç tarihine göre lehe olan biçimde uygulanır. Ara sonuç: hangi metin uygulanacak?
2. Geçici maddeler: 7242 sayılı Kanun ve TCK geçici m.6 gibi düzenlemeler, belirli suç tipleri dışında oranları değiştirmiştir; kapsam dışı suçlar (terör, kasten öldürme, cinsel suçlar, uyuşturucu ticareti) için istisna rejimi kontrol edilir.
3. Af: genel af mahkûmiyeti tüm sonuçlarıyla, özel af cezanın infazını etkiler (TCK m.65); af kanununun kapsam ve şartları metinden doğrulanır.
4. Karşılaştırmalı uygulama: suç tarihindeki ve hâlihazırdaki düzenlemelere göre iki ayrı infaz hesabı yapılır, hükümlü lehine olan benimsenir. İspat: yürürlük tarihleri ve geçici madde metinleri mevzuat.gov.tr üzerinden.
5. İtiraz/uyarlama: lehe hükmün uygulanması talebi infaz savcılığına/infaz hâkimliğine; uyarlama gereken hâllerde hükmü veren mahkemeye yöneltilir.
6. İlkesel içtihat: lehe kanun ve infaz oranı için karararama.yargitay.gov.tr Yargıtay CGK ve 1. CD; AYM eşitlik/öngörülebilirlik kararları (kararlarbilgibankasi.anayasa.gov.tr). Künye `[doğrulanacak]`.
7. Ara sonuç: uygulanacak metin + lehe hesap + başvuru mercii.

## Çıktı modülleri
- İki senaryolu lehe karşılaştırma tablosu.
- Kapsam/istisna kontrol listesi.
- Lehe hüküm uygulanması veya uyarlama talebi dilekçesi tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
