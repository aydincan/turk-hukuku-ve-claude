---
name: pinpoint-ve-dogru-alinti
description: "Bir karardan veya doktrinden alıntı yapılırken; tam olarak hangi paragraf, sayfa veya gerekçeye dayanıldığını göstermek ve cımbızlama/çarpıtma olmadan alıntılamak gerektiğinde kullanılır."
---

# Pinpoint Atıf ve Doğru Alıntı

## Görev
Bir kaynağa atıf yaparken dayanılan tam yeri (karar paragrafı, doktrin sayfası) göstermek ve alıntıyı bağlamından kopararak çarpıtmamak.

## Soğuk başlangıç (intake)
- Kaynak içinde hangi tam yere dayanılıyor (sayfa, paragraf, gerekçe bölümü)?
- Alıntı bağlayıcı gerekçeye mi (ratio) yoksa geçer söze mi (obiter) dayanıyor?
- Tam metin elimizde mi, yoksa özet üzerinden mi atıf yapılıyor?
- Lehe görünen ifade, kararın bütününde gerçekten lehe mi?

## Denetim şeması
1. **Pinpoint zorunluluğu** — "Genel olarak şu karar" yetmez; doktrinde sayfa (s. …), kararda ilgili paragraf/gerekçe işaret edilir. AYM/AİHM kararlarında paragraf numarası (§ …) kullanılır.
2. **Ratio / obiter ayrımı** — Kararın bağlayıcı/taşıyıcı gerekçesi (ratio decidendi) ile yan/geçer sözü (obiter dictum) ayrılır; atıf gücü ratioya bağlanır, obiter "ek olarak" diye sunulur.
3. **Bağlamı koruma** — Cümle, paragrafın ve kararın bütünündeki anlamıyla aktarılır; şart cümlesinden koşul atılarak, istisnadan istisna kaldırılarak alıntı yapılmaz (cımbızlama yasağı).
4. **Doğrudan/dolaylı alıntı** — Doğrudan alıntı tırnak içinde aynen verilir; özetleyen dolaylı alıntı "kararın özüne göre…" diye işaretlenir, kelimesi kelimesine gibi gösterilmez.
5. **Karşı içtihat dürüstlüğü** — Aleyhe yerleşik içtihat veya karşı oy varsa gizlenmez; en azından "karşı yönde …" diye anılır.
6. **Özet üzerinden atıf riski** — Üçüncü el özetler hatalı olabilir; tam metne inilemeyen yerde alıntı "tam metin doğrulanacak" notuyla bırakılır.

## Çıktı modülleri
- Pinpoint atıf (sayfa/§/paragraf ile).
- Ratio/obiter işareti.
- Bağlam notu (alıntının çevresi).
- Karşı içtihat/karşı oy uyarısı + `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `atif-turk-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
