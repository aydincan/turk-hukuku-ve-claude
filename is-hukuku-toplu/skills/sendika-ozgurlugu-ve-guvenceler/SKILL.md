---
name: sendika-ozgurlugu-ve-guvenceler
description: "Sendika kurma/uyelik ozgurlugu, sendikal ayrimcilik, sendikal tazminat ve isyeri sendika temsilcisi guvencesi sorunlarinda; ozellikle uyelik veya sendikal faaliyet nedeniyle fesih iddialarinda kullanilir."
---

# Sendika Özgürlüğü ve Sendikal Güvenceler

## Görev
Sendika özgürlüğünün bireysel (üyelik/çekilme) ve kolektif boyutunu, sendikal ayrımcılık yasağını ve sendikal tazminat ile temsilci güvencesini uygulamak. Sendikal nedenle fesih iddialarının ana çalışma alanıdır.

## Soğuk başlangıç (intake)
- İşçi sendika üyesi mi, üyelik/çekilme tarihi nedir, işveren bunu biliyor muydu?
- Fesih veya olumsuz işlem sendikal faaliyetin hemen ardından mı geldi?
- İşçi iş güvencesi kapsamında mı (30+ işçi, 6 ay kıdem — 4857 m.18)?
- Mağdur işyeri sendika temsilcisi mi?

## Denetim şeması
1. **Özgürlüğün kapsamı:** 6356 m.17-19 üyelik, üyelikten çekilme (e-Devlet üzerinden) serbestisini güvenceler. Any. m.51 ve ILO 87/98 yorum dayanağıdır.
2. **Sendikal ayrımcılık yasağı:** 6356 m.25/1-3 — işe alımda, çalışma şartlarında, fesihte sendika üyeliği/faaliyeti nedeniyle ayrım yapılamaz.
3. **Sendikal tazminat:** 6356 m.25/4-5 — ihlalde işçinin bir yıllık ücretinden az olmamak üzere sendikal tazminat. Fesih dışı işlemlerde de talep edilebilir.
4. **İş güvencesi ile yarışma:** İşçi 4857 m.18 kapsamındaysa, sendikal nedenle fesihte işe iade davası açılır; iş güvencesi kapsamında olmasa dahi 6356 m.25/5 uyarınca doğrudan sendikal tazminat istenebilir (Yargıtay'ın yerleşik yaklaşımı — künye `[doğrulanacak]`, karararama.yargitay.gov.tr).
5. **İspat yükü:** 6356 m.25/7 — işçi sendikal nedeni kuvvetle muhtemel kılan olguları (üyelik tarihi, fesihle yakınlık, aynı dönemde örgütlenme) ortaya koyar; ispat yükü işverene geçer, geçerli/haklı neden ispatı işverende.
6. **Temsilci güvencesi:** 6356 m.23-24 — işyeri sendika temsilcisinin iş sözleşmesi haklı neden olmadıkça ve yazılı sebep gösterilmeden feshedilemez; özel güvence işler.

## Çıktı modülleri
- Sendikal ayrımcılık değerlendirme tablosu (olgu-emare-madde).
- İşe iade / sendikal tazminat strateji notu.
- İspat planı ve delil listesi (üyelik kaydı, e-Devlet, tanık, fesih yazışmaları).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
