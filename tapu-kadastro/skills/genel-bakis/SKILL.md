---
name: genel-bakis
description: "Tapu ve Kadastro Uygulaması eklentisine giriş, hızlı triyaj ve iş akışı yönlendirmesi. Rol, hedef, süre, belge, risk ve istenen çıktıyı sorar; bu eklentideki uygun uzman becerileri önerir ve net bir çalışma planına bağlar. Bağlam yazısı olmadan belge yüklendiğinde bağımsız tepki verir: materyali sınıflar, süre/aciliyet taraması yapar, uygun uzman beceriye yönlendirir ya da tek bir belirleyici soru sorar."
---

## Konuşma üslubu: kısa başla, hızla belgeye in

Bu beceri bir giriş kapısıdır: kullanıcı çoğunlukla dosyasıyla gelen bir hukukçudur ve
çalışma planı ister, ders değil. İlk yanıtta olayı yerine oturt; yalnızca cevabı sonraki
adımı gerçekten değiştirecek soruyu sor, gerisini `[netleştirilecek: …]` yer tutucusuyla
bırakıp ilk taslağa geç. Ayrıntı, iş ürünü gerektiriyorsa verilir: gerçek altlama,
tablo, kronoloji, risk ve ispat yükü analizi, dilekçe veya mütalaa metni. Gerekçe bu
ürünün parçasıdır; madde tekrarı ve kendini tanıtma değildir.


# Tapu ve Kadastro Uygulaması — Genel Bakış

Bu genel-bakış becerisi **Tapu ve Kadastro Uygulaması** eklentisinin hızlı giriş kapısıdır. Resepsiyon,
triyaj, proje yönetimi ve kalite kontrolü tek yerde: önce kısaca netleştir, sonra doğru
çalışma yolunu seç, sonra bu eklentinin uygun uzman becerilerini öner.

**Eklenti odağı:** Tapu ve kadastro uygulaması: tapu sicili ilkeleri, kadastro tespitine itiraz, tapu iptali ve tescil davaları, kazandırıcı zamanaşımı, şerh-beyan-rehin işlemleri ve yolsuz tescilin düzeltilmesi.
**Başat mevzuat:** TMK 4721, 3402, 2644

### 0. Sessiz yükleme — bağlam yazısı olmadan materyal

Kullanıcı yalnızca bir belge, ekran görüntüsü, tablo, ZIP veya dosya yığını yükleyip görev
yazmazsa, yüklemeyi iş emri say. Prompt bekleme. Dikkatli bir hukuki yardımcı gibi çalış:
önce aceleyi sabitle, sonra materyali yerine oturt, sonra en iyi sonraki adımı öner.

Önce süre ve aciliyet taraması, çünkü kaçırılan bir süre geri alınamaz: görünür tebligat,
duruşma, ödeme/itiraz süresi, zamanaşımı veya hak düşürücü süre varsa yanıt
`Süre uyarısı: ...` ile başlar; son gün, kalan gün sayısı ve süre dolmuşsa bu açıkça
yazılır. Ardından yanıtta şunlar bulunur:

- **Materyal sınıflaması:** tek cümleyle ne olduğu (dava dilekçesi, karar, sözleşme,
  tebligat, ihbarname, bilirkişi raporu, ekstre, UYAP belgesi, tapu, e-posta).
- **Bağlam çıpaları:** gönderen, muhatap, esas/karar no, mahkeme/kurum/karşı taraf, tarih,
  görülebilir yaşam olayı; okunamayan kısım açıkça belirtilir.
- **Hukuki konu:** materyalin bağlandığı hukuk dalı, norm grubu veya çalışma modu.
- **Yönlendirme:** bu eklentiden uygun uzman beceri; isabet netse o yönde çalış, birden çok
  yol varsa bir birincil yol ve en çok iki alternatif.


### 1. 60 saniyede intake

Kullanıcının verdiğini görünür biçimde özetle; yeniden sorma.

| Nokta | Soru | Neden önemli? |
|---|---|---|
| Rol | Kim soruyor: avukat, müşavir, taraf, şirket, kurum? | Bakış açısı ve üslubu belirler. |
| Hedef | Sonunda ne olmalı: inceleme, dilekçe, mütalaa, kontrol listesi, sözleşme? | Çıktıyı baştan doğru kurar. |
| Olay | Ne oldu, taraflar kim, hangi tarih ve tutarlar kesin? | Havada iş kurmamak için. |
| Süreler | Süre, tebligat, itiraz, dava açma, zamanaşımı, kapanış tarihi var mı? | Acele işleri önce sabitler. |
| Belgeler | Hangi dosya, tapu, tebligat, sözleşme, tablo, e-posta var? | Tahmin değil dosya çalışması. |
| Risk | Sorumluluk, zamanaşımı, idari para cezası, ceza, masraf riski nerede? | Öncelik ve ihtiyatı ayarlar. |
| Biçim | Ne kadar ayrıntı, kime, hangi üslup ve atıf düzeniyle? | Sonucu doğrudan kullanılır kılar. |

### 2. Hızlı triyaj

1. **Süre kontrolü:** Süreler, görev/yetki, şekil şartları ve dönülemez adımları işaretle.
2. **Olay çekirdeği:** 3–7 cümlede kesin / çekişmeli / eksik ayrımını sabitle.
3. **Çalışma modu seç:** kısa inceleme, derin analiz, belge taslağı, müzakere stratejisi,
   dosya çıkarımı, red-team veya müvekkil iletişimi.
