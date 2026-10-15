---
name: temel-kavramlar-ve-sistem
description: "Borç ilişkisinin kaynağını ve yapısını çözmek; sözleşme mi haksız fiil mi sebepsiz zenginleşme mi olduğunu ve hangi genel hükmün uygulanacağını saptamak gerektiğinde kullanılır."
---

# Temel Kavramlar ve Borç İlişkisinin Sistematiği

## Görev
Önündeki olayda borç ilişkisinin kaynağını, taraflarını, edimin türünü ve uygulanacak genel hüküm bloğunu doğru saptamak; sonraki tüm analizin altyapısını kurmak.

## Soğuk başlangıç (intake)
- Talep neye dayanıyor: bir sözleşme mi, bir zarar mı, yoksa haksız bir malvarlığı kayması mı?
- Taraflar kim, aralarında önceden hukuki bir ilişki var mı?
- Edim ne: verme, yapma, yapmama? Para borcu mu, parça borcu mu, cins borcu mu?
- Olay ne zaman gerçekleşti (zamanaşımı ve uygulanacak kanun için)?

## Denetim şeması
1. Kaynak tespiti: TBK m.1 vd. (sözleşme), m.49 vd. (haksız fiil), m.77 vd. (sebepsiz zenginleşme). Birden çok kaynak yarışabilir; talep yarışması hâlinde lehe olan değerlendirilir.
2. Sözleşmesel ise: Borç sözleşmeden mi yoksa kanundan mı doğuyor? İsimli sözleşme varsa özel hükümlere (TBK İkinci Kısım) köprü kur; isimsiz/karma ise genel hükümler ve kıyas.
3. Edimin niteliği: Para borcu mu? (faiz, m.88, 120 ve 3095 s.K. gündeme gelir). Parça borcunda imkânsızlık riski (m.136), cins borcunda kural olarak imkânsızlık savunulamaz.
4. Borç-sorumluluk ayrımı: Borç (Schuld) var ama dava/icra edilemiyor mu (eksik borç, örn. zamanaşımına uğramış borç, kumar borcu)? TBK m.604-605.
5. İspat yükü: Hakkını dayandıran iddiasını ispatla yükümlüdür (TMK m.6). Borcun doğduğunu alacaklı, sona erdiğini/ifa edildiğini borçlu ispatlar.
6. Ara sonuç: Uygulanacak norm bloğu ve takip edilecek alt-beceri (geçerlilik, ifa, temerrüt) belirlenir.

## Çıktı modülleri
- Borç ilişkisi künyesi (kaynak, taraf, edim, muacceliyet).
- Uygulanacak madde haritası ve yönlendirilecek alt-beceri.
- İlk bakışta zamanaşımı/hak düşürücü süre uyarısı.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
