---
name: dava-usul-gorev-yetki-tahkim
description: "Deniz ticareti uyuşmazlığında dava açmadan veya savunma kurmadan önce görevli ve yetkili mahkemeyi, tahkim/yabancı hukuk şartının geçerliliğini, dava şartlarını ve kanun yollarını belirlemek için kullan."
---

# Dava, Görev-Yetki ve Tahkim

## Görev
Deniz ticareti uyuşmazlığını doğru forumda (mahkeme veya tahkim) konumlandırmak; görevli/yetkili mahkemeyi, tahkim ve yabancı hukuk kayıtlarının geçerliliğini, dava şartlarını ve istinaf/temyiz yolunu belirlemek.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu nedir ve taraflar tacir mi (ticari dava niteliği)?
- Sözleşmede tahkim şartı, yetki kaydı veya yabancı hukuk seçimi var mı?
- Yabancılık unsuru var mı (yabancı bayrak, yabancı taraf, yurt dışı ifa)?
- Talep edilen geçici koruma var mı (ihtiyati haciz/tedbir)?

## Denetim şeması
1. **Görevli mahkeme**: Deniz ticaretine ilişkin uyuşmazlıklar mutlak ticari dava olup **asliye ticaret mahkemesi**nde görülür (TTK m.4, m.5); ticaret mahkemesi bulunmayan yerde asliye hukuk mahkemesi ticaret mahkemesi sıfatıyla bakar.
2. **Yetki**: HMK'nın genel yetki kurallarıyla birlikte deniz hukukuna özgü kuralları (örn. ihtiyati hacizde geminin bulunduğu yer; taşıma sözleşmesinde teslim/varış yeri) uygula; tacirler arası geçerli yetki sözleşmesini (HMK m.17) gözet.
3. **Tahkim ve yabancı hukuk şartı**: Çarter partilerdeki tahkim ve yabancı hukuk kayıtlarının geçerliliğini ve konişmentoya incorporation (atıf) yoluyla sirayetini değerlendir; milletlerarası tahkimde MTK (4686) ve yabancı hakem kararlarının tenfizini (New York Sözleşmesi) gözet.
4. **Dava şartları ve geçici koruma**: Hukuki yarar, husumet ve gerekirse dava şartı arabuluculuk (ticari alacaklarda 6325 sayılı HUAK) kontrolünü yap; ihtiyati haciz/tedbir talebini ayrı değerlendir.
5. **İspat ve kanun yolu**: İddiayı ileri süren ispatlar; belge ve sörvey raporları esastır. İlk derece sonrası **istinaf** (BAM) ve kesinlik sınırını aşan kararlarda **temyiz** (Yargıtay) yolunu ve sürelerini hesapla. Çıktıda forum ve süre haritasını netleştir.

## Çıktı modülleri
- Görev-yetki-forum karar tablosu
- Tahkim/yabancı hukuk kaydı geçerlilik notu
- Dava şartı ve kanun yolu süre takvimi

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
