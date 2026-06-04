---
name: karar-sadelestirme
description: "Yargıtay, Danıştay, AYM, BAM/BİM veya ilk derece kararını müvekkilin anlayacağı dile çevirmek; ne kazanıldı ne kaybedildi, gerekçe ne, hangi yol açık sorularını yanıtlamak gerektiğinde kullanılır."
---

# Mahkeme Kararı Sadeleştirme

## Görev
Bir mahkeme kararını (ilk derece, istinaf, temyiz, AYM bireysel başvuru) müvekkilin "kazandık mı,
ne demek, şimdi ne olacak" sorularına cevap verecek şekilde yalınlaştırmak; hüküm fıkrasını,
gerekçeyi ve sonraki yolu net aktarmak.

## Soğuk başlangıç (intake)
1. Karar hangi merciden ve hangi aşama (ilk derece, BAM/BİM, Yargıtay/Danıştay, AYM)?
2. Müvekkil hangi tarafta ve sonuç onun lehine mi aleyhine mi?
3. Karar kesin mi, yoksa kanun yolu açık mı?
4. Okuyucunun en çok merak ettiği nokta (para, süre, sonraki adım)?

## Denetim şeması
1. HÜKÜM FIKRASINI BUL: Kararın bağlayıcı kısmı gerekçe değil hüküm fıkrasıdır. Sade metin önce
   "mahkeme ne karar verdi" sorusunu hüküm fıkrasından yanıtlar (kabul/ret/kısmen kabul,
   tazminat miktarı, vekâlet ücreti, yargılama gideri).
2. LEHE/ALEYHE NETLİĞİ: Sonucun müvekkil için anlamı açık yazılır; "davanın reddi" gibi ifadeler
   "talebimiz kabul edilmedi / karşı tarafın talebi reddedildi" diye okuyucuya göre çevrilir.
3. GEREKÇE ÖZÜ: Mahkemenin asıl dayandığı hukuki sebep (madde atfıyla) 2-3 cümlede verilir;
   yan değerlendirmeler özetlenir.
4. KANUN YOLU VE SÜRE (kritik sonuç): Karara karşı istinaf (HMK m.345 / İYUK m.45) veya temyiz
   (HMK m.361 / İYUK m.46) yolu ve süresi takvim tarihiyle belirtilir; kesinse "bu karar
   kesindir" denir. AYM bireysel başvuruda 30 günlük süre (6216 s. K. m.47) ayrıca anılır.
5. İÇTİHAT HİJYENİ: Kararın künyesi (mahkeme/daire/esas-karar no/tarih) aktarılırken doğrulanır;
   numara uydurulmaz, gerekirse karararama.yargitay.gov.tr / karararama.danistay.gov.tr ile
   teyit edilir, belirsizse "[doğrulanacak]" bırakılır.
6. ARA SONUÇ: Hüküm fıkrası, lehe/aleyhe yorumu ve süre eksiksiz mi denetlenir.

## Çıktı modülleri
- "Sonuç tek cümlede" özeti.
- Ne kazandık / ne kaybettik tablosu (talep bazında).
- Gerekçe özü (madde atıflı).
- Sonraki adım ve son tarih; kesinlik notu.

## Plugin bağlamı

Bu beceri `sade-hukuk-dili` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
