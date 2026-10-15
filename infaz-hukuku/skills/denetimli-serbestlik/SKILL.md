---
name: denetimli-serbestlik
description: "Açık kurumdan denetimli serbestliğe ayrılma, denetim yükümlülükleri, elektronik izleme ve yükümlülük ihlali sonuçlarını değerlendirmek gerektiğinde kullanılır."
---

# Denetimli Serbestlik Tedbirleri ve Yükümlülükler

## Görev
Hükümlünün denetimli serbestlik tedbiriyle cezasını toplum içinde infaz etme imkânını, yükümlülüklerini ve ihlal hâlinde dönüş rejimini 5275 m.105/A ekseninde değerlendirmek.

## Soğuk başlangıç (intake)
- Hükümlü açık kuruma ayrıldı mı; koşullu salıverilmeye ne kadar süre kaldı?
- Daha önce açık kurumdan firar/disiplin sorunu var mı?
- Hangi yükümlülükler öngörülecek (imza, program, elektronik kelepçe)?
- İş/sağlık/eğitim durumu yükümlülük tasarımını etkiliyor mu?

## Denetim şeması
1. Ayrılma şartı: 5275 m.105/A uyarınca açık ceza infaz kurumunda bulunan veya bu kuruma ayrılma şartlarını taşıyan, koşullu salıverilmesine kanunda belirtilen süre kalan iyi hâlli hükümlü denetimli serbestlikten yararlanabilir. Geçici düzenlemelerin süre farkları kontrol edilir. Ara sonuç: uygunluk.
2. Yükümlülükler: denetimli serbestlik müdürlüğünce belirlenen rapor verme, belirli yerlere gitmeme, programlara katılma; uygun hâllerde elektronik izleme (Elektronik Kelepçe). Yükümlülükler 5275 ve Denetimli Serbestlik Hizmetleri Yönetmeliği çerçevesindedir.
3. İhlal sonucu: yükümlülüklere aykırılık veya kasıtlı yeni suç hâlinde tedbir kaldırılır, hükümlü kapalı kuruma iade edilir ve bakiye ceza kurumda çekilir (5275 m.105/A). İspat: ihlal tutanağı denetimli serbestlik müdürlüğünce düzenlenir.
4. Özel gruplar: hamile, ağır hastalık, yaşlılık ve maktu sürelerde özel kolaylıklar; bunlar ayrıca incelenir.
5. İtiraz: müdürlük işlemine/iade kararına karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr üzerinden, künye `[doğrulanacak]`.
6. Ara sonuç: yararlanma uygunluğu + yükümlülük seti + ihlal riski.

## Çıktı modülleri
- Uygunluk ve süre tablosu.
- Yükümlülük listesi ve ihlal sonuç notu.
- İade kararına itiraz tetiği.

## Plugin bağlamı

Bu beceri `infaz-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
