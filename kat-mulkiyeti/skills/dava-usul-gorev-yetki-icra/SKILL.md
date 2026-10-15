---
name: dava-usul-gorev-yetki-icra
description: "KMK uyuşmazlığında dava açılmadan önce görevli/yetkili mahkeme, dava şartları, süreler, husumet ve aidat alacağının icra takibi ile ihtiyati tedbir stratejisinin belirlenmesi gerektiğinde; doğru usul çatısını kurmak için kullanılır."
---

# Kat Mülkiyetinde Usul, Görev-Yetki ve İcra

## Görev
KMK'dan doğan davanın usulî çerçevesini kurmak: görevli ve yetkili mahkemeyi, dava şartlarını ve süreleri, husumeti (kim kime karşı), aidat alacağının icra yolunu ve gerekli ihtiyati tedbir/şerh stratejisini belirlemek.

## Soğuk başlangıç (intake)
- Talep türü ne: karar iptali, aidat/gider alacağı, projeye/ortak yere aykırılığın giderilmesi, çıkarma, yönetici hesabı?
- Uyuşmazlık tek anagayrimenkulü mü yoksa toplu yapıyı mı ilgilendiriyor?
- İşliyor olabilecek süreler var mı (karar iptalinde 1 ay/6 ay; işletme projesine itirazda 7 gün)?
- Aidat alacağı için icra takibi başlatılacak mı; itiraz bekleniyor mu?

## Denetim şeması
1. **Görev (KMK m.33 ve Ek hükümler)**: Kat mülkiyetinden kaynaklanan davalar — karar iptali, gider alacağı, projeye aykırılık, yönetici hesabı, çıkarma — kural olarak **sulh hukuk mahkemesinde** görülür. Görev kesindir, re'sen gözetilir.
2. **Yetki**: Davalarda yetki **anagayrimenkulün bulunduğu yer** mahkemesine aittir; taşınmazın aynına ilişkin nitelik nedeniyle bu yetki kesindir (HMK m.12 ile uyumlu). Sözleşmeyle değiştirilemez.
3. **Süreler**: Karar iptalinde m.33/1 süreleri (katılıp aykırı oy kullanan için 1 ay; katılmayan için öğrenmeden 1 ay, her hâlde 6 ay); işletme projesine itirazda 7 gün (m.37); gider alacağında genel zamanaşımı (TBK m.146/m.147 — periyodik edim niteliğine göre değerlendirilir) işler.
4. **Husumet**: Karar iptali ve aykırılık davaları diğer kat maliklerine veya temsilen yöneticiye; aidat alacağı borçlu malike (ve gerektiğinde müteselsil sorumlu kiracıya, m.22) yöneltilir. Çıkarma davasında husumet ilgili malike kurulur.
5. **İcra yolu**: Kesinleşmiş işletme projesi/karar gider tablosuyla ilamsız icra (İİK m.42 vd.); m.37 belgesi İİK m.68 kapsamında değerlendirilir; itiraz hâlinde itirazın iptali (İİK m.67) veya kaldırılması (m.68). Teminat için KMK m.22/2 kanuni ipoteği tescil ettirilir.
6. **İhtiyati tedbir (HMK m.389 vd.)**: Devam eden izinsiz inşaatın durdurulması, ortak yere el atmanın men'i veya kararın icrasının ertelenmesi için tedbir istenir; yaklaşık ispat ve teminat gerekir.
7. **Ara sonuç**: Sulh hukuk + anagayrimenkulün yeri + süre kontrolü + doğru husumet → dava; alacakta İİK yolu + kanuni ipotek.

## Çıktı modülleri
- Görev/yetki ve süre kontrol listesi.
- Husumet tablosu (karar iptali / alacak / çıkarma için davalı tayini).
- İcra takip ve itirazın iptali yol haritası.
- İhtiyati tedbir/şerh dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
