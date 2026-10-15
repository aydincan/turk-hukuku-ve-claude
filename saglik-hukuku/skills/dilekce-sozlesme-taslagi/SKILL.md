---
name: dilekce-sozlesme-taslagi
description: "Tıbbi uyuşmazlıkta dava dilekçesi, onam formu, sağlık hizmeti sözleşmesi veya idareye başvuru gibi belgelerin iskeletini üretmek için kullanılır; yer tutucu disipliniyle avukat incelemesine hazır taslak sağlar."
---

# Dilekçe, Sözleşme ve Başvuru Taslağı

## Görev
Tıbbi uyuşmazlığa uygun usul ve içerikte dilekçe, sözleşme veya başvuru taslağını, doğrulanması gereken her veriyi [doldurulacak] yer tutucuyla işaretleyerek üretmek.

## Soğuk başlangıç (intake)
1. Hangi belge gerekli: dava dilekçesi, idari başvuru, onam formu, hizmet sözleşmesi?
2. Yargı kolu adli mi idari mi; mahkeme/merci belli mi?
3. Taraflar, vekiller ve talep sonucu net mi?
4. Dayanak vakıalar ve deliller listelendi mi?

## Denetim şeması
1. **Belge türü ve usul çerçevesi**: Adli dava → HMK m.119 dava dilekçesi zorunlu unsurları. İdari dava → İYUK m.3 dilekçe unsurları. Onam → Hasta Hakları Yönetmeliği m.15/24-31 içerik standardı.
2. **Dava dilekçesi mimarisi**: Mahkeme, taraflar, dava değeri/harç, açık talep sonucu, vakıaların sıralı anlatımı, hukuki sebepler (TBK m.49/112/502, TCK ilgili maddeler), her vakıanın dayandığı delil (HMK m.119/f.1-e,f).
3. **Talep sonucu**: Maddi tazminat kalemleri (tedavi gideri, iş gücü/destek kaybı), manevi tazminat, faiz başlangıcı ve türü, yargılama gideri ve vekâlet ücreti.
4. **Onam/sözleşme taslağı**: Aydınlatma içeriği (tanı, yöntem, riskler, alternatifler, başarısızlık olasılığı), tarih ve makul süre, imza alanları; sorumluluğu tamamen kaldıran şartların geçersizliği (TBK m.115).
5. **Yer tutucu disiplini**: Tüm tarih, tutar, ad ve teknik veri [doldurulacak] olarak işaretlenir; uydurma veri girilmez.
6. **Ara sonuç**: Zorunlu unsur eksikse dilekçe reddi/HMK m.119/2 süre verme riski; taslakta bu kontrol yapılır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlıklı, yer tutuculu)
- Zorunlu unsur kontrol listesi (HMK m.119 / İYUK m.3)
- Talep sonucu ve faiz bloğu
- Doldurulacak veri listesi

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
