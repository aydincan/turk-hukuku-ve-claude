---
name: yenilenebilir-yekdem-destek
description: "YEK belgesi, YEKDEM kapsamında fiyat garantisi, yerli katkı ilavesi, destek süresi ve YEKA yarışmaları gibi yenilenebilir destek konuları ele alındığında ve destekten yararlanma uyuşmazlıklarında kullanılır."
---

# Yenilenebilir Enerji ve YEKDEM Destek Mekanizması

## Görev
Yenilenebilir üretim tesisinin 5346 sayılı YEK Kanunu destek mekanizmasından (YEKDEM/YEK belgesi) yararlanma koşullarını, fiyat ve süre hesabını ve destek uyuşmazlıklarını çözümlemek.

## Soğuk başlangıç (intake)
1. Kaynak türü (rüzgâr, GES, HES, biyokütle, jeotermal) ve kapasite?
2. İşletmeye giriş/geçici kabul tarihi nedir?
3. YEK belgesi alındı mı; YEKDEM'e kayıtlı mı, hangi dönem?
4. Yerli aksam/katkı ilavesi talep ediliyor mu?

## Denetim şeması
1. **Kapsam**: 5346 — destekten yararlanacak kaynaklar ve YEK belgesinin alınması. Ara sonuç: kaynak ve tesis destek kapsamında mı.
2. **Fiyat ve süre**: 5346 ve eki I sayılı cetvel — kaynak bazlı taban fiyat ($/MWh); destek süresi kural olarak işletmeye giriş tarihinden itibaren on yıl. Olay tarihindeki cetvel ve kur/dönem uygulaması esastır (tarih kilidi).
3. **Yerli katkı ilavesi**: Yerli üretim aksam kullanımına bağlı ilave fiyat; aksamın yerlilik belgesi ve süre sınırı (kural olarak ilk beş yıl) ispatla aranır. İspat yükü üreticide.
4. **YEKDEM kayıt ve uzlaştırma**: EPİAŞ nezdinde YEKDEM kayıt başvurusu, son tarihler ve dönemsel beyan. Kayıt/süre kaçırılırsa o dönem destek dışı kalınır; bu, doğrudan alacak kaybı doğurur.
5. **YEKA modeli**: YEKA yarışmalarında fiyat ve yerli üretim taahhütleri sözleşmesel olup 5346 destek rejiminden ayrı; ihale şartnamesi ve sözleşme hükümleri esas alınır.

Uyuşmazlıkta EPİAŞ uzlaştırma verisi ve bilirkişi hesabı temel delildir; idari ret kararına karşı İYUK yolu, alacak için sözleşmesel/idari ayrımı yapılır.

## Çıktı modülleri
- Destek uygunluk ve fiyat/süre hesap notu.
- Yerli katkı belge kontrol listesi.
- YEKDEM kayıt/itiraz başvuru taslağı.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
