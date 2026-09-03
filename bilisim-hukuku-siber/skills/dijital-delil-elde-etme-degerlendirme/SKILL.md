---
name: dijital-delil-elde-etme-degerlendirme
description: "Loglar, imajlar, e-posta, mesaj kayıtları gibi dijital delillerin hukuka uygun elde edilmesi, bütünlüğünün korunması ve mahkemede değerlendirilebilirliğini denetlemek gerektiğinde kullanılır."
---

# Dijital Delilin Elde Edilmesi ve Değerlendirilmesi

## Görev
Dijital delillerin hukuka uygun şekilde elde edilip edilmediğini, bütünlük zincirinin korunup korunmadığını ve yargılamada değerlendirilebilirliğini denetlemek; itiraz veya delil tespiti stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Hangi dijital delil? (log, disk imajı, e-posta, WhatsApp/mesaj, ekran görüntüsü?)
2. Nasıl elde edildi? (CMK m.134 kararıyla mı, taraf rızasıyla mı, tek taraflı mı?)
3. Bütünlük korundu mu? (hash, imaj, zaman damgası, gözetim zinciri var mı?)
4. Delil kim aleyhine ve hangi yargılamada (ceza/hukuk) kullanılacak?

## Denetim şeması
1. **Elde etme yetkisi.** Ceza yargılamasında bilgisayar, program ve kütüklerde arama, kopyalama ve elkoyma CMK m.134'e tabidir: kural olarak hâkim kararı, sistemdeki verilerin yedeklenmesi ve istem halinde bir kopyasının ilgiliye verilmesi gerekir. Genel arama-elkoyma rejimi (CMK m.116-123) tamamlayıcıdır.
2. **Hukuka aykırı delil yasağı.** Hukuka aykırı elde edilen delil hükme esas alınamaz (Anayasa m.38/6; CMK m.206/2-a, m.217/2, m.230/1). Özel hayata/haberleşmeye müdahale ile elde edilen kayıtlar TCK m.132-134 kapsamında ayrıca suç oluşturabilir; bir suçun işlendiğini gösteren tesadüfen elde edilmiş kayıtların durumu ayrıca değerlendirilir.
3. **Bütünlük ve zincir.** İmaj alma, hash (özet) değeri, zaman damgası ve gözetim zinciri (chain of custody) belgelenmelidir; bütünlüğü ispatlanamayan delilin değeri tartışmalıdır. Ekran görüntüsü/mesaj çıktısı tek başına zayıf delildir, teknik doğrulama ile desteklenmelidir.
4. **Hukuk yargılamasında.** HMK uyarınca senet/belge ve diğer deliller rejimi (HMK m.199 belge tanımı elektronik verileri kapsar) ile delil tespiti (HMK m.400 vd.) yolları kullanılır. **İspat yükü** delili sunan taraftadır; karşı taraf bütünlük ve hukuka uygunluk itirazını ileri sürer.
5. **Ara sonuç.** Delilin elde edilme usulü, bütünlüğü ve değerlendirilebilirliği; itiraz veya delil tespiti talebi gerekli mi belirlenir.

## Çıktı modülleri
- Delil değerlendirme tablosu (kaynak, yetki, bütünlük, hukuka uygunluk).
- Hukuka aykırılık/itiraz dilekçesi iskeleti.
- Delil tespiti veya bilirkişi (adli bilişim) talebi taslağı.

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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
