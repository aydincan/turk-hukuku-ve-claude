---
name: kambiyo-takibi-icra
description: "Çek-bono-poliçeye dayalı kambiyo senetlerine özgü haciz/iflas yolunu, ödeme emrine itiraz ve imza/borç itirazını yürütmek; alacağın icra yoluyla tahsili veya borçlu savunması için kullanılır."
---

# Kambiyo Senetlerine Özgü Takip

## Görev
Kambiyo senedine (çek, bono, poliçe) dayalı icra takibini başlatmak veya ona karşı savunma kurmak; özgü takip yolunun şartlarını, ödeme emrine itiraz usulünü ve sürelerini yönetmek.

## Soğuk başlangıç (intake)
- Senet kambiyo vasfını taşıyor mu (şekil şartları tam mı)?
- Takip alacaklısı yetkili hamil mi; vade geldi mi / çek ibraz edildi mi?
- Müvekkil takip alacaklısı mı, borçlu mu; borçlu hangi sıfatla (düzenleyen, ciranta, avalist) takip ediliyor?
- Ödeme emri tebliğ edildi mi; tebliğ tarihi nedir?

## Denetim şeması
1. Yola elverişlilik: senet kambiyo senedi olmalı ve takip yetkili hamil tarafından, vadesi gelmiş/ibraz edilmiş senetle başlatılmalı (İİK m.167). Eksik senetle bu yol kullanılamaz.
2. Ödeme emri ve süre: borçluya İİK m.168 ödeme emri gönderilir; ödeme süresi 10 gün, itiraz süresi 5 gündür.
3. İmza itirazı: borçlu imzaya itiraz ederse bunu açıkça ve ayrıca bildirmek zorundadır (İİK m.170); imza itirazı satışı durdurmaz ama icra mahkemesi inceler. İmza itirazının reddinde para cezası riski vardır.
4. Borca itiraz: imza dışındaki itirazlar (ödeme, zamanaşımı, yetki) İİK m.169-169/a kapsamında icra mahkemesine yapılır; kural olarak takibi kendiliğinden durdurmaz, mahkemeden tedbir/itirazın kabulü gerekir.
5. İtirazın incelenmesi: icra (hukuk) mahkemesi yetkilidir; alacaklı belgelerle, borçlu da yazılı/usulüne uygun delillerle ispatlar. Sebepsiz itirazda tazminat (İİK m.169/a).
6. Menfi tespit/istirdat: borçlu borçlu olmadığını İİK m.72 ile genel mahkemede dava edebilir; takibi durdurmak için teminatla tedbir gerekir.
7. Ara sonuç: süre ve usul tutulmuşsa takip kesinleşir ve haciz-satış aşamasına geçilir; aksi halde itiraz/iptal yolları işletilir.

## Çıktı modülleri
- Takip talebi ve ödeme emri için veri seti (taraf, senet, bedel [doldurulacak]).
- Süre takvimi (tebliğ + 5/10 gün).
- Borçlu için itiraz dilekçesi (imza/borç/zamanaşımı/yetki) taslağı.

## Plugin bağlamı

Bu beceri `kiymetli-evrak` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
