---
name: dava-gorev-yetki-arabuluculuk
description: "Sözleşme uyuşmazlığında hangi mahkemenin görevli ve yetkili olduğunu, dava şartı arabuluculuğun zorunlu olup olmadığını ve usul rotasını belirlemek gerektiğinde kullanılır."
---

# Dava Yolu — Görev, Yetki ve Dava Şartı Arabuluculuk

## Görev
İsimli sözleşme uyuşmazlığında görevli ve yetkili mahkemeyi, dava şartı arabuluculuk zorunluluğunu ve dava açma rotasını belirlemek; yanlış mahkeme/eksik arabuluculuk dava şartı eksikliğiyle usulden ret riski doğurur.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve tarafların sıfatı (tacir, tüketici, gerçek kişi)?
- Talep para alacağı mı, tahliye mi, tespit mi?
- Sözleşmede yetki/tahkim şartı var mı?
- Daha önce arabuluculuğa/hakem heyetine başvuruldu mu?

## Denetim şeması
1. **Görevli mahkeme.** Genel kural Asliye Hukuk (HMK m.2). İstisnalar: kira ilişkisinden doğan davalar ve sözleşme konusu değere bakılmaksızın Sulh Hukuk (HMK m.4); iki tarafın da tacir olduğu ticari işlerde Asliye Ticaret (TTK m.4-5); tüketici işlemlerinde Tüketici Mahkemesi (6502 m.73), belirli tutar altında Tüketici Hakem Heyeti zorunlu.
2. **Yetkili mahkeme.** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davalarda sözleşmenin ifa yeri de yetkili (HMK m.10). Taşınmaza ilişkin ayni uyuşmazlıkta taşınmazın yeri kesin yetkili (HMK m.12).
3. **Dava şartı arabuluculuk.** Ticari davalarda konusu para olan alacak/tazminat talepleri için TTK m.5/A uyarınca arabuluculuk dava şartı; tüketici uyuşmazlıklarında 6502 m.73/A; kira (m.4 kapsamı) uyuşmazlıkları için de dava şartı arabuluculuk (7445 ile genişletilen kapsam) kontrol edilir. Başvurulmadan açılan dava usulden reddedilir.
4. **Tüketici hakem heyeti eşiği.** Yıllık güncellenen parasal sınır altındaki tüketici uyuşmazlıklarında hakem heyetine başvuru zorunlu; karara karşı tüketici mahkemesine itiraz (`[doğrulanacak: güncel tutar]`).
5. **Tahkim/yetki sözleşmesi.** Geçerli tahkim şartı varsa mahkeme yetkisizdir; yetki sözleşmesi yalnızca tacir/kamu tüzel kişileri arasında geçerli (HMK m.17).
6. **Ara sonuç.** Görev + yetki + ön şart (arabuluculuk/hakem heyeti) zinciri; dava açma sırası ve süre. İspat/itiraz: görev kamu düzeninden resen; yetki itirazı ilk itiraz olarak süresinde ileri sürülür.

## Çıktı modülleri
- Görev-yetki-ön şart karar ağacı.
- Arabuluculuk başvuru ve son tutanak kontrol notu.
- Doğru mahkemeye dava açma yol haritası.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
