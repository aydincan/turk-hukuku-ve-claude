---
name: ad-soyad-degistirme
description: "Ad üzerindeki hakka tecavüz, adın haksız kullanımı ya da haklı sebeple ad/soyad değiştirme veya nüfus kaydı düzeltme talebi gündeme geldiğinde kullanılır."
---

# Ad ve Soyadın Korunması ve Değiştirilmesi

## Görev
Ad üzerindeki hakkın korunmasını sağlamak (tecavüzün men'i/tespiti, tazminat) ya da haklı sebebe dayalı ad/soyad değiştirme veya nüfus kaydı düzeltme talebini doğru usul ve dayanakla kurmak.

## Soğuk başlangıç (intake)
- Talep koruma mı (başkası adımı haksız kullanıyor) yoksa değiştirme mi (kendi adımı değiştirmek istiyorum)?
- Değiştirme sebebi nedir: gülünç/incitici ad, fiilen kullanılan farklı ad, yabancı/yanlış yazım, dini/etnik aidiyet, cinsiyet, telaffuz güçlüğü?
- Adın kullanımından zarar/karışıklık doğuyor mu; somut örnek var mı?
- Nüfus kaydında maddi hata mı var (sehven yazım), yoksa irade ile değiştirme mi isteniyor?

## Denetim şeması
1. **Adın korunması** — TMK m.26: adının kullanılması çekişmeli olan kişi hakkının tespitini; adı haksız kullanılan kişi ise haksız kullanmanın önlenmesini, kusur varsa maddi-manevi tazminat ve kazancın iadesini isteyebilir. Tüzel kişinin adı/unvanı da kişilik hakkı kapsamında korunur.
2. **Ad değiştirme** — TMK m.27: haklı sebeplerin varlığında kişi, adının değiştirilmesini hâkimden isteyebilir; değişiklik nüfus siciline kaydolunur ve ilan edilir; değiştirmeden zarar gören bir yıl içinde dava açabilir. Haklı sebep takdiri hâkime aittir (gülünçlük, fiilî kullanım, aidiyet vb. yerleşik içtihatla kabul edilir).
3. **Görev ve usul** — Asliye hukuk mahkemesi görevlidir; ad değiştirme çekişmesiz yargıya yakın bir yapıda yürür (HMK m.382). Yetki: talep edenin yerleşim yeri (TMK m.19). Nüfus müdürlüğü hasım gösterilir.
4. **Nüfus kaydı düzeltme** — Maddi/sehven hatalarda 5490 sayılı Nüfus Hizmetleri Kanunu çerçevesinde idari düzeltme; çekişmeli/irade içeren değişiklikte mahkeme kararı gerekir.
5. **Soyadı** — Soyadı değişikliği de m.27 haklı sebep rejimine tabidir; aile soyadıyla bağ ve nüfus kaydının bütünlüğü gözetilir.

## Çıktı modülleri
- Talep türü ve dayanak (m.26 koruma / m.27 değiştirme) belirlemesi.
- Haklı sebep gerekçesi ve destekleyici delil listesi.
- Dilekçe iskeleti (görevli mahkeme, hasım nüfus müdürlüğü, talep sonucu).
- Yerleşik içtihat ilkesi atfı, künye `[doğrulanacak]`.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
