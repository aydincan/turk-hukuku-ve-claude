---
name: spor-hukuku-sistematigi
description: "Bir spor uyuşmazlığında devlet mevzuatı, federasyon talimatları, sözleşme ve milletlerarası lex sportiva katmanlarını ayırmak, uyuşmazlığı doğru nitelemek ve uygulanacak normu belirlemek gerektiğinde kullanın."
---

# Spor Hukuku Sistematiği ve Norm Katmanları

## Görev
Spor uyuşmazlığını doğru nitelemek (disiplin, sözleşme, transfer, doping, idari, ceza), hangi norm katmanının ve hangi federasyonun uygulanacağını belirlemek ve devlet hukuku ile özerk spor düzeni (lex sportiva) arasındaki ilişkiyi kurmaktır.

## Soğuk başlangıç (intake)
1. Hangi branş ve hangi federasyon? (TFF mi, bağımsız bir federasyon mu?)
2. Uyuşmazlığın türü ne: disiplin cezası, sözleşmesel alacak, transfer/uygunluk, doping, idari işlem, ceza?
3. Taraflar kim: sporcu, kulüp, menajer, federasyon, üçüncü kişi?
4. Milletlerarası unsur var mı (yabancı kulüp, FIFA/uluslararası federasyon, CAS)?
5. Daha önce bir kurul/merci karar verdi mi; eldeki karar ve tarihi nedir?

## Denetim şeması
1. **Branş ve federasyon tespiti**: Futbolsa 5894 sayılı Kanun ve TFF talimatları; diğer branşlarda 3289 sayılı Kanun çerçevesinde ilgili bağımsız federasyonun ana statüsü ve talimatları uygulanır.
2. **Katman ayrımı**: (a) devlet mevzuatı (7405, 6222, TCK, TBK); (b) federasyon ana statüsü ve talimatları; (c) özel hukuk sözleşmeleri; (d) milletlerarası düzen (FIFA, WADA Kodu, CAS). Aynı olay birden çok katmana değebilir (ör. şike hem TFF disiplinine hem 6222 m.11 ceza normuna girer).
3. **Nitelendirme**: Disiplin → federasyon disiplin kurulu + tahkim. Sözleşmesel → federasyon uyuşmazlık çözüm kurulu/tahkim ya da genel mahkeme (tahkim şartına göre). İdari → kural olarak federasyon tahkimi; istisnaen idari yargı. Ceza → adli yargı.
4. **Özerklik ve Anayasa m.59**: Federasyonların yönetsel ve disipline ilişkin kararlarında zorunlu tahkim ve tahkim kararlarının kesinliği anayasal temele dayanır; bu, devlet yargısına başvuru imkânını sınırlar.
5. **Ara sonuç**: Uygulanacak norm metni, görevli merci ve süre rejimi tek cümlede sabitlenir.

## Çıktı modülleri
- Katman ve nitelendirme tablosu (olay → katman → norm → merci)
- Uygulanacak talimat/madde listesi (yürürlük tarihiyle)
- Görev-yetki ve süre özeti
- Açık sorular ve doğrulanacak içtihat notu

## Plugin bağlamı

Bu beceri `spor-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
