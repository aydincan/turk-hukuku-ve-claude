---
name: dava-gorev-yetki-ve-ihtarname
description: "Sebepsiz zenginleşme alacağı için ihtarname çekmek, görevli ve yetkili mahkemeyi belirlemek, dava şartı arabuluculuğu kontrol etmek ve dava dilekçesi iskeleti kurmak gerektiğinde kullanılır."
---

# Dava Yolu, Görev-Yetki ve İhtar/Dilekçe Taslağı

## Görev
İade talebini ihtardan davaya taşıyan usul rotasını kurmak: temerrüt için ihtar, görevli ve yetkili mahkeme, dava şartı arabuluculuk kontrolü ve HMK'ya uygun dilekçe iskeleti. Eksik ön şart veya yanlış mahkeme, dava şartı yokluğundan usulden ret doğurur.

## Soğuk başlangıç (intake)
- Tarafların sıfatı (gerçek kişi, tacir); iş ticari mi?
- Talep para alacağı mı, aynen iade mi; miktar ne?
- Borçluya ihtar çekildi mi; temerrüt oluştu mu?
- Daha önce arabuluculuğa başvuruldu mu?

## Denetim şeması
1. **Temerrüt ve ihtar (TBK m.117).** Sebepsiz zenginleşme borcu kural olarak muaccel; alacaklının ihtarıyla borçlu temerrüde düşer ve temerrüt faizi (TBK m.120; ticari işte 3095 s.K.) ihtardan itibaren işler. İhtar, faiz başlangıcı için kritik belge.
2. **Görevli mahkeme.** Genel kural Asliye Hukuk (HMK m.2). İki tarafın da tacir olduğu ve işin ticari sayıldığı hallerde Asliye Ticaret (TTK m.4-5). Tüketici işleminden kaynaklanıyorsa Tüketici Mahkemesi/Hakem Heyeti (6502 m.73) kapsamı kontrol edilir.
3. **Yetkili mahkeme.** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşme ilişkisinden doğan iadelerde ifa yeri mahkemesi de yetkili olabilir (HMK m.10). Para borçlarında alacaklının yerleşim yeri kuralı (TBK m.89) ifa yeri belirlemede gözetilir.
4. **Dava şartı arabuluculuk.** İki tarafın tacir olduğu, konusu para olan alacak/tazminat talepleri için TTK m.5/A uyarınca arabuluculuk dava şartıdır; başvurulmadan açılan dava usulden reddedilir. Genişleyen kapsam (7445 s.K.) ayrıca kontrol edilir.
5. **Dilekçe mimarisi (HMK m.119).** Taraflar, vakıalar (kazandırma + sebepsizlik), hukuki sebep (TBK m.77 vd.), deliller ve açık talep sonucu (anapara + faiz başlangıcı + tip). Tip (geçerli olmayan/gerçekleşmeyen/sona eren sebep) açıkça belirtilir.
6. **Ara sonuç.** İhtar → arabuluculuk (gerekirse) → doğru mahkemede dava sıralaması; görev kamu düzeninden resen, yetki itirazı ilk itiraz olarak süresinde ileri sürülür.

## Çıktı modülleri
- İade ihtarnamesi taslağı (temerrüt + faiz başlangıcı vurgulu).
- Görev-yetki-arabuluculuk karar ağacı.
- Dava dilekçesi iskeleti (HMK m.119 unsurları + [doldurulacak] yer tutucular).

## Plugin bağlamı

Bu beceri `sebepsiz-zenginlesme` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
