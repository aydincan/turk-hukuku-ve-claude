---
name: layiha-mimarisi-ve-secim
description: "Hangi yargı kolunda hangi dilekçe türünün yazılacağını saptamak, doğru iskeleti (HMK/İYUK/CMK) kurmak ve vakıa-hukuki sebep-talep sonucu omurgasını oturtmak gerektiğinde kullanılır."
---

# Layiha Mimarisi ve Dilekçe Türü Seçimi

## Görev
Somut talebe uygun yargı kolunu ve dilekçe türünü belirlemek; doğru biçim iskeletini seçip vakıa-hukuki sebep-talep sonucu omurgasını kurmak. Yanlış iskelet, baştan usulden ret veya hak kaybı doğurur; bu beceri tüm atölyenin giriş kapısıdır.

## Soğuk başlangıç (intake)
- Uyuşmazlık özel hukuk mu, idari mi, cezai mı? (taraflardan biri kamu idaresi mi?)
- İlk dilekçe mi, cevap/replik mi, yoksa kanun yolu (istinaf/temyiz) dilekçesi mi?
- Hak düşürücü süre veya dava açma süresi işliyor mu, son gün ne?
- Talep para alacağı mı, tespit mi, iptal mi, eda mı?

## Denetim şeması
1. Yargı kolu tespiti: Taraflardan biri idare ve uyuşmazlık idari işlem/eylemden doğuyorsa İYUK (2577) iskeleti. Suç isnadı varsa CMK (5271). Aksi halde HMK (6100). Karma durumlarda (ör. idari para cezasına itiraz) özel kanun yolunu kontrol edin (Kabahatler K. m.27 — sulh ceza hâkimliği).
2. Dilekçe türü: İlk dava (HMK m.119 / İYUK m.3), cevap (HMK m.126-129), replik-düplik (m.136), istinaf (HMK m.342 / İYUK m.45), temyiz (HMK m.361 / İYUK m.46).
3. İskelet seçimi: HMK m.119 zorunlu unsurları başlık olarak yerleştirin; idari dilekçede İYUK m.3 unsurları (idarenin işlemi, tarihi, tebliğ tarihi) eklenir.
4. Omurga: Vakıalar (numaralı, kronolojik) → her vakıaya delil → hukuki sebep (altlama) → talep sonucu. Ara sonuç: omurga eksiksizse türe özgü beceriye devredin.
5. İspat yükü ön kontrolü (HMK m.190): iddia eden ispatla yükümlüdür; vakıaları bu yüke göre seçin.

## Çıktı modülleri
- Yargı kolu + dilekçe türü kararı (gerekçeli, bir paragraf)
- Seçilen iskeletin başlık listesi (madde atıflı)
- Doldurulması gereken zorunlu unsur kontrol listesi
- İlgili türe özgü beceriye yönlendirme notu

## Plugin bağlamı

Bu beceri `dava-dilekce-atolyesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
