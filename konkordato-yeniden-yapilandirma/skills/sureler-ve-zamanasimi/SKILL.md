---
name: sureler-ve-zamanasimi
description: "Konkordato sürecindeki tüm kanuni süreleri, mühlet ve uzatma takvimini, faiz ve zamanaşımı etkilerini hesaplamak ve takip etmek gerektiğinde kullanılır."
---

# Süreler, Mühlet Takvimi ve Zamanaşımı

## Görev
Konkordatonun süre yoğun yapısını kontrol altına almak: geçici/kesin mühlet süreleri ve uzatmaları, alacak bildirim ve toplantı süreleri, kanun yolu süreleri, mühletin zamanaşımı ve faize etkisi.

## Soğuk başlangıç (intake)
- Hangi kararın tarihi referans alınacak (geçici mühlet, kesin mühlet, tasdik)?
- Mühlet uzatması talep edildi mi?
- Bir kanun yolu süresi mi hesaplanacak?
- Faiz ve zamanaşımı bakımından hangi alacaklar inceleniyor?

## Denetim şeması
1. **Geçici mühlet (m.287).** Kural üç ay; mahkeme bir ay daha uzatabilir (toplam en çok dört ay). Başlangıç: geçici mühlet kararı tarihi.
2. **Kesin mühlet (m.289).** Bir yıl; güçlük halinde komiser raporuyla altı aya kadar uzatma (toplam en çok bir buçuk yıl). Uzatma talebinin mühlet bitmeden yapılması gerekir.
3. **Alacak bildirim ve toplantı süreleri (m.299, m.302).** Davet ilanındaki bildirim süresi ve projenin kabulü için tanınan süre takip edilir; sürelerin kaçırılması çoğunluk hesabını etkiler.
4. **Faiz (m.294).** Kesin mühlet içinde faiz işlemeye devam edip etmeyeceği alacağın türüne göre (rehinli/rehinsiz, sözleşme/kanun) değerlendirilir; faizin durması/işlemesi tasdik projesinde gösterilir.
5. **Zamanaşımı ve hak düşürücü süreler.** Mühletin zamanaşımını ve hak düşürücü süreleri durdurması/kesmesi (İİK ve TBK genel hükümleriyle birlikte) incelenir. Kanun yolu süreleri (istinaf/temyiz) gün gün hesaplanır; resmi tatil ve adli tatil etkisi gözetilir (HMK m.104, m.92-93). İspat: kararın tebliğ/ilan tarihi esas alınır. Ara sonuç: bağlayıcı tarihler takvimi.

## Çıktı modülleri
- Mühlet ve uzatma süre takvimi (tarih bazlı).
- Kanun yolu süre hesabı.
- Faiz ve zamanaşımı etki notu.
- Kritik tarih hatırlatma listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
