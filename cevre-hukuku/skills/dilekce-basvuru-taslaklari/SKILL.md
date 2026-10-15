---
name: dilekce-basvuru-taslaklari
description: "ÇED/izin iptali dava dilekçesi, idari para cezasına itiraz, çevresel tazminat dilekçesi, idareye başvuru ve çevresel taahhüt/uyum sözleşmesi taslaklarını üretmek gerektiğinde; vakıa-hukuki sebep-talep mimarisiyle layiha hazırlarken kullan."
---

# Dilekçe, Başvuru ve Sözleşme Taslakları

## Görev
Çevresel uyuşmazlığa uygun dava dilekçesi, idari başvuru/itiraz ve sözleşme metinlerini doğru usul kalıbı ve madde dayanaklarıyla üretmek; eksik bilgileri [doldurulacak] yer tutucularıyla işaretlemek.

## Soğuk başlangıç (intake)
1. Hangi metin: iptal/tam yargı dilekçesi, idari para cezasına itiraz, tazminat dilekçesi, idareye başvuru, uyum/taahhüt sözleşmesi?
2. Taraflar, işlem/karar künyesi ve dayanak madde nedir?
3. Talep sonucu net mi (iptal, yürütmenin durdurulması, tazminat tutarı, el atmanın önlenmesi)?
4. Eldeki deliller (ÇED dosyası, ölçüm, tutanak, bilirkişi) nelerdir?

## Denetim şeması
1. **Usul kalıbını seç**: İdari dava → 2577 sayılı İYUK m.3 unsurları (taraflar, konu, sebepler, deliller, talep). Adli dava → 6100 sayılı HMK m.119 zorunlu unsurları. İdari para cezası itirazında görevli mercie göre dilekçe formatı belirlenir.
2. **Mimari**: Vakıa → hukuki sebep (somut madde: 2872 ilgili maddesi, ÇED/izin yönetmeliği, İYUK/HMK) → talep sonucu zinciri kurulur; her vakıa bir delile bağlanır.
3. **Acil talepler**: İdari dilekçede yürütmenin durdurulması (İYUK m.27), adli dilekçede ihtiyati tedbir (HMK m.389) ve delil tespiti gerekçeli olarak eklenir.
4. **Sözleşme metinleri**: Çevresel taahhüt, uyum yol haritası, atık devir/bertaraf veya saha rehabilitasyon sözleşmelerinde sorumluluk dağılımı, tazminat/cezai şart (TBK m.179) ve emredici çevre yükümlülüklerinin sözleşmeyle bertaraf edilemeyeceği gözetilir.
5. **İspat ve ara sonuç**: Delil dizini ve ispat yükü dağılımı dilekçede açıkça kurulur; içtihat atıfları yalnızca doğrulanmış künye ile, aksi halde [doğrulanacak] işaretiyle eklenir.

## Çıktı modülleri
- Seçilen metin türüne uygun dilekçe/başvuru iskeleti
- Vakıa-hukuki sebep-talep tablosu ve delil dizini
- Acil talep (YD/ihtiyati tedbir) bölümü
- Sözleşme/taahhüt taslağı ve risk maddeleri ([doldurulacak] yer tutuculu)

## Plugin bağlamı

Bu beceri `cevre-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
