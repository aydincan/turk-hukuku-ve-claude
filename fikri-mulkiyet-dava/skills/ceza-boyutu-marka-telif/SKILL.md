---
name: ceza-boyutu-marka-telif
description: "Marka hakkına tecavüz suçu (SMK m.30) ile FSEK telif suçlarında (m.71-72) şikâyet, uzlaşma, arama-el koyma ve adli süreç değerlendirmesi gerektiğinde kullanılır."
---

# Ceza Boyutu (Marka ve Telif Suçları)

## Görev
Fikri-sınai tecavüzün ceza boyutunu (marka suçları SMK m.30, telif suçları FSEK m.71-72) şikâyet, soruşturma ve koruma tedbiri yönünden değerlendirmek.

## Soğuk başlangıç (intake)
- Tecavüz markaya mı yoksa telife mi ilişkin; hak tescilli mi?
- Taklit ürün üretimi/satışı/ithali var mı; ticari ölçek nedir?
- Şikâyet süresi içinde misiniz; uzlaşma kapsamı düşünüldü mü?
- Arama-el koyma için yeterli somut delil var mı?

## Denetim şeması
1. Marka suçları: SMK m.30 — taklit marka taşıyan ürünü üretmek, satmak, ithal/ihraç etmek, marka hakkına tecavüz suçtur. Suçun oluşması için markanın tescilli olması şarttır (SMK m.30/4). Şikâyete bağlıdır (m.30/5).
2. Telif suçları: FSEK m.71 — eseri izinsiz çoğaltma, yayma, umuma iletim, manevi haklara tecavüz; m.72 koruyucu programları etkisiz kılma. Şikâyet ve uzlaşma rejimi (CMK m.253) uygulanır.
3. Şikâyet: Suçlar takibi şikâyete bağlıdır; şikâyet süresi fiili ve faili öğrenmeden itibaren işler (TCK m.73 — 6 ay). Süre ve şikâyet hakkı sahipliği denetlenir.
4. Koruma tedbirleri: Arama ve el koyma CMK m.116 vd. ve m.127; taklit ürünlere el konulması. Hukuk davasındaki delil tespitinden ayrı, ceza muhakemesi disiplini geçerlidir.
5. İspat ve görev: Suçun sübutu ceza standardıyla (şüpheden sanık yararlanır); görevli mahkeme FSHM Ceza/asliye ceza. Bilirkişi taklit/iltibas tespiti yapar.
6. Ara sonuç: Ceza ve hukuk yolları paralel yürütülebilir; ceza davasındaki tespit hukuk davasında delil değeri taşır, ancak hukuk hâkimi bağlı değildir (HMK/maddî vakıa ayrımı).

## Çıktı modülleri
- Şikâyet dilekçesi iskeleti ve süre uyarısı.
- Arama-el koyma talep gerekçesi.
- Ceza-hukuk yolu koordinasyon notu.

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
