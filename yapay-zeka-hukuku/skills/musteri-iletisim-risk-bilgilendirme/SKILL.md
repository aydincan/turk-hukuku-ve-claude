---
name: musteri-iletisim-risk-bilgilendirme
description: "Teknik bir yapay zekâ konusunun hukuki risklerini müvekkile yalın ve doğru biçimde anlatmak, beklenti yönetimi yapmak ve mevzuat belirsizliğini şeffafça aktarmak gerektiğinde bilgilendirme ve risk haritası üretildiğinde kullanılır."
---

# Müvekkil İletişimi ve Yapay Zekâ Risk Bilgilendirmesi

## Görev
Yapay zekâya ilişkin teknik-hukuki riskleri müvekkilin anlayacağı yalın Türkçeyle, hukuki doğruluğu koruyarak aktarmak; özellikle Türkiye'de yatay YZ kanunu olmamasından doğan belirsizliği ve AB Tüzüğü'nün bağlayıcı olmadığını net biçimde iletmek.

## Soğuk başlangıç (intake)
1. Müvekkilin teknik/hukuki bilgi düzeyi ve asıl kaygısı nedir?
2. Hangi karar verilecek: ürünü yayınlamak, veri kullanmak, sözleşme imzalamak, uyuşmazlığa girmek?
3. Risk toleransı ve zaman/bütçe kısıtı nedir?
4. AB pazarına dokunan bir boyut var mı (uygulanabilir hukuk farkı)?

## Denetim şeması
1. **Çerçeveleme**: Sorunu hukuki katmanlara ayırarak anlat (veri/KVKK, sözleşme, sorumluluk, fikri mülkiyet); her katmanda "kesin / muhtemel / belirsiz" şeklinde risk seviyesi belirt. Ara sonuç: müvekkil neyin kesin neyin gri olduğunu görür.
2. **Belirsizliğin dürüst aktarımı**: Türkiye'de YZ'ye özgü yatay kanun yok; mevcut normların uyarlanmasıyla çalışılıyor ve içtihat henüz oturmuş değil. Bunu olduğu gibi söyle; kesinlik vaadi verme.
3. **Uygulanır hukuk uyarısı**: AB Yapay Zekâ Tüzüğü ve GDPR yalnızca AB'ye dokunulduğunda devreye girer; Türkiye içi kullanım için KVKK + sektörel mevzuat esastır.
4. **Aksiyon ve öncelik**: Riski azaltan somut adımları (aydınlatma, insan gözetimi, sözleşme maddesi, log) öncelik sırasıyla öner; her adımın hangi riski düşürdüğünü açıkla.
5. **Karar müvekkilin**: Seçenekleri ve sonuçlarını sun; ticari kararı müvekkile bırak, hukuki çerçeveyi sen koy.

İddialı her hukuki dayanağı mevzuat madde/fıkra ile bağla; doğrulanmamış içtihat künyesini paylaşma, [doğrulanacak] işaretle.

## Çıktı modülleri
- Yalın dilde risk haritası (kesin/muhtemel/belirsiz).
- Öncelikli aksiyon listesi ve gerekçesi.
- Bilgilendirme notu / e-posta taslağı.

## Plugin bağlamı

Bu beceri `yapay-zeka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
