---
name: iptal-davasi-denetim-semasi
description: "Bir idari işlemin hukuka aykırılığının yetki, şekil, sebep, konu ve maksat unsurları yönünden incelenmesi gerektiğinde kullanılır; işlemin iptali için hangi sakatlık sebebinin ileri sürüleceğinin belirlenmesinde başvurulur."
---

# İptal Davası Denetim Şeması (Beş Unsur)

## Görev
İdari işlemi beş unsuru (yetki, şekil, sebep, konu, maksat) yönünden denetleyerek hukuka aykırılık iddialarını sistematik biçimde kurmak ve iptal sebeplerini gerekçelendirmek.

## Soğuk başlangıç (intake)
- İşlemi tesis eden makam ve dayandığı mevzuat nedir?
- İşlemin gerekçesi/sebebi dosyada açıkça gösterilmiş mi?
- İşlemden önce zorunlu bir usul (savunma, bilirkişi, kurul kararı) öngörülmüş mü?
- İşlemin amacı kamu yararı mı, yoksa başka bir saik mi?

## Denetim şeması
1. **Yetki** (İYUK m.2/1-a): Kişi, konu, yer ve zaman bakımından yetki. Yetkisiz makamın işlemi ve fonksiyon gaspı/yetki tecavüzü ağır sakatlık; bazı hâllerde yokluk doğurur. Yetki kuralları kamu düzenindendir, resen incelenir.
2. **Şekil**: Yazılılık, gerekçe, imza, kurul kararı, ilan/tebliğ gibi asli şekil şartları. Asli şekil sakatlığı iptal sebebidir; tali/önemsiz şekil eksikliği tek başına iptal gerektirmeyebilir.
3. **Sebep**: İşlemin dayandığı maddi ve hukuki olgu. Sebebin hiç bulunmaması, gerçeğe aykırı olması veya yanlış nitelendirilmesi (sebep sakatlığı) iptali gerektirir. Sebebin varlığına ilişkin dayanak belgeleri idare sunmalıdır (resen araştırma — İYUK m.20).
4. **Konu**: İşlemin doğurduğu hukuki sonuç. İmkânsız, mevzuata aykırı veya kazanılmış hakkı ihlal eden konu sakatlık doğurur.
5. **Maksat**: İşlemin kamu yararı amacı taşıması zorunludur. Kişisel husumet, siyasi saik veya yetki saptırması (maksat unsurunda sapma) iptal sebebidir; ispatı güç olduğundan emarelere dayanılır.
6. **Ara sonuç**: Takdir yetkisi denetiminde ölçülülük, eşitlik ve gerekçe ilkeleri ölçü alınır; idarenin takdiri yerindelik denetimine dönüşmemelidir (İYUK m.2/2).

## Çıktı modülleri
- Unsur unsur sakatlık tablosu (iddia + dayanak madde + delil)
- Öncelik sıralaması: en güçlü iptal sebebi başa
- Dilekçe için hukuki sebepler taslağı

## Plugin bağlamı

Bu beceri `idari-yargilama` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
