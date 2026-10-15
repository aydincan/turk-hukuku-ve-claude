---
name: ispat-delil-ve-tutanak
description: "İdari yaptırıma dayanak tutanak, cihaz/kayıt ve tespitlerin ispat değerini değerlendirmek, ispat yükünü dağıtmak ve çürütücü delil stratejisi kurmak gerektiğinde kullanılır."
---

# İspat, Delil ve Tutanak Denetimi

## Görev
Kabahatin sübutunu sağlayan delilleri (tutanak, ölçüm cihazı, kamera/ses kaydı, tanık) ispat değeri açısından denetlemek ve çürütücü delil stratejisi kurmak.

## Soğuk başlangıç (intake)
- Kabahat hangi delille tespit edilmiş (tutanak, mobese, hız/emisyon cihazı, numune)?
- Tutanağı kim, hangi yetkiyle, nasıl düzenlemiş; imza/tanık var mı?
- Ölçüm cihazının kalibrasyon/muayene belgesi mevcut mu?
- İlgili kişiye tespit anında bildirim/savunma imkânı tanınmış mı?

## Denetim şeması
1. **İspat yükü:** Kabahatin gerçekleştiğini ispat kural olarak **idareye** düşer. İdare somut, doğrulanabilir delil sunmalıdır; soyut tespit yetersizdir.
2. **Tutanağın değeri:** Usulüne uygun düzenlenmiş tutanak güçlü bir delildir ancak kesin (mutlak) delil değildir; aksi her türlü delille ispatlanabilir. Tutanağın yer-zaman-fiil-tespit yöntemi yönünden çelişki ve eksikliklerini tara.
3. **Teknik tespitler:** Hız/emisyon/gürültü ölçümü, kantar vb. cihazların yetkili kurumca kalibre/muayene edilmiş olması; ölçüm koşullarının kurallara uygunluğu denetlenir. Kalibrasyonsuz/usulsüz ölçüm ispat değerini düşürür.
4. **Hukuka aykırı delil:** Hukuka aykırı yolla elde edilen delilin değerlendirme dışı bırakılması ilkesi (genel ispat hukuku ve Anayasa m.38/6) kabahatler bakımından da gözetilir.
5. **Çürütücü delil:** Tanık, karşı belge, bilirkişi/teknik rapor ve keşif talepleriyle idarenin delilini sars. Başvuruda delillerini açıkça göster.
6. **Ara sonuç:** İspat yükü dengesini değerlendir — idare sübutu sağlayamıyorsa kabahat sabit sayılmaz ve ceza kaldırılır.

## Çıktı modülleri
- Delil-tespit eleştiri tablosu (her delil için zayıf nokta).
- Çürütücü delil listesi ve talep dilekçesi taslağı.
- İspat yükü değerlendirme notu.

## Plugin bağlamı

Bu beceri `kabahatler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
