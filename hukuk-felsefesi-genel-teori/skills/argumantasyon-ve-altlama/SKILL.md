---
name: argumantasyon-ve-altlama
description: "Soyut bir norm ile somut olayı gerekçeli biçimde bağlamak (altlama/subsumption), tümdengelimli hukuki kıyas kurmak, argüman türlerini sıralamak ve bir mütalaa/dilekçenin mantıksal iskeletini denetlemek gerektiğinde kullanın."
---

# Hukuki Argümantasyon ve Altlama Tekniği

## Görev
Hukuki kıyas (büyük önerme: norm; küçük önerme: olay; sonuç) ile altlamayı kurallı biçimde
kurmak; argüman türlerini sıralamak ve bir hukuki metnin gerekçe iskeletini denetlemek. Bu
beceri, mütalaa ve dilekçe üretiminin mantıksal omurgasıdır.

## Soğuk başlangıç (intake)
- Uygulanacak norm(lar) net mi; metni ve koşul unsurları çıkarıldı mı?
- Olayın hangi vakıaları sabit, hangileri çekişmeli/ispatı gerekli?
- Talep sonucu ne; hangi norm bu sonucu üretiyor?
- Karşı argüman(lar) tahmin edilebiliyor mu?

## Denetim şeması
1. **Büyük önermeyi kur.** Uygulanacak normun koşul unsurlarını (tatbik şartları) ve hukuki
   sonucunu ayrıştır; belirsiz/yorum gerektiren unsur varsa önce yorum becerisiyle anlamlandır.
   Norm metni ve madde atfı açıkça verilir.
2. **Küçük önermeyi (olayı) çıkar.** Somut vakıaları normun her koşul unsuruna tek tek
   eşle (altlama). Eşlenemeyen unsur varsa o talep çöker; ispatı gereken vakıayı işaretle
   (TMK m.6; HMK m.190 ispat yükü).
3. **Sonucu türet.** Tüm koşullar gerçekleşmişse hukuki sonuç doğar; kısmen gerçekleşmişse
   kısmî sonuç/terditli talep kurulur. Ara sonuç: norm + olay → talep sonucu bağı kanıtlanır.
4. **Argüman türlerini diz.** Lafzî, sistematik, amaçsal, tarihsel argümanlar; kıyas,
   a fortiori, a contrario; otorite argümanı (içtihat/doktrin) ve sonuç argümanı (consequentialist)
   sırasıyla güçlendirilir. Otorite argümanında karar künyesi doğrulanmadıkça [doğrulanacak]
   konur; uydurma künye yasaktır.
5. **Çürütme testi.** Karşı argümanı en güçlü hâliyle kur ve cevapla (steel-man); altlamada
   zayıf halkayı (genellikle çekişmeli vakıa veya belirsiz koşul unsuru) açıkça işaretle.

## Çıktı modülleri
- Kıyas iskeleti (büyük önerme / küçük önerme / sonuç).
- Altlama tablosu (koşul unsuru ↔ vakıa ↔ ispat durumu).
- Argüman sıralaması (güçten zayıfa) ve karşı argümana cevap.
- Zayıf halka / ispat boşluğu uyarısı.

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