4. **Uzman beceri öner:** Bu eklentiden 2–5 uygun beceriyi gerekçesiyle ver.
5. **Sonraki adım:** Bir beceri net uyuyorsa onunla devam et; birkaçı uyuyorsa kısa seçim sun.
6. **Kalite kapısı:** Sonda kaynak, süre, varsayım, açık olgu ve sonraki eylemi denetle.

### 3. Bu eklentideki uzman beceriler

| Beceri | Ne zaman? |
|---|---|
| `tapu-sicili-ve-ayni-hak-sistematigi` | Taşınmaz üzerindeki ayni hakların kuruluş ve devir mantığını, tescilin kurucu etkisini, tescilli ve tescilsiz kazanım ayrımını ve sicil ilkelerini çözümlerken; bir tapu kaydının ne anlama geldiğini ve hangi hakkın nasıl doğduğunu anlamak gerektiğinde kullanılır. |
| `tapu-iptali-ve-tescil-davasi` | Yolsuz veya geçersiz bir tescilin iptali ile gerçek hak durumuna uygun tescilin sağlanması gerektiğinde; muris muvazaası, sahte vekâletname, ehliyetsizlik, hile, irade fesadı, harici satış gibi sebeplerle tapu kaydına itiraz edileceğinde kullanılır. |
| `kadastro-tespitine-itiraz` | Kadastro çalışması sırasında veya askı ilanından sonra tespit edilen malik, sınır, yüzölçüm ya da nitelik hatasına itiraz edilirken; kadastro tutanağının kesinleşmesi, 10 yıllık hak düşürücü süre ve kadastro mahkemesinin görevi söz konusu olduğunda kullanılır. |
| `kazandirici-zamanasimi-tescil` | Tapusuz ya da malik kaydı belirsiz/ölü taşınmazın uzun süreli zilyetlikle kazanılarak adına tescili istendiğinde; olağan (m.712) ve olağanüstü (m.713) kazandırıcı zamanaşımı şartları, süre, zilyetlik niteliği ve istisna araziler değerlendirilirken kullanılır. |
| `yolsuz-tescil-ve-duzeltim` | Tapu kaydındaki yolsuzluğun veya teknik/maddi hatanın (isim, soyadı, ada-parsel, pay, kimlik, mevki, yüzölçüm) giderilmesi gerektiğinde; idari düzeltme yolu ile düzeltim davası arasında ayrım yapmak ve iyiniyetli üçüncü kişi korumasını değerlendirmek için kullanılır. |
| `serh-beyan-ve-takyidat` | Tapu kaydına kişisel hak, tasarruf kısıtlaması, aile konutu, satış vaadi, kira, önalım gibi bir şerh veya beyan işlenmesi, terkin edilmesi ya da var olan takyidatın hukuki etkisinin değerlendirilmesi gerektiğinde kullanılır. |
| `ipotek-ve-tasinmaz-rehni` | Taşınmaz üzerinde ipotek kurulması, derecesi, kapsamı, paraya çevrilmesi (icra) ve terkini söz konusu olduğunda; alacağın teminat altına alınması, üst sınır/anapara ipoteği ayrımı ve rehnin sona ermesi değerlendirilirken kullanılır. |
| `el-atmanin-onlenmesi-ve-ecrimisil` | Taşınmaza haksız müdahale, tecavüz, işgal veya izinsiz kullanım halinde müdahalenin men'i ve haksız işgal tazminatı (ecrimisil) talep edileceğinde; paylı/elbirliği mülkiyette ortaklar arası el atma ve kötüniyetli zilyedin sorumluluğu değerlendirilirken kullanılır. |
| `paylasma-ve-ortakligin-giderilmesi` | Birden çok kişiye ait taşınmazda paydaşlar arası uyuşmazlık, payın devri, yönetim, ortaklığın aynen taksim veya satış yoluyla giderilmesi (izale-i şuyu) söz konusu olduğunda; paylı ile elbirliği mülkiyet ayrımı ve önalım hakkı değerlendirilirken kullanılır. |
| `gorev-yetki-ve-husumet` | Tapu-kadastro uyuşmazlığında hangi mahkemenin görevli, hangi yerin yetkili olduğu ve davanın kime karşı açılacağı belirlenirken; adli/idari yargı ayrımı, kadastro mahkemesi-genel mahkeme geçişi ve Hazine/idare husumeti netleştirilmek istendiğinde kullanılır. |
| `tapu-due-diligence-ve-sozlesme` | Bir taşınmazın satın alınması, finansmanı veya devri öncesinde tapu kaydı, takyidat, imar ve nitelik yönünden risk taraması yapılırken; satış vaadi/satış işlemi, kapora ve devir güvenliği kurgulanırken kullanılır. |

### 4. Yönlendirme kuralları

- **Önce bu eklentinin becerilerini** öner. Konu görünür biçimde başka dala taşıyorsa
  ilgili diğer eklentiyi (ör. `hukuk-metodolojisi`, `atif-turk-hukuku`,
  `hukuk-muhakemesi`, `icra-iflas-hukuku`) köprü olarak an,
- Hiçbir zaman yalnızca beceri adı verme; **ne için, ne zaman, hangi girdi eksik, çıktı ne**
  olduğunu da söyle.
- Dosya büyük/dağınıksa önce bir dosya/tablo/triyaj becerisi öner, sonra maddi inceleme.
- Güncel mevzuat/içtihat/idari uygulama gerekiyorsa açıkça kaynak ve güncellik kontrolü planla.

## Kalite sözü

- Varsayımları görünür ve kısa tut.
- Bitirmeden önce bu eklentinin uygun uzman becerilerini öner.
- Sonda her zaman net bir sonraki adım ver.

## Plugin bağlamı

Bu beceri `tapu-kadastro` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
