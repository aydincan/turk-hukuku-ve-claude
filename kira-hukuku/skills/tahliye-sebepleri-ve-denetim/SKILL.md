---
name: tahliye-sebepleri-ve-denetim
description: "Kiraya veren tahliye istediğinde veya kiracı tahliye tehdidiyle karşılaştığında hangi tahliye sebebinin uygulanabilir olduğunu, şekil ve süre şartlarını ve dava yolunu belirlemek için bu beceriyi kullan."
---

# Tahliye Sebepleri ve Dava Yolu

## Görev
Konut/çatılı işyeri kirasında tahliye talebini doğru kanuni sebebe oturtmak; her sebebin şekil, süre, bildirim ve ispat şartlarını ayrı ayrı denetlemek; uygun dava/icra yolunu seçmek.

## Soğuk başlangıç (intake)
- Tahliye gerekçesi ne (ihtiyaç, yeniden inşa, taahhüt, ödememe, iki haklı ihtar)?
- Sözleşme belirli/belirsiz süreli mi; dönem sonu ne zaman?
- Daha önce ihtar/bildirim yapıldı mı; tarihleri?
- Taşınmaz el değiştirdi mi (yeni malik)?

## Denetim şeması
1. **Gereksinim — kiraya veren/yakınları (TBK m.350/1)**: Kiraya veren, kendisi, eşi, altsoyu, üstsoyu veya bakmakla yükümlü olduğu kişiler için konut/işyeri **gerçek, samimi ve zorunlu** ihtiyaç ileri sürebilir. Dava süresi m.353'e tabidir.
2. **Yeniden inşa/imar (TBK m.350/2)**: Taşınmazın yeniden inşası veya imarı zorunlu ve esaslı onarımı, kullanım sırasında mümkün değilse tahliye istenebilir.
3. **Yeni malik gereksinimi (TBK m.351)**: Edinme tarihinden başlayarak bir ay içinde durumu kiracıya yazılı bildirmek koşuluyla, altı ay sonra gereksinim sebebiyle dava açabilir; ya da sözleşme süresinin/feshe ilişkin sürelerin sonunu bekleyebilir.
4. **Yazılı tahliye taahhüdü (TBK m.352/1)**: Kiracı, kiralananı belli tarihte boşaltmayı yazılı taahhüt etmiş ve boşaltmamışsa; kiraya veren bu tarihten başlayarak bir ay içinde icra/dava ile tahliye isteyebilir.
5. **İki haklı ihtar (TBK m.352/2)**: Kiracı bir kira yılı içinde iki haklı ihtara sebep olmuşsa, kira yılının/dönemin bitiminden başlayarak bir ay içinde dava.
6. **Temerrüt (TBK m.315)**: Ayrı denetim şeması (bkz. temerrüt becerisi).
7. **Dava süreleri (TBK m.353)** ve **yeniden kiralama yasağı (TBK m.355)**: Tahliye sonrası taşınmaz, haklı sebep olmaksızın üç yıl başkasına kiralanamaz.

## Çıktı modülleri
- Sebep-süre-şekil eşleştirme tablosu.
- Tahliye dava dilekçesi iskeleti.
- Süre uyarı takvimi (hak düşürücü tarihler).

## Plugin bağlamı

Bu beceri `kira-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
