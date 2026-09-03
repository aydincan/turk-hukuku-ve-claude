---
name: resmi-belge-ve-sicile-guven-tmk-7
description: "Tapu, nüfus, ticaret sicili gibi resmî sicillere veya resmî senetlere dayanılan ya da bunların içeriğine itiraz edilen durumlarda; resmî belgenin ispat gücünü ve aksinin nasıl ispatlanacağını belirlemek için kullanılır."
---

# Resmî Belgelerin İspat Gücü ve Sicile Güven (TMK m.7)

## Görev
Resmî sicil ve resmî senetlerin TMK m.7 uyarınca sahip olduğu ispat karinesini, bu karinenin kapsamını ve aksinin nasıl ispatlanacağını belirlemek; resmî belgeyle sicile güven ilkesi arasındaki bağı kurmak.

## Soğuk başlangıç (intake)
- Hangi resmî belge/sicil söz konusu (tapu kaydı, nüfus kaydı, ticaret sicili, resmî senet)?
- Karine, belgenin *hangi içeriğine* ilişkin (belgeyi düzenleyen memurun huzurunda olup bittiğini tespit ettiği olgular mı, beyanların doğruluğu mu)?
- Belgenin içeriğine itiraz mı ediliyor, yoksa sahteliği mi iddia ediliyor?
- Üçüncü kişinin sicile/belgeye iyiniyetle güveni var mı (TMK m.1023, m.3)?

## Denetim şeması
1. **Karine** — TMK m.7: resmî sicil ve senetler, belgeledikleri olguların doğruluğuna kanıt oluşturur; bunların içeriğinin doğru olmadığının ispatı, kanunlarda başka bir hüküm olmadıkça herhangi bir şekle bağlı değildir.
2. **Karinenin kapsamı** — Resmî belgenin güçlü ispat değeri, memurun *kendi tespit ve işlemlerine* ilişkin kısmıdır. Tarafların memura yaptığı beyanların maddî doğruluğu bu güçlü karineye dahil değildir; bunlar aksi serbestçe ispatlanabilen kısımdır.
3. **Aksini ispat** — İçeriğin doğru olmadığı, kanun başka şekil aramıyorsa serbest delille ispatlanır. Sahtelik iddiası ise ayrı bir rejime (HMK senedin sahteliği, ceza boyutu) tabidir.
4. **Sicile güven köprüsü** — Tapu siciline iyiniyetle güvenerek ayni hak kazanan üçüncü kişinin kazanımı korunur (TMK m.1023); yolsuz tescile rağmen iyiniyetli üçüncü kişi m.3 + m.1023 ile korunabilir. Bu, m.7 karinesinin maddi hukuktaki uzantısıdır.
5. **İspat yükü etkisi** — m.7, lehine karine olan tarafı ispat yükünden kurtarır; içeriğin yanlışlığını ileri süren aksini ispatla yükümlüdür (TMK m.6 ile bağ).
6. **Sınır** — Karine, belgenin geçerli ve usulüne uygun düzenlenmiş olmasını varsayar; yetkisiz makam/usulsüzlük karineyi zayıflatır.

## Çıktı modülleri
- Resmî belge/sicil türü ve karine kapsamı tespiti.
- Güçlü karine kısmı / serbest ispata açık kısım ayrımı.
- Aksini ispat yolu ve yükü.
- Sicile güven (m.1023/m.3) bağı + ilkesel içtihat `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `medeni-hukuk-baslangic` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
