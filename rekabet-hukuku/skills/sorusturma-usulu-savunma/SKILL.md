---
name: sorusturma-usulu-savunma
description: "Önaraştırma, yerinde inceleme, soruşturma açılması, savunma yazıları ve sözlü savunma gibi Rekabet Kurulu önündeki idari süreçte hak ve süreleri yönetmek istendiğinde kullanılır."
---

# Rekabet Kurulu Soruşturma Usulü ve Savunma

## Görev
4054 m.40-55 çerçevesinde Rekabet Kurumu/Kurulu önündeki sürecin aşamalarını, teşebbüsün usuli haklarını ve savunma stratejisini yönetmek; yerinde inceleme ve bilgi taleplerine hukuka uygun yanıt vermek.

## Soğuk başlangıç (intake)
- Süreç hangi aşamada: önaraştırma, yerinde inceleme yapıldı mı, soruşturma açıldı mı, soruşturma raporu tebliğ edildi mi?
- Teşebbüse tebliğ edilen belge ve tanınan süre nedir?
- Yerinde incelemede zorluk çıkarma/engelleme riski oluştu mu?
- Pişmanlık veya uzlaşma yolu gündemde mi?

## Denetim şeması
1. **Önaraştırma (m.40)** — Kurum şikâyet/resen bilgiyle önaraştırma yapar; bu aşamada henüz taraf savunması zorunlu değildir, ancak işbirliği tonu önemlidir.
2. **Yerinde inceleme (m.15)** — Kurum yetkilileri defter, belge ve elektronik kayıtları inceleyebilir; engelleme/yanlış-eksik bilgi nispi para cezası ve ihlal karinesini güçlendirme riski doğurur (m.16). Yasal sınırlar ve mesleki sır savunması dikkatle yönetilir.
3. **Soruşturma açılması (m.41)** — Kurul soruşturma açarsa teşebbüse bildirilir; ilk yazılı savunma için süre tanınır.
4. **Savunma hakkı ve dosyaya erişim (m.43-44)** — soruşturma raporu tebliğinden sonra yazılı savunma; eşit silah ilkesi gereği iddia ve delillere erişim sağlanır. Süreler hak düşürücüdür; kaçırılması savunmasız kalma sonucunu doğurabilir.
5. **Sözlü savunma toplantısı (m.46)** — talep hâlinde yapılır; iddialar ve savunmalar Kurul önünde tartışılır.
6. **Nihai karar ve yaptırım (m.16, m.52)** — ihlal tespiti hâlinde ciro üzerinden idari para cezası; kararın gerekçesiyle tebliği. Pişmanlık (kartelde) ve Uzlaşma Yönetmeliği kapsamında indirim/erken bitirme imkânları değerlendirilir.

## Çıktı modülleri
- Süreç aşaması ve süre takvimi (hak düşürücü tarihler işaretli).
- Yerinde inceleme yanıt protokolü ve sır savunması notu.
- Yazılı/sözlü savunma iskeleti ve argüman önceliklendirme.
- Pişmanlık/uzlaşma fizibilite değerlendirmesi.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
