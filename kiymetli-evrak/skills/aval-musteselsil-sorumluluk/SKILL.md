---
name: aval-musteselsil-sorumluluk
description: "Avalin geçerlilik şartlarını, avalistin sorumluluk kapsamını ve kambiyo borçlularının müteselsil sorumluluğunu çözümlemek; teminat ve borçlu çevresi analizi gerektiğinde kullanılır."
---

# Aval ve Müteselsil Sorumluluk

## Görev
Senet borcuna kefil niteliğindeki aval ilişkisini denetlemek, avalistin kime ve hangi kapsamda sorumlu olduğunu belirlemek; tüm kambiyo borçlularının hamile karşı müteselsil sorumluluğunu çözümlemek.

## Soğuk başlangıç (intake)
- Senet üzerinde aval kaydı ("aval içindir", "kefil") veya senet yüzünde sadece imza var mı?
- Aval kimin için verilmiş; belirtilmemişse kimin lehine sayılır?
- Müvekkil avalist mi, yoksa avalistten talep eden hamil mi?
- Borçlu çevresi (düzenleyen, cirantalar, kabul eden) çıkarıldı mı?

## Denetim şeması
1. Aval şekli: TTK m.700 — aval senet üzerine/alonja "aval içindir" benzeri ibare ve imzayla verilir; poliçe yüzündeki keşideci ve muhatap dışındaki salt imza aval sayılır.
2. Kimin için: aval kimin için verildiği yazılmamışsa poliçede keşideci, bonoda düzenleyen lehine verilmiş sayılır (m.700/4).
3. Sorumluluğun kapsamı: avalist, lehine aval verdiği kişiyle aynı derecede sorumludur (TTK m.702/1). Aval, kefaletten farklı olarak fer'i değildir; lehine aval verilenin taahhüdü şekil dışında bir sebeple geçersiz olsa da aval geçerli kalır (m.702/2 — bağımsızlık).
4. Rücu: ödeyen avalist, lehine aval verdiği kişiye ve ona karşı sorumlu olanlara rücu eder (m.702/3).
5. Müteselsil sorumluluk: düzenleyen, kabul eden, cirantalar ve avalistler hamile karşı müteselsilen sorumludur; hamil sıraya bakmaksızın her birine başvurabilir (TTK m.724). Ödeyen borçlu kendinden önceki borçlulara müracaat eder.
6. Ara sonuç: aval geçerliyse avalist asıl borçlu gibi takip edilebilir; aval lehtarının belirsizliği veya şekil eksikliği halinde sorumluluk yeniden değerlendirilir.

## Çıktı modülleri
- Borçlu çevresi ve sorumluluk haritası (kim-kime-müteselsil).
- Aval geçerlilik ve kapsam notu (m.700-702 dayanaklı).
- Avalist için savunma / hamile karşı talep stratejisi.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
