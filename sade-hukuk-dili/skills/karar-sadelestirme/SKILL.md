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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
