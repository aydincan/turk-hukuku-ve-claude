---
name: genel-bakis
description: "Eşya Hukuku eklentisine giriş, hızlı triyaj ve iş akışı yönlendirmesi. Rol, hedef, süre, belge, risk ve istenen çıktıyı sorar; bu eklentideki uygun uzman becerileri önerir ve net bir çalışma planına bağlar. Bağlam yazısı olmadan belge yüklendiğinde bağımsız tepki verir: materyali sınıflar, süre/aciliyet taraması yapar, uygun uzman beceriye yönlendirir ya da tek bir belirleyici soru sorar."
---

## Konuşma üslubu: kısa başla, hızla belgeye in

Bu beceri bir giriş kapısıdır: kullanıcı çoğunlukla dosyasıyla gelen bir hukukçudur ve
çalışma planı ister, ders değil. İlk yanıtta olayı yerine oturt; yalnızca cevabı sonraki
adımı gerçekten değiştirecek soruyu sor, gerisini `[netleştirilecek: …]` yer tutucusuyla
bırakıp ilk taslağa geç. Ayrıntı, iş ürünü gerektiriyorsa verilir: gerçek altlama,
tablo, kronoloji, risk ve ispat yükü analizi, dilekçe veya mütalaa metni. Gerekçe bu
ürünün parçasıdır; madde tekrarı ve kendini tanıtma değildir.


# Eşya Hukuku — Genel Bakış

Bu genel-bakış becerisi **Eşya Hukuku** eklentisinin hızlı giriş kapısıdır. Resepsiyon,
triyaj, proje yönetimi ve kalite kontrolü tek yerde: önce kısaca netleştir, sonra doğru
çalışma yolunu seç, sonra bu eklentinin uygun uzman becerilerini öner.

**Eklenti odağı:** Eşya hukuku: zilyetlik ve tapu sicili, taşınır/taşınmaz mülkiyeti, sınırlı ayni haklar (irtifak, rehin, intifa), istihkak ve el atmanın önlenmesi (müdahalenin meni) davaları.
**Başat mevzuat:** TMK 4721

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
| `temel-kavramlar-ve-sistem` | Eşya hukuku uyuşmazlığını ilk kez nitelendirirken; ayni hak mı zilyetlik mi borç ilişkisi mi, taşınır mı taşınmaz mı, mülkiyet mi sınırlı ayni hak mı sorularını ayırmak ve doğru hukuki temeli kurmak için kullanılır. |
| `istihkak-ve-mulkiyetin-korunmasi` | Malik, malını haksız elinde bulunduran kişiden geri istemek (istihkak) veya mülkiyetine yönelen haksız müdahaleyi durdurmak istediğinde; taşınır/taşınmaz farkı, ispat yükü ve iyiniyetli kazanım savunmaları için kullanılır. |
| `el-atmanin-onlenmesi-mudahalenin-meni` | Taşınmaza haksız tecavüz, işgal, geçiş, akıntı veya komşunun taşkın kullanımı söz konusu olduğunda; el atmanın önlenmesi, kal (yıkım) ve ecrimisil taleplerini kurmak ve müşterek mülkiyette husumeti çözmek için kullanılır. |
| `zilyetlik-ve-korunmasi` | Tapu veya mülkiyet ispatı olmaksızın fiilî hâkimiyetin gasp ya da saldırı ile bozulduğu durumlarda; zilyetlik karinesi, gaspta geri alma, saldırıyı durdurma davaları ve kısa hak düşürücü süreler için kullanılır. |
| `tapu-sicili-ve-iptal-tescil` | Tapu kaydının gerçek hak durumunu yansıtmadığı (yolsuz tescil, sahtecilik, muvazaa, hata) hâllerde; tapu iptali ve tescil davası, tescile güven ilkesi ile iyiniyetli üçüncü kişinin korunması ve şerhlerin etkisi için kullanılır. |
| `kazandirici-zamanasimi-tescili` | Tapulu taşınmazda kaydın yanlış/eksik olduğu ya da tapusuz taşınmazda uzun süreli malik gibi zilyetlik bulunduğu hâllerde; olağan ve olağanüstü kazandırıcı zamanaşımı şartları ile tescil davasını kurmak için kullanılır. |
| `paydaslik-ortakligin-giderilmesi` | Birden çok kişinin malik olduğu taşınmaz/taşınırda kullanım, yönetim ve pay tasarrufu sorunları ya da ortaklığın sona erdirilmesi (izale-i şuyu) gündeme geldiğinde; aynen taksim ve satış suretiyle giderme yollarını kurmak için kullanılır. |
| `irtifak-haklari` | Bir taşınmaz üzerinde başkası lehine kullanım/yararlanma hakkı kurulması, kullanılması veya sona erdirilmesi söz konusu olduğunda; intifa, oturma, üst hakkı ve geçit/mecra gibi irtifakların tesisi, içeriği ve terkini için kullanılır. |
| `tasinmaz-rehni-ipotek` | Bir alacağın taşınmaz teminatına bağlanması, ipoteğin kurulması/derecesi/paraya çevrilmesi veya fekki gündeme geldiğinde; ipotek, ipotekli borç senedi ayrımı, üst sınır ipoteği ve takip yolu için kullanılır. |
| `tasinir-rehni-ticari-islem` | Taşınır mal, alacak veya işletme varlığının teminat gösterilmesi söz konusu olduğunda; klasik teslime bağlı taşınır rehni ile 6750 sayılı Kanun kapsamında teslimsiz (sicil) rehin ayrımı ve paraya çevirme için kullanılır. |
| `dava-usul-gorev-yetki-tedbir` | Eşya hukuku davası açılmadan önce görevli/yetkili mahkeme, dava şartları, harç-değer, ispat yükü ve taşınmazın devrini önleyici ihtiyati tedbir/şerh stratejisinin belirlenmesi gerektiğinde kullanılır. |

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

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
