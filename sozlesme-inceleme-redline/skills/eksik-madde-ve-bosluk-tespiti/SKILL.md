---
name: eksik-madde-ve-bosluk-tespiti
description: "Sözleşmede bulunması gereken ama eksik bırakılan koruyucu maddeleri, belirsiz tanımları ve çapraz atıf hatalarını tespit etmek gerektiğinde kullanılır."
---

# Eksik Madde, Boşluk ve Tanım Denetimi

## Görev
Sözleşmede bulunması gereken standart koruyucu maddelerin eksikliğini, tanım belirsizliklerini, çapraz atıf ve tutarlılık hatalarını tespit etmek; tamamlayıcı taslak önermek.

## Soğuk başlangıç (intake)
- Sözleşme tipine göre olması gereken standart maddeler hangileri?
- Tanımlar bölümü var mı; kullanılan terimler tanımlanmış mı?
- Ek/anex, fiyat listesi, hizmet seviyesi gibi referanslı belgeler mevcut mu?
- Bildirim, devir, değişiklik gibi "boilerplate" maddeler eksik mi?

## Denetim şeması
1. **Standart madde envanteri**: Süre/yenileme, fesih, sorumluluk-tazminat, cezai şart, gizlilik, KVKK/veri (6698), fikri mülkiyet, devir yasağı (TBK m.183 vd.), mücbir sebep, uyarlama (m.138), bildirim, uygulanacak hukuk-yetki/tahkim, bölünebilirlik, tüm sözleşme (entire agreement), değişiklik şekli. Eksikler işaretlenir.
2. **Boşluk doldurma riski**: Eksik nokta hâkim tarafından tamamlayıcı hukuk kurallarıyla (TBK genel/özel hükümler) doldurulur; bu müvekkil aleyhine sonuç verirse açık hüküm önerilir.
3. **Tanım denetimi**: Kullanılan ama tanımlanmayan terimler; tanımlı ama metinde tutarsız kullanılan terimler; "dahil ancak bunlarla sınırlı olmamak üzere" gibi kapsam ifadeleri.
4. **Çapraz atıf/ek tutarlılığı**: Madde numarası atıfları, eklere yapılan referanslar ve eklerin fiilen var olup olmadığı; çelişkide aleyhe yorum (TBK m.23) riski.
5. **Şekil/yürürlük boşluğu**: İmza, tarih, yürürlük tarihi, nüsha, yetkili imza ve vekâlet teyidi.
6. **İspat etkisi**: Eksik bildirim/şekil maddesi ileride ispat ve hak kullanımını zorlaştırır; somutlaştırma önerilir.

## Çıktı modülleri
- Eksik standart madde kontrol listesi (tip bazlı).
- Tanım ve çapraz atıf hata listesi.
- Tamamlayıcı madde taslakları (`[doldurulacak]` yer tutucularıyla).

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
